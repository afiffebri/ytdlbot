#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - config.py
# 8/28/21 15:01
#

__author__ = "Afif.afiffebriandy@gmail.com>"

import os

# general settings
WORKERS: "int" = int(os.getenv("WORKERS", 100))
PYRO_WORKERS: "int" = int(os.getenv("PYRO_WORKERS", 100))
APP_ID: "int" = int(os.getenv("APP_ID", 
23533320))
APP_HASH = os.getenv("APP_HASH", "d011d4627744d8d86c57b7acd8a47169")
TOKEN = os.getenv("TOKEN", "6279088232:AAFDvXnnma8ux-VH7OgkmVcSnz1JfY_YCF4")

REDIS = os.getenv("REDIS")

# quota settings
QUOTA = int(os.getenv("QUOTA", 5 * 1024 * 1024 * 1024))  # 5G
if os.uname().sysname == "Darwin":
    QUOTA = 10 * 1024 * 1024  # 10M

TG_MAX_SIZE = 2 * 1024 * 1024 * 1024 * 0.99
# TG_MAX_SIZE = 10 * 1024 * 1024

EX = int(os.getenv("EX", 24 * 3600))
MULTIPLY = os.getenv("MULTIPLY", 10)  # VIP1 is 5*5-25G, VIP2 is 50G
USD2CNY = os.getenv("USD2CNY", 6)  # $5 --> ¥30

ENABLE_VIP = os.getenv("VIP", False)
MAX_DURATION = int(os.getenv("MAX_DURATION", 60))
AFD_LINK = os.getenv("AFD_LINK", "https://afdian.net/@BennyThink")
COFFEE_LINK = os.getenv("COFFEE_LINK", "https://www.buymeacoffee.com/bennythink")
COFFEE_TOKEN = os.getenv("COFFEE_TOKEN")
AFD_TOKEN = os.getenv("AFD_TOKEN")
AFD_USER_ID = os.getenv("AFD_USER_ID")
OWNER = os.getenv("OWNER", "Afiffebri")

# limitation settings
AUTHORIZED_USER: "str" = os.getenv("AUTHORIZED_USER", "")
# membership requires: the format could be username/chat_id of channel or group
REQUIRED_MEMBERSHIP: "str" = os.getenv("REQUIRED_MEMBERSHIP", "")

# celery related
ENABLE_CELERY = os.getenv("ENABLE_CELERY", False)
ENABLE_QUEUE = os.getenv("ENABLE_QUEUE", False)
BROKER = os.getenv("BROKER", f"redis://{REDIS}:6379/4")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASS = os.getenv("MYSQL_PASS", "root")

AUDIO_FORMAT = os.getenv("AUDIO_FORMAT")
ARCHIVE_ID = os.getenv("ARCHIVE_ID")

IPv6 = os.getenv("IPv6", False)
ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", True)
# 0.01 means basically no limit
RATE = float(os.getenv("RATE", 0.01))
BURST = int(os.getenv("BURST", 3))
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN") or "1234"
PLAYLIST_SUPPORT = os.getenv("PLAYLIST_SUPPORT", True)
ENABLE_ARIA2 = os.getenv("ENABLE_ARIA2", True)
