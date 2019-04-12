COMMAND_LINE_OPTIONS=
export PYTHONPATH := .:$(PWD)/vendor/:$(PYTHONPATH)

all: run

run:
	./webapp.py $(COMMAND_LINE_OPTIONS)
