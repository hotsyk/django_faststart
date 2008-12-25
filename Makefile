# Copyright (C) 
include Makefile.def

# Targets
.PHONY: test clean dist todo

test: clean nosetests

nosetests:
	$(MAKE) -C $(app) build test

clean:
	-[ -d db ] && $(MAKE) -C db clean
	$(MAKE) -C $(app) clean
	-rm *~*
	-find . -name '*.pyc' -exec rm {} \;

dist: clean test pylint
	$(MAKE) clean
	git tag -a -f -m "Making release $(ver)" rel-$(ver)
	git archive --prefix=$(proj)-$(ver)/ rel-$(ver) | bzip2 > ../$(proj)-$(ver).tar.bz2

pylint:
	pylint $(app) --max-public-methods=50 --method-rgx='[a-z_][a-z0-9_]{2,40}$$'

run:
	PYTHONPATH=$(PYTHON) $(app)/manage.py runserver
   
syncdb:
	PYTHONPATH=$(PYTHON) $(app)/manage.py syncdb
   
### Local variables: ***
### compile-command:"make" ***
### tab-width: 2 ***
### End: ***