file_one = open("newFile.txt", "r") # r for read, w for write, a for append
#print(file_one.readable())
#file_one.write("\nHello Mango People")
#print(file_one.read())
#print(file_one.read()[6])
#print(file_one.readline())
#print(file_one.readlines())
print(file_one.readlines()[2])
file_one.close()

