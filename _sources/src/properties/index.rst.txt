.. _properties:

Platform Properties
=====================

Property values describe the behavior to the platform. These properties can be populated with guesses or characterization data (see comments in the files themselves). They can be used to analyze expected nonideality or to produce designs that minimize nonideality.

The rationale for this approach is that XML files can be loaded by anything, such as layout code, analysis code, etc. In this way, they enable calculations of

1. Waveguide routing loss
2. Metal routing resistance, including vias
3. Automatic resistor geometry
4. Automatic widening of long, straight waveguides

Example
*******
A straight waveguide might have loss `L_rib` if it's a rib WG or loss `L_ridge` if it's a ridge WG. It must start and end as a rib. Let's say a WG transition has loss `L_trans`. Then, if::

    L_ridge + 2 * L_trans < L_rib

then the waveguide will automatically widen in the middle section. Later, if the WG loss improves, it is entered it into WAVEGUIDES.xml > Strip > loss. As a result, the whole layout will update accordingly.


.. toctree::
    :maxdepth: 2
    :glob:

    *