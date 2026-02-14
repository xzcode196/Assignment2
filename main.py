import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    machine = SandwichMaker(resources)

    while True:
        choice = input("what would you like? (small/ medium/ large/ off/ report: ").lower()

        if choice == "off":
            print("Machine is turning off.")
            break

        elif choice == "report":
            machine.report()

        elif choice in recipes:
            sandwich = recipes[choice]
            if machine.check_resources(sandwich["ingredients"]):
                payment = machine.process_coins()
                if machine.transaction_result(payment, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])

        else:
            print("Invalid selection. Please choose again.")

if __name__=="__main__":

    main()
