# ids_to_text_inkscape
*Updated for Inkscape ^1.0! If you need the previous version, you can find it as a zip file (ids\_to\_text\_Inkscape\_0.92.zip) in the root of the repo*.

### A simple Inkscape extension that lets you extract attributes (like `id`) from all selected paths, and show them as `<text>` elements inside the paths.

Useful for when you want to have all paths' `id` shown on the SVG document as `<text>` nodes.

You can also use it for other path attributes, like `label`, `fill`, `stroke`, `width`, `height`.

Available under the `Extensions > Text` menu.

<p align="center">
<img width="50%" src="https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/examples/extension_window.jpg"/>
</p>
  
**Note: only works on `<path>` elements. If you have a `<circle>`, `<rectangle>`, `<text>`, etc., first use Object > Object to Path to convert it.**

## Examples:

* ### Get the ids (names) of all the countries on the Africa map and show them on the map as labels.

<p align="center">
<img width="80%" src="https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/examples/example_africa_1.png"/>
</p> 
<p align="center">
<img width="80%" src="https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/examples/example_africa_2.png"/>
</p>

* ### Get the fill color for all circles and show it as a `<text>` element on top of them.

<p align="center">
<img width="80%" src="https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/examples/example_circles_1.jpg"/>
</p> 
<p align="center">
<img width="80%" src="https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/examples/example_circles_2.jpg"/>
</p>

* ### Get the width attribute for all planets and show it as a `<text>` element on top of them.

<p align="center">
<img width="80%" src="https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/examples/example_heliocentric_1.jpg"/>
</p> 
<p align="center">
<img width="80%" src="https://github.com/whiplashoo/ids_to_text_inkscape/blob/master/examples/example_heliocentric_2.jpg"/>
</p>

Options for styling and formatting the text:

* **Font size** in px
* **Color** (the fill color of the `<text>` elements)
* **Font** (should be installed on the system)
* **Font Weight** (should be supported by the selected font)
* **Angle** (controls the rotation of the generated `<text>` elements, in degrees)

Options for further editing the extracted text (only used with `id` and `label` attributes):
* **Text to replace** (a simple replace function to remove characters you may not want from the text)
* **Match Regular Expression** (matches the extracted text of each path to a regular expression and uses the result on the path, e.g. if the id is `Province_055` and this field `\d+`, the text on the path will be just `055`)
* **Capitalize** (capitalize all text)
* **Group paths with the generated text elements ** (if checked, also group (`<g>`) the path with its text label)


Also published on the [Inkscape extensions repository](https://inkscape.org/~whidev/%E2%98%85ids-to-text-elements "Inkscape extensions repository").