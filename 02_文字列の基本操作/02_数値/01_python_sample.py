def myfunc(num):
    if num % 2 == 0:
    	return "偶数です"
    return "奇数です"

for i in range(1, 10):
    print(str(i) + "は" + myfunc(i))
