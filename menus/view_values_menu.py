from utils.console import Console
from repositories.xml_repository import XMLRepository

def display_values_menu(repository: XMLRepository) -> None:
    """Display values from a selected item."""
    Console.clear_console()
    Console.print_title("View Values")

    root = repository.get_root()
    items = root.findall('item')

    if not items:
        Console.print_warning("No items available to view values")
        input()
        return

    while True:
        Console.clear_console()
        Console.print_title("Select Item to View")

        print("1. Back to Main Menu")
        for index, item in enumerate(items, start=2):
            print(f"{index}. {item.get('name')}")

        try:
            selection = int(Console.prompt("Select an option"))

            if selection == 1:
                break
            elif 2 <= selection < 2 + len(items):
                item_index = selection - 2
                selected_item = items[item_index]

                Console.clear_console()
                Console.print_title(f"{selected_item.get('name')} value")

                values = selected_item.findall('value')

                if values:
                    for value in values:
                        print(f"{value.get('text')}")
                else:
                    print("No values found")

                input()
            else:
                Console.print_warning("Invalid selection")
                input()
        except ValueError:
            Console.print_warning("Please enter a number")
            input()
