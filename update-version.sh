#!/bin/bash

git pull 

touch version

currentDate = $(date +"%D %T") 

echo $currentDate >> version

git push --set-upstream origin main 

git push 
