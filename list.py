friends = ["Pabel", "Biplop", "Forid", "Rakib", "Sabuj"]
print(friends)
print(friends[1]) #index
print(friends[1:])
print(friends[2:4])
friends[0] = "Nasif"
print(friends)
print(friends[-1])
age =[21,24,28,30]
friends.append(age)
print(friends)
friends.remove("Forid")
print(friends)
friends.pop() # pop eliminates last value from a list
print(friends)
print(friends.index("Sabuj"))
friendsNew = friends.copy()
print(friendsNew)


