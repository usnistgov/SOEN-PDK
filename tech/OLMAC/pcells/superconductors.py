from phidl import Device, geometry as pg
import numpy as np

import os
from phidl.utilities import load_lyp
lyp_file = os.path.join(os.path.dirname(__file__), '..', 'klayout_layers_OLMAC.lyp')
lys = load_lyp(lyp_file)


def htron(nanowire_width = 0.15, nanowire_spacing = 0.1,
          meander_num_squares = 5000, heater_num_squares = 1):

    # Create blank device
    D = Device(name = 'htron')

    # Basic calculations
    extra_meander_width = 2
    extra_meander_height = 1
    area_per_meander_sq = (nanowire_width+nanowire_spacing)*nanowire_width
    meander_area = area_per_meander_sq*meander_num_squares
    meander_total_width = np.sqrt(meander_area/heater_num_squares)
    meander_total_height = heater_num_squares*meander_total_width
    meander_size = np.array([meander_total_width, meander_total_height])
    heater_size = meander_size

    meander_size = meander_size + [extra_meander_width,extra_meander_height]

    # meander_size = heater_size + np.array([meander_extra_width,0])
    meander_pitch = nanowire_width + nanowire_spacing
    # heater_standoff_y = 1

    # Create components
    Meander = pg.snspd_expanded(wire_width = nanowire_width, wire_pitch = meander_pitch, size = meander_size,
               terminals_same_side = False, connector_width = nanowire_width*4, layer = lys['m2_nw'])
    # heater_size_actual = heater_size + np.array([0, heater_standoff_y])
    Heater = pg.compass(size = heater_size, layer = lys['m3_res'])

    # Add references to components
    m = D.add_ref(Meander)
    h = D.add_ref(Heater)
    h.center = m.center


    # Record meta-information
    heater_area = heater_size[0]*heater_size[1]
    D.info['nanowire_width'] = nanowire_width
    D.info['nanowire_pitch'] = nanowire_width + nanowire_spacing
    D.info['meander_num_squares'] = np.round(m.info['num_squares'],2)
    D.info['meander_size'] = np.round((m.xsize, m.ysize),2).tolist()
    D.info['heater_size'] = np.round(heater_size,2).tolist()
    D.info['heater_area'] = np.round(heater_size[0]*heater_size[1],2)
    D.info['heater_num_squares'] = np.round(heater_num_squares,2)
    D.info['overlap_area'] = np.round(m.ysize*heater_size[0],1)
    D.info['overlap_num_squares'] = np.round(heater_area/area_per_meander_sq,1)

    D.add_port(name = 1, port = h.ports['N'])
    D.add_port(name = 2, port = h.ports['S'])
    D.add_port(name = 3, port = m.ports[1])
    D.add_port(name = 4, port = m.ports[2])

    return D


if __name__ == '__main__':
    D = htron()
    D.write_gds('htron.gds')
