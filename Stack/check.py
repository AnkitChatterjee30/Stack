array = [1,2,3,4,5,6]
for i in range(10):
    x=int(input("Enter :"))
    array.append(x)
    if len(array)==10:
        print("Stack overflow")