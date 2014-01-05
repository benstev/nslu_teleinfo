#!/bin/sh

EDF_HOME=/root/edf
BIN=/opt/bin

echo "Content-type: application/json"
echo "Access-Control-Allow-Origin: *"
echo ""

FROM=`echo "$QUERY_STRING" | grep -oE "(^|[?&])from=[0-9]+" | cut -f 2 -d "=" | head -n1`
TO=`echo "$QUERY_STRING" | grep -oE "(^|[?&])to=[0-9]+" | cut -f 2 -d "=" | head -n1`
RES=`echo "$QUERY_STRING" | grep -oE "(^|[?&])res=[0-9]+" | cut -f 2 -d "=" | head -n1`

#echo "from = $FROM, to = $TO, with res=$RES"
#echo "fetch edf.rrd AVERAGE -s $FROM -e $TO" > zob

echo "fetch edf.rrd AVERAGE -r $RES -s $FROM -e $TO" | \
  nc localhost 13900 | $BIN/tail -n +3 | $BIN/head -n -2 | ./make_json.sh
