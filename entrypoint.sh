#!/bin/bash

set -euo pipefail

input="list_of_gamestop_sites.txt"

while IFS=: read -r line
do

	site=$line

	for site in ${site}; do

		./wher_da_switches_at.py --chromedriver ${CHROMEDRIVER_PATH} --url ${site} --account_SID ${ACCOUNT_SID} --auth_token ${AUTH_TOKEN} --twilio_number ${TWILIO_NUMBER} --recipient ${RECIPIENT};

	done

done < "$input"
