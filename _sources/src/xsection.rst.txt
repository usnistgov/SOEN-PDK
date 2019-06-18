.. _xsection:

Cross Sections
==============
Cross sections are nice tools for examining structures in three dimensions.


Setup
-----
#. Open KLayout
#. Click the menu Tools > Manage Packages
#. Double-click "xsection"
#. Click "Apply"


Usage
-----
The xsection script is based on a ruler. Start by drawing a ruler by pressing "R".

.. figure:: images/basic_ruler.png
    :alt: A ruler
    :figwidth: 300px
    :align: center

    This is a ruler.

Run the xsection script by going to Tools > Xsection Scripts > Xsection: Active Technology (Cmd-X). Xsection needs exactly one ruler present. You can clear all rulers with Cmd-K.


Try it out
----------
`OLMAC/xsect/example.py` produces a dummy layout (`example.gds`) designed to illustrate all aspects of the OLMAC layer stack. Try drawing rulers there. A ruler across the whole thing and its corresponding cross-section look like this.

.. figure:: images/xs_source.png
    :alt: examplegds
    :figwidth: 700px
    :align: center

    Layout example contained in this PDK, designed to show XSection.

.. figure:: images/xs_result.png
    :alt: examplexs
    :figwidth: 700px
    :align: center

    Corresponding cross-section.

