#!/bin/bash

sudo -u vscode bash << EOF
pip install --no-warn-script-location --user -e .[dev,ci]
git config --unset core.hookspath
pre-commit install
rm -Rf *.egg-info build data
pkill -f vscode-pylance || true
