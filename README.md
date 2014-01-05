teleinfo
========

teleinfo capture system on the NSLU2 (Unslung)

## Files
- createRRD: one shot creation of the RRD database
- capture: background job for reading teleinfo from serial port
- misajour: cron job launched every minute to extract a 1 minute average from RRD and send to Pachube/Thinkspeak
- init_edf: initialize port for communication with the electricity meter

## Directories
- Mods: contains mods to apply to Linux configuration files
- www: sources for the CGI web services to query RRD database
- www/EdfMon: location for the web app to query RRD database (see EdfMon repo)

## www monitoring
the site is thttpd served on the NSLU.
The pages contain a jquery application that queries CGI based web services on the server.