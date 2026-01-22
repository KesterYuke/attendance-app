# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,plyer,python-dateutil

# (str) Application versioning (method 1)
version = 1.0

# (str) Application name
title = 考勤助手

# (str) Package name
package.name = attendance

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = bin,build

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application entry point
entrypoint = my_attendance_gui.py

# (list) List of application modules to import
#modules = mymodule

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of screen sizes
# supported_screens = xxhdpi, xhdpi, hdpi, mdpi, ldpi

# (str) List of icon files
#icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/presplash.png

# (str) Presplash background color (for android toolchain)
#presplash.color = #FFFFFF

# (str) Window background color (for sdl2 windowing tool)
#window.color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Android API, should be as high as possible.
android.api = 34

# (str) Minimum API your APK will support.
android.minapi = 31

# (str) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (str) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 31

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android keystore file (if not specified, debug keystore will be used)
#android.keystore = %(source.dir)s/keystore.keystore

# (str) Android keystore alias (if not specified, debug keystore will be used)
#android.keyalias = myalias

# (str) Android keystore password (if not specified, debug keystore will be used)
#android.keystore_password = mypassword

# (str) Android key alias password (if not specified, debug keystore will be used)
#android.keyalias_password = mypassword

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be presented with the license when first
# running buildozer.
android.accept_sdk_license = True

# (str) Python for android fork to use, defaults to upstream (kivy/python-for-android)
#p4a.source_dir = ../python-for-android

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/build/gradle-tips#configure-compile-options for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
#android.gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle dependencies
# android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (str) screenOrientation to set for the main activity.
# Valid values can be found at https://developer.android.com/guide/topics/manifest/activity-element
#android.manifest.orientation = fullSensor

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the app should be fullscreen or not
android.fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie
#android.presplash_lottie = "path/to/lottie/file.json"

# (list) Cache directory to speed up build
#android.cache_dir = .buildozer/android-cache

# (bool) Skip the compilation of .java files
#android.skip_build = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (bool) Use the old toolchain instead of the new one
#android.use_legacy_toolchain = False

# (str) The Python arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.python_arch = armeabi-v7a

# (str) The Android API to use for compiling
#android.api = 28

# (str) The Android SDK version to use for compiling
#android.sdk = 24

# (str) The Android NDK version to use for compiling
#android.ndk = 17.2.4988734

# (str) The Android NDK API to use for compiling
#android.ndk_api = 21

# (str) The Android NDK path
#android.ndk_path =

# (str) The Android SDK path
#android.sdk_path =

# (str) Buildozer Android path
#android.buildtools_path =

# (bool) Whether to copy the native binaries into the libs folder
#android.copy_libs = 1

# (list) The Android packages to install (via sdkmanager)
#android.sdk_install_packages =

# (str) The Android lint tool to use (if empty, use the default)
#android.lint_tool =

# (str) Path to the default keystore file
#android.keystore =

# (str) Keystore alias
#android.keyalias =

# (str) Keystore password
#android.keystore_password =

# (str) Keyalias password
#android.keyalias_password =

# (str) Path to the debug keystore
#android.debug_keystore =

# (str) Debug keystore password
#android.debug_keystore_password = android

# (str) Debug keystore alias
#android.debug_keystore_alias = androiddebugkey

# (bool) Always use debug keystore
#android.always_use_debug_keystore = False

# (bool) Skip signing the debug version
#android.skip_debug_signing = False

# (bool) Skip signing the release version
#android.skip_release_signing = False

# (str) The default target architecture to build
#android.target_arch = armeabi-v7a

# (list) The Android architectures to build for
#android.archs = armeabi-v7a,arm64-v8a

# (str) The default Android API to use
#android.api = 34

# (str) The minimum Android API to support
#android.minapi = 31

# (str) The Android SDK version to use
#android.sdk = 34

# (str) The Android NDK version to use
#android.ndk = 25.2.9519653

# (str) The Android NDK API to use
#android.ndk_api = 31

# (str) The path to the Android SDK
#android.sdk_path =

# (str) The path to the Android NDK
#android.ndk_path =

# (str) The path to the Android build tools
#android.buildtools_path =

# (str) The path to the Android platform tools
#android.platformtools_path =

# (str) The path to the Android tools
#android.tools_path =

# (str) The path to the Android emulator
#android.emulator_path =

# (str) The path to the Android SDK manager
#android.sdkmanager_path =

# (str) The path to the Android AVD manager
#android.avdmanager_path =

# (bool) Use a custom gradle build script
#android.use_custom_gradle = False

# (str) The path to the custom gradle build script
#android.custom_gradle_path =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) Gradle repositories to add
#android.gradle_repositories =

# (list) Gradle plugins to apply
#android.gradle_plugins =

# (list) Gradle build types to use
#android.gradle_build_types =

# (list) Gradle product flavors to use
#android.gradle_product_flavors =

# (str) The Android build type to use
#android.gradle_build_type = debug

# (str) The Android product flavor to use
#android.gradle_product_flavor =

# (bool) Use the new Android App Bundle format
#android.use_aab = False

# (bool) Generate an APK with the debug symbols included
#android.include_debug_symbols = False

# (bool) Generate an APK with the release symbols included
#android.include_release_symbols = False

# (str) The path to the Android manifest template
#android.manifest_template =

# (str) The path to the Android strings.xml template
#android.strings_xml_template =

# (str) The path to the Android styles.xml template
#android.styles_xml_template =

# (str) The path to the Android colors.xml template
#android.colors_xml_template =

# (str) The path to the Android ic_launcher_foreground.xml template
#android.ic_launcher_foreground_xml_template =

# (str) The path to the Android ic_launcher_background.xml template
#android.ic_launcher_background_xml_template =

# (str) The path to the Android ic_launcher_round.xml template
#android.ic_launcher_round_xml_template =

# (str) The path to the Android ic_launcher.xml template
#android.ic_launcher_xml_template =

# (str) The path to the Android ic_launcher_round.png template
#android.ic_launcher_round_template =

# (str) The path to the Android ic_launcher.png template
#android.ic_launcher_template =

# (str) The path to the Android ic_launcher_legacy.png template
#android.ic_launcher_legacy_template =

# (str) The path to the Android ic_launcher_round_legacy.png template
#android.ic_launcher_round_legacy_template =

# (str) The path to the Android ic_launcher_foreground.png template
#android.ic_launcher_foreground_template =

# (str) The path to the Android ic_launcher_background.png template
#android.ic_launcher_background_template =

# (str) The path to the Android presplash.png template
#android.presplash_template =

# (str) The path to the Android icon.png template
#android.icon_template =

# (str) The path to the Android splash.png template
#android.splash_template =

# (str) The path to the Android splash_landscape.png template
#android.splash_landscape_template =

# (str) The path to the Android splash_portrait.png template
#android.splash_portrait_template =

# (str) The path to the Android splash_landscape_legacy.png template
#android.splash_landscape_legacy_template =

# (str) The path to the Android splash_portrait_legacy.png template
#android.splash_portrait_legacy_template =

# (str) The path to the Android splash_landscape_round.png template
#android.splash_landscape_round_template =

# (str) The path to the Android splash_portrait_round.png template
#android.splash_portrait_round_template =

# (str) The path to the Android splash_landscape_round_legacy.png template
#android.splash_landscape_round_legacy_template =

# (str) The path to the Android splash_portrait_round_legacy.png template
#android.splash_portrait_round_legacy_template =

# (str) The path to the Android splash_foreground.png template
#android.splash_foreground_template =

# (str) The path to the Android splash_background.png template
#android.splash_background_template =

# (str) The path to the Android splash_foreground_landscape.png template
#android.splash_foreground_landscape_template =

# (str) The path to the Android splash_background_landscape.png template
#android.splash_background_landscape_template =

# (str) The path to the Android splash_foreground_portrait.png template
#android.splash_foreground_portrait_template =

# (str) The path to the Android splash_background_portrait.png template
#android.splash_background_portrait_template =

# (str) The path to the Android splash_foreground_legacy.png template
#android.splash_foreground_legacy_template =

# (str) The path to the Android splash_background_legacy.png template
#android.splash_background_legacy_template =

# (str) The path to the Android splash_foreground_round.png template
#android.splash_foreground_round_template =

# (str) The path to the Android splash_background_round.png template
#android.splash_background_round_template =

# (str) The path to the Android splash_foreground_round_legacy.png template
#android.splash_foreground_round_legacy_template =

# (str) The path to the Android splash_background_round_legacy.png template
#android.splash_background_round_legacy_template =

# (str) The path to the Android splash_foreground_landscape_round.png template
#android.splash_foreground_landscape_round_template =

# (str) The path to the Android splash_background_landscape_round.png template
#android.splash_background_landscape_round_template =

# (str) The path to the Android splash_foreground_portrait_round.png template
#android.splash_foreground_portrait_round_template =

# (str) The path to the Android splash_background_portrait_round.png template
#android.splash_background_portrait_round_template =

# (str) The path to the Android splash_foreground_landscape_round_legacy.png template
#android.splash_foreground_landscape_round_legacy_template =

# (str) The path to the Android splash_background_landscape_round_legacy.png template
#android.splash_background_landscape_round_legacy_template =

# (str) The path to the Android splash_foreground_portrait_round_legacy.png template
#android.splash_foreground_portrait_round_legacy_template =

# (str) The path to the Android splash_background_portrait_round_legacy.png template
#android.splash_background_portrait_round_legacy_template =

# (str) The path to the Android splash_foreground_landscape_round.png file
#android.splash_foreground_landscape_round_path =

# (str) The path to the Android splash_background_landscape_round.png file
#android.splash_background_landscape_round_path =

# (str) The path to the Android splash_foreground_portrait_round.png file
#android.splash_foreground_portrait_round_path =

# (str) The path to the Android splash_background_portrait_round.png file
#android.splash_background_portrait_round_path =

# (str) The path to the Android res directory
#android.res_dir =

# (str) The path to the Android assets directory
#android.assets_dir =

# (str) The path to the Android jni directory
#android.jni_dir =

# (str) The path to the Android src directory
#android.src_dir =

# (str) The path to the Android libs directory
#android.libs_dir =

# (str) The path to the Android obj directory
#android.obj_dir =

# (str) The path to the Android bin directory
#android.bin_dir =

# (str) The path to the Android build directory
#android.build_dir =

# (str) The path to the Android dist directory
#android.dist_dir =

# (str) The path to the Android local.properties file
#android.local_properties_path =

# (str) The path to the Android gradle.properties file
#android.gradle_properties_path =

# (str) The path to the Android settings.gradle file
#android.settings_gradle_path =

# (str) The path to the Android build.gradle file
#android.build_gradle_path =

# (str) The path to the Android app/build.gradle file
#android.app_build_gradle_path =

# (str) The path to the Android app/src/main/AndroidManifest.xml file
#android.manifest_path =

# (str) The path to the Android app/src/main/res directory
#android.res_path =

# (str) The path to the Android app/src/main/assets directory
#android.assets_path =

# (str) The path to the Android app/src/main/java directory
#android.java_path =

# (str) The path to the Android app/src/main/jniLibs directory
#android.jni_libs_path =

# (str) The path to the Android app/src/main/python directory
#android.python_path =

# (str) The path to the Android app/src/main/res/values/strings.xml file
#android.strings_xml_path =

# (str) The path to the Android app/src/main/res/values/styles.xml file
#android.styles_xml_path =

# (str) The path to the Android app/src/main/res/values/colors.xml file
#android.colors_xml_path =

# (str) The path to the Android app/src/main/res/drawable/ic_launcher_foreground.xml file
#android.ic_launcher_foreground_xml_path =

# (str) The path to the Android app/src/main/res/drawable/ic_launcher_background.xml file
#android.ic_launcher_background_xml_path =

# (str) The path to the Android app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml file
#android.ic_launcher_xml_path =

# (str) The path to the Android app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml file
#android.ic_launcher_round_xml_path =

# (str) The path to the Android app/src/main/res/mipmap-hdpi/ic_launcher.png file
#android.ic_launcher_hdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-hdpi/ic_launcher_round.png file
#android.ic_launcher_round_hdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-mdpi/ic_launcher.png file
#android.ic_launcher_mdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-mdpi/ic_launcher_round.png file
#android.ic_launcher_round_mdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-xhdpi/ic_launcher.png file
#android.ic_launcher_xhdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-xhdpi/ic_launcher_round.png file
#android.ic_launcher_round_xhdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-xxhdpi/ic_launcher.png file
#android.ic_launcher_xxhdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png file
#android.ic_launcher_round_xxhdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-xxxhdpi/ic_launcher.png file
#android.ic_launcher_xxxhdpi_path =

# (str) The path to the Android app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png file
#android.ic_launcher_round_xxxhdpi_path =

# (str) The path to the Android app/src/main/res/drawable/presplash.png file
#android.presplash_path =

# (str) The path to the Android app/src/main/res/drawable/splash.png file
#android.splash_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash.png file
#android.splash_landscape_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash.png file
#android.splash_portrait_path =

# (str) The path to the Android app/src/main/res/drawable/splash_legacy.png file
#android.splash_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_legacy.png file
#android.splash_landscape_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_legacy.png file
#android.splash_portrait_legacy_path =

# (str) The path to the Android app/src/main/res/drawable/splash_round.png file
#android.splash_round_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_round.png file
#android.splash_landscape_round_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_round.png file
#android.splash_portrait_round_path =

# (str) The path to the Android app/src/main/res/drawable/splash_round_legacy.png file
#android.splash_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_round_legacy.png file
#android.splash_landscape_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_round_legacy.png file
#android.splash_portrait_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable/splash_foreground.png file
#android.splash_foreground_path =

# (str) The path to the Android app/src/main/res/drawable/splash_background.png file
#android.splash_background_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_foreground.png file
#android.splash_foreground_landscape_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_background.png file
#android.splash_background_landscape_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_foreground.png file
#android.splash_foreground_portrait_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_background.png file
#android.splash_background_portrait_path =

# (str) The path to the Android app/src/main/res/drawable/splash_foreground_legacy.png file
#android.splash_foreground_legacy_path =

# (str) The path to the Android app/src/main/res/drawable/splash_background_legacy.png file
#android.splash_background_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_foreground_legacy.png file
#android.splash_landscape_legacy_foreground_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_background_legacy.png file
#android.splash_landscape_legacy_background_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_foreground_legacy.png file
#android.splash_portrait_legacy_foreground_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_background_legacy.png file
#android.splash_portrait_legacy_background_path =

# (str) The path to the Android app/src/main/res/drawable/splash_foreground_round.png file
#android.splash_foreground_round_path =

# (str) The path to the Android app/src/main/res/drawable/splash_background_round.png file
#android.splash_background_round_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_foreground_round.png file
#android.splash_foreground_landscape_round_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_background_round.png file
#android.splash_background_landscape_round_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_foreground_round.png file
#android.splash_foreground_portrait_round_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_background_round.png file
#android.splash_background_portrait_round_path =

# (str) The path to the Android app/src/main/res/drawable/splash_foreground_round_legacy.png file
#android.splash_foreground_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable/splash_background_round_legacy.png file
#android.splash_background_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_foreground_round_legacy.png file
#android.splash_foreground_landscape_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-land/splash_background_round_legacy.png file
#android.splash_background_landscape_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_foreground_round_legacy.png file
#android.splash_foreground_portrait_round_legacy_path =

# (str) The path to the Android app/src/main/res/drawable-port/splash_background_round_legacy.png file
#android.splash_background_portrait_round_legacy_path =

# (str) The path to the Android app/src/main/AndroidManifest.xml file
#android.manifest_path =

# (str) The path to the Android app/build.gradle file
#android.build_gradle_path =

# (str) The path to the Android build.gradle file
#android.root_build_gradle_path =

# (str) The path to the Android settings.gradle file
#android.settings_gradle_path =

# (str) The path to the Android gradle.properties file
#android.gradle_properties_path =

# (str) The path to the Android local.properties file
#android.local_properties_path =

# (str) The path to the Android gradle wrapper
#android.gradle_wrapper_path =

# (str) The path to the Android gradle wrapper properties
#android.gradle_wrapper_properties_path =

# (str) The path to the Android gradle wrapper jar
#android.gradle_wrapper_jar_path =

# (str) The path to the Android gradle wrapper bin
#android.gradle_wrapper_bin_path =

# (str) The path to the Android gradle wrapper distribution url
#android.gradle_wrapper_distribution_url =

# (str) The path to the Android gradle wrapper distribution sha256
#android.gradle_wrapper_distribution_sha256 =

# (str) The path to the Android gradle wrapper distribution base
#android.gradle_wrapper_distribution_base =

# (str) The path to the Android gradle wrapper zip store base
#android.gradle_wrapper_zip_store_base =

# (str) The path to the Android gradle wrapper zip store path
#android.gradle_wrapper_zip_store_path =

# (str) The path to the Android gradle wrapper distribution path
#android.gradle_wrapper_distribution_path =

# (str) The path to the Android gradle wrapper zip store url
#android.gradle_wrapper_zip_store_url =

# (str) The path to the Android gradle wrapper zip store username
#android.gradle_wrapper_zip_store_username =

# (str) The path to the Android gradle wrapper zip store password
#android.gradle_wrapper_zip_store_password =

# (str) The path to the Android gradle wrapper distribution username
#android.gradle_wrapper_distribution_username =

# (str) The path to the Android gradle wrapper distribution password
#android.gradle_wrapper_distribution_password =

# (str) The path to the Android gradle wrapper distribution proxy host
#android.gradle_wrapper_distribution_proxy_host =

# (str) The path to the Android gradle wrapper distribution proxy port
#android.gradle_wrapper_distribution_proxy_port =

# (str) The path to the Android gradle wrapper distribution proxy user
#android.gradle_wrapper_distribution_proxy_user =

# (str) The path to the Android gradle wrapper distribution proxy password
#android.gradle_wrapper_distribution_proxy_password =

# (str) The path to the Android gradle wrapper distribution no proxy hosts
#android.gradle_wrapper_distribution_no_proxy_hosts =

# (str) The path to the Android gradle wrapper zip store proxy host
#android.gradle_wrapper_zip_store_proxy_host =

# (str) The path to the Android gradle wrapper zip store proxy port
#android.gradle_wrapper_zip_store_proxy_port =

# (str) The path to the Android gradle wrapper zip store proxy user
#android.gradle_wrapper_zip_store_proxy_user =

# (str) The path to the Android gradle wrapper zip store proxy password
#android.gradle_wrapper_zip_store_proxy_password =

# (str) The path to the Android gradle wrapper zip store no proxy hosts
#android.gradle_wrapper_zip_store_no_proxy_hosts =

# (str) The path to the Android gradle wrapper daemon
#android.gradle_wrapper_daemon =

# (str) The path to the Android gradle wrapper daemon max heap size
#android.gradle_wrapper_daemon_max_heap_size =

# (str) The path to the Android gradle wrapper daemon max perm size
#android.gradle_wrapper_daemon_max_perm_size =

# (str) The path to the Android gradle wrapper daemon jvm args
#android.gradle_wrapper_daemon_jvm_args =

# (str) The path to the Android gradle wrapper daemon idle timeout
#android.gradle_wrapper_daemon_idle_timeout =

# (str) The path to the Android gradle wrapper daemon enabled
#android.gradle_wrapper_daemon_enabled =

# (str) The path to the Android gradle wrapper parallel
#android.gradle_wrapper_parallel =

# (str) The path to the Android gradle wrapper build cache
#android.gradle_wrapper_build_cache =

# (str) The path to the Android gradle wrapper build cache dir
#android.gradle_wrapper_build_cache_dir =

# (str) The path to the Android gradle wrapper build cache push
#android.gradle_wrapper_build_cache_push =

# (str) The path to the Android gradle wrapper build cache pull
#android.gradle_wrapper_build_cache_pull =

# (str) The path to the Android gradle wrapper build scan
#android.gradle_wrapper_build_scan =

# (str) The path to the Android gradle wrapper build scan terms of service url
#android.gradle_wrapper_build_scan_terms_of_service_url =

# (str) The path to the Android gradle wrapper build scan terms of service accept
#android.gradle_wrapper_build_scan_terms_of_service_accept =

# (str) The path to the Android gradle wrapper no build scan
#android.gradle_wrapper_no_build_scan =

# (str) The path to the Android gradle wrapper no daemon
#android.gradle_wrapper_no_daemon =

# (str) The path to the Android gradle wrapper no parallel
#android.gradle_wrapper_no_parallel =

# (str) The path to the Android gradle wrapper no build cache
#android.gradle_wrapper_no_build_cache =

# (str) The path to the Android gradle wrapper offline
#android.gradle_wrapper_offline =

# (str) The path to the Android gradle wrapper refresh dependencies
#android.gradle_wrapper_refresh_dependencies =

# (str) The path to the Android gradle wrapper rerun tasks
#android.gradle_wrapper_rerun_tasks =

# (str) The path to the Android gradle wrapper dry run
#android.gradle_wrapper_dry_run =

# (str) The path to the Android gradle wrapper quiet
#android.gradle_wrapper_quiet =

# (str) The path to the Android gradle wrapper info
#android.gradle_wrapper_info =

# (str) The path to the Android gradle wrapper debug
#android.gradle_wrapper_debug =

# (str) The path to the Android gradle wrapper stacktrace
#android.gradle_wrapper_stacktrace =

# (str) The path to the Android gradle wrapper full stacktrace
#android.gradle_wrapper_full_stacktrace =

# (str) The path to the Android gradle wrapper no deprecation warnings
#android.gradle_wrapper_no_deprecation_warnings =

# (str) The path to the Android gradle wrapper no warnings
#android.gradle_wrapper_no_warnings =

# (str) The path to the Android gradle wrapper project properties
#android.gradle_wrapper_project_properties =

# (str) The path to the Android gradle wrapper system properties
#android.gradle_wrapper_system_properties =

# (str) The path to the Android gradle wrapper jvm args
#android.gradle_wrapper_jvm_args =

# (str) The path to the Android gradle wrapper max workers
#android.gradle_wrapper_max_workers =

# (str) The path to the Android gradle wrapper daemon max workers
#android.gradle_wrapper_daemon_max_workers =

# (str) The path to the Android gradle wrapper build cache max size
#android.gradle_wrapper_build_cache_max_size =

# (str) The path to the Android gradle wrapper build cache remove unused entries after days
#android.gradle_wrapper_build_cache_remove_unused_entries_after_days =

# (str) The path to the Android gradle wrapper build cache enabled
#android.gradle_wrapper_build_cache_enabled =

# (str) The path to the Android gradle wrapper build cache push
#android.gradle_wrapper_build_cache_push =

# (str) The path to the Android gradle wrapper build cache pull
#android.gradle_wrapper_build_cache_pull =

# (str) The path to the Android gradle wrapper build scan
#android.gradle_wrapper_build_scan =

# (str) The path to the Android gradle wrapper build scan terms of service url
#android.gradle_wrapper_build_scan_terms_of_service_url =

# (str) The path to the Android gradle wrapper build scan terms of service accept
#android.gradle_wrapper_build_scan_terms_of_service_accept =

# (str) The path to the Android gradle wrapper no build scan
#android.gradle_wrapper_no_build_scan =

# (str) The path to the Android gradle wrapper no daemon
#android.gradle_wrapper_no_daemon =

# (str) The path to the Android gradle wrapper no parallel
#android.gradle_wrapper_no_parallel =

# (str) The path to the Android gradle wrapper no build cache
#android.gradle_wrapper_no_build_cache =

# (str) The path to the Android gradle wrapper offline
#android.gradle_wrapper_offline =

# (str) The path to the Android gradle wrapper refresh dependencies
#android.gradle_wrapper_refresh_dependencies =

# (str) The path to the Android gradle wrapper rerun tasks
#android.gradle_wrapper_rerun_tasks =

# (str) The path to the Android gradle wrapper dry run
#android.gradle_wrapper_dry_run =

# (str) The path to the Android gradle wrapper quiet
#android.gradle_wrapper_quiet =

# (str) The path to the Android gradle wrapper info
#android.gradle_wrapper_info =

# (str) The path to the Android gradle wrapper debug
#android.gradle_wrapper_debug =

# (str) The path to the Android gradle wrapper stacktrace
#android.gradle_wrapper_stacktrace =

# (str) The path to the Android gradle wrapper full stacktrace
#android.gradle_wrapper_full_stacktrace =

# (str) The path to the Android gradle wrapper no deprecation warnings
#android.gradle_wrapper_no_deprecation_warnings =

# (str) The path to the Android gradle wrapper no warnings
#android.gradle_wrapper_no_warnings =

# (str) The path to the Android gradle wrapper project properties
#android.gradle_wrapper_project_properties =

# (str) The path to the Android gradle wrapper system properties
#android.gradle_wrapper_system_properties =

# (str) The path to the Android gradle wrapper jvm args
#android.gradle_wrapper_jvm_args =