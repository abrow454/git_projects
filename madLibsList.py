def printRequest(request):
    for x in (request):
        input ("Give me a "+ x)
    return input

#main
print("Give us the following things for our Mad Lib!")
request = ["adjective: " , "animal: " , "vehicle: " , "verb: " , "color: " , "noun: " , "1st food: " , "2nd food: " , "person: " , "saying: "]
print(printRequest(request))