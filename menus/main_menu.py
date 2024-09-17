from utils.console import Console

def display_main_menu() -> int:
    """Display the main menu and handle user choice."""
    Console.clear_console()
    Console.print_title("Main Menu")
    
    print("1. Manage Items")
    print("2. Manage Values")
    print("3. View Values")
    print("4. Exit")
    
    try:
        choice = int(input("Select an option: "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid option")
        return choice
    except ValueError as e:
        Console.print_error(f"Error: {e}")
        return 0
