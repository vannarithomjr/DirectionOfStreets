"""
Start by getting the street number
If the street number is even, display Eastbound
If it is not even, display Westbound
Finish the program
"""

def street_calculator(n):
    street_name = " "
    print("Divide:", n/2)
    print("Modulus:", n%2)
    if (n%2) == 0:
        street_name = "Eastbound"

    else:
        street_name = "Westbound"

    return street_name

def main():
    street_number = int(input("Enter the number of the street: "))
    print("That street number belongs to", street_calculator(street_number))

main()