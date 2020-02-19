# ids_to_text_inkscape
A simple Inkscape extension that lets you **extract the ids from all selected paths and show them as `<text>` elements inside the paths.**


Useful for when you want to have all paths' ids shown on the SVG document as `<text>` nodes.

**Example:**

Get the ids (names) of all the countries on the Africa map and show them on the map as labels.


![Before](https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/example1.PNG)


![After](https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/example2.PNG)



There are options available for styling and formatting the text:

* **Font size** in px
* **Color** (the fill color of the `<text>` nodes)
* **Font** (should be installed on the system)
* **Font Weight** (should be supported by the selected font)
* **Text to replace** (a simple replace function to remove characters you may not want from the ids during the extraction)
* **Angle** (controls the rotation of the generated `<text>` nodes, in degrees)
* **Capitalize** (option to capitalize all text)

![UI](https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/example3.PNG)

**Note: only works on `<path>` elements. If you have a `<circle>`, `<rectangle>`, `<text>`, etc., first use Object -> Object to Path to convert it.**

For Inkscape v0.92 and before users, you should check the version provided in the [extension's Inkscape repository](https://inkscape.org/~whidev/%E2%98%85ids-to-text-elements "Inkscape repository").