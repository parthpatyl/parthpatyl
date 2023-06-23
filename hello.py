hello = input("enter text: ")
l = 0
for i in hello:
    l = l + 1
    print(hello[0:l])
for i in hello:
    l = l - 1
    print(hello[0:l])