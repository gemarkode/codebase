lis =[]
n = int(input("Banyak: "))
a = list(map(int,input("\nIsi : ").strip().split()))[:n]

for i in a:
	x = oct(i)
	lis.append(x)

print('angka dalam octal: ', lis)
