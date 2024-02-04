#!/bin/bash

source venv/bin/activate

cd rawUi/
for i in *.ui; do
	j=$(echo ${i} | sed 's/ui$/py/')
	echo ${i} ${j}
		pyuic5 -x ${i} -o ../tmp-${j}
done

pyrcc5 -o ../logo_rc.py ../logo.qrc

deactivate

