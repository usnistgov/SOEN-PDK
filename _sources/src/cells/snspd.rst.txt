Waveguide integrated SNSPD
==========================
Description
-----------
SNSPD is a superconducting nanowire single-photon detector. This device is waveguide coupled meaning it detects photons traveling in the silicon waveguide. A similar device with SiN waveguides was shown in :cite:`Shainline:16` and :cite:`Shainline:17`.


.. image:: micrographs/snspd_image.png
    :width: 45%


Characteristics
---------------
The response on SiN measured in :cite:`Shainline:16` is shown here. Response saturation was observed. Characterization on the SOI platform is still in progress.

.. image:: data/snspd_response.pdf
    :width: 45%

Layout
------

.. figure:: layout_pics/snspd_cell.png
    :figwidth: 500px
    :align: center

    The layout produced by the below code.

.. literalinclude:: /../tech/OLMAC/olmac_pcells/detectors.py
    :pyobject: wg_to_snspd