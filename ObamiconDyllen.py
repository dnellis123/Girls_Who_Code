from PIL import Image

#Import the Image
myImage = Image.open("Dyllen.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation

for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    intensity = red+green+blue

    if intensity<182: #darkBlue
        red = 0
        green = 51
        blue = 76
    elif 182<intensity<364: #red
        red = 217
        green = 26
        blue = 33
    elif 364<intensity<520: #lightBlue
        red = 112
        green = 150
        blue = 158
    else: #yellow
        red = 252
        green = 227
        blue = 166

    p = (red,green,blue)


    #add pixel to new pixel list
    newPixelList.append(p)
    

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
