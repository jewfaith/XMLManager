from abc import ABC, abstractmethod

class IConsole(ABC):
    """Interface for console operations."""
    
    @abstractmethod
    def clear_console(self) -> None:
        """Clear the console screen."""
        pass
    
    @abstractmethod
    def print_title(self, title: str) -> None:
        """Print a formatted title."""
        pass

    @abstractmethod
    def print_success(self, message: str) -> None:
        """Print a success message in green."""
        pass

    @abstractmethod
    def print_warning(self, message: str) -> None:
        """Print a warning message in yellow."""
        pass

    @abstractmethod
    def print_error(self, message: str) -> None:
        """Print an error message in red."""
        pass

    @abstractmethod
    def prompt(self, message: str) -> str:
        """Prompt the user for input."""
        pass
