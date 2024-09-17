# Makefile for GatorTaxi project
# code by Kushagra Sikka
# UFID: 3979-0988
# ADS Project final submission

# set the python interpreter
PYTHON = python3

# set the default input file
DEFAULT_INPUT_FILE = input.txt

# compile the source code
run:
	$(PYTHON) gatorTaxi.py $(input_file)

# remove the output file
clean:
	rm output_file.txt
