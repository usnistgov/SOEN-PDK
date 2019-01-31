# SOEN PDK
NIST Superconducting Optoelectronic Networks (SOEN) Process Design Kits (PDK).

This kit defines the *OLMEC* process, which combines superconducting electronics, such as SNSPDs and three-terminal devices, active optoelectronics, such as LEDs and modulators, and passive optics, such as waveguides and resonators.


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
All the documentation is html. It is found on the WWW at pages.nist.gov (not yet).

For now, you must build and view it yourself with

```bash
make docs
open docs/_build/html/index.html
```


## NIST Developers
### Branching structure
- master [protected]: release code, must work at all times; pulls only from development; every merge commit is a tagged version such as "v0.1.1"
- development: base point for new features, should be working almost all the time; when ready, merges new features into master
- nist-pages [protected]: documentation "master" that is hosted, based off of *development* and pulls only from development; features documented that are not yet released should be marked as "beta" or "pre-release"
- other: in-progress features, based off of development

[protected] means there are no direct commits.

### Directory structure
It is designed to be able to hold independent PDKs for multiple processes. These can be installed into klayout one at a time.

### How to document
Jekyll setup, viewing your local changes, Markup languages, documentation structure...



#### Authors: Sonia Buckley, Jeff Shainline, Adam McCaughan, Jeff Chiles, Alex Tait, Rich Mirin, Sae Woo Nam
#### National Institute of Standards and Technology, Boulder, CO, USA
