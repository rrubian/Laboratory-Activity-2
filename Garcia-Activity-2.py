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