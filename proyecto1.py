def prob_1(n):
	r=n%2==0
	return r

def prob_2(F):
	c=(F-32)*5/9
	return c

def prob_3(B,P):
	r=B
	for i in range (P-1):
		r=B*P
	return r

def prob_4(n,F):
	h=list(F)
	largo=len(F)
	jamon=(n-largo)//2
	r=("*"*jamon+F+"*"*jamon)
	return r


def prob_5(l1, l2):
	a=l1[2]*l2[1]-l1[1]*l2[1], l1[2]*l2[0]-l1[0]*l2[2], l1[0]*l2[2]-l1[2]*l2[2]
	return a

