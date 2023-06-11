from pynterface import Color
def printh(*args):
    """ For printing answers highlighted in blue. """
    print(Color.BLUE + " ".join(map(str, args)) + Color.RESET_COLOR)