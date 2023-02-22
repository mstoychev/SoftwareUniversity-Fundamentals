# lst = list(map(int, input().split()))
# average = sum(lst) / len(lst)
# top = sorted([x for x in lst if x > average], reverse=True)
#
# if top:
#     print(*top[0:5], sep=" ")
# else:
#     print("No")

lst = list(map(int, input().split()))
average = sum(lst) / len(lst)
top = sorted([x for x in lst if x > average])   #whithout reversing the list
if top:
    print(*top[-5:][-1::-1])  #slicing
else:
    print("No")
