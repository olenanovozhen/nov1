import random
a: list[int] = [random.randint(0,15) for i in range(15)]
print(a)
a_filtered = []
for num in a:
    if num == 2:
        a_filtered.append(num)
print(a_filtered)
na = a.count(2)
print("na = ", na)
element = int(input())
if element in a:
    print(element, 'exists in the list')
else:
    print(element, 'is not in the list')


int(input())
























