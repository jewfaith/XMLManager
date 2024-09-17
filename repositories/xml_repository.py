import os
import xml.etree.ElementTree as ET

class XMLRepository:
    """Handles XML file operations."""
    
    def __init__(self, file_path: str) -> None:
        """Initialize with the path to the XML file, create if it doesn't exist."""
        self.file_path = file_path
        
        if not os.path.isfile(self.file_path):
            self.create_empty_xml_file()
        
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()
    
    def create_empty_xml_file(self) -> None:
        """Create an empty XML file with a root element."""
        root = ET.Element('root')
        tree = ET.ElementTree(root)
        tree.write(self.file_path, encoding='utf-8', xml_declaration=True)
    
    def get_root(self) -> ET.Element:
        """Return the root element of the XML file."""
        return self.root
    
    def save(self) -> None:
        """Save changes to the XML file."""
        self.tree.write(self.file_path, encoding='utf-8', xml_declaration=True)
