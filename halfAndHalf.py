from PIL import Image

#FUNCTIONS
newPixelList = []

def doubleRed(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*2
    if newRed>255:
        newRed = 255

    newGreen = green
    if newGreen>255:
        newGreen = 255

    newBlue = blue
    if newBlue>255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)

    #add pixel to new pixel list
    newPixelList.append(p)

def blackWhite(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    avg=(red+blue+green)//3

    newRed = avg
    if newRed>255:
        newRed = 255

    newGreen = avg
    if newGreen>255:
        newGreen = 255

    newBlue = avg
    if newBlue>255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)


    #add pixel to new pixel list
    newPixelList.append(p)

def overExpose(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newRed = red*3
    if newRed>255:
        newRed = 255

    newGreen = green
    if newGreen>255:
        newGreen = 255

    newBlue = blue*2
    if newBlue>255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)


    #add pixel to new pixel list
    newPixelList.append(p)

def doubleBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newRed = red
    if newRed>255:
        newRed = 255

    newGreen = green
    if newGreen>255:
        newGreen = 255

    newBlue = blue*2
    if newBlue>255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)


    #add pixel to new pixel list
    newPixelList.append(p)

##RUNNING CODE
#Import the Image
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

length = len(pixelList)
thirdWay = length//3
twoThirdWay = thirdWay*2

counter = 0

for pixel in pixelList:
    #pixel manipulation
    if (counter < thirdWay): #this is the top half of the photo
        doubleRed(pixel)
    elif (counter < twoThirdWay):
        blackWhite(pixel)
    else: #this is the bottom half of the photo
        doubleBlue(pixel)
    counter += 1

    



    #create new pixel



    #add pixel to new pixel list
##    newPixelList.append(p)

    

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
