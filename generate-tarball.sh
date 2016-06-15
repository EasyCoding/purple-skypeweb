#!/bin/sh

NAME=purple-skypeweb

git clone -q --depth=1 --branch=master https://github.com/EionRobb/skype4pidgin.git
cd skype4pidgin

COMMIT=$(git log -n 1 --format=%H)
SHORTCOMMIT=${COMMIT:0:7}

mv skypeweb ../$NAME-$COMMIT
cd ..

tar -cJf $NAME-$SHORTCOMMIT.tar.xz $NAME-$COMMIT
rm -rf $NAME-$COMMIT skype4pidgin

echo commit0 $COMMIT
echo Source0 $NAME-$SHORTCOMMIT.tar.xz
