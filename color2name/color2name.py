from .colorvalues import colors, hues


def closest(comparison: dict, rgb: tuple):
    def get_dist(r1, g1, b1, r2, g2, b2):
        return abs(r1 - r2), abs(g1 - g2), abs(b1 - b2)

    r, g, b = rgb

    search = f'({r},{g},{b})'
    if search in comparison:
        return comparison[search]

    distances = []
    for option in comparison:
        distances.append((sum(get_dist(r, g, b, *map(int, option.strip("(").strip(")").split(",")))), option))

    distances.sort()
    return comparison[distances[0][1]]


def rgb2name(rgb: tuple) -> str:
    """
    Converts an rgb value to a color name
    :param rgb: RGB Tuple input
    :return: Color name corresponding to inputted RGB value
    """
    return closest(colors, rgb)


def rgb2hue(rgb: tuple) -> str:
    """
    Converts an rgb value to a hue name
    :param rgb: RGB Tuple input
    :return: Hue name corresponding to inputted RGB value
    """
    return closest(hues, rgb)


def hex2name(h: str) -> str:
    """
    Converts a hex value to a color name
    :param h: Hex input
    :return: Color name corresponding to inputted hex value
    """
    return rgb2name(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))


def hex2hue(h: str) -> str:
    """
    Converts a hex value to a hue name
    :param h: Hex input
    :return: Hue name corresponding to the inputted hex value
    """
    return rgb2hue(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))
