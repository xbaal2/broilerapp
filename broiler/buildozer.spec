[app]
title = BroilerApp
package.name = broilerapp
package.domain = org.xbaal
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,json
source.include_patterns = icons/*

requirements = python3,kivy==2.3.1,openssl,requests,cython,setuptools
orientation = portrait
fullscreen = 0

icon.filename = icons/icon.png

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 26
android.archs = arm64-v8a,armeabi-v7a
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk

log_level = 2
