#!/bin/bash

source ../venv/bin/activate

for i in *.ui; do
	j=$(echo ${i} | sed 's/ui$/py/')
	echo ${i} ${j}
		pyuic5 -x "${i}" -o "../${j}"
done

pyrcc5 -o ../logo_rc.py ../logo.qrc

deactivate
