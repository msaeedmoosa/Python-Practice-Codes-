sub1 = int(input("Enter First Subject Marks:\n "))
sub2 = int(input("Enter Second Subject Marks:\n "))
sub3 = int(input("Enter Third Subject Marks:\n "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You failed bcz you have less than 33 marks in one of the subjects")

elif(sub1 + sub2 + sub3)/3 < 40:
    print("You failed because your percentage is less than 40")
else: 
    print("Congratulations you passed this exam")
