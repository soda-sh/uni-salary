#!/bin/bash

case ${1} in
	-ui)
		if [ -d venv ]; then
			source venv/bin/activate
		fi

		cd rawUi/
		for i in *.ui; do
			j=$(echo ${i} | sed 's/ui$/py/')
			echo ${i} ${j}
				pyuic5 -x ${i} -o ../tmp-${j}
		done

		pyrcc5 -o ../resources/logo_rc.py ../resources/logo.qrc

		if [ -d venv ]; then
			deactivate
		fi
		;;
	-eol)
		find -type f -name '*.py'  \
			| grep -v 'venv\|git' \
			| xargs -I {} unix2dos {}
		;;
	*)
		echo "Help is not implemented"
		;;
esac




