print("This Program wil compute student average: ")

Prelims = float(input("Enter your prelims score here: "))
Midterms = float(input("Enter your midterms score here: "))
Semis = float(input("Enter your semis score here: "))
Finals = float(input("Enter your finals score here: "))

avg = (Prelims+Midterms+Semis+Finals)/4

avg=("Your average is {}!".format(avg))
if avg>=75:
    print("You passed!")
elif avg<75:
    print("You have failed.")

    if avg>=75:
        print("You passed!")
    if avg>=99 and avg<=100:
        print("Your grade is A!")
    elif avg>=90 and avg<=98:
        print("Your grade is B!")
    elif avg>=80 and avg<=89:
        print("Your grade is C!")
    elif avg>=75 and avg<=79:
        print("You have failed.")
    if avg>=71 and avg<=74:
        print("Your grade is D.")
    elif avg>=61 and avg<=70:
        print("Your grade is E.")