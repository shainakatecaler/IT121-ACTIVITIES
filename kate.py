# Create Empty List
users = []

while True:
    print("\n==== USER MANAGEMENT SYSTEM ====")
    print("1. Show Users")
    print("2. Add Users")
    print("3. Update Users")
    print("4. Delete Users")
    print("5. Exit")
    
    choice = input("Enter your choice : (1-5):")
    
    # Show Users
    if choice == "1":
        if len(users) == 0:
            print("No users found.")
        else:
            print("\nUser List:")
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
                
    # Add Users
    elif choice == "2":
        new_user = input("Enter new user name: ")
        users.append(new_user)
        print(f"User added successfully.")
        
    # Update Users
    elif choice == "3":
        if len(users) == 0:
            print("No users to update. ")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            try:
                num = int(input("Enter user name number to update: "))
                if 1 <= num <= (len(users)):
                    new_name = input("Enter new name: ")
                    users[num - 1] = new_name
                    print(f"User updated successfully.")
                else:
                    print("Invalid input.")
            except:
                print("Invalid input.")
                
    # Delete User
    elif choice == "4":
        if len(users) == 0:
            print("No users to delete.")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            try:
                num = int(input("Enter user number to delete: "))
                if 1 <= num <= len(users):
                    removed = users.pop(num - 1)
                    print(f"{removed} deleted successfully. ")
                else:
                    print("Invalid input.")
            except:
                print("Invalid input.")
                    
    # Exit
    elif choice == "5":
        print("Exiting the program..")
        break
    
    else:
        print("Invalid choice. Please again.")
