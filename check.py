from datetime import date, timedelta
from database import dock_dict, check_dockreservations

def check_size(dock_num, length, width):
    if float(dock_dict[int(dock_num) - 1]["length"]) >= float(length) and float(dock_dict[int(dock_num) - 1]["width"]) >= float(width):
        return True
    else:
        return False

def check_date(dock_num, start, end): #this can be more optimal than o(n^2)
    rows = check_dockreservations(dock_num, end, start)
    arr = []
    for row in rows:
        arr.append(row)

    if len(arr) > 0:
        return arr
    else:
        return True