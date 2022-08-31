from os import get_terminal_size as gts

def print(
    *values,
    sep="",
    end="",
    coordinates=()
):
    if coordinates:

        if type(coordinates) != tuple:
            raise Exception("Coordinates must be a tuple.")
        
        if len(coordinates) != 2:
            raise Exception("Length of coordinates must be 2.")

        if not all([type(coord) == int for coord in coordinates]):
            raise Exception("Coordinates must be a tuple of integer.")

        y, x = coordinates

        if y > gts().lines:
            raise Exception("Coordinate Y can't be higher than the number of lines of the terminal.")

        if x > gts().columns:
            raise Exception("Coordinate X can't be higher than the number of columns of the terminal.")

        __import__('os').system('')

        values = str(*values)
        values = f"\033[{coordinates[0]};{coordinates[1]}H"+values
        values = (values,)

    return __builtins__['print'](*values, sep, end)


def input(
    *values,
    sep="",
    end="",
    coordinates=()
):
    if coordinates:

        if type(coordinates) != tuple:
            raise Exception("Coordinates must be a tuple.")
        
        if len(coordinates) != 2:
            raise Exception("Length of coordinates must be 2.")

        if not all([type(coord) == int for coord in coordinates]):
            raise Exception("Coordinates must be a tuple of integer.")

        y, x = coordinates

        if y > gts().lines:
            raise Exception("Coordinate Y can't be higher than the number of lines of the terminal.")

        if x > gts().columns:
            raise Exception("Coordinate X can't be higher than the number of columns of the terminal.")

        __import__('os').system('')

        values = str(*values)
        values = f"\033[{coordinates[0]};{coordinates[1]}H"+values
        values = (values,)

    return __builtins__['input'](*values)