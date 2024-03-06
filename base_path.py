import os
import sys

def get_base_path():
    """Get the base path depending on whether the script is run as a script or frozen."""
    if getattr(sys, 'frozen', False):
        # When packaged, use the temporary directory created by PyInstaller
        return sys._MEIPASS
    else:
        # When running as a script, use the directory of the script
        return os.path.dirname(os.path.abspath(__file__))


# Define the path to the sounds directory relative to the base directory
def get_file_path(directory, file_name):
    base_path = get_base_path()
    sounds_dir = os.path.join(base_path, directory)
    return os.path.join(sounds_dir, file_name)