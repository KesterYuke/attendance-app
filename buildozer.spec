[app]
# (str) Title of your application
app_name = 考勤助手

# (str) Package name
package.name = attendance

# (str) Package domain (needed for android/ios packaging)
package.domain = org

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application entry point
source.include_patterns = my_attendance_gui.py

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,plyer,python-dateutil

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 31

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (str) Android ABI to use
android.arch = arm64-v8a

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
