import os, sys
from os.path import realpath, dirname, join
klayout_dot_config_dir = realpath(join(dirname(__file__), '..', '..', '..'))
olmac_dir = join(klayout_dot_config_dir, 'tech', 'OLMAC')
dataprep_dir = join(olmac_dir, 'dataprep')
pcell_dir = join(olmac_dir, 'pcells')
