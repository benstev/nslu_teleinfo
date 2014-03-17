#!/bin/sh
echo -n "["                                     
/opt/bin/gawk -F ":" \
  'BEGIN {first=1} {fmt = (first==1) ? "[%d,%d]" : ",[%d,%d]"; first=0; \
   printf fmt,$1*1000,$2; }' 
echo "]"                                                                        
