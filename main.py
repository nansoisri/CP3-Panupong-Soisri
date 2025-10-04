#read
file = open("demo.txt", "r")
print(file.read())

#write
file = open("demo.txt", "w")
file.write("Haha From Next Lecture")

#append
file = open("demo.txt", "a")
file.write("Haha From Next Lecture")

#cre
file = open("demo1.txt", "x")
file.write("Haha From Next Lecture")
