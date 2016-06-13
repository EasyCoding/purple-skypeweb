#!/bin/bash

COMMIT=$1
SHORTCOMMIT=${COMMIT:0:7}
shopt -s extglob

if [ -f "skype4pidgin-$SHORTCOMMIT.tar.gz" ]; then
	tar -xzf skype4pidgin-$SHORTCOMMIT.tar.gz
	rm -f skype4pidgin-$SHORTCOMMIT.tar.gz
	
	pushd skype4pidgin-$COMMIT
	rm -r !(skypeweb)
	popd

	tar -czf skype4pidgin-$SHORTCOMMIT.tar.gz skype4pidgin-$COMMIT
	rm -rf skype4pidgin-$COMMIT
fi
