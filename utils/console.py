import os

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
        print(f"\033[92m{message}\033[0m")  # Green

    @staticmethod
    def print_warning(message: str) -> None:
        """Print a warning message in yellow."""
        print(f"\033[93m{message}\033[0m")  # Yellow

    @staticmethod
    def print_error(message: str) -> None:
        """Print an error message in red."""
        print(f"\033[91m{message}\033[0m")  # Red

    @staticmethod
    def prompt(message: str) -> str:
        """Prompt the user for input."""
        return input(f"{message}: ").strip()
