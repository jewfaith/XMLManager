from menus.main_menu import display_main_menu
from repositories.xml_repository import XMLRepository

def main() -> None:
    """Main function to run the application."""
    repository = XMLRepository('script.xml')
    
    while True:
        choice = display_main_menu()
        if choice == 1:
            from menus.items_menu import handle_items_menu
            handle_items_menu(repository)
        elif choice == 2:
            from menus.values_menu import handle_values_menu
            handle_values_menu(repository)
        elif choice == 3:
            from menus.view_values_menu import display_values_menu
            display_values_menu(repository)
        elif choice == 4:
            break

if __name__ == "__main__":
    main()
