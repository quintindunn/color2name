# color2name
A python library to convert RGB or HEX values to their respective name and hue

Usage:
```py
>>> from color2name import rgb2name, rgb2hue, hex2name, hex2hue

>>> rgb = (100, 20, 70)
>>> hex_value = "D745D4"
>>> print(f"RGB: {rgb}")
RGB: (100, 20, 70)
>>> print(f"HEX: {hex_value}")
RGB: (100, 20, 70)
>>> print(f"RGB Name: {rgb2name(rgb)}")
RGB Name: Pompadour
>>> print(f"RGB Hue: {rgb2hue(rgb)}")
RGB Hue: Violet
>>> print(f"Hex Name: {hex2name(hex_value)}")
Hex Name: Free Speech Magenta
>>> print(f"Hex Hue: {hex2hue(hex_value)}")
Hex Hue: Red
```
