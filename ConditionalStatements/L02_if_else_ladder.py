eng=float(input("Enter Your English Number\n"))
urdu=float(input("Enter Your Urdu Number\n"))
mathematics=float(input("Enter Your Math Number\n"))
islamicStudies=float(input("Enter Your Islamic Studies Number\n"))
chemistry=float(input("Enter Your Chemistry Number\n"))


obtained_marks=eng+urdu+mathematics+islamicStudies+chemistry
print("Obatined Marks",obtained_marks)
percentage=obtained_marks/500*100

print("Percentage ",percentage )


if percentage <=100 and percentage >=80:
    print("Grade A1")
elif percentage <=79 and percentage >=70:
    print("Grade A")
elif percentage <=69 and percentage >=60:
    print("Grade B")
elif percentage <=59 and percentage >=50:
    print("Grade C")
elif percentage <=49 and percentage >=40:
    print("Grade D")
else:
    print("IU Jaien")




