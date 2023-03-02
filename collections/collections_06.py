dict1 = {"aa": 77, "bb": 666}

dict1["alex"] = 42
print(dict1)

print(dict1["alex"])

dict1["alex"] = 55
print(dict1["alex"])

dict1.pop("alex")
print(dict1)
