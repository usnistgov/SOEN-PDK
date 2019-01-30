.. _cells:

PCell library
=============

Using these PCells
******************
PCells are specified in the phidl language in the "pcells" directory. phidl is open-source and available on PyPI, so anybody can instantiate their geometry (i.e. compile them) regardless of what layout software they choose to use::

    pip install phidl

If you are just checking it out and want to see the GDS, compile with::

    python detectors.py

If you are using them in actual code, use a python interface. That would look like

.. code-block:: python

    # my_layout_script.py
    import detectors
    phidlDevice = detectors.snspd(nw_width=.15)
    phidlDevice.write_gds('my_snspd.gds')

    import my_preferred_geometry_package
    newDevice = my_preferred_geometry_package.load_gds('my_snspd.gds')

In order to "import detectors", that module has to be on your python path. You must add it like this

.. code-block:: python

    # my_layout_script.py
    import os, sys
    sys.path.append('path/to/SOEN-PDK/tech/OLMAC/pcells')
    import detectors
    ...

.. note::
    Path manipulation is annoying but also explicit. This is intentional. We are still deliberating whether it is wise to install these modules system-wide and how to prevent possible name clashes if so.


The cells are self-testing to ensure that their geometry does not change unexpectedly. Fixed reference layouts are tracked in the ``ref_layouts`` directory. A test consists of running the code and comparing the resulting layout (not tracked) to the reference layout. Tests are run from the top SOEN-PDK directory with::

    make test


.. toctree::
    :maxdepth: 1
    :caption: Available PCells
    :glob:

    *

