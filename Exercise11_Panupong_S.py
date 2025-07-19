number = int(input())
for i in range(number):
    space = " "*int(((number*2)-2)/2)
    text = ((i*2)+1)*"*"
    print(space,text,space)
    number -=1

