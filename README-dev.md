# SOEN PDK for developers

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
