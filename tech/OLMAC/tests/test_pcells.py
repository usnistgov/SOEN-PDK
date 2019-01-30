''' This file defines tests that produce pcell geometry.
    The geometry is compared by XOR to the reference layouts.

    If the pcell code results in different behavior, the test will fail,
    so that you can be sure that your layouts will not change even if the PDK updates.

    An exception is when the behavior changes intentionally.
    This change will be visible in the commits (the .gds in ref_layouts will change).
    It will always be accompanied by some kind of announcement or deprecation warning.
        - We really don't want to break your stuff.
        - But this is early stage, so there will be changes happening, possibly sloppily.
    For this reason, it is encouraged that you do your own testing with lytest on your own layouts:
    github.com/atait/lytest
'''
import sys
from conftest import pcell_dir, olmac_dir
sys.path.append(olmac_dir)  # make pcells visible
import pcells

import lytest
from lytest import contained_phidlDevice, difftest_it

@contained_phidlDevice
def htron(TOP):
    lytest.utest_buds.test_root = pcell_dir  # look for ref_layouts in the right place
    TOP << pcells.htron()
    TOP << pcells.htron(heater_num_squares = 10).movex(20)

def test_htron(): difftest_it(htron)()


@contained_phidlDevice
def mmi1x2(TOP):
    lytest.utest_buds.test_root = pcell_dir  # look for ref_layouts in the right place
    TOP << pcells.mmi1x2()

def test_mmi1x2(): difftest_it(mmi1x2)()
