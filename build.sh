#!/bin/bash

pyinstaller src/core.py
read -p "Run distributable (y/)? " run
case "$run" in 
  y|Y ) dist/core/core.exe ;;
esac