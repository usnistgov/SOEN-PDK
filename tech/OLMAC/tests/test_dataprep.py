''' This file defines tests that produce mask files.
    The geometry is compared by XOR to the reference layouts.
'''

import os
dataprep_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'dataprep'))
klayout_dot_config_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..'))

import lytest
lytest.utest_buds.test_root = dataprep_dir  # look for ref_layouts in the right place
lytest.utest_buds.get_test_dir()  # create the test dir if it does not exist yet
from lytest import contained_script, difftest_it
from lymask import batch_main


@contained_script
def default_dataprep():
    os.environ['KLAYOUT_HOME'] = klayout_dot_config_dir
    layout_file = os.path.join(dataprep_dir, 'src_layouts', 'default_dataprep.gds')
    outfile = os.path.join(dataprep_dir, 'run_layouts', 'default_dataprep.gds')
    batch_main(layout_file, ymlspec='default', outfile=outfile, technology='OLMAC')
    return outfile

def test_default_dataprep(): difftest_it(default_dataprep)()