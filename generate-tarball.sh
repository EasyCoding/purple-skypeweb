#!/bin/sh

TARBALL=purple-skypeweb

git clone -q https://github.com/EionRobb/skype4pidgin.git
cd skype4pidgin

COMMIT=$(git log -n 1 --format=%H)
SHORTCOMMIT=${COMMIT:0:7}

mv skypeweb ../$TARBALL-$COMMIT
cd ..

tar -cJf $TARBALL-$SHORTCOMMIT.tar.xz $TARBALL-$COMMIT
rm -rf $TARBALL-$COMMIT skype4pidgin

echo commit0 $COMMIT
echo Source0 $TARBALL-$SHORTCOMMIT.tar.xz
