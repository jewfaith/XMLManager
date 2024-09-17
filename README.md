## Setup

- Python 3.7 *or higher*

```bash
git clone https://github.com/jewfaith/XMLManager.git

cd XMLManager-main/

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