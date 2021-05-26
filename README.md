# ids_to_text_inkscape
*__Updated for Inkscape 1.0 !__ If you need the previous version, you can find it as a zip file (ids\_to\_text\_Inkscape\_0.92.zip) in the root of the repo*.

A simple Inkscape extension that lets you **extract the ids from all selected paths and show them as `<text>` elements inside the paths.**


Useful for when you want to have all paths' ids shown on the SVG document as `<text>` nodes.

Available under the Extensions > Text menu.

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
* **Match Regular Expression** (matches the id of each path to a regular expression and uses that as text on the path, e.g. if the id is `Province_055` and this field `\d+`, the text on the path will be just `055`)



![UI](https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/example3.PNG)

**Note: only works on `<path>` elements. If you have a `<circle>`, `<rectangle>`, `<text>`, etc., first use Object > Object to Path to convert it.**

Also published on the [Inkscape extensions repository](https://inkscape.org/~whidev/%E2%98%85ids-to-text-elements "Inkscape extensions repository").