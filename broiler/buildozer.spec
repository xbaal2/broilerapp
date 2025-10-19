[app]
# Nama aplikasi
title = BroilerApp
package.name = broilerapp
package.domain = org.iqbalyda

# Versi aplikasi
version = 0.1

# File utama dan resource
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json
source.include_patterns = icons/*

# Requirements Python dan Kivy
requirements = python3,kivy==2.3.1,openssl,requests

# Orientasi layar
orientation = portrait

# Ikon launcher
icon.filename = icons/icon.png

# Permissions Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Versi SDK Android
android.minapi = 26
android.api = 31

# Arsitektur Android (gunakan ini agar kompatibel)
android.archs = arm64-v8a,armeabi-v7a

# Aplikasi mode
fullscreen = 0

# Build type
build_type = debug

# Entry point
android.entrypoint = main.py

# Gunakan legacy SDK agar tidak error di runner
android.accept_sdk_license = True

# Mode debug agar log build terlihat jelas
log_level = 2


[buildozer]
warn_on_root = 1
build_dir = .buildozer

# Path SDK & NDK manual
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

log_level = 2
