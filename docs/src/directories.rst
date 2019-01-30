Project directory structure
===========================
The PDK files are tracked on github [no public link yet]. Most users can follow the :ref:`installation` and not worry about the directory structure below.

OLMAC.lyt
    General technology properties used by klayout

klayout_layers_OLMAC.lyp
    Layer appearance specification. Layers are summarized in :ref:`layers`

camera_ready_OLMAC.lyp
    Another layer appearance specification that is better for making figures in powerpoint or papers.


pcells
------------------------
[in progress]

Parameterized cells specified in phidl code and fixed GDS formats. Available cells are described in :ref:`cells`.


drc
------------------------
OLMAC.lydrc defines the Design Rule Check procedure for klayout's DRC engine. Design rules are documented in :ref:`design_rules`.


xsect
------------------------
OLMAC.xs
    script defining how a top-down layout is turned into a cross-section
OLMAC-xs.lyp
    layer appearance specification for the cross-section view
example.py
    script that produces a fake layout meant to demonstrate all components of the layer stack


properties
------------------------
xml files that describe behavior. This is the measured platform quantities and device quantities. These properties can be populated with guesses or characterization data (see comments in the files themselves). The rationale for this approach is that XML files can be loaded by anything, such as layout code, analysis code, etc.

They enable calculations of
1. Waveguide routing loss
2. Metal routing resistance, including vias
3. Automatic resistor geometry
4. Automatic widening of long, straight waveguides

Example
*******
A straight waveguide might have loss `L_rib` if it's a rib or loss `L_ridge` if it's a ridge. It must start and end as a rib. Let's say a WG transition has loss `L_trans`. If::

    L_ridge + 2 * L_trans < L_rib

then the waveguide will automatically widen in the middle section. Later, the WG loss improves, it is entered it into WAVEGUIDES.xml > transitions > Strip to Ridge > loss, and the whole layout can update accordingly.


docs
------------------------
This documentation


tests
------------------------
[in progress]

Automated unit-tests that ensure the pcells produce consistent geometries


dataprep
------------------------
Procedures defining how to convert user designs to masks

