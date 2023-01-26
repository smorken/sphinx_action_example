import os


def example_function1(a: int, b: float) -> float:
    """Compute the sum of a and b

    Args:
        a (int): the a argument
        b (float): the b argument

    Returns:
        float: a, and b added together
    """
    return a + b


def read_package_data() -> str:
    """reads a packaged file to confirm packaging worked

    Returns:
        str: the packaged file's contents
    """
    package_data_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "package_data",
        "package_data1.txt",
    )
    with open(package_data_file, "r") as fp:
        return fp.read()
