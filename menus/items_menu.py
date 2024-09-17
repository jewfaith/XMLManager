import xml.etree.ElementTree as ET
from repositories.xml_repository import XMLRepository
from utils.console import Console

def handle_items_menu(repository: XMLRepository) -> None:
    """Handle the items menu operations."""
    while True:
        Console.clear_console()
        Console.print_title("Manage Items")
        
        options = [
            "1. Add Item",
            "2. Remove Item",
            "3. Back to Main Menu"
        ]
        
        for option in options:
            print(option)
        
        choice = Console.prompt("Select an option")
        
        if choice == '1':
            add_item(repository)
        elif choice == '2':
            remove_item(repository)
        elif choice == '3':
            break
        else:
            Console.print_error("Invalid choice, please try again")
            input()

def add_item(repository: XMLRepository) -> None:
    """Add a new item to the XML root."""
    Console.clear_console()
    Console.print_title("Add New Item")
    while True:
        item_name = input("Item Name: ").strip()
        if item_name:
            root = repository.get_root()
            if any(item.get('name') == item_name for item in root.findall('item')):
                Console.print_warning("Item Already Exists")
            else:
                new_item = ET.Element('item', name=item_name)
                root.append(new_item)
                repository.save()
                Console.print_success("Item Added Successfully")
                break
        else:
            Console.print_error("Item Name Required")
        input()

def remove_item(repository: XMLRepository) -> None:
    """Remove an item from the XML root."""
    Console.clear_console()
    Console.print_title("Remove Item")
    
    root = repository.get_root()
    items = root.findall('item')
    
    if not items:
        Console.print_warning("No items available to remove")
        input()
        return
    
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item.get('name')}")
    
    item_index = Console.prompt("Select an option").strip()
    
    try:
        item_index = int(item_index)
        if 1 <= item_index <= len(items):
            item_to_remove = items[item_index - 1]
            root.remove(item_to_remove)
            repository.save()
            Console.print_success("Item Removed")
        else:
            Console.print_warning("Invalid item number")
    except ValueError:
        Console.print_warning("Please enter a number")
    input()
