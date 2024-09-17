## Overview

A versatile console-based application for managing XML data. This project allows users to handle items and values within an XML file using a menu-driven interface. It includes functionalities to add, remove, and view items and values, all managed through a user-friendly console interface.

## Setup

- Python 3.7 *or higher*

```bash
git clone https://github.com/jewfaith/XMLManager.git

pip install colorama

python main.py
```

## Layout

```plaintext
main.py                               # Entry point for the application

interfaces/
├── console_interface.py              # Defines the IConsole interface
└── xml_repository_interface.py       # Defines the IXMLRepository interface

menus/
├── main_menu.py                      # Manages the main menu
├── items_menu.py                     # Manages item-related actions
├── values_menu.py                    # Manages value-related actions
└── view_values_menu.py               # Handles value viewing

repositories/
└── xml_repository.py                 # Implements XML repository operations

utils/
└── console.py                        # Provides console utility functions

README.md                             # Project documentation
```