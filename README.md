## Overview

A versatile console-based application for managing XML data. This project allows users to handle items and values within an XML file using a menu-driven interface. It includes functionalities to add, remove, and view items and values, all managed through a user-friendly console interface.

## Features

- **Manage Items:** Add or remove items in the XML.
- **Manage Values:** Add or remove values associated with items.
- **Console Interface:** Provides clear and colored output for a better user experience.

## Setup

- Python 3.7 *or higher*

```bash
git clone https://github.com/jewfaith/XMLManager.git
```

```bash
pip install colorama
```

- Run the application

```bash
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

- **main.py**: This is the main entry point of the application. The main.py file contains the main function that starts the application and controls the primary execution flow, including menu selection and executing the appropriate functionalities based on user input.
- **interfaces/**: This directory contains abstract interfaces for dependency injection, making it easier to swap out components if needed.

  - **console_interface.py**: Defines the IConsole interface, specifying methods for console operations like clearing the screen, printing formatted titles, success, warning, and error messages, and prompting for user input. This interface separates presentation logic from control code.

  - **xml_repository_interface.py**: Defines the IXMLRepository interface for interacting with XML data, including methods to get the root element and save changes. This allows for easy swapping of XML repository implementations.

- **menus/**: This directory contains modules that manage different menus of the application. Each module is responsible for a specific part of the menu, aiding in modularity and code maintenance.

  - **main_menu.py**: Manages the main menu of the application. This module displays the primary options to the user and directs them to the appropriate modules based on their selection.

  - **items_menu.py**: Handles item-related actions, such as adding and removing items. It provides an interface for the user to manage items in the XML file.

  - **values_menu.py**: Manages actions related to values associated with items, such as adding and removing values. It allows the user to modify values within items.

  - **view_values_menu.py**: Handles the display of values for selected items. It enables the user to view the values associated with items in the XML file.

- **repositories/**: Contains the implementation of the XML data repository. This directory is responsible for directly interacting with the XML file, performing operations like reading and writing data.

  - **xml_repository.py**: Implements the IXMLRepository interface. This module provides the concrete logic for handling XML file operations, including obtaining the root element and saving changes made to the XML.

- **utils/**: Contains general utility functions used throughout the project. These utilities help with common tasks and centralize auxiliary functionalities.

  - **console.py**: Provides functions for console operations, such as clearing the screen and printing colored messages. It uses the colorama library to add color to console output.

- **README.md:** The project documentation file. It includes important information about the project, such as an overview, installation instructions, usage, and other relevant details for developers and users.