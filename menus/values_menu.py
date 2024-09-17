import xml.etree.ElementTree as ET
from utils.console import Console
from repositories.xml_repository import XMLRepository


def handle_values_menu(repository: XMLRepository) -> None:
    """Handle the values menu operations."""
    while True:
        Console.clear_console()
        Console.print_title("Manage Values")

        options = ["1. Add Value", "2. Remove Value", "3. Back to Main Menu"]

        for option in options:
            print(option)

        choice = Console.prompt("Select an option")

        if choice == "1":
            add_value(repository)
        elif choice == "2":
            remove_value(repository)
        elif choice == "3":
            break
        else:
            Console.print_error("Invalid choice, please try again")
            input()


def add_value(repository: XMLRepository) -> None:
    """Add new values to the selected item until an empty input is received."""
    root = repository.get_root()
    items = root.findall("item")

    if not items:
        Console.print_warning("No items available to add values")
        input()
        return

    item_name = select_item(items)
    if item_name:
        item = next(item for item in items if item.get("name") == item_name)
        while True:
            value = input("Enter value (empty to finish): ").strip()
            if value:
                value = " ".join(value.split())
                item.append(ET.Element("value", text=value))
                repository.save()
                Console.print_success("Value Added")
            else:
                Console.print_success("Finished adding values")
                break
    else:
        Console.print_warning("No valid item selected")
    input()

def remove_value(repository: XMLRepository) -> None:
    """Remove a value from the selected item."""
    root = repository.get_root()
    items = root.findall("item")

    if not items:
        Console.print_warning("No items available to remove values")
        input()
        return

    item_name = select_item(items)
    if item_name:
        item = next((item for item in items if item.get("name") == item_name), None)

        if item is None:
            Console.print_warning("Selected item not found")
            input()
            return

        values = item.findall("value")
        if not values:
            Console.print_warning("No values available to remove")
            input()
            return

        while True:
            Console.clear_console()
            Console.print_title("Remove Value")
            for i, value in enumerate(values, start=1):
                print(f"{i}. {value.get('text')}")

            value_text = input("Select an option: ").strip()

            if value_text:
                value_to_remove = next(
                    (value for value in values if value.get("text") == value_text), None
                )

                if value_to_remove:
                    item.remove(value_to_remove)
                    repository.save()
                    Console.print_success("Value Removed Successfully")
                    return

                Console.print_warning("Value Not Found")
            else:
                Console.print_error("Value Required")

            input()
    else:
        Console.print_warning("No valid item selected")
        input()

def select_item(items: list[ET.Element]) -> str:
    """Select an item from the list of items."""
    Console.clear_console()
    Console.print_title("Select Item")
    for index, item in enumerate(items):
        print(f"{index + 1}. {item.get('name')}")
    try:
        choice = int(input("Select an option: ")) - 1
        if 0 <= choice < len(items):
            return items[choice].get("name")
        else:
            Console.print_error("Invalid Item Selection")
            return None
    except ValueError:
        Console.print_error("Invalid Input")
        return None
