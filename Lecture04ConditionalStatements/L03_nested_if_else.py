name=input("Enter Your Name \n")
email=input("Enter Your Email \n")
password=input("Enter Your Password \n")
contact=input("Enter Your Contact \n")

print("account successfully created")

emailLogin=input("Enter Your Login Email \n")
passwordLogin=input("Enter Your Login Password \n")


if email== emailLogin and password== passwordLogin:
    print("Welcome  ", name)

    year=int(input("Enter Your Year\n"))
    if year %4==0:
        print("Leap Year")
    else:
        print("Is not Leap Year")

    num1=int(input("Enter Your Number \n"))

    if num1<0:
        print("negative")
    else:
        print("positive")
else:
    print("Incorrect email or password")