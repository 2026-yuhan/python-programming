# 패스워드를 검증하는 함수 checkPass(p)를 작성하고 테스트하라.
# 패스워드는 적어도 8글자 이상이어야 하며,
# 적어도 1글자의 대문자와 소문자, 1개의 숫자가 들어가야 한다.

# 실행 결과
"""
패스워드를 입력하시오: abcdefgh
사용할 수 없습니다. 다시 입력하세요!

패스워드를 입력하시오: abcdefG1
사용할 수 있습니다.
"""

def checkPass(p):
    if len(p) < 8:
        return False

    upper = False
    lower = False
    digit = False

    for c in p:
        if c.isupper():
            upper = True
        elif c.islower():
            lower = True
        elif c.isdigit():
            digit = True

    return upper and lower and digit

while True:
    p = input("패스워드를 입력하시오: ")

    if checkPass(p):
        print("사용할 수 있습니다.")
        break
    else:
        print("사용할 수 없습니다. 다시 입력하세요!")