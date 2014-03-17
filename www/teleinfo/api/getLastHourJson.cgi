#!/bin/sh

EDF_HOME=/root/edf
BIN=/opt/bin

echo "Content-type: application/json"
echo "Access-Control-Allow-Origin: *"
echo ""
echo "fetch edf.rrd AVERAGE -e now-1min -s end-1hour" | nc localhost 13900 | \
    $BIN/tail -n +3 | $BIN/head -n -2 | ./make_json.sh