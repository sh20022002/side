import os

def map_directory(directory: str, indent: str = "", depth: int = 0, max_depth: int = 1):
    if depth > max_depth:
        return
    
    try:
        items = os.listdir(directory)
    except PermissionError:
        print(f"{indent}[ACCESS DENIED] {directory}")
        return
    
    for item in sorted(items):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            print(f"{indent}[DIR] {item}")
            map_directory(path, indent + "    ", depth + 1, max_depth)
        else:
            print(f"{indent}{item}")

if __name__ == "__main__":
    directory = os.getcwd()
    print(f"Mapping directory: {directory}\n")
    map_directory(directory)
