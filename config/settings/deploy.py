from config.settings.base_set import *
from json import loads


# deploy_key.json 파일로 secret키 따로 관리.
with open("deploy_key.json", "r", encoding="UTF_8") as f:
    key_list = loads(f.read()) 

def get_key(key, key_list=key_list):
    try:
        return key_list[key]
    except KeyError:
        raise ImproperlyConfigured(f"{key}의 오류입니다.")


SECRET_KEY = get_key("KEY_DJANGO")

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        "ENGINE":   get_key("KEY_DP_DB_ENGINE"),
        "NAME":     get_key("KEY_DP_DB_NAME"),
        "USER":     get_key("KEY_DP_DB_USER"),
        "PASSWORD": get_key("KEY_DP_DB_PASSWORD"),
        "HOST":     get_key("KEY_DP_DB_HOST"),
        "PORT":     get_key("KEY_DP_DB_PORT"),
    }
}