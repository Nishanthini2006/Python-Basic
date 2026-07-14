def add_contact():
    try:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        
        if not phone.isdigit():
            raise ValueError("Phone number should contain only digits")
            
        with open("contacts.txt", "a") as f:
            f.write(f"{name},{phone}\n")
        print("Contact saved successfully!")
        
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Something went wrong:", e)

def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            data = f.readlines()
        
        if not data:
            print("No contacts found")
        else:
            print("\n--- Contact List ---")
            for line in data:
                name, phone = line.strip().split(",")
                print(f"Name: {name} | Phone: {phone}")
                
    except FileNotFoundError:
        print("No contacts file found. Add contacts first!")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
