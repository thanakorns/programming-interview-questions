def rand7():
    num = 5*(rand5()-1) + rand5()
    if num < 22:
        return num % 7 + 1
    else:
        return rand7()