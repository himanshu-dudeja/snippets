
from collections import namedtuple


def usual_method():
    # Here its difficult to see and guess what are these values
    color = (24, 45, 34)
    print(color[0])


def better_way():
    Color = namedtuple('Color', ['red', 'green', 'blue'])
    color = Color(24, 45, 34)
    # color = Color(red=24, green=45, blue=34)
    print(color[0])
    print(color.red)
    print(color.green)


usual_method()
better_way()
