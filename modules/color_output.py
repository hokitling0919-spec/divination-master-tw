def print_color(text, color):
    color_map = {
        "cyan": "\033[96m",
        "yellow": "\033[93m",
        "white": "\033[97m",
        "green": "\033[92m",
        "reset": "\033[0m"
    }
    c = color_map.get(color, "")
    print(f"{c}{text}{color_map['reset']}")
