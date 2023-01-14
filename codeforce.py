def check(l1,l2,l3):
	for i in range(9):
		for j in range(1,10):
			if j not in l1[i] or j not in l2[i] or j not in l3[i]:
				return 0
	return 1


for t in range(int(input())):
	l1=[list(map(int,input().split())) for _ in range(9)]
	l2=[[l1[j][i] for j in range(9)] for i in range(9)]
	l3=[[l1[(i//3)*3+(j//3)][(i%3)*3+(j%3)] for j in range(9)] for i in range(9)]
	print('#'+str(t+1)+' '+str(check(l1,l2,l3)))