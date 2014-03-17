#!/bin/sh

EDF_HOME=/root/edf
EDF_TMP=/tmp
BIN=/opt/bin

echo "Content-type: text/plain; charset=ASCII"
echo "Access-Control-Allow-Origin: *"
echo ""

cat $EDF_TMP/cv
