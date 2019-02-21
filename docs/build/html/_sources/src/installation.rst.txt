.. _installation:

Installation
============

To get this PDK itself::

    git clone git@github.com:usnistgov/SOEN-PDK.git

If you do not have KLayout yet, `download klayout here <https://www.klayout.de/build.html>`_ and follow its installation instructions.

To use them together, you must create a link::

    pip install lygadgets
    lygadgets_link SOEN-PDK

.. warning::

    If you are a Windows/Anaconda user, you must do these commands within an Anaconda 3 prompt with administrator privileges.

Restart KLayout. Under the below dropdown, you should see OLMAC. Select it. Then press the "T".

.. figure:: images/tech_menu.png
    :alt: The technology button
    :figwidth: 200px
    :align: center

    This is where you change technolgies


.. _xsection_install:

Recommended: Cross Section Engine
---------------------------------
In order to create cross-sections, you need another package that is distributed via the KLayout package manager. The steps are

#. Open KLayout
#. Click the menu Tools > Manage Packages
#. Double-click "xsection"
#. Click "Apply"


Recommended: If you use script-based layout
-------------------------------------------
Script-based layout is vastly superior to hand-based layout, but it carries challenges. The variable and geometry state is opaque during execution, and the relationship between code changes and produced geometry is not obvious. We have released some packages to address these issues

* `lyipc <https://github.com/atait/klayout-ipc>`_: visual geometry debugging at runtime
* `lytest <https://github.com/atait/lytest>`_: automated verification of script-to-geometry correctness

See their READMEs. Both are available via pip, and both are language-independent (phidl, gdspy, pya, klayout.db, nazca). It wouldn't be too hard to extend them to MatlabGDSPhotonics, KiCad, CNST Toolbox, ZIC, etc. Email me if you use one of these and like the idea of lypackages.


Building this documentation
---------------------------
NIST developers, please help write this documentation. To build the docs, `cd` into the SOEN-PDK directory and call::

    make docs

First time, it will spew a lot of text at you. Open your local version of them with::

    open docs/_build/html/index.html

Upon subsequent builds, make sure to refresh the pages, not just backspace in Safari.



