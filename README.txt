Victor Cintra
November 2022

Car Distance Finder
This program finds the distance traveled by a car. Begin by taking any video of a car moving and screenshotting the beginning and end. The program takes user input of the first photo, second photo, real life car length, and coordinates for three different points on the car. From here, it subtracts both photos from eachother so that we can see both cars on one photo. It then uses Euclidian distance to find the pixel distance between both the cars as well as the length of the car. By dividing the real world length of the car by the pixel distance, we are given a ratio of inches to pixels on the image. We then can apply the ratio to the Euclidan distance between both cars to find the distance traveled.

To run the program with the example images provided:
Upload the images
First picture is "Beginning.png"
Second picture is "End.png"
Y coordinate = 450
Front x coordinate for first car = 30
Rear x coordinate for first car = 240
Front x coordinate for second car = 585
Length of car (Ferrari 458) = 180

In this example, I used a Top Gear video of a Ferrari 458. We know that a Ferrari 458 is 180 inches long, and that the pixel length is 210. By dividing, we get a ratio of 0.857 that we can then multiply to the distance traveled by the car.

In reality, this program could be used to find the distance between any two moving objects as long as you have the measurement for an object in the image and a steady camera.
