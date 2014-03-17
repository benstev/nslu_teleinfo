#!/bin/sh
# toggleStopFlag.cgi

EDF_HOME=/root/edf

echo "Content-type: application/json"
echo "Access-Control-Allow-Origin: *"
echo ""

RUN=`echo "$QUERY_STRING" | /opt/bin/gawk \
  'BEGIN {IGNORECASE=1} \
  /(^|[?&])run=go/ {print "GO"} \
  /(^|[?&])run=stop/ {print "STOP"}'`

if [ "$RUN" == 'STOP' ]
then
  touch $EDF_HOME/stop
  echo "STOP"
else
  if [ "$RUN" == 'GO' ]
  then
    rm $EDF_HOME/stop
    echo "GO"
  fi
fi
