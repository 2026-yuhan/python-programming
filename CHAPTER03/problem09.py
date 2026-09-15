# 본문에서 덧셈 퀴즈를 자동으로 생성해보았다.
# 이번에는 덧셈, 뺄셈, 곱셈, 나눗셈 중에서 하나를 랜덤하게 선택하고
# 피연산자도 난수로 생성하여 사용자에게 제시하고 사용자의 답을 자동으로 채점하는 프로그램을 작성해보자.

# 실행 결과
"""
1 / 5의 값은?: 0.2
맞았습니다.

7 + 5의 값은?: 12
맞았습니다.
"""

import random

operator = ["+", "-", "x", "/"]

for i in range(2):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(0,3)

    answer = int(input(f"{num1} {operator[num3]} {num2}의 값은?: "))

    match operator[num3]:
        case "+": correct = answer == num1 + num2
        case "-": correct = answer == num1 - num2
        case "x": correct = answer == num1 * num2
        case "/": correct = answer == num1 / num2
        
    print(f"{"맞았습니다." if correct else "틀렸습니다."}")
        
