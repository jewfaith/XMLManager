from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element

class IXMLRepository(ABC):
    @abstractmethod
    def get_root(self) -> Element:
        """Return the root element of the XML file."""
        pass

    @abstractmethod
    def save(self) -> None:
        """Save changes to the XML file."""
        pass
