# 원의 둘레를 계산하는 함수 get_peri(radius)를 정의하고 테스트하라.
# 만약 원의 반지름이 주어지지 않았다면 5.0으로 간주한다. 함수의 기본 인수를 사용하라.

# 실행 결과
"""
get_peri() = 31.416
get_peri(4.0) = 25.133
"""

import math

def get_peri(radius=5.0):
    return 2 * math.pi * radius

print(f"get_peri() = {get_peri():.3f}")
print(f"get_peri(4.0) = {get_peri(4.0):.3f}")