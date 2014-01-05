#!/bin/sh
# toggleStopFlag.cgi

EDF_HOME=/root/edf

echo "Content-type: text/plain"
echo "Access-Control-Allow-Origin: *"
echo ""

if test -f $EDF_HOME/stop
then
  rm $EDF_HOME/stop
  echo "{ \"Stopped\":false }"
else
  touch $EDF_HOME/stop
  echo "{ \"Stopped\":true }"
fi
