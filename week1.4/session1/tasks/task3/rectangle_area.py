
# function implementation

def rectangle_area(width, height ):  # define suitable input data
    area = width * height            # implement the function
    return area                      # return an appropriate value

def produceList(length):
    numberList = []
    i = 0
    while(i <= length):
        numberList.append(i)
        i = i+1
    return numberList

def findMean(intList):
    totalNumbers = 0
    totalValue = 0
    for num in intList:
        totalValue = totalValue + num
        totalNumbers = totalNumbers + 1
    return(totalValue/totalNumbers)


intList = [1,2,3,4,5,6,7,8]

print(findMean(intList))

length = int(input("Enter length of list: "))
print(produceList(length))

# testing the function
width = int(input("Enter width: "))
height = int(input("Enter hight: "))

print(f"Area is {rectangle_area(width, height)}")   # provide suitable data matching your inputs

