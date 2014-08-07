#!/bin/bash

# old aux files can contaminate when compiling
rm *.aux
# compile
pdflatex --shell-escape example
# cleanup
rm *.aux
rm *.log


