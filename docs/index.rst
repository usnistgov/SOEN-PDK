OLMAC Technology Definition and Documentation
================================================

This technology package, a.k.a process design kit (PDK), defines the NIST superconducting optolectronics process: **OLMAC**. It is in the `klayout <https://www.klayout.de>`_ format of technology definition.

OLMAC combines **superconducting electronics**, such as SNSPDs and three-terminal devices, **active optoelectronics**, such as LEDs and modulators, and **passive optics**, such as waveguides and resonators.

.. It stands for Ol' Macdonald had a farm, EOEOE. EOEOE refers to the conversion of electric current to electric current with high gain and an Optical/Electrical/Optical intermediarity. This "intermediatiary" is a photonic neuron.

.. If you'd like, you could view this PDK as a standardization of an open optical process design kit. It pertains specifically to NIST's neuromorphic photonics process, yet it is theoretically applicable to SOI foundries, certain III/V business, proprietary BEOL steps, and in-house SiNx stuff (given a forthcoming package on advanced waveguide specification). Fork it, modify it, and, if you can generalize out the non-sensitive components of your work, make pull requests.

Contributors: Sonia Buckley, Adam McCaughan, Jeff Chiles, Alex Tait, Saeed Khan, Jeff Shainline, Rich Mirin, Sae Woo Nam

NIST, PML, Applied Physics, Faint/Quantum Nanophotonics group, Boulder, CO, United States

:ref:`Jump to installation <installation>`

What's in the box
-----------------

:ref:`PCells <cells>`
*********************
This PDK includes standard devices as fixed cells (GDS) and `phidl <https://github.com/amccaugh/phidl>`_ code (python). These HTML pages include optical/electron micrographs and measured data of the standard devices.

.. image:: src/cells/layout_pics/hTron_blender.png
    :target: src/cells/hTron.html
    :height: 150px
.. image:: src/cells/layout_pics/led_blender.png
    :target: src/cells/led.html
    :height: 150px
.. image:: src/cells/layout_pics/mmi1x2_cell.png
    :target: src/cells/mmi1x2.html
    :height: 150px


:ref:`Design Tools <design_rules>`
******************************************
GDS layers, datatypes, names, and appearance.
All of these components integrate with the klayout application


:ref:`Platform Properties <properties>`
***************************************
Measured behavioral properties of the platform

.. warning::

    Some of these properties are not yet measured, as indicated in the properties files (.xml).

.. note::

    We have a package in development that allows you to read these properties into phidl and use them in your code. Let's say you want to make a resistor function with a layer argument (wiring, doped Si, etc.). That function could read the sheet resistance out of the properties file. If properties change, the resistor geometry will change automatically. Updates to come.


Fabrication Procedures
***************************
#. Fabrication steps
#. Process sheets (too detailed?)
#. Mask preparation procedures


.. toctree::
    :maxdepth: 2
    :caption: Contents

    src/installation
    src/cells/index
    src/layers
    src/xsection
    src/drc/index
    src/properties/index
    src/directories
    src/todo


Acknowledgements
----------------
This documentation is templated upon `lightlab <https://lightlab.readthedocs.io>`_, the experimental frameworks of the Princeton Lightwave Research Laboratory:

* Paul Prucnal, Thomas Ferreira de Lima, Bhavin Shastri, Heidi Miller, Siamak Abbaslou, Yechi Ma, Chaoran Huang, Aashu Jha, Eric Blow, and Mitch Nahmias.

PDK structure was modeled around the General Silicon Photonics (GSiP) tech found within the `SiEPIC-Tools <https://github.com/lukasc-ubc/SiEPIC-Tools>`_ project:

* Lukas Chrostowski, Zeqin Lu, Jonas Flueckiger, Xu Wang, Jackson Klein, Amy Liu, Jaspreet Jhoja, and James Pond



