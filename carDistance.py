import numpy as np
from matplotlib.pyplot import imshow, imread
from matplotlib import image
import cv2

def coordinates(pic, y, xf, xm, xe):#Takes a picture and 4 integers as a parameter
    rearCar1 = cv2.circle(pic, (xe,y), radius = 1, color = (0, 0, 255), thickness = -1)#puts one dot of radius 1 and color red on the picture at the specified coordinate
    frontCar1 = cv2.circle(pic, (xf,y), radius = 1, color = (0, 0, 255), thickness = -1)
    frontCar2 = cv2.circle(pic, (xm,y), radius = 1, color = (0, 0, 255), thickness = -1)
    plotted = cv2.imshow('image', pic)#gives picture with plotted points
    return plotted

def calculate(y, xf, xm, xe, carLength):#takes 5 integers as a parameter, 4 of which are coordinates and one is the real world car length
    frontCarFront = np.array((xf,y))
    frontCarRear = np.array((xm,y))
    rearCarFront = np.array((xe,y))
    pixCarLength = np.linalg.norm(frontCarRear - frontCarFront)#by subtracting the front coordinate of a car by the back coordinate and using euclidian distance, we can get the length of the car in pixel distance
    carPixDist = np.linalg.norm(frontCarRear - rearCarFront)#by subtracting the rear coordinate of the first car by the front coordinate of the second and using euclidean distance, we can get the pixel distance between both cars
    pixelToCarRatio = carLength / pixCarLength#the real car length divided by the pixelated car length gives us the appropriate ratio that we can then apply to the distance
    distanceInInches = pixelToCarRatio * carPixDist#we apply the ratio to the pixelated distance to get distance in inches
    return distanceInInches

def enterCord():#this method was created so the if need be, we can continue to ask for coordinates until they are plotted correctly
    yCord = input("Please enter your y coordinate: ")#entering the y coordinate
    yVal = int(yCord)#setting string to int
    front = input("Please enter x coordinate of front of first car: ")#30
    frontVal = int(front)
    middle = input("Please enter x coordinate of the back of the first car: ")#240
    middleVal = int(middle)
    end = input("Please enter x coordinate of the front bumper of the rear car: ")#585
    endVal = int(end)
    return yVal, frontVal, middleVal, endVal#returns a tuple
    


picture1 = input("Please type filename of first picture.")#input file name of first picture
car1 = image.imread(picture1)
cv2.imshow('x', car1)
cv2.waitKey(0)#waits for key press in order to confirm correct picture

picture2 = input("Please type file name of second picture")#input file name of second picture
car2 = image.imread(picture2)
cv2.imshow('y', car2)
cv2.waitKey(0)#waits for key press in order to confirm correct picture

difference = cv2.subtract(car1, car2)#subtracts the two images from eachother so we can see both cars in one image

realCarLength = input("What is the length in inches of your car model?")
realCarLengthVal = int(realCarLength)

tup = enterCord()#calls enter cord and assigns it to a tuple to be used

coordinates(difference, tup[0], tup[1], tup[2], tup[3])#shows picture of both cars with coordinates
cv2.waitKey(0)

while True:#used to continue to loop through to ensure coordinates are properly placed
    yesno = input("Are these coordinates correctly placed? (y/n)")
    if yesno == 'n':#if coodinates are not properply placed, then "enterCord()" is called again to ensure proper placement, then the user is asked for input to see if coordinates are correct
        tup = enterCord()
        combinedPic = coordinates(difference, tup[0], tup[1], tup[2], tup[3])
        cv2.waitKey(0)
        continue
    else:#if the coordinates are correct, we use tup as coordinates in calculate as well as the real car length
        dist = calculate(tup[0], tup[1], tup[2], tup[3], realCarLengthVal)
        distanceInFeet = dist / 12#dividing by 12 gives us the distance in feet as well
        print('The distance between the cars in inches is: ' + str(dist))#transfer dist to string so we can concatenate
        print('The distance between cars in feet is: ' + str(distanceInFeet))
        break