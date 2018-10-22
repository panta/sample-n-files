SHELL = /bin/bash

ifeq (0,${MAKELEVEL})
	PWD      := $(shell pwd)
	TOP_DIR  := $(PWD)
	PRJ_DIR  := $(TOP_DIR)/targasystem_portal
	MAKE := ${MAKE} TOP_DIR=${TOP_DIR} PRJ_DIR=${PRJ_DIR} V=${V}
endif

# PREFIX can be overridden using an environment variable
ifeq ($(PREFIX),)
    PREFIX := /usr/local
endif

venv:
	( \
		if [ ! -e venv ] ; then \
			python -m venv venv ; \
		fi ; \
		source venv/bin/activate && pip install -r requirements.txt && pip install pex && pip install wheel ; \
	)

# see https://idle.run/simple-pex
build sample_n_files.pex: venv
	( \
		source venv/bin/activate && \
		pip wheel -w . . && \
		pex --python="$(PWD)/venv/bin/python" --python-shebang="$(shell pyenv which python3.6)" -f $(PWD) -r ./requirements.txt sample_n_files -e sample_n_files -o sample_n_files.pex ; \
	)

oldbuild:
	pip wheel -w . .
	pex --python-shebang="$(shell pyenv which python3.6)" -f $(PWD) -r ./requirements.txt sample_n_files -e sample_n_files -o sample_n_files.pex ; \

install: build
	install -d $(DESTDIR)$(PREFIX)/bin/
	install -m 755 sample_n_files.pex $(DESTDIR)$(PREFIX)/bin/sample-n-files

clean:
	-rm -f *.whl *.pex
	-rm -rf *.egg-info __pycache__

realclean: clean
	-rm -rf venv
