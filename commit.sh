#!/bin/bash
echo 'the code aims to push code to github'
echo '=========='
git add $1
git ci -m "$2"
git push origin master
echo "=========="
echo "It is over!"

