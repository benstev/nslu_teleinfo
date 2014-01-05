#!/bin/sh
# toggleStopFlag.cgi

EDF_HOME=/root/edf

echo "Content-type: text/plain"
echo "Access-Control-Allow-Origin: *"
echo ""

if test -f $EDF_HOME/stop
then
  echo "{ \"Stopped\":true }"
else
  echo "{ \"Stopped\":false }"
fi
