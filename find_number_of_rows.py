def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    data = data.split("\n")
    return len(data[1:])

# Read the csv file
data = open('data.csv').read()
