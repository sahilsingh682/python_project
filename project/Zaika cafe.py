# from art import logo
#print(logo)
print("welcome in Zaika")
menu = {
    "chowin" : 70,
    "cold drink:": 50,
    "cicken rice":130,
    "biryani": 140,
    "roasted chicken": 250,
    "pasta": 70,
    "cold coffrr": 60,
    "chhola rice": 60,
    "sandwitch": 20

}
print("our menu:")
print("----------")
total_order = 0
for item, price in menu.items():
    print(f"{item} : Rs.{price}")

next_order = True
while next_order:
     order = input("Enter the name of item you want added in order").lower()
     if order in menu:
         total_order += menu[order]
         print(f"{order} added in your order")
         another_order = input("Do you want to add another item? press(yes/no").lower()
         if another_order == 'yes':
            next_order = True
         else:
             next_order = False
     else:
         print(f"{order} is not available")
         anoter_order = input("Do you want to add another item? press(yes/no)").lower()
         if another_order == 'yes':
              next_order = True
         else:
             next_order = False

print(f"your total bill is : Rs.{total_order}")
    

