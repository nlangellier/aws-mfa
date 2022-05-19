from pathlib import Path

fpath_package_version = Path(__file__).parent / 'VERSION.txt'
with open(fpath_package_version, 'r') as file_pointer:
    __version__ = file_pointer.read().splitlines()[0]

del fpath_package_version, file_pointer, Path
