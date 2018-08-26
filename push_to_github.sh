#!/bin/bash
#$ chmod a+x push.sh

git add .

git commit -m "auto push"

git push ericdai713 master

# git push origin master