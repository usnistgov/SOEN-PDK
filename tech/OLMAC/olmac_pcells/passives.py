from phidl import Device, geometry as pg
import numpy as np

import os
from phidl.utilities import load_lyp
lyp_file = os.path.join(os.path.dirname(__file__), '..', 'klayout_layers_OLMAC.lyp')
lys = load_lyp(lyp_file)


def mmi1x2(wg_width=0.35, length_port=0.2, length_mmi=2.8, width_mmi=1.55, gap_mmi=0.4):

    D=Device()

    Port_wg=pg.taper(length=length_port,width1=wg_width,width2=wg_width,layer=lys['wg_deep'])
    port_in=D.add_ref(Port_wg)
    MMI=pg.taper(length=length_mmi,width1=width_mmi,width2=width_mmi,layer=lys['wg_deep'])
    mmi=D.add_ref(MMI)

    mmi.connect(port=1,destination=port_in.ports[2])

    port_up=D.add_ref(Port_wg)
    port_up.connect(port=1,destination=mmi.ports[2])
    port_up.movey(gap_mmi)

    port_down=D.add_ref(Port_wg)
    port_down.connect(port=1,destination=mmi.ports[2])
    port_down.movey(-gap_mmi)

    D.add_port(name=1,port=port_in.ports[1])
    D.add_port(name=2,port=port_up.ports[2])
    D.add_port(name=3,port=port_down.ports[2])

    return D

if __name__ == '__main__':
    mmi1x2().write_gds('mmi1x2.gds')