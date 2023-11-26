from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET = 'django-insecure--&!5diwm9c7%^vaehpo)a9z*#x*nm99upak=kwd00&teeog7ak'
# 꼭 변수명이 SECRET일 필요는 없으나, SECRET_KEY에 대한 내용이니 통일성을 유지하자

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# 마찬가지로 변수명이 database일 필요는 없으나 통일성 유지!