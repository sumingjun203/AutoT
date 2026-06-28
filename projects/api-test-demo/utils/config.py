"""
config.py - 配置管理
"""
import os
from pathlib import Path

import yaml


# 项目根目录
ROOT_DIR = Path(__file__).parent.parent
CONFIG_FILE = ROOT_DIR / "config" / "config.yaml"


def load_config():
    """加载全局配置"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


# 全局配置对象
CONFIG = load_config()

# 基础 URL
BASE_URL = os.getenv("API_BASE_URL", CONFIG.get("base_url", "https://reqres.in/api"))

# 超时
TIMEOUT = CONFIG.get("timeout", 10)

# API Key
API_KEY = CONFIG.get("auth", {}).get("api_key", "reqres-free-v1")