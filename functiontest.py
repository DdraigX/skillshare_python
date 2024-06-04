# number = 10

# def fModifyNumb(number):
#     print("Argument passed in = ", number)
#     number = number * 10
#     print("After mod = ", number)
#     return 


# fModifyNumb(number)


# number2 = 11

# def fReassignNumb(number2):
#     print("passed in ",number2)
#     number2 = number + number2
#     #number2 = 3.14
#     print("after assign ", number2)
#     return

# print("val",number2)

# fReassignNumb(number2)
# print(number2)


# def calculatedAreaofCirc(radius):
#     area = 3.14 * radius * radius
#     return area

# radius = float(input("whats the radius?"))
# area = calculatedAreaofCirc(radius)

# print("Radius = ", radius, "Area = ", area)


# def PrintAreaofCirc(radius):
#     print("A circle radius = ", radius, "Area = ", (3.14*radius*radius) )

# PrintAreaofCirc(radius)

# resultsList = []

# def calcAreaofCircles(radiuslist):
#     for i in radiuslist:
#         resultsList.append(3.14*i*i)
#     return resultsList

# radiuslist = [1, 2, 4, 5]
# areaList = calcAreaofCircles(radiuslist)

# print("circle radius =", radiuslist, " area = ", areaList)


print("  ")

radiuslist = [1, 2, 4, 5]

def calcAreaandCirc(radiuslist):
    areaResultlist = []
    circresultlist = []
    resultHash = {'Areas':areaResultlist,'Circ':circresultlist}
    
    for i in radiuslist:
        areaResultlist.append(3.14*i*i)
        circresultlist.append(3.14*2*i)
    return resultHash


resultMap = calcAreaandCirc(radiuslist)

print("circle raidius ", radiuslist,"\n Areas = ",resultMap['Areas'],"\n Circ = ",resultMap['Circ'] )


