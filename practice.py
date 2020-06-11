#The Global list variable
cart = []
#creating function that adds items to the cart
def AddItem(item):
    cart.append(item)
    print(f"{item}, has been added")
#creating function that removes itwm from the cart
def RemoveItem(item):
    try:
        cart.remove(item)
        print(f"The {item} has been removed")
    except:
        print(f"Sorry, this {item} could not be removed")
# creatin a function that shows the items in the cart
def showItems():
    if cart:
        print("Here is your cart")
        for item in cart:
            print(f"{item}")
    else:
        print("Your cart is empty")
# clearing the motherfucking cart
def Clearcart():
    cart.clear()
    print("Your cart is empty")
# creat main function that loops till the user quits
def main():
    done = False 
    while not done:
        ans = "add"
        if ans = "quit":
            print("Thanks for using our program")
            showItems()
            done = True
        
main()

   




    
        