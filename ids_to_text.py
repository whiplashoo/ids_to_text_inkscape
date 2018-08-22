#!/usr/bin/env python

# We will use the inkex module with the predefined Effect base class.
import inkex
import simpletransform
import cubicsuperpath
import bezmisc
# The simplestyle module provides functions for style parsing.
import simplestyle

# third party
try:
    import numpy
except:
    inkex.errormsg(_("Failed to import the numpy modules. These modules are required by this extension. Please install them and try again.  On a Debian-like system this can be done with the command, sudo apt-get install python-numpy."))
    exit()

mat_area   = numpy.matrix([[  0,  2,  1, -3],[ -2,  0,  1,  1],[ -1, -1,  0,  2],[  3, -1, -2,  0]])
mat_cofm_0 = numpy.matrix([[  0, 35, 10,-45],[-35,  0, 12, 23],[-10,-12,  0, 22],[ 45,-23,-22,  0]])
mat_cofm_1 = numpy.matrix([[  0, 15,  3,-18],[-15,  0,  9,  6],[ -3, -9,  0, 12],[ 18, -6,-12,  0]])
mat_cofm_2 = numpy.matrix([[  0, 12,  6,-18],[-12,  0,  9,  3],[ -6, -9,  0, 15],[ 18, -3,-15,  0]])
mat_cofm_3 = numpy.matrix([[  0, 22, 23,-45],[-22,  0, 12, 10],[-23,-12,  0, 35],[ 45,-10,-35,  0]])

def csparea(csp):
    area = 0.0
    for sp in csp:
        if len(sp) < 2: continue
        for i in range(len(sp)):            # calculate polygon area
            area += 0.5*sp[i-1][1][0]*(sp[i][1][1] - sp[i-2][1][1])
        for i in range(1, len(sp)):         # add contribution from cubic Bezier
            vec_x = numpy.matrix([sp[i-1][1][0], sp[i-1][2][0], sp[i][0][0], sp[i][1][0]])
            vec_y = numpy.matrix([sp[i-1][1][1], sp[i-1][2][1], sp[i][0][1], sp[i][1][1]])
            area += 0.15*(vec_x*mat_area*vec_y.T)[0,0]
    return -area                            # require positive area for CCW
def cspcofm(csp):
    area = csparea(csp)
    xc = 0.0
    yc = 0.0
    if abs(area) < 1.e-8:
        inkex.errormsg(_("Area is zero, cannot calculate Center of Mass"))
        return 0, 0
    for sp in csp:
        for i in range(len(sp)):            # calculate polygon moment
            xc += sp[i-1][1][1]*(sp[i-2][1][0] - sp[i][1][0])*(sp[i-2][1][0] + sp[i-1][1][0] + sp[i][1][0])/6
            yc += sp[i-1][1][0]*(sp[i][1][1] - sp[i-2][1][1])*(sp[i-2][1][1] + sp[i-1][1][1] + sp[i][1][1])/6
        for i in range(1, len(sp)):         # add contribution from cubic Bezier
            vec_x = numpy.matrix([sp[i-1][1][0], sp[i-1][2][0], sp[i][0][0], sp[i][1][0]])
            vec_y = numpy.matrix([sp[i-1][1][1], sp[i-1][2][1], sp[i][0][1], sp[i][1][1]])
            vec_t = numpy.matrix([(vec_x*mat_cofm_0*vec_y.T)[0,0], (vec_x*mat_cofm_1*vec_y.T)[0,0], (vec_x*mat_cofm_2*vec_y.T)[0,0], (vec_x*mat_cofm_3*vec_y.T)[0,0]])
            xc += (vec_x*vec_t.T)[0,0]/280
            yc += (vec_y*vec_t.T)[0,0]/280
    return -xc/area, -yc/area

class IdsToText(inkex.Effect):

    def __init__(self):
        """
        Constructor.
        """
        
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        self.OptionParser.add_option('-s', '--fontsize', action = 'store',
          type = 'int', dest = 'fontsize', default = '10',
          help = 'Font Size')
        self.OptionParser.add_option('-c', '--color', action = 'store',
          type = 'string', dest = 'color', default = '#000000',
          help = 'Color')
        self.OptionParser.add_option('-f', '--font', action = 'store',
          type = 'string', dest = 'font', default = 'Roboto',
          help = 'Font Family')
        self.OptionParser.add_option('-w', '--fontweight', action = 'store',
          type = 'string', dest = 'fontweight', default = 'bold',
          help = 'Font Weight')
        self.OptionParser.add_option('-r', '--replaced', action = 'store',
          type = 'string', dest = 'replaced', default = '',
          help = 'Text to replace')
        self.OptionParser.add_option('-q', '--replacewith', action = 'store',
          type = 'string', dest = 'replacewith', default = '',
          help = 'Replace with this text')
        self.OptionParser.add_option('-a', '--angle', action = 'store',
          type = 'float', dest = 'angle', default = 0,
          help = 'Rotation angle')

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

        if len(self.selected) == 0:
            inkex.errormsg(_("Please select some paths first."))
            exit()

        for id, node in self.selected.iteritems():
            mat = simpletransform.composeParents(node, [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
            p = cubicsuperpath.parsePath(node.get('d'))
            simpletransform.applyTransformToPath(mat, p)
            self.group = inkex.etree.SubElement(node.getparent(),inkex.addNS('text','svg'))
            tx, ty = cspcofm(p)
            new = inkex.etree.SubElement(self.group, inkex.addNS('tspan','svg'), {inkex.addNS('role','sodipodi'): 'line'})
            s = {'text-align': 'center', 'vertical-align': 'bottom',
                'text-anchor': 'middle', 'font-size': fontsize,
                'font-weight': fontweight, 'font-style': 'normal', 'font-family': font, 'fill': color}
            new.set('style', simplestyle.formatStyle(s))
            new.text = id.replace(replaced, replacewith)
            self.group.set('x', str(tx))
            self.group.set('y', str(ty))
            self.group.set('transform', 'rotate(%s, %s, %s)' % (angle, tx, ty))



# Create effect instance and apply it.
effect = IdsToText()
effect.affect()