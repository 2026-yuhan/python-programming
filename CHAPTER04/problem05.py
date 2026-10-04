# 중첩 반복문을 사용하여서 다음과 같이 출력하는 프로그램을 작성하여 보자.

# 실행 결과
"""
정수를 입력하시오: 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

num = int(input("정수를 입력하시오: "))
i = 1

while i  <= num:
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")
    i += 1