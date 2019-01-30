import os, sys
klayout_dot_config_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
olmac_dir = os.path.join(klayout_dot_config_dir, 'tech', 'OLMAC')
dataprep_dir = os.path.join(olmac_dir, 'dataprep')
pcell_dir = os.path.join(olmac_dir, 'pcells')
