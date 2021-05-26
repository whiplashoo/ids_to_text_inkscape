#!/usr/bin/env python3
import re
import inkex

#  change deprecated APIs for 1.1
#  add option to make other attributes <text> nodes, like fill or stroke
# option to scale text according to path area.

class IdsToText(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            '--fontsize', type=int, default='10', help='Font Size')
        self.arg_parser.add_argument(
            '--color', type=inkex.Color, default=255, help='Color')
        self.arg_parser.add_argument(
            '--font', default='Roboto', help='Font Family')
        self.arg_parser.add_argument(
            '--fontweight', default='bold', help='Font Weight')
        self.arg_parser.add_argument(
            '--replaced', default='', help='Text to replace')
        self.arg_parser.add_argument(
            '--replacewith', default='', help='Replace with this text')
        self.arg_parser.add_argument(
            '--matchre', default='', help='Match regular expression')
        self.arg_parser.add_argument(
            '--angle', type=float, dest='angle', default=0,
            help='Rotation angle')
        self.arg_parser.add_argument(
            '--capitals', type=inkex.Boolean, default=False, help='Capitalsze')

    def effect(self):
        if len(self.svg.selected) == 0:
            inkex.errormsg("Please select some paths first.")
            exit()

        for id, node in self.svg.selection.filter(inkex.PathElement).items():
            id = node.get('id')
            node.path.transform(node.composed_transform()).to_superpath()
            bbox = node.bounding_box()
            tx, ty = bbox.center

            text_element = node.getparent().add(inkex.TextElement())
            tspan_element = text_element.add(inkex.Tspan())
            tspan_element.set('sodipodi:role', 'line')
            styles = {'text-align': 'center',
                      'vertical-align': 'bottom',
                      'text-anchor': 'middle',
                      'font-size': str(self.options.fontsize) + 'px',
                      'font-weight': self.options.fontweight,
                      'font-style': 'normal',
                      'font-family': self.options.font,
                      'fill': str(self.options.color)
                      }
            tspan_element.set('style', str(inkex.Style(styles)))
            tspan_element.set('dy', '0')

            if self.options.capitals:
                id = id.upper()

            if self.options.matchre != '':
                matches = re.findall(self.options.matchre, id)
                if len(matches) > 0:
                    id = matches[0]

            if self.options.replaced != '':
                id = id.replace(
                    self.options.replaced, self.options.replacewith)

            tspan_element.text = id
            tspan_element.set('id', id + "_tspan")
            text_element.set('id', id + "_text")
            text_element.set('x', str(tx))
            text_element.set('y', str(ty))
            text_element.set('transform', 'rotate(%s, %s, %s)' %
                             (-int(self.options.angle), tx, ty))


if __name__ == '__main__':
    IdsToText().run()
