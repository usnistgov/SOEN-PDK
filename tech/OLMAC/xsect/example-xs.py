''' This script makes a layout that demonstrates the cross-sections of relevant devices.
    The layout itself is meaningless geometry.

    How to use
        1. python example-xs.py
        2. open example-xs.gds
        3. activate the correct technology
        3. draw a ruler across the middle
        4. Cmd-X (mac osx users), or go to the menu: Tools > XSection Scripts > Active Technology

    This requires the xsection package. Get it through klayout's salt package manager.
'''

''' Development Questions
    - should resistor always autofill pedestal
    - i think we need a pedestal KO layer, or should we have to place explicitly
    - i am confused about oxides. it looks like there are 3 so shouldnt we have three via layers?
    - how do we change the aspect ratio of xsect display so it is easier to see? just multiply the thicknesses?
'''

import os
from phidl.utilities import load_lyp
lyp_file = os.path.join(os.path.dirname(__file__), '..', 'klayout_layers_OLMAC.lyp')
lys = load_lyp(lyp_file)

from phidl import Device, geometry as pg


def do_something_interesting():
    x_section = Device()
    def insert_wx(lname, width, x):
        shape = x_section << pg.rectangle((width, 2), layer=lys[lname])
        shape.x = x
        shape.y = 50
        return shape

    def insert(lname, xmin, xmax):
        shape = x_section << pg.rectangle((xmax-xmin, 2), layer=lys[lname])
        shape.xmin = xmin
        shape.y = 50
        return shape

    # LED
    ppdopant_x = .65
    outer_wgx = ppdopant_x+.17
    insert_wx('wg_deep', 2*outer_wgx, 0)
    insert('wg_shallow', .15, outer_wgx)
    insert('wg_shallow', -outer_wgx, -.15)
    insert_wx('dp_e', .1, 0)
    insert('dp_n', .05, outer_wgx)
    insert('dp_p', -outer_wgx, -.05)
    insert_wx('dp_n+', .3, ppdopant_x)
    insert_wx('dp_p+', .3, -ppdopant_x)
    for side in [-1, 1]:
        insert_wx('m4_ledpad', .28, side*ppdopant_x)
        insert_wx('v5', .25, side*ppdopant_x)
    insert_wx('m5_wiring', .35, -ppdopant_x)
    insert_wx('v3', .3, -ppdopant_x)
    insert_wx('m5_wiring', .65, ppdopant_x+.4)
    insert_wx('v3', .4, ppdopant_x+.4)

    # WG
    wg = insert_wx('wg_deep', .2, 2)

    # SNSPD
    nw = insert_wx('m2_nw', .3, wg.xmax + 1)
    pad = insert('m1_nwpad', nw.xmax - .1, nw.xmax+.4)
    via = insert('v3', pad.xmax-.3, pad.xmax-.1)
    wire = insert('m5_wiring', pad.x, pad.x+1)
    insert_wx('v5', .3, wire.xmax - .2)

    # resistor
    res = insert_wx('m3_res', 2, wire.xmax+1.5)
    via1 = insert('v5', res.xmin+.1, res.xmin+.5)
    wire1 = insert_wx('m5_wiring', .5, via1.x)
    insert_wx('v3', .4, wire1.x)
    via2 = insert('v5', res.xmax-.5, res.xmax-.1)
    wire2 = insert_wx('m5_wiring', .5, via2.x)
    insert_wx('v3', .4, wire2.x)
    insert('wg_deep', wire1.xmin-.1, wire2.xmax+.1)

    # htron
    snspd = x_section << pg.snspd(wire_width = 0.05, wire_pitch = 0.3, size = (2,2), layer=lys['m2_nw'])
    snspd.rotate(90)
    snspd.y = wire2.y
    snspd.xmin = wire2.xmax + 1.5
    heater = x_section << pg.rectangle((2.4, 2), layer=lys['m3_res'])
    heater.xmin = snspd.xmin
    heater.y = snspd.y
    pad = insert('m1_nwpad', snspd.xmin - .5, snspd.xmin+.02)
    via = insert('v5', pad.xmin, pad.xmax-.2)
    wire = insert_wx('m5_wiring', .4, via.x)
    insert_wx('v3', .3, wire.x-.05)
    # pad = insert('m1_nwpad', heater.xmax - .2, heater.xmax-.05)
    via = insert('v5', heater.xmax - .2, heater.xmax-.05)
    wire = insert_wx('m5_wiring', .4, via.x)
    insert_wx('v3', .3, wire.x-.05)

    return x_section


if __name__ == '__main__':
    D = do_something_interesting().flatten()
    D.write_gds('example-xs.gds')
