#basic dictionary syntax



myDict={
"name":"alishan",
"class":"mca",
"college":"its college"
}

print(type(myDict))


print(myDict)

for key in myDict:
    print(key)

for item in myDict:
    print(myDict[item])


print(myDict.get("name"))