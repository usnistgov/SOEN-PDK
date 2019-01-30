.. _installation:

Installation
============

If you do not have KLayout yet, `download klayout here <https://www.klayout.de/build.html>`_ and follow its installation instructions.

Then run these lines::

    git clone git@github.com:atait/SOEN_PDK.git
    pip install lygadgets
    lygadgets_link SOEN_PDK/klayout_dot_config
    # Good to go

The meanings of these lines are explained below.

.. warning::

    If you are a Windows/Anaconda user, you must do these commands within an Anaconda 3 prompt with administrator privileges.

.. KLayout is arguably the highest-performing and most advanced layout viewer in the 10\ :sup:`0`\ €/$ – 10\ :sup:`4`\ €/$ range. It is `free software <https://www.gnu.org/philosophy/open-source-misses-the-point.html>`_.

SOEN PDK
--------
Download this `SOEN_PDK tarball <https://github.com/atait/SOEN_PDK/archive/master.tar.gz>`_. Or, if you want to look through the sources and/or develop and/or keep up to date with changes, clone it with::

    git clone git@github.com:atait/SOEN_PDK.git

.. note::

    This PDK is not yet publicly available. Please request private access to the repo or follow the enclosed instructions to download/clone from a NIST server.


Linking SOEN PDK to KLayout
---------------------------
For this you need something called lygadgets::

    pip install lygadgets

Then `cd` into the "SOEN_PDK" directory and call::

    lygadgets_link klayout_dot_config

.. warning::

    If you are a Windows/Anaconda user, you must do these commands within an Anaconda 3 prompt with administrator privileges.

.. note::

    By default, lygadgets creates a symbolic link that will break if you trash the original tarball. If you like to clean your Downloads, add the `-c` (hard copy) flag to the `lygadgets_link` call.

.. In the future, the OLMAC PDK will probably be pulled apart from the somewhat nebulous "SOEN_PDK" repo, which also has a bunch of code. If you just want the OLMAC PDK, or, for a more semi-future-proof version, do lygadgets_link klayout_dot_config/tech/OLMAC


Activation
----------
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


SOEN Developers
---------------
Please help write this documentation. To build the docs, `cd` into the OLMAC/docs directory and call::

    make

First time, it will spew a lot of text at you. Open your local version of them with::

    open _build/html/index.html`

Upon subsequent builds, make sure to refresh the pages, not just backspace in Safari.

Windows users
*************
Open a new *Anaconda 3* shell. Install virtualenv::

    pip install virtualenv
    pip install virtualenvwrapper-win

Navigate to the "OLMAC/docs" directory that you use or just downloaded. The first time, you will make a new environment::

    virtualenv --prompt "(OLMAC-docs-venv) " --distribute venv
    venv\Scripts\activate
    pip install -r requirements.txt

You can exit this environment with the `deactivate` command. Make the documentation with::

    sphinx-build -b html -j4 . _build/html

Then open it with::

    start _built/html/index.html


