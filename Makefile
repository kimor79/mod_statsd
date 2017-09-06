#!/usr/bin/make -f
#
#
all:
	apxs -a -c -Wl,-Wall -Wl,-lm -I. mod_statsd.c


