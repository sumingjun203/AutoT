"""
logger.py - 日志封装

使用 loguru 提供简单好用的日志功能。
"""
import sys
from pathlib import Path

from loguru import logger

# 日志目录
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 配置 logger
logger.remove()  # 移除默认 handler

# 控制台输出（带颜色）
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    level="INFO",
)

# 文件输出（按日期切分）
logger.add(
    LOG_DIR / "test_{time:YYYY-MM-DD}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="00:00",  # 每天切分
    retention="7 days",  # 保留 7 天
    encoding="utf-8",
)

__all__ = ["logger"]