# SOEN PDK
NIST Superconducting Optoelectronic Networks (SOEN) Process Design Kit (PDK).

This kit defines the *OLMEC* process, which combines superconducting electronics, such as SNSPDs and three-terminal devices, active optoelectronics, such as LEDs and modulators, and passive optics, such as waveguides and resonators.

*Documentation is in transition, so some features won't work yet*

See the main documentation on pages.nist.gov (not yet)

## Installation
```bash
git clone git@github.com:usnistgov/SOEN-PDK.git
pip install lygadgets
lygadgets_link OLMEC
```

If you are a Windows/Anaconda user, you must do these commands within an Anaconda 3 prompt with administrator privileges.

**Salt package** to come.


## Contents
### Process specification
- Layer physical dimensions
- Layout indices and appearance
- Design rule check (DRC)

All of this information can be used by KLayout in some way.

### Platform properties
- Waveguide loss
- Resistivity
- Critical temperature
- etc.

### Device PCells
Tested device designed as fixed cells (OAS/GDS) and phidl code (python).

Detailed docs include optical/electron micrographs and measured data of the standard devices.

### Fabrication info
- Process steps
- Mask data preparation



## NIST Developers
See the [Developer documentation](README-developer.md)



#### Authors: Sonia Buckley, Jeff Shainline, Adam McCaughan, Jeff Chiles, Alex Tait, Rich Mirin, Sae Woo Nam
#### National Institute of Standards and Technology, Boulder, CO, USA
