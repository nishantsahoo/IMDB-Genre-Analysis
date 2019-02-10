import string

list_1 = ['Horror', ' Horror']
for i in range(0, len(list_1)):
	list_1[i] = list_1[i].strip()

print(list_1)
print(" Horror")
print(" Horror".lstrip())