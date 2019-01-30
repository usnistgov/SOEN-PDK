# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -j4
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

DOCTYPE_DEFAULT = html
# Server ports for CI hosting. You can override by setting an environment variable DOCHOSTPORT
DOCHOSTPORT ?= 8035

.PHONY: all help venv clean purge host html epub latexpdf text changes linkcheck

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  venv       to initialize virtualenv and install packages needed to build the docs
	@echo "  clean      to clear build cache
	@echo "  purge      to clear build and dump the virtualenv
	@echo "  host       to host an HTTP server on DOCHOSTPORT
	@echo "  html       to make standalone HTML files"
	@echo "  epub       to make an epub"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"

.DEFAULT_GOAL := html

# Virtual environment for building and hosting the docs
venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -e venv/bin/activate || virtualenv -p python3 --prompt "(OLMAC-docs-venv) " --distribute venv
	touch venv/bin/activate
	( \
		source venv/bin/activate; \
		pip install -r requirements.txt | grep -v 'Requirement already satisfied'; \
	)

clean:
	rm -rf $(BUILDDIR)

purge: clean
	rm -rf venv/*

host: venv
	( \
		source venv/bin/activate; \
		cd _build/html; \
		python3 -m http.server $(DOCHOSTPORT); \
	)




# Below is typical boilerplate for Sphinx projects
html: venv
	( \
		source venv/bin/activate; \
		$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html; \
	)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

epub: venv
	( \
		source venv/bin/activate; \
		$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub; \
	)
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latexpdf: venv
	( \
		source venv/bin/activate; \
		$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex; \
		@echo "Running LaTeX files through pdflatex..."
		$(MAKE) -C $(BUILDDIR)/latex all-pdf
	)
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text: venv
	( \
		source venv/bin/activate; \
		$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text; \
	)
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

changes: venv
	( \
		source venv/bin/activate; \
		$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes; \
	)
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck: venv
	( \
		source venv/bin/activate; \
		$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck; \
	)
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."
