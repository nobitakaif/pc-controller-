from pathlib import Path

def create_folder(folder_name : str) ->str:
    desktop = Path.home() / "Desktop"
    print("desktop ->",desktop)
    folder = desktop / folder_name
    folder.mkdir(exist_ok=True)

    return f"Folder '{ folder_name }' created successfully on desktop"


print(create_folder("bitch"))
