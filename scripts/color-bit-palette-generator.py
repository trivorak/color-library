print("Please Input:")

# Input Prompt Variables
redB = int(input("Red bits: "))
greenB = int(input("Green bits: "))
blueB = int(input("Blue bits: "))

totalB = redB + greenB + blueB

binRep = str()
print("Total bits = " + str(totalB))

for x in range(totalB):
    binRep = binRep + str(1)

# Computation Variables & arrays
totalVal = int(binRep,2)+1
aBinaryList = []

print(binRep)
print("Max Value = " + str(int(binRep,2)))
print("Total Values = " + str(int(binRep,2)+1))

# Create all Binary Values Needed for Color Gen
for x in range(totalVal):
    conv = bin(x)
    remv = conv[-(len(conv)-2):]
    
    if len(str(remv)) < totalB:
        for x in range(totalB-len(remv)):
            remv = '0' + str(remv)

    aBinaryList.append(remv)
    
#Debug    
print(aBinaryList)

#     Splitting Actions:
#     print("Red = " + str(remv[:redB]))
#     print("Green = " + str(remv[redB:-blueB]))
#     print("Blue = " + str(remv[-blueB]))