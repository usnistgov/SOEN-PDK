from phidl import Device, geometry as pg
import numpy as np

import os
from phidl.utilities import load_lyp
lyp_file = os.path.join(os.path.dirname(__file__), '..', 'klayout_layers_OLMAC.lyp')
lys = load_lyp(lyp_file)

import lyipc.client as ipc
kqp = ipc.generate_display_function(None, 'debugging.gds')

def wg_to_snspd(meander_width=0.4, num_squares=5000.0,
                wgnw_width=0.1, wgnw_length=100, wgnw_gap=0.15,
                wg_width=0.75):
    # the length and width of the meander are chosen so that it is approximately square

    D = Device('wg_to_snspd')
    # If given number of squares as input, calculate number of squares in meander.
    MEANDER_FILL_FACTOR = .5
    meander_pitch = meander_width/MEANDER_FILL_FACTOR

    numsquares_meander = num_squares - 2*wgnw_length/wgnw_width
    if numsquares_meander<1000:
        numsquares_meander=1000

    wgnw_pitch = wgnw_width+wgnw_gap

    meander_length = np.sqrt(numsquares_meander*meander_width*meander_pitch)

    Snspd = pg.snspd(wire_width = meander_width, wire_pitch = meander_pitch, terminals_same_side = False, size = (meander_length,None),
                              num_squares=numsquares_meander, layer = lys['m2_nw'])
    meander = D.add_ref(Snspd)
    numsquares_meander = meander.info['num_squares']
    meander.reflect(p1=(0,0), p2=(1,0))

    wgnw = D.add_ref(pg.optimal_hairpin(width = wgnw_width, pitch = wgnw_pitch, length = wgnw_length, layer = lys['m2_nw']))
    wgnw.reflect(p1 = wgnw.ports[1].midpoint, p2 = wgnw.ports[2].midpoint)
    numsquares_wgnw = 2*wgnw_length/wgnw_width
    #
    Taper = pg.optimal_step(start_width = wgnw_width, end_width = meander_width, num_pts = 50, width_tol = 1e-3,
                     anticrowding_factor = 1.2, layer = lys['m2_nw'])
    taper = D.add_ref(Taper)
    #
    taper.connect(port = 2, destination = meander.ports[1])
    #
    wgnw.xmax = meander.xmin
    wgnw.connect(port = 1, destination = taper.ports[1])


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