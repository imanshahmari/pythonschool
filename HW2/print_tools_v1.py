""" Python module with useful printing functions!
Author: Emilia Emilsson (2020), emiemi@chalmers.se """

version = "1.0.0"  # Module global variable


def print_two_objects(object1, object2):
    """Prints the two objects to stdout.

    :param object1: The first object to print
    :type object1: Any type convertible to str

    :param object2: The second object to print
    :type object2: Any type convertible to str
    """

    print(f'The two objects are: "{object1}" and "{object2}".')


def task_done():
    """Indicate that a task is done by printing a message."""
    print(f'Task done in the "{__name__}" module.')


if __name__ == "__main__":
    print_two_objects("This is a test", "of print_two_objects")
    task_done()