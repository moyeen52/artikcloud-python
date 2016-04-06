 #!/bin/bash

REQUIREMENTS_FILE=dev-requirements.txt
REQUIREMENTS_OUT=dev-requirements.txt.log
SETUP_OUT=*.egg-info
VENV=.venv

clean:
		rm -rf $(REQUIREMENTS_OUT)
		rm -rf $(SETUP_OUT)
		rm -rf $(VENV)
		rm -rf .tox
		rm -rf .coverage
		find . -name "*.py[oc]" -delete
		find . -name "__pycache__" -delete

test: clean 
		bash ./test.sh

test-all: clean 
		bash ./test-all.sh
