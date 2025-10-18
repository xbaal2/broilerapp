[app]
# Nama aplikasi
title = BroilerApp
package.name = broilerapp
package.domain = org.iqbalyda

# Versi aplikasi
version = 0.1

# File Python utama
source.include_exts = py,png,jpg,kv,json
source.dir = .
source.include_patterns = icons/*

# Requirements Python + Kivy
requirements = python3,kivy==2.3.1

# Orientasi
orientation = portrait

# Ikon APK (launcher Android)
icon.filename = icons/icon.png

# Permissions Android (optional)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Versi minimum SDK Android
android.minapi = 26

# Format build
# debug: bisa langsung install ke HP tanpa signature release
# release: untuk Play Store
build_type = debug

# Package Android
android.arch = arm64-v8a


[buildozer]
log_level = 2
warn_on_root = 1
