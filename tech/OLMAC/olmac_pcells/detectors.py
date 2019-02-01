from phidl import Device, geometry as pg
import numpy as np

import os
from phidl.utilities import load_lyp
lyp_file = os.path.join(os.path.dirname(__file__), '..', 'klayout_layers_OLMAC.lyp')
lys = load_lyp(lyp_file)


def wg_to_snspd(wgnw_width=0.1, wgnw_length=100, wgnw_gap=0.15,
                num_squares=5000.0, meander_width=0.4, meander_fill_factor=0.5,
                wg_width=0.75):
    ''' Waveguide coupled to SNSPD with inductor (meander).
        The length and width of the meander are chosen so that it is approximately square

        Args:
            meander_width (float): nanowire width within meander inductor
            num_squares (float): total squares in meander and out-and-back
            wgnw_width (float): width of out-and-back nanowire
            wgnw_length (float): length of out-and-back
            wgnw_gap (float): spacing between the out-and-back wires
            wg_width (float): waveguide width
    '''

    D = Device('wg_to_snspd')

    # Calculations and checks
    numsquares_wgnw = 2 * wgnw_length / wgnw_width
    numsquares_meander = num_squares - numsquares_wgnw
    if numsquares_meander < 1000:
        print('Warning: Not enough squares in SNSPD meander. Clipped to 1000 from {:.1f}'.format(numsquares_meander))
        numsquares_meander=1000
    wgnw_pitch = wgnw_width + wgnw_gap
    meander_pitch = meander_width / meander_fill_factor
    meander_length = np.sqrt(numsquares_meander * meander_width * meander_pitch)

    meander = D << pg.snspd(wire_width = meander_width, wire_pitch = meander_pitch,
                            terminals_same_side = False, size = (meander_length,None),
                            num_squares=numsquares_meander, layer = lys['m2_nw'])
    meander.reflect(p1=(0,0), p2=(1,0))

    Taper = pg.optimal_step(start_width = wgnw_width, end_width = meander_width, num_pts = 50, width_tol = 1e-3,
                                 anticrowding_factor = 1.2, layer = lys['m2_nw'])
    taper1 = D << Taper
    taper1.connect(port = 2, destination = meander.ports[1])

    wgnw = D << pg.optimal_hairpin(width = wgnw_width, pitch = wgnw_pitch, length = wgnw_length, layer = lys['m2_nw'])
    wgnw.reflect(p1 = wgnw.ports[1].midpoint, p2 = wgnw.ports[2].midpoint)

    #
    # wgnw.xmax = meander.xmin
    wgnw.connect(port = 1, destination = taper1.ports[1])


    taper2 = D.add_ref(Taper)
    taper2.reflect(taper2.ports[1].midpoint, taper2.ports[2].midpoint)
    taper2.connect(port = 1, destination = wgnw.ports[2])

    taper3 = D.add_ref(pg.optimal_step(start_width = meander_width, end_width = meander_width*4, num_pts = 50, width_tol = 1e-3,
                     anticrowding_factor = 1.2, layer = lys['m2_nw']))
    taper3.connect(port=1, destination = meander.ports[2])
    bend = D << pg.optimal_90deg(width = meander_width, num_pts = 15,
                                 length_adjust = 1, layer = lys['m2_nw'])
    bend.connect(port=2, destination=taper2.ports[2])

    ## Add the electrical ports
    # With breakouts to vias
    # route1 = D.add_ref(port2pad(port = taper3.ports[2], Pad = nw_pad_device, pad_offset = [nw_pad_device.size[0],0], wiring_layer = lys['m2_nw']))
    # route2 = D.add_ref(port2pad(port = bend.ports[1], Pad = nw_pad_device, pad_offset = [nw_pad_device.size[0],nw_pad_device.size[0]/2], wiring_layer = lys['m2_nw']))
    # D.add_port(midpoint = route1.ports[1].midpoint, width =route1.ports[1].width, orientation = 0, name = 'wiring1')
    # p = D.add_port(port = route2.ports[1], name = 'wiring2')
    # p.orientation = 0

    ## Add optical piece and ports
    wgnw_distance = wg_width - wgnw_width - wgnw_gap / 2
    wg = D.add_ref(pg.compass(size = [wgnw_length + wgnw_distance, wgnw_width+wgnw_pitch+wgnw_distance*2], layer = lys['wg_deep']))
    wg.xmax = wgnw.xmax
    wg.y = wgnw.y

    D.add_port(name = 'de_edge', port = wg.ports['E'])
    D.add_port(name = 'optical', port = wg.ports['W'])
    D.ports['de_edge'].info['is_waveguide_edge'] = True

    pos = D.ports['optical'].midpoint
    D.move(-1*pos)

    numsquares_taper = 3
    D.info['num_squares'] = numsquares_meander+numsquares_wgnw-meander_length/meander_width + 3*numsquares_taper
    # D.info['expected_resistance'] = D.info['num_squares']*EXPECTED_RSQ_WSI
    D.info['wire_width'] = wgnw_width
    D.info['length']= wgnw_length
    return D