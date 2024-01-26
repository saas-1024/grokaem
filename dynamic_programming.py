print("Input a value")
a = int(input())
print("Input b value")
b = int(input())

list_kekov = []

if a > b:
    while a >= b:
        #  val = b*b
        list_kekov.append(b*b)
        b+=1
else:
    while b >= a:
        #  val = a*a
        list_kekov.append(a*a)
        a+=1

print(list_kekov)

