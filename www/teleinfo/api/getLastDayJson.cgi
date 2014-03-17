#!/bin/sh

EDF_HOME=/root/edf
BIN=/opt/bin

echo "Content-type: application/json"
echo "Access-Control-Allow-Origin: *"
echo ""

TIME=$(date +%s)
RRDRES=900
echo "fetch edf.rrd AVERAGE -r $RRDRES -e $(($TIME/$RRDRES*$RRDRES)) -s end-1day" | \
  nc localhost 13900 | $BIN/tail -n +3 | $BIN/head -n -2 | ./make_json.sh