#!/bin/sh

SHORTCOMMIT=$1
COMMIT=$2

tar -xzf skype4pidgin-$SHORTCOMMIT.tar.gz
rm -f skype4pidgin-$SHORTCOMMIT.tar.gz

shopt -s extglob
pushd skype4pidgin-$COMMIT
rm -r !(skypeweb)
popd

tar -czf skype4pidgin-$SHORTCOMMIT.tar.gz skype4pidgin-$COMMIT
rm -rf skype4pidgin-$COMMIT
