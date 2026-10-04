# 사용자로부터 두 개의 정수를 입력받아서 최대 공약수를 찾는 함수를 작성해보자.
# 가장 간단한 알고리즘을 생각하자.

# 실행 결과
"""
첫 번째 정수: 36
두 번째 정수: 12
12
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))

print(gcd(a, b))