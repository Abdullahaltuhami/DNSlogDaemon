#!/bin/bash
#cut the 28 header lines.
sed '1,29d' $1 > DNSdebugLogCut
# Convert log from Windows to Unix format to handle pesky line returns
awk '{ sub("\r$", ""); print }' DNSdebugLogCut > dnsdebug.wintounix
# Get rid of blank lines:
sed '/^$/d' dnsdebug.wintounix > $2

echo 'Done converting'
rm DNSdebugLogCut
rm dnsdebug.wintounix
echo 'Removed unnecessary files'
