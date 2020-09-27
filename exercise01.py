"""
1.匹配一个.com邮箱格式字符串
2.匹配一个密码 8-12位 数字字母下划线构成
3.匹配一个数字,包含整数 小数  正数  负数  分数1/2  百分数 4.6%
4.匹配一段文字中以大写字母开头的单词,注意文字中可能含有 iPython 这种,不算大写字母开头, H-base这种算大写字母开头,  BSD 也是
"""

import re

str01 = "lvze@163.com"
print(re.findall(r"\w+@\w+\.com", str01))

str02 = "Tedu01234"
print(re.findall(r"\w{8,12}", str02))

str03 = "1 -21 12.5 -12.87 1/3 4.6%"
print(re.findall(r"-?\d+\.?/?\d*%?", str03))

str04 = "Hello iPython H-base BSD."
print(re.findall(r"\b[A-Z][A-Za-z_-]*\b", str04))
