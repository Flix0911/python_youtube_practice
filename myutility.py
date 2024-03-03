# control flow / if statements
# """ allows you to work in multiple lines

choice = input("""
                What do you want to do today? 
               a) calculate tip
               b) calculate tax
               """)

# if takes a boolean expression
# start a block with :
# python handles on alignment / indentation
if(choice == "a"):
    bill = int(input("How much was the bill?: "))
    tip = bill * .2
    print(f"The tip is {tip} for a total bill of {bill + tip}")
# else if - elif
elif(choice == "b"):
    tax = int(input("What is the tax amount?: "))
    bill = int(input("How much was the bill?: "))
    print(f"The tax would be {bill * (tax / 100)}")
# else
else:
    print("you did not choose a or b")
