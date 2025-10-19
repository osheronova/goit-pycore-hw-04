import sys
from pathlib import Path
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def color_dir_structure(dir_path: Path, indent: str = "") -> None:
    for entry in dir_path.iterdir():
        try:
            if entry.is_dir():
                print(indent + Fore.YELLOW + f"Directory: {entry.name}/")
                color_dir_structure(entry, indent + "    ")
            else:
                print(indent + Fore.GREEN + f"File: {entry.name}")
        except PermissionError:
            print(indent + Fore.MAGENTA + f"[No access] {entry.name}")

def main() -> None:
    if len(sys.argv) < 2:
        print(Fore.MAGENTA + "Usage: python task3.py <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1]).expanduser().resolve()
    if not directory_path.exists() or not directory_path.is_dir():
        print(Fore.MAGENTA + "Invalid directory path.")
        sys.exit(1)

    color_dir_structure(directory_path)

if __name__ == "__main__":
    main()
