from database import dock_dict

def check_size(dock_num, length, width):
    if float(dock_dict[int(dock_num) - 1]["length"]) >= float(length) and float(dock_dict[int(dock_num) - 1]["width"]) >= float(width):
        return True
    else:
        return False