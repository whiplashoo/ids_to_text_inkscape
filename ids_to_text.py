#!/usr/bin/env python

import inkex
from inkex import TextElement, TextPath, Tspan
from inkex.bezier import csparea, cspcofm, csplength

class IdsToText(inkex.Effect):

    def __init__(self):
        """
        Constructor.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        self.arg_parser.add_argument('-s', '--fontsize', 
          type = int, dest = 'fontsize', default = '10',
          help = 'Font Size')
        self.arg_parser.add_argument('-c', '--color', 
          type = str, dest = 'color', default = '#000000',
          help = 'Color')
        self.arg_parser.add_argument('-f', '--font', 
          type = str, dest = 'font', default = 'Roboto',
          help = 'Font Family')
        self.arg_parser.add_argument('-w', '--fontweight', 
          type = str, dest = 'fontweight', default = 'bold',
          help = 'Font Weight')
        self.arg_parser.add_argument('-r', '--replaced', 
          type = str, dest = 'replaced', default = '',
          help = 'Text to replace')
        self.arg_parser.add_argument('-q', '--replacewith', 
          type = str, dest = 'replacewith', default = '',
          help = 'Replace with this text')
        self.arg_parser.add_argument('-a', '--angle', 
          type = float, dest = 'angle', default = 0,
          help = 'Rotation angle')
        self.arg_parser.add_argument('-p', '--capitals', 
          type = inkex.Boolean, dest = 'capitals', default = False,
          help = 'Capitalize')
        self.arg_parser.add_argument("--active-tab",
          help="Active tab.")

    def effect(self):
        """
        Effect behaviour.
        """
        # Get script's "--what" option value.
        fontsize = str(self.options.fontsize) + 'px'
        color = self.options.color
        font = self.options.font
        fontweight = self.options.fontweight
        replaced = self.options.replaced
        replacewith = self.options.replacewith
        angle = -int(self.options.angle)
        capitals = self.options.capitals

        if len(self.svg.selected) == 0:
            inkex.errormsg(_("Please select some paths first."))
            exit()

        for id, node in self.svg.selected.items():
            self.group = node.getparent().add(TextElement())
            csp = node.path.transform(node.composed_transform()).to_superpath()
            bbox = node.bounding_box()
            tx, ty = bbox.center
            anchor = 'middle'

            node = self.group
            new = node.add(Tspan())
            new.set('sodipodi:role', 'line')
            s = {'text-align': 'center', 'vertical-align': 'bottom',
                'text-anchor': 'middle', 'font-size': fontsize,
                'font-weight': fontweight, 'font-style': 'normal', 'font-family': font, 'fill': color}
            new.set('style', str(inkex.Style(s)))
            new.set('dy', '0')

            if capitals:
                id = id.upper()

            new.text = id.replace(replaced, replacewith)
            node.set('x', str(tx))
            node.set('y', str(ty))
            node.set('transform', 'rotate(%s, %s, %s)' % (angle, tx, ty))            

# Create effect instance and apply it.
effect = IdsToText()
effect.run()