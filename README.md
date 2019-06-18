# SOEN PDK
NIST Superconducting Optoelectronic Networks (SOEN) Process Design Kits (PDK).

This kit defines the *OLMEC* process, which combines superconducting electronics, such as SNSPDs and three-terminal devices, active optoelectronics, such as LEDs and modulators, and passive optics, such as waveguides and resonators.

**This project in in a preliminary stage. Major updates are planned before first release, and anything (including the project name) is subject to change.**


## Installation
```bash
git clone git@github.com:usnistgov/SOEN-PDK.git
pip install lygadgets
lygadgets_link SOEN-PDK/tech/OLMAC
```

If you are a Windows/Anaconda user, you must do these commands within an Anaconda 3 prompt with administrator privileges.

**Salt package** to come.

**PyPI** release is not planned.

### Activation
On the klayout menu bar, there is a "T" in a circle which has a down triangle. In the dropdown list, select OLMAC. When you restart KLayout, this technology should stay selected.


## Documentation
Main [documentation](https://pages.nist.gov/SOEN-PDK) on NIST pages.

Developers who are modifying the docs can rebuild them with `make docs` or `make html`. The output is in `_site/index.html`.


## Feature Summary
- Superconducting optoelectronic PCells
- Layer properties
- DRC specification
- Xsection specification
- "tech" package that can be understood by and loaded into KLayout application
- XML properties for WAVEGUIDES, VIAS, etc.
- Data preparation specifications to be used with [lymask](https://github.com/atait/lymask)


## Testing
Test that PCells produce the expected geometry and that dataprep is working, run `make test` in the repo root.


## Using PCells
PCells are implemented in [phidl](https://github.com/amccaugh/phidl), so that must be installed.
```
pip install phidl
```
Despite this, the PCells can be used in pya, SiEPIC-type projects, and the klayout GUI by wrapping the implementation with the appropriate interface.

To have the pcells appear in the KLayout GUI and the klayout.db standalone
```
lygadgets_link lygadgets
```
Go to klayout's Cell placement icon. "OLMAC" should appear in the list of available libraries. By changing parameters and clicking "Apply," the outline will update live.

To use the PCells in a script, you must first specify the pcell location.
```
from lygadgets.technology import Technology
olmac_path = Technology.technology_by_name('OLMAC').base_path()
import sys
sys.path.append(olmac_path)
```
This will allow you to see `olmac_pcells`. They are ready to use in `phidl` right away
```
from olmac_pcells import wg_to_snspd
D = wg_to_snspd(wgnw_length=200)  # this is a phidl.Device object
```

To use them in a pya-based script,
```
from lygadgets.autolibrary import WrappedPCell
WgToSNSPD = WrappedPCell(wg_to_snspd)  # This is a subclass of PCellDeclarationHelper
```
How it is used varies depending on whether you use raw `pya` or SiEPIC-style KlayoutPCells. An example of the latter, assuming that `layout` is defined:
```
wg_cell, wg_ports = WgToSNSPD('My_SNSPD').pcell(layout, params={'wgnw_length': 200})
```


#### Authors: Alex Tait, Sonia Buckley, Jeff Shainline, Adam McCaughan, Jeff Chiles, Rich Mirin, Sae Woo Nam
#### National Institute of Standards and Technology, Boulder, CO, USA
