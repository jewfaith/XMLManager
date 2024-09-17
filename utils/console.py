import os
from colorama import Fore, Style

class Console:
    """Utility class for console operations."""

    @staticmethod
    def clear_console() -> None:
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_title(title: str) -> None:
        """Print a title with formatting."""
        print(f"\n{'=' * len(title)}")
        print(f"  {title}")
        print(f"{'=' * len(title)}\n")

    @staticmethod
    def print_success(message: str) -> None:
        """Print a success message in green."""
        print(Fore.GREEN + message + Style.RESET_ALL)
    
    @staticmethod
    def print_warning(message: str) -> None:
        """Print a warning message in yellow."""
        print(Fore.YELLOW + message + Style.RESET_ALL)
    
    @staticmethod
    def print_error(message: str) -> None:
        """Print an error message in red."""
        print(Fore.RED + message + Style.RESET_ALL)

    @staticmethod
    def print_info(message: str) -> None:
        """Print an informational message in cyan."""
        print(Fore.CYAN + message + Style.RESET_ALL)

    @staticmethod
    def prompt(message: str) -> str:
        """Prompt the user for input."""
        return input(f"{message}: ").strip()