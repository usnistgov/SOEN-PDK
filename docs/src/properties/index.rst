.. _properties:

Platform Properties
=====================

Properties pertain to the platform. They are experimentally measurable but distinct from device behavior. Platform properties are more general in that they apply to many different types of devices and nonideality cases. They can be used to analyze expected nonideality or to produce designs that minimize nonideality.

For example, sheet resistivity can be used to analyze parasitics in wiring nets or to design discrete resistors or to model parasitics in a parallel plate capacitor between two conductive layers.

Another example: consider a straight waveguide that incurs optical loss. We've found that loss is dominated by sidewall scattering, which means multimode (a.k.a. "longhaul") waveguides have less loss per centimeter. If the waveguide is long enough, this propagation loss can more than amortize the loss from tapering from regular to longhaul. Your code can make the decision of whether to taper based on these properties.

.. toctree::
    :maxdepth: 2
    :glob:

    *