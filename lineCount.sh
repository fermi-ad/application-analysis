#!/bin/bash

paArray=$(cat app_data.json | jq -r '[.[].program] | @sh')

echo '['
for pa in $paArray; do
    if [[ $pa == *'pa'* ]]; then
        count=$(wc -l /usr/local/mecca_head/mecca/pas/${pa//\'/}/*.{c,cpp,h,ftn,sql} 2>/dev/null | grep 'total' | awk '{print $1}' | grep -v "wc:")
        echo "{ \"program\":$pa, \"count\":$count },"
    else
        count=$(wc -l /usr/local/mecca_head/mecca/sas/${pa//\'/}/*.{c,cpp,h,ftn,sql} 2>/dev/null | grep 'total' | awk '{print $1}' | grep -v "wc:")
        echo "{ \"program\":$pa, \"count\":$count },"
    fi
done
echo ']'
