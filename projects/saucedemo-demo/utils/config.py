"""
config.py - 配置管理

从环境变量 / yaml 文件读取配置
"""
import os
from pathlib import Path

import yaml

# 项目根目录
ROOT_DIR = Path(__file__).parent.parent


def load_config():
    """加载配置文件（如果存在）"""
    config_path = ROOT_DIR / "config.yaml"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


# 全局配置
CONFIG = load_config()

# 浏览器配置
BROWSER = os.getenv("BROWSER", CONFIG.get("browser", "chrome"))
HEADLESS = os.getenv("HEADLESS", str(CONFIG.get("headless", True))).lower() == "true"
BASE_URL = os.getenv("BASE_URL", CONFIG.get("base_url", "https://www.saucedemo.com/"))

# 超时配置
IMPLICIT_WAIT = CONFIG.get("implicit_wait", 5)
EXPLICIT_WAIT = CONFIG.get("explicit_wait", 10)