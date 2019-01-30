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
import os, sys
pcell_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'pcells'))
sys.path.append(pcell_dir)  # make pcells visible
import pcells

import lytest
from lytest import contained_phidlDevice, difftest_it
lytest.utest_buds.test_root = pcell_dir  # look for ref_layouts in the right place
lytest.utest_buds.get_test_dir()  # create the test dir if it does not exist yet

@contained_phidlDevice
def htron(TOP):
    TOP << pcells.htron()
    TOP << pcells.htron(heater_num_squares = 10).movex(20)

def test_htron(): difftest_it(htron)()


@contained_phidlDevice
def mmi1x2(TOP):
    TOP << pcells.mmi1x2()

def test_mmi1x2(): difftest_it(mmi1x2)()
