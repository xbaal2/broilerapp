[app]
title = BroilerApp
package.name = broilerapp
package.domain = org.iqbalyda
version = 0.1

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json
source.include_patterns = icons/*

requirements = python3,kivy==2.3.1,openssl,requests
orientation = portrait
icon.filename = icons/icon.png
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.minapi = 26
android.api = 31
android.archs = arm64-v8a,armeabi-v7a
fullscreen = 0
build_type = debug
android.entrypoint = main.py

android.accept_sdk_license = True

# Manual SDK/NDK path
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

log_level = 2

[buildozer]
warn_on_root = 1
build_dir = .buildozer
log_level = 2
