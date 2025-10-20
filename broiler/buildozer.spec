[app]

# Nama dan package
title = BroilerApp
package.name = broilerapp
package.domain = org.xbaal

# File utama
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.include_patterns = icons/*

# Nama file main
main.py = main.py

# Ikon (bisa kamu ganti)
icon.filename = icons/app_icon.png

# Versi
version = 1.0.0
requirements = python3,kivy==2.3.1,openssl,requests,cython,setuptools

orientation = portrait

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Include Python libraries
android.api = 31
android.minapi = 26
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

# Paths
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = ~/.buildozer/android/platform/android-sdk

# Debug/Release
android.debug = True

# Package format
package.format = apk

# Window
fullscreen = 0
log_level = 2

# Presplash (opsional)
presplash.filename = icons/icon.png
