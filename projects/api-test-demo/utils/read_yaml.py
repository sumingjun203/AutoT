"""
read_yaml.py - YAML 工具

封装 YAML 文件读取逻辑。
"""
from pathlib import Path

import yaml


def read_yaml(file_path):
    """读取 YAML 文件"""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"YAML 文件不存在: {file_path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_test_data(category, key=None):
    """
    从 data/ 目录读取测试数据
    :param category: 数据分类（如 user / auth / order）
    :param key: 数据键（可选，如果指定则返回该 key 下的数据）
    """
    base = Path(__file__).parent.parent / "data"
    files = {
        "user": base / "user_data.yaml",
        "auth": base / "auth_data.yaml",
        "order": base / "order_data.yaml",
    }
    if category not in files:
        raise ValueError(f"未知数据分类: {category}，可选: {list(files.keys())}")

    data = read_yaml(files[category])
    if key:
        return data.get(key, [])
    return data