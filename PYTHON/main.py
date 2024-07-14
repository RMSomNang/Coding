# print("Hello World")

# def twoequalnumber(x,y):
#     if x == y:
#         print(True)
#     else:
#         print(False)

# twoequalnumber(10,10)

x = ["RM", "SAMNANG", "CHRISTIANO", "MESSI"]
y = [20,30,40,50]
z = len(x)
a = [10,20,30,40,50,60]

# while z > 0:
#     print(x[z-1])
#     z -= 1

# for i in range(len(x)):
#     print(x[i])

dictionary = {"RM": 23, "RONALDO": 38, "HERO": 90}
dictionary.update({"SAMNANG": 20})
print(dictionary)

dictionary.popitem()
print(dictionary)

dictionary.pop("RM")
print(dictionary)

if dictionary.__contains__("RONALDO"):
    print("Has Ronaldo.")
else:
    print("Do not have.")