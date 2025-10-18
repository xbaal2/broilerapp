[app]
# Nama aplikasi
title = BroilerApp
package.name = broilerapp
package.domain = org.iqbalyda
version = 0.1

# File Python utama
source.include_exts = py,png,jpg,kv,json
source.dir = .
source.include_patterns = icons/*

# Requirements
requirements = python3,kivy==2.3.1

# Orientasi layar
orientation = portrait

# Ikon aplikasi
icon.filename = icons/app_icon.png

# Permissions Android (contoh)
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Target Android API
android.api = 33
android.minapi = 26
android.sdk = 33
android.ndk = 25b
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.0'
