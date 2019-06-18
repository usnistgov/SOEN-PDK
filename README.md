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


## Documentation
All the documentation is html. It is found on the WWW at [here](https://pages.nist.gov/SOEN-PDK).

Test link: [here](docs/tmp/index.html)

For now, you must build and view it yourself with

```bash
make docs
open docs/build/html/index.html
```


## Dependencies
There are no explicit python dependencies, but there are some needed for full functionality.

To build the pcells
```
pip install phidl
```

To have the pcells appear in the KLayout GUI and the klayout.db standalone
```
pip install lygadgets
lygadgets_link lygadgets
```

#### Authors: Sonia Buckley, Jeff Shainline, Adam McCaughan, Jeff Chiles, Alex Tait, Rich Mirin, Sae Woo Nam
#### National Institute of Standards and Technology, Boulder, CO, USA
