from traceback import format_exc


"{}".format(10)
"{} {}".format(10,20)
s = "name: {} , number {} , soccer: {}"
print(s.format("SON",7,True))
format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 연봉 {}만 원 만들기".format(5000)
format_c = "{}과 {}학년 학생? {}".format("정보통신",3,True)
print(format_a)
print(format_b)
print(format_c)
