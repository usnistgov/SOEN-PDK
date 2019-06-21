SHELL := /bin/bash

venv: venv/bin/activate
venv/bin/activate:
	test -d venv || virtualenv -p python3 --prompt "(NIST-SOEN-venv)" --distribute venv
	touch venv/bin/activate

clean:
	rm -rf docs/build
	rm -rf _site

purge: clean
	rm -rf venv

# Testing
testbuild: venv/build_info/testreqs
venv/build_info/testreqs: venv requirements-test.txt
	source venv/bin/activate && pip install -r requirements-test.txt
	@mkdir -p venv/build_info/testreqs
	@touch venv/build_info/testreqs

test: testbuild
	source venv/bin/activate && pytest tech/OLMAC/tests


# Documentation
SPHINXOPTS = -j4
BUILDDIR = docs/build
docbuild: venv/build_info/docreqs
venv/build_info/docreqs: venv requirements-docs.txt
	source venv/bin/activate && pip install -r requirements-docs.txt
	mkdir -p venv/build_info/docreqs
	touch venv/build_info/docreqs

html: docbuild
	( \
		source venv/bin/activate; \
		sphinx-build -b html $(SPHINXOPTS) docs $(BUILDDIR)/html; \
	)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

latexpdf: docbuild
	( \
		source venv/bin/activate; \
		sphinx-build -b latex $(SPHINXOPTS) docs $(BUILDDIR)/latex; \
		@echo "Running LaTeX files through pdflatex..."
		$(MAKE) -C $(BUILDDIR)/latex all-pdf
	)
	@echo "Build finished. The PDF files are in $(BUILDDIR)/latex."

docs: html

docdeploy: html
	# When NIST pages gets fixes, I should be able to delete my local nist-pages branch
	git subtree push --prefix $(BUILDDIR)/html origin nist-pages

.PHONY: clean purge test html latexpdf docs