ifndef SPECFILE
	SPECFILE = $(firstword $(wildcard *.spec))
endif

NAME = mod_statsd

VERSION = 0.0.1

REVISION = 1

ifndef WORKDIR
  WORKDIR = $(shell pwd)
endif

ifndef SRCRPMDIR
  SRCRPMDIR = $(WORKDIR)
endif

ifndef BUILDDIR
  BUILDDIR = $(WORKDIR)
endif

ifndef RPMDIR
  RPMDIR = $(WORKDIR)
endif

ifndef SOURCEDIR
  SOURCEDIR = $(shell pwd)
endif

SED_INLINE_BY_OS=$(shell [ "`uname`" == "Darwin" ] && echo ".tmp")

info:
	@echo NAME: $(NAME)-$(VERSION)-$(REVISION)
	@echo SPEC: $(SPECFILE)

clean:
	rm -f *~ $(NAME)*.bz2 $(NAME)*.src.rpm
	rm -rf .$(NAME)-$(VERSION)
	
git-clean:
	@git clean -d -q -x

prepare-spec:
	sed -i $(SED_INLINE_BY_OS) 's/#VERSION#/$(VERSION)/' $(WORKDIR)/$(SPECFILE) | true
	sed -i $(SED_INLINE_BY_OS) 's/#REVISION#/$(REVISION)/' $(WORKDIR)/$(SPECFILE) | true
	@rm -f $(WORKDIR)/$(SPECFILE).tmp

zip-files:
	tar cvjf /root/rpmbuild/SOURCES/mod_statsd.tar.bz2 -C /usr/src/ mod_statsd

tarball: clean prepare-spec zip-files

sources: tarball


rpm: tarball
	$(RPM_WITH_DIRS) $(DIST_DEFINES) -bb $(SPECFILE)


REPORTER ?= dot

.PHONY: info 
