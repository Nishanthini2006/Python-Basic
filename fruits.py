def add_fruit():
    fruit = input("Enter fruit name: ")
    f = open("fruits.txt", "a")
    f.write(fruit + "\n")
    f.close()
    print("Added successfully!")

def show_fruits():
    f = open("fruits.txt", "r")
    data = f.read()
    print("\n--- Fruits List ---")
    print(data)
    f.close()

while True:
    print("\n1. Add Fruit\n2. Show Fruits\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_fruit()
    elif choice == "2":
        show_fruits()
    else:
        break
