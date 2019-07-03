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

### Notes on subtrees
The idea is to put the documentation build wherever you want, then push only that to the root of the nist-pages branch. This means you can organize your master however you want.

See the Makefile for the commands. The reason you have to auto-add and commit every time is that pushing doesn't work unless your changes are committed.

If you get this error,
```
! [rejected]        e66bbb1de3a69c0d5fd336926d23cabccd09038a -> nist-pages (non-fast-forward)
error: failed to push some refs to 'git@github.com:usnistgov/SOEN-PDK.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
then you did something wrong. This can be caused by making changes to a local nist-pages branch, then pushing them to remote. This will diverge the history. I recommend not even having a local version of the nist-pages branch.

To fix it, you can run
```
git subtree merge --prefix=docs/build/html origin/nist-pages
git checkout --ours docs/build/html
git add docs/build/html
git commit
```
You can pick either ours or theirs version because you are about to overwrite the docs anyways.

If you delete nist-pages branch on the repo, you are done for. You need to contact Steve Barber to delete delete the clone held by pages.nist.gov server and then reclone it.

#### Authors: Sonia Buckley, Jeff Shainline, Adam McCaughan, Jeff Chiles, Alex Tait, Rich Mirin, Sae Woo Nam
#### National Institute of Standards and Technology, Boulder, CO, USA
