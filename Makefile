SHELL := /bin/bash

venv: venv/bin/activate
venv/bin/activate:
	test -d venv || virtualenv -p python3 --prompt "(NIST-SOEN-venv)" --distribute venv
	touch venv/bin/activate

clean:
	rm -rf docs/_build

purge: clean
	rm -rf venv

# Testing
testbuild: venv/build_info/testreqs
venv/build_info/testreqs: requirements-test.txt
	source venv/bin/activate && pip install -r requirements-test.txt
	@touch venv/build_info/testreqs

test: testbuild
	source venv/bin/activate && pytest


# Documentation
SPHINXOPTS    = -j4
BUILDDIR = docs/_build
docbuild: venv/build_info/docreqs
venv/build_info/docreqs: requirements-docs.txt
	source venv/bin/activate && pip install -r requirements-docs.txt
	@touch venv/build_info/docreqs

html:
	( \
		source venv/bin/activate; \
		sphinx-build -b html $(SPHINXOPTS) docs $(BUILDDIR)/html; \
	)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

latexpdf: venv
	( \
		source venv/bin/activate; \
		sphinx-build -b latex $(SPHINXOPTS) docs $(BUILDDIR)/latex; \
		@echo "Running LaTeX files through pdflatex..."
		$(MAKE) -C $(BUILDDIR)/latex all-pdf
	)
	@echo "Build finished. The PDF files are in $(BUILDDIR)/latex."

docs: html


.PHONY: clean purge test html latexpdf docs