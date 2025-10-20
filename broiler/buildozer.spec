[app]
title = Broiler
package.name = broiler
package.domain = com.xbaal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy==2.3.0,android
orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 26
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.sdk = 24
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = ~/.buildozer/android/platform/android-sdk

android.release_artifact = bin/Broiler-1.0-release.apk
log_level = 2
p4a.branch = master
buildozer.version = 1.5.0
