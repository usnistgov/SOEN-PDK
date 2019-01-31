.. _cells:

PCell library
=============

Using these PCells
******************
PCells are specified in the phidl language in the "olmac_pcells" directory. phidl is open-source and available on PyPI, so anybody can instantiate their geometry (i.e. compile them) regardless of what layout software they choose to use::

    pip install phidl

If you are just checking it out and want to see the GDS, compile with::

    python detectors.py

If you are using them in actual code, use a python interface. That would look like

.. code-block:: python

    # my_layout_script.py
    import olmac_pcells
    phidlDevice = olmac_pcells.snspd(nanowire_width=.15)
    phidlDevice.write_gds('my_snspd.gds')

    import my_preferred_geometry_package
    newDevice = my_preferred_geometry_package.load_gds('my_snspd.gds')

In order to "import olmac_pcells", that package has to be on your python path. For now, our preferred safe approach is to add these lines at the beginning of your script.

.. code-block:: python

    # my_layout_script.py
    import os, sys
    from lygadgets import klayout_home
    sys.path.append(os.path.join(klayout_home(), 'salt', 'soen_pdk', 'tech', 'OLMAC'))
    import olmac_pcells
    ...

.. note::
    We are still deliberating whether it is wise to install pcells system-wide and how to prevent possible name clashes if so. Stay tuned.

Self Tests
**********
The cells are self-testing to ensure that their geometry does not change unexpectedly. Fixed reference layouts are tracked in the ``ref_layouts`` directory. A test consists of running the code and comparing the resulting layout to the reference layout. This is all handled by `lytest <https://github.com/atait/lytest>`_.

Tests are run from the top SOEN-PDK directory with::

    make test

The reason for doing is is to allow for frequent updates to the PDK. Code should be able to change (e.g. better implementation, additional arguments). It is, of course, very bad if those changes result in geometry changes affecting your layouts. Self-testing that is performed automatically offers an assurance that you can count on those pcells being exactly the same, at least for the tested arguments.


.. toctree::
    :maxdepth: 1
    :caption: Available PCells
    :glob:

    *

