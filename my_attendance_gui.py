#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
企业微信考勤助手 - 图形化APP版本
功能：
1. 现代化图形化界面
2. 一键企业微信打卡
3. 强提醒功能
4. 智能节假日识别
5. 连续打卡统计
6. 移动设备友好
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.config import Config

# 设置中文字体支持
Config.set('kivy', 'default_font', ['SimHei', 'Arial', 'sans-serif'])

from datetime import datetime, timedelta
import os
import platform
import subprocess

# ===================== 2026年法定节假日配置 =====================
HOLIDAYS_2026 = [
    ("2026-01-01", "2026-01-01", "元旦"),
    ("2026-02-17", "2026-02-23", "春节"),
    ("2026-04-04", "2026-04-06", "清明节"),
    ("2026-05-01", "2026-05-03", "劳动节"),
    ("2026-06-19", "2026-06-21", "端午节"),
    ("2026-09-25", "2026-09-27", "中秋节"),
    ("2026-10-01", "2026-10-07", "国庆节")
]
COMPENSATORY_WORKDAYS = [
    "2026-02-15", "2026-02-26",
    "2026-04-07", "2026-05-04",
    "2026-09-28", "2026-10-10"
]
# =================================================================

# 个人考勤全局状态
check_in_status = {"work": False, "off": False}
check_in_time = {"work": None, "off": None}
reminder_time = {"work": (9, 0), "off": (18, 0)}
warning_minute = 10
on_leave = False
leave_start = None
leave_end = None
current_streak = 0
max_streak = 0
last_check_in_date = None
reminder_enabled = True

# 本地文件路径
LOG_FILE = os.path.join(os.path.expanduser("~"), "my_work_check_log.txt")
STREAK_FILE = os.path.join(os.path.expanduser("~"), "my_streak_data.txt")
REPORT_FILE = os.path.join(os.path.expanduser("~"), "my_monthly_report.txt")
CONFIG_FILE = os.path.join(os.path.expanduser("~"), "my_attendance_config.txt")

def load_config():
    """加载配置"""
    global reminder_time, warning_minute, reminder_enabled
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("work_time:"):
                    time_str = line.split(":", 1)[1].strip()
                    h, m = map(int, time_str.split(":"))
                    reminder_time["work"] = (h, m)
                elif line.startswith("off_time:"):
                    time_str = line.split(":", 1)[1].strip()
                    h, m = map(int, time_str.split(":"))
                    reminder_time["off"] = (h, m)
                elif line.startswith("warning_minute:"):
                    warning_minute = int(line.split(":", 1)[1].strip())
                elif line.startswith("reminder_enabled:"):
                    reminder_enabled = line.split(":", 1)[1].strip().lower() == "true"
    except:
        save_config()

def save_config():
    """保存配置"""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(f"work_time: {reminder_time['work'][0]:02d}:{reminder_time['work'][1]:02d}\n")
        f.write(f"off_time: {reminder_time['off'][0]:02d}:{reminder_time['off'][1]:02d}\n")
        f.write(f"warning_minute: {warning_minute}\n")
        f.write(f"reminder_enabled: {reminder_enabled}\n")

def check_holiday():
    """检查今天是否为节假日"""
    today = datetime.now().strftime("%Y-%m-%d")
    for start, end, name in HOLIDAYS_2026:
        if start <= today <= end:
            return f"今日{name}假期"
    if today in COMPENSATORY_WORKDAYS:
        return "今日补班"
    return ""

def is_workday():
    """判断今天是否为工作日"""
    today = datetime.now()
    if today.weekday() >= 5:
        date_str = today.strftime("%Y-%m-%d")
        return date_str in COMPENSATORY_WORKDAYS
    holiday_info = check_holiday()
    return not holiday_info or "补班" in holiday_info

def mark_work():
    """标记上班打卡"""
    global check_in_status, check_in_time, current_streak, max_streak, last_check_in_date
    if check_in_status["work"]:
        return "今日已完成上班打卡"
    check_in_status["work"] = True
    check_in_time["work"] = datetime.now()
    current_time = check_in_time["work"].strftime("%H:%M:%S")
    update_streak()
    save_check_in()
    return f"上班打卡成功: {current_time}"

def mark_off():
    """标记下班打卡"""
    global check_in_status, check_in_time
    if check_in_status["off"]:
        return "今日已完成下班打卡"
    if not check_in_status["work"]:
        return "请先完成上班打卡"
    check_in_status["off"] = True
    check_in_time["off"] = datetime.now()
    current_time = check_in_time["off"].strftime("%H:%M:%S")
    save_check_in()
    return f"下班打卡成功: {current_time}"

def request_leave(days=1):
    """请假"""
    global on_leave, leave_start, leave_end
    leave_start = datetime.now()
    leave_end = leave_start + timedelta(days=days)
    on_leave = True
    return f"请假成功: {days}天 ({leave_start.strftime('%Y-%m-%d')} 到 {leave_end.strftime('%Y-%m-%d')})"

def update_streak():
    """更新连续打卡天数"""
    global current_streak, max_streak, last_check_in_date
    today = datetime.now().strftime("%Y-%m-%d")
    if last_check_in_date == today:
        return
    if last_check_in_date:
        last_date = datetime.strptime(last_check_in_date, "%Y-%m-%d")
        today_date = datetime.strptime(today, "%Y-%m-%d")
        if (today_date - last_date).days == 1:
            current_streak += 1
        else:
            current_streak = 1
    else:
        current_streak = 1
    last_check_in_date = today
    if current_streak > max_streak:
        max_streak = current_streak
    save_streak()

def save_check_in():
    """保存打卡记录"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 上班: {check_in_status['work']}, 下班: {check_in_status['off']}\n")

def save_streak():
    """保存连续打卡数据"""
    with open(STREAK_FILE, "w", encoding="utf-8") as f:
        f.write(f"{current_streak},{max_streak},{last_check_in_date}\n")

def generate_report():
    """生成月报"""
    try:
        with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
            logs = f.readlines()
        with open(REPORT_FILE, "w", encoding="utf-8") as f:
            f.write(f"月度考勤报告 - {datetime.now().strftime('%Y年%m月')}\n")
            f.write("=" * 50 + "\n")
            for log in logs:
                f.write(log)
        return "月报生成成功，已保存到桌面"
    except Exception as e:
        return "生成月报时出错"

def load_streak():
    """加载连续打卡数据"""
    global current_streak, max_streak, last_check_in_date
    try:
        with open(STREAK_FILE, "r", encoding="utf-8") as f:
            data = f.readline().strip().split(",")
            if len(data) == 3:
                current_streak = int(data[0])
                max_streak = int(data[1])
                last_check_in_date = data[2]
    except:
        pass

def open_wechat_work():
    """打开企业微信"""
    system = platform.system()
    if system == "Windows":
        try:
            subprocess.run(["start", "weixinwork://"], shell=True, check=False)
            return True
        except:
            return False
    elif system == "Darwin":
        try:
            subprocess.run(["open", "weixinwork://"], check=False)
            return True
        except:
            return False
    else:
        return False

class RoundedButton(Button):
    """圆角按钮"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.2, 0.6, 1, 1)  # 默认蓝色
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(20)])
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MainScreen(Screen):
    """主屏幕"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # 顶部状态栏
        self.top_bar = BoxLayout(size_hint_y=0.15, spacing=dp(10))
        self.date_label = Label(text=datetime.now().strftime('%Y-%m-%d %A'), 
                               font_size='16sp', bold=True)
        self.status_label = Label(text='', font_size='14sp', color=(1, 0.6, 0, 1))
        self.top_bar.add_widget(self.date_label)
        self.top_bar.add_widget(self.status_label)
        self.layout.add_widget(self.top_bar)
        
        # 打卡状态
        self.checkin_status = BoxLayout(size_hint_y=0.15, spacing=dp(10))
        self.work_status = Label(text='上班: 未打卡', font_size='16sp', 
                                color=(1, 0, 0, 1), bold=True)
        self.off_status = Label(text='下班: 未打卡', font_size='16sp', 
                               color=(1, 0, 0, 1), bold=True)
        self.checkin_status.add_widget(self.work_status)
        self.checkin_status.add_widget(self.off_status)
        self.layout.add_widget(self.checkin_status)
        
        # 连续打卡
        self.streak_layout = BoxLayout(size_hint_y=0.1, spacing=dp(10))
        self.streak_label = Label(text=f'连续: {current_streak}天 | 最长: {max_streak}天', 
                                 font_size='14sp', color=(0, 0.8, 0, 1))
        self.streak_layout.add_widget(self.streak_label)
        self.layout.add_widget(self.streak_layout)
        
        # 主要按钮
        self.main_buttons = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=0.4)
        
        # 一键打卡按钮
        self.one_click_btn = RoundedButton(text='🚀 一键企业微信打卡', 
                                           font_size='18sp', 
                                           background_color=(0.2, 0.6, 1, 1))
        self.one_click_btn.bind(on_press=self.one_click_checkin)
        self.main_buttons.add_widget(self.one_click_btn)
        
        # 手动打卡按钮
        self.checkin_buttons = BoxLayout(spacing=dp(10))
        self.work_btn = RoundedButton(text='✅ 上班打卡', 
                                     font_size='16sp', 
                                     background_color=(0, 0.8, 0, 1))
        self.work_btn.bind(on_press=self.mark_work)
        self.off_btn = RoundedButton(text='✅ 下班打卡', 
                                    font_size='16sp', 
                                    background_color=(0.8, 0.6, 0, 1))
        self.off_btn.bind(on_press=self.mark_off)
        self.checkin_buttons.add_widget(self.work_btn)
        self.checkin_buttons.add_widget(self.off_btn)
        self.main_buttons.add_widget(self.checkin_buttons)
        
        # 其他功能按钮
        self.other_buttons = BoxLayout(spacing=dp(10))
        self.leave_btn = RoundedButton(text='📝 请假', 
                                      font_size='16sp', 
                                      background_color=(1, 0.6, 1, 1))
        self.leave_btn.bind(on_press=self.open_leave_popup)
        self.report_btn = RoundedButton(text='📊 生成月报', 
                                       font_size='16sp', 
                                       background_color=(0.8, 0.8, 0.2, 1))
        self.report_btn.bind(on_press=self.generate_report)
        self.other_buttons.add_widget(self.leave_btn)
        self.other_buttons.add_widget(self.report_btn)
        self.main_buttons.add_widget(self.other_buttons)
        
        self.layout.add_widget(self.main_buttons)
        
        # 设置按钮
        self.settings_btn = RoundedButton(text='🛠 设置', 
                                         font_size='16sp', 
                                         background_color=(0.5, 0.5, 0.5, 1),
                                         size_hint_y=0.1)
        self.settings_btn.bind(on_press=self.go_to_settings)
        self.layout.add_widget(self.settings_btn)
        
        self.add_widget(self.layout)
        
        # 定时更新状态
        Clock.schedule_interval(self.update_status, 60)
        self.update_status()
    
    def update_status(self, dt=None):
        """更新状态"""
        # 更新日期
        self.date_label.text = datetime.now().strftime('%Y-%m-%d %A')
        
        # 更新节假日状态
        holiday_info = check_holiday()
        if holiday_info:
            self.status_label.text = holiday_info
        else:
            workday_status = "工作日" if is_workday() else "休息日"
            self.status_label.text = workday_status
        
        # 更新打卡状态
        if check_in_status["work"]:
            self.work_status.text = '上班: 已打卡'
            self.work_status.color = (0, 0.8, 0, 1)
        else:
            self.work_status.text = '上班: 未打卡'
            self.work_status.color = (1, 0, 0, 1)
        
        if check_in_status["off"]:
            self.off_status.text = '下班: 已打卡'
            self.off_status.color = (0, 0.8, 0, 1)
        else:
            self.off_status.text = '下班: 未打卡'
            self.off_status.color = (1, 0, 0, 1)
        
        # 更新连续打卡
        self.streak_label.text = f'连续: {current_streak}天 | 最长: {max_streak}天'
    
    def one_click_checkin(self, instance):
        """一键打卡"""
        if open_wechat_work():
            self.show_popup('企业微信已打开', '请在企业微信中完成打卡，完成后点击确认')
        else:
            self.show_popup('提示', '请手动打开企业微信完成打卡')
    
    def mark_work(self, instance):
        """上班打卡"""
        result = mark_work()
        self.show_popup('打卡结果', result)
        self.update_status()
    
    def mark_off(self, instance):
        """下班打卡"""
        result = mark_off()
        self.show_popup('打卡结果', result)
        self.update_status()
    
    def open_leave_popup(self, instance):
        """打开请假弹窗"""
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        content.add_widget(Label(text='请输入请假天数:', font_size='16sp'))
        self.leave_input = TextInput(hint_text='例如: 1', font_size='16sp', 
                                    input_filter='int', size_hint_y=0.2)
        content.add_widget(self.leave_input)
        
        buttons = BoxLayout(spacing=dp(10))
        cancel_btn = Button(text='取消', background_color=(0.8, 0.8, 0.8, 1))
        confirm_btn = Button(text='确认', background_color=(0.2, 0.6, 1, 1))
        
        def cancel(instance):
            self.leave_popup.dismiss()
        
        def confirm(instance):
            try:
                days = int(self.leave_input.text) if self.leave_input.text else 1
                result = request_leave(days)
                self.show_popup('请假结果', result)
                self.leave_popup.dismiss()
            except ValueError:
                self.show_popup('错误', '请输入正确的天数')
        
        cancel_btn.bind(on_press=cancel)
        confirm_btn.bind(on_press=confirm)
        buttons.add_widget(cancel_btn)
        buttons.add_widget(confirm_btn)
        content.add_widget(buttons)
        
        self.leave_popup = Popup(title='请假申请', content=content, 
                                size_hint=(0.8, 0.5))
        self.leave_popup.open()
    
    def generate_report(self, instance):
        """生成月报"""
        result = generate_report()
        self.show_popup('月报生成', result)
    
    def go_to_settings(self, instance):
        """进入设置页面"""
        self.manager.current = 'settings'
    
    def show_popup(self, title, message):
        """显示弹窗"""
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        content.add_widget(Label(text=message, font_size='16sp', halign='center'))
        ok_btn = Button(text='确定', background_color=(0.2, 0.6, 1, 1))
        
        def close_popup(instance):
            popup.dismiss()
        
        ok_btn.bind(on_press=close_popup)
        content.add_widget(ok_btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        popup.open()

class SettingsScreen(Screen):
    """设置页面"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # 标题
        self.title = Label(text='⚙️ 系统设置', font_size='20sp', bold=True)
        self.layout.add_widget(self.title)
        
        # 上班时间
        self.work_time_layout = BoxLayout(size_hint_y=0.1, spacing=dp(10))
        self.work_time_label = Label(text='上班时间:', font_size='16sp')
        self.work_h = TextInput(text=str(reminder_time['work'][0]), 
                               font_size='16sp', input_filter='int', 
                               size_hint_x=0.2)
        self.work_m = TextInput(text=str(reminder_time['work'][1]), 
                               font_size='16sp', input_filter='int', 
                               size_hint_x=0.2)
        self.work_time_layout.add_widget(self.work_time_label)
        self.work_time_layout.add_widget(self.work_h)
        self.work_time_layout.add_widget(Label(text=':', font_size='16sp'))
        self.work_time_layout.add_widget(self.work_m)
        self.layout.add_widget(self.work_time_layout)
        
        # 下班时间
        self.off_time_layout = BoxLayout(size_hint_y=0.1, spacing=dp(10))
        self.off_time_label = Label(text='下班时间:', font_size='16sp')
        self.off_h = TextInput(text=str(reminder_time['off'][0]), 
                              font_size='16sp', input_filter='int', 
                              size_hint_x=0.2)
        self.off_m = TextInput(text=str(reminder_time['off'][1]), 
                              font_size='16sp', input_filter='int', 
                              size_hint_x=0.2)
        self.off_time_layout.add_widget(self.off_time_label)
        self.off_time_layout.add_widget(self.off_h)
        self.off_time_layout.add_widget(Label(text=':', font_size='16sp'))
        self.off_time_layout.add_widget(self.off_m)
        self.layout.add_widget(self.off_time_layout)
        
        # 提醒时间
        self.warning_layout = BoxLayout(size_hint_y=0.1, spacing=dp(10))
        self.warning_label = Label(text='提前提醒:', font_size='16sp')
        self.warning_spinner = Spinner(text=f'{warning_minute}分钟', 
                                      values=['5分钟', '10分钟', '15分钟', '20分钟'],
                                      font_size='16sp', size_hint_x=0.3)
        self.warning_layout.add_widget(self.warning_label)
        self.warning_layout.add_widget(self.warning_spinner)
        self.layout.add_widget(self.warning_layout)
        
        # 提醒开关
        self.reminder_layout = BoxLayout(size_hint_y=0.1, spacing=dp(10))
        self.reminder_label = Label(text='提醒功能:', font_size='16sp')
        self.reminder_spinner = Spinner(text='开启' if reminder_enabled else '关闭', 
                                       values=['开启', '关闭'],
                                       font_size='16sp', size_hint_x=0.3)
        self.reminder_layout.add_widget(self.reminder_label)
        self.reminder_layout.add_widget(self.reminder_spinner)
        self.layout.add_widget(self.reminder_layout)
        
        # 按钮
        self.buttons = BoxLayout(spacing=dp(10), size_hint_y=0.2)
        self.save_btn = RoundedButton(text='保存设置', 
                                     font_size='16sp', 
                                     background_color=(0.2, 0.8, 0.2, 1))
        self.save_btn.bind(on_press=self.save_settings)
        self.reset_btn = RoundedButton(text='重置默认', 
                                      font_size='16sp', 
                                      background_color=(0.8, 0.4, 0, 1))
        self.reset_btn.bind(on_press=self.reset_settings)
        self.back_btn = RoundedButton(text='返回', 
                                     font_size='16sp', 
                                     background_color=(0.5, 0.5, 0.5, 1))
        self.back_btn.bind(on_press=self.go_back)
        self.buttons.add_widget(self.save_btn)
        self.buttons.add_widget(self.reset_btn)
        self.buttons.add_widget(self.back_btn)
        self.layout.add_widget(self.buttons)
        
        self.add_widget(self.layout)
    
    def save_settings(self, instance):
        """保存设置"""
        global reminder_time, warning_minute, reminder_enabled
        try:
            work_h = int(self.work_h.text) if self.work_h.text else 9
            work_m = int(self.work_m.text) if self.work_m.text else 0
            off_h = int(self.off_h.text) if self.off_h.text else 18
            off_m = int(self.off_m.text) if self.off_m.text else 0
            
            reminder_time['work'] = (work_h, work_m)
            reminder_time['off'] = (off_h, off_m)
            warning_minute = int(self.warning_spinner.text.replace('分钟', ''))
            reminder_enabled = self.reminder_spinner.text == '开启'
            
            save_config()
            self.show_popup('成功', '设置保存成功！')
        except ValueError:
            self.show_popup('错误', '请输入正确的时间格式')
    
    def reset_settings(self, instance):
        """重置设置"""
        global reminder_time, warning_minute, reminder_enabled
        reminder_time = {"work": (9, 0), "off": (18, 0)}
        warning_minute = 10
        reminder_enabled = True
        
        # 更新界面
        self.work_h.text = '9'
        self.work_m.text = '0'
        self.off_h.text = '18'
        self.off_m.text = '0'
        self.warning_spinner.text = '10分钟'
        self.reminder_spinner.text = '开启'
        
        save_config()
        self.show_popup('成功', '设置已重置为默认值')
    
    def go_back(self, instance):
        """返回主页面"""
        self.manager.current = 'main'
    
    def show_popup(self, title, message):
        """显示弹窗"""
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        content.add_widget(Label(text=message, font_size='16sp', halign='center'))
        ok_btn = Button(text='确定', background_color=(0.2, 0.6, 1, 1))
        
        def close_popup(instance):
            popup.dismiss()
        
        ok_btn.bind(on_press=close_popup)
        content.add_widget(ok_btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        popup.open()

class AttendanceApp(App):
    """考勤APP"""
    def build(self):
        # 加载数据
        load_config()
        load_streak()
        
        # 设置窗口
        Window.size = (400, 600)  # 手机大小
        Window.clearcolor = (1, 1, 1, 1)
        
        # 创建屏幕管理器
        self.sm = ScreenManager()
        
        # 添加屏幕
        self.main_screen = MainScreen(name='main')
        self.settings_screen = SettingsScreen(name='settings')
        
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.settings_screen)
        
        return self.sm

if __name__ == '__main__':
    AttendanceApp().run()