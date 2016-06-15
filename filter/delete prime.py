#删除1~100的素数
def f(n):
	for m in range(2,n/2) :   //和比它的一半小数相除，如果都除不尽，证明素数
		if n % m == 0 :
			return False
	return n

print filter(f,range(1,101))
