print("Please Input:")

# Input Prompt Variables
redB = int(input("Red bits: "))
greenB = int(input("Green bits: "))
blueB = int(input("Blue bits: "))
paletteName = input("Name of Palette? ")

# Create Palette File
colorFile = open(paletteName+".gpl","w")

# Create Header in palette File
colorFile.write("GIMP Palette\n")
colorFile.write("Name:"+paletteName+"\n")
colorFile.write("#\n")


totalB = redB + greenB + blueB

binRep = str()
#print("Total bits = " + str(totalB))

for x in range(totalB):
    binRep = binRep + str(1)

# Computation Variables & arrays
totalVal = int(binRep,2)+1
aBinaryList = []

#print(binRep)
#print("Max Value = " + str(int(binRep,2)))
#print("Total Values = " + str(int(binRep,2)+1))

def getMaxValue(bits):
    num = str()
    for x in range(bits):
        num = num + str(1)
    return num

#Get Max Value
redM = int(getMaxValue(redB),2)
greenM = int(getMaxValue(greenB),2)
blueM = int(getMaxValue(blueB),2)

# Create all Binary Values Needed for Color Gen
for x in range(totalVal):
    conv = bin(x)
    remv = conv[-(len(conv)-2):]
    
    if len(str(remv)) < totalB:
        for x in range(totalB-len(remv)):
            remv = '0' + str(remv)

    aBinaryList.append(remv)
    
##Debug    
#print(aBinaryList)
#print(getMaxValue(redB))
#print(getMaxValue(greenB))
#print(getMaxValue(blueB))


for i in aBinaryList:
    #Splitting Actions:
    redS = str(i[:redB])
    greenS = str(i[redB:-blueB])
    blueS = str(i[-blueB:])
    
    #Convert to desc
    redS = int(redS,2)
    greenS = int(greenS,2)
    blueS = int(blueS,2)
    
    #Apply to Range (0-255)
    redV = round(redS/redM * 255)
    greenV = round(greenS/greenM * 255)
    blueV = round(blueS/blueM * 255)
	
	#Write to File each color
    colorFile.write(str(redV) + " " + str(greenV) + " " + str(blueV) + " " + "Color\n")

colorFile.close()
