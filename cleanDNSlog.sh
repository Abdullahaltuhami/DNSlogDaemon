#!/bin/bash
#cut the 28 header lines.
sed '1,29d' dnsdebug.txt
# Convert log from Windows to Unix format to handle pesky line returns
awk '{ sub("\r$", ""); print }' dnsdebug.txt > dnsdebug.wintounix
# Get rid of blank lines:
sed '/^$/d' dnsdebug.wintounix > dnsdebug.nolines

echo 'done converting and cleaning, Ready for python..'
