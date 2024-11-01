import os
import sys


def remove_paths_from_sys_path():
    """Remove the paths from sys.path that contain the word 'path'."""
    # Remove unwanted directories from sys.path
    unwanted_paths = [
        "C:\\Users\\guilh\\repo\\103-hubdog\\petshop_management\\utils",
        "C:\\Users\\guilh\\repo\\103-hubdog\\petshop_management",
    ]
    sys.path = [p for p in sys.path if p not in unwanted_paths]


def set_root_path():
    """Set the root path of the project."""
    # Identify the root directory of your project
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Add the root directory to sys.path
    if root_dir not in sys.path:
        sys.path.append(root_dir)


if __name__ == "__main__":
    remove_paths_from_sys_path()
    set_root_path()
    print(
        sys.path
    )  # Debugging: Print sys.path to ensure it only contains the desired directories
