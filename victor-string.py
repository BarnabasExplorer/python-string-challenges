str= "This is the ultimate string"

length= len(str)
print(length)
print(str[0])
print(str[1])
print(str[0]+str[1])
print(str[0:2])
print(str[8:11])
print(str[21:27])

#index=str.find("string")
#print(index)

#x=input("what do you wont to find")
#index=str.find(x)
#print(index)

index1=str.find(" ")


str2 = str[(index1+1):length]
print(str2)

index2 = str2.find(" ")
print(index2)

finalIndex = index1 + index2 + 1
print(finalIndex)












#str2=str[5:length]
#print(str2)
#print(str2.find(" "))

      
