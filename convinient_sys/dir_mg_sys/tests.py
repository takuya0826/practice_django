
import random

# Create your tests here.

list_num = [1]
for i in range(2000):
    num = random.randrange(100000, 999999, 7)
    for j in range(len(list_num)):
        if list_num[j] == num :
           break
        else:
            print("データ追加中")
            list_num.append(num)

for list in list_num:
    print(list_num)
