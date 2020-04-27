#!/bin/bash

acl cpld_log/start=2yearsago | awk -v OFS=, '{ print substr($0, 1, 11), substr($0, 13, 8), substr($0, 22, 6), substr($0, 29, 4), substr($0, 34, 4), substr($0, 47, 8) }' > ./data/usage.csv
tail -100 ./data/usage.csv > ./data/test.csv
acl program_info/pas > ./data/pas.txt
acl program_info/sas > ./data/sas.txt
