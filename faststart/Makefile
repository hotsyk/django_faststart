# Copyright (C) 

include ../Makefile.def

noseopt=-w .. --with-coverage --cover-package=$(app) --exe

modules=$(app)

.PHONY: build test clean doc

test:
	PYTHONPATH=$(PYTHONPATH):. DJANGO_SETTINGS_MODULE=$(test_settings) nosetests  $(noseopt) $(modules)

clean:
	-rm *~*
	-rm *.pyc

### Local variables: ***
### compile-command:"make" ***
### tab-width: 2 ***
### End: ***