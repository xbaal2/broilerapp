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
android.api = 29
android.build_tools_version = 29.0.2

# Arsitektur Android
android.archs = arm64-v8a,armeabi-v7a

# Nama package unik
package.domain = org.iqbalyda

# Aplikasi mode
fullscreen = 0

# Build type
build_type = debug

# Entry point
android.entrypoint = main.py

# SDK/NDK paths
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25b

# Accept licenses otomatis
android.accept_sdk_license = True

# Mode debug agar log terlihat jelas
log_level = 2

[buildozer]
warn_on_root = 1
build_dir = .buildozer
log_level = 2
