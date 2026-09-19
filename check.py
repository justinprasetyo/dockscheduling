from datetime import date, timedelta
from database import dock_dict, check_dockreservations

def check_size(dock_num, length, width):
    if float(dock_dict[int(dock_num) - 1]["length"]) >= float(length) and float(dock_dict[int(dock_num) - 1]["width"]) >= float(width):
        return True
    else:
        return False

def check_date(dock_num, start, end): #this can be more optimal than o(n^2)
    arr = check_dockreservations(dock_num)
    for i in range(0, (date.fromisoformat(end) - date.fromisoformat(start)).days + 1):
        day = start + timedelta(days=i)
        for j in range(len(arr)):
            if day >= arr[j][0] and day <= arr[j][1]:
                return False #make it return the overlapping dates
    return True