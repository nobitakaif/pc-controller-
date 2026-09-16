from langchain_core.tools import tool
from pathlib import Path

@tool
def create_folder(folder_name : str) -> str:
    """Create a nre folder with the given name on the user's desktop 

    Args:
        folder_name (str): your what would be your folder

    Returns:
        str: folder is created 
    """
    
    desktop = Path.home() / "Desktop" 
    folder = desktop / folder
    folder.mkdir(exist_ok=True)
    return f"folder '{ folder_name }' created successfully on desktop "


print(create_folder.args)
print(create_folder.name)

