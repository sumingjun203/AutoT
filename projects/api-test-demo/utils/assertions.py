"""
assertions.py - 自定义断言

封装常用的接口断言逻辑。
"""


def assert_status_code(resp, expected):
    """断言 HTTP 状态码"""
    actual = resp.status_code
    assert actual == expected, f"状态码断言失败: 期望 {expected}, 实际 {actual}"


def assert_json_key(resp, key, expected=None):
    """断言 JSON 响应中包含某个字段"""
    try:
        data = resp.json()
    except Exception as e:
        raise AssertionError(f"响应不是 JSON: {e}")

    assert key in data, f"响应中缺少字段 '{key}': {data}"
    if expected is not None:
        actual = data[key]
        assert actual == expected, f"字段 '{key}' 值不匹配: 期望 {expected}, 实际 {actual}"
    return data[key]


def assert_response_time(resp, max_seconds):
    """断言响应时间"""
    elapsed = resp.elapsed.total_seconds()
    assert elapsed <= max_seconds, f"响应时间超限: {elapsed}s > {max_seconds}s"


def assert_jsonpath(resp, expression, expected=None):
    """使用 JSONPath 提取并断言"""
    from jsonpath import jsonpath

    data = resp.json()
    result = jsonpath(data, expression)
    assert result is not False and result is not None, f"JSONPath '{expression}' 未匹配到数据"
    if expected is not None:
        assert result[0] == expected, f"JSONPath 值不匹配: 期望 {expected}, 实际 {result[0]}"
    return result[0] if result else None