#------------------------------------------------------------------------------#
# This makefile was generated by 'cbp2make' tool rev.147                       #
#------------------------------------------------------------------------------#


WRKDIR = `pwd`
MAKE = make

all: sdx_api_sdx_api sdx_examples_sdx_examples

sdx_api_sdx_api: 
	$(MAKE) -C sdx_api all -f sdx_api.cbp.mak

sdx_examples_sdx_examples: sdx_api_sdx_api
	$(MAKE) -C sdx_examples all -f sdx_examples.cbp.mak

clean: clean_sdx_api_sdx_api clean_sdx_examples_sdx_examples

clean_sdx_api_sdx_api: 
	$(MAKE) -C sdx_api clean -f sdx_api.cbp.mak

clean_sdx_examples_sdx_examples: 
	$(MAKE) -C sdx_examples clean -f sdx_examples.cbp.mak

.PHONY: clean_sdx_api_sdx_api clean_sdx_examples_sdx_examples

