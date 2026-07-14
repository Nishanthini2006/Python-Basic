def add_fruit():
    fruit = input("Enter fruit name: ")
    with open("fruits.txt", "a") as f:
        f.write(fruit + "\n")
    print(f"{fruit} added successfully!")

def view_fruits():
    try:
        with open("fruits.txt", "r") as f:
            data = f.read()
        print("\n--- Fruits List ---")
        print(data if data else "No fruits added yet")
    except FileNotFoundError:
        print("No fruits file found. Add some fruits first!")

while True:
    print("\n1. Add Fruit")
    print("2. View Fruits")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_fruit()
    elif choice == "2":
        view_fruits()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
