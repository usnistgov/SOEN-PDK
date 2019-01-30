try:
    import phidl
except ImportError as err:
    err.args = ('''phidl is required to run tests and generate fixed GDSs.
                   pip install phidl
                ''' + err.args[0],) + err.args[1:]
    raise

try:
    import lytest
except ImportError as err:
    err.args = ('''lytest is required to run tests.
                   pip install lytest
                ''' + err.args[0],) + err.args[1:]
    raise

try:
    import lymask
except ImportError as err:
    err.args = ('''lymask is required to run tests.
                   pip install lymask
                ''' + err.args[0],) + err.args[1:]
    raise


import sys, os
klayout_dot_config_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..'))
pcell_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'pcells'))
dataprep_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'dataprep'))
sys.path.append(pcell_dir)  # make pcells visible