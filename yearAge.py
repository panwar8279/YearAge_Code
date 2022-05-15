# Program to know your Age in Python
# Author=Pratigya Panwar

yearAge=int(input("What is your Age/year of birth\n"))
isAge=False
isYear=False

if len(str(isYear))==4:
    isYear=True

else:
    isAge=True

if(isYear<1900 and isAge>150):
    print("You seems to be old person alive")
    exit()
if(isYear>2022):
    print("You are not yet born")

if isAge:
    yearAge=2022-yearAge

print(f"you will be 100 years old in {yearAge+100}")

interestedYear=int(input("Enter the year you want to know your Age in\n"))
print(f"you will be {interestedYear-yearAge} years old in {interestedYear}")