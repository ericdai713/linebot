#!/bin/bash
#$ chmod a+x push.sh

git add .

git commit -m "auto push"

git push origin master

