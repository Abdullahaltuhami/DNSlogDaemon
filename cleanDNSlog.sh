#!/bin/bash
#cut the 28 header lines.
sed '1,29d' ../DNSdebugLog2
# Convert log from Windows to Unix format to handle pesky line returns
awk '{ sub("\r$", ""); print }' ../DNSdebugLog2 > dnsdebug.wintounix
# Get rid of blank lines:
sed '/^$/d' dnsdebug.wintounix > dnsdebug.nolines

echo 'done converting and cleaning, Ready for python..'
