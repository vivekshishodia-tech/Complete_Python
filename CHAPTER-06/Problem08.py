'''TRINGLE VALIDITY 
Take three angles as input. Check whether they can form a valid triangle.
Condition: All angles must be greater than 0, and their sum must be 180 degrees.'''


angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0:

    if(angle1 + angle2 + angle3 == 180):
        print("valid angle")

    else:
        print("Invalid angle")

else:
    print("invalid angle")