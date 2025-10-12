import re

def contains_url(s):
    # 常见URL正则表达式
    url_pattern = re.compile(
        r'[a-zA-Z][a-zA-Z0-9+.-]*:\/\/[^\s/$.?#]+[^\s]*', re.I
    )
    return url_pattern.findall(s)

# 示例用法
s = input()

print(contains_url(s))