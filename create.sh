#!/bin/bash

# https://stackoverflow.com/a/4774063/6748004
DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
DESK="$DIR/desk"

PROBLEM=$1

SRC="$DIR/template.py"
DEST="$DESK/$PROBLEM.py"

if [ -f "$DEST" ]; then
	echo "$DEST already exists"
	exit 1
fi

mkdir -p "$DESK"
sed -E "2s/(problem=)\?/\1$PROBLEM/g" "$SRC" > "$DEST"

if command -v subl &> /dev/null; then subl "$DEST"; fi
