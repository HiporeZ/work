
print(a+b)
a,b = map(int, input().split())

print(a+b)
with open("input.txt", "r") as f:
    a, b = map(int, f.readline().split())


with open("output.txt", "w") as f2:
	f2.write(str(a+b))