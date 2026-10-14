marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 75:
    print("Grade A")

elif marks >= 50:
    print("Grade B")

else:
    print("Grade C")