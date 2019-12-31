meat = input(
    "Menu:\n     1 - Beef (well done) \n     2 - Chicken \n     3 - Lamb \n     4 - Pork \nType your choice: "
)

weight = int(input("Enter the weight of the meat(kg): "))


if meat == "1":
    time = weight * 50 + 20
    print("The cooking time for a piece of Beef (well done) that weighs {0} Kg is {1} minutes".format(weight, time))
if meat == "2":
    time = weight * 45 + 20
    print("The cooking time for a piece of Chicken that weighs {0} Kg is {1} minutes".format(weight, time))
if meat == "3":
    time = weight * 60 + 30
    print("The cooking time for a piece of Lamb that weighs {0} Kg is {1} minutes".format(weight, time))
if meat == "4":
    time = weight * 70 + 35
    print("The cooking time for a piece of Pork that weighs {0} Kg is {1} minutes".format(weight, time))
