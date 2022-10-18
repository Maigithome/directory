def get_info(name_file):
    with open(name_file, "r", encoding="utf-8") as file:
        info = file.read().split(",")
    return info
