#!/bin/sh

EDF_HOME=/root/edf
BIN=/opt/bin

echo "Content-type: text/plain"
echo "Access-Control-Allow-Origin: *"
echo ""

echo "lastupdate edf.rrd" | nc localhost 13900 | \
  $BIN/tail -n +3 | $BIN/head -n -1 | \
  $BIN/gawk 'BEGIN {FS=":"} {print $2+0}'