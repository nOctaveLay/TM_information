#!/bin/bash
YEAR=`date +%Y`
MON=`date +%m`
DAY=`date +%d`
if test $# = 0
then filename=${YEAR}"-"${MON}"-"${DAY}".md"
else filename=${YEAR}"-"${MON}"-"${DAY}"-"$1".md"
fi
echo "$filename"
if ! test -f "$filename"
then touch "$filename"
fi
subl "$filename"