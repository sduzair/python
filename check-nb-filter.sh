#!/bin/bash

if ! git config --get "filter.$1.clean"; then
  echo "Error: Filter '$1' is not defined" >&2
  exit 1
fi

exec git config --get "filter.$1.clean"
