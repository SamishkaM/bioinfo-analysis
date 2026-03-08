def check_quality(data):
    if len(data) == 0:
        return "No data"
    return "Data looks good"

print(check_quality([1,2,3]))