#!/bin/bash
#echo -n "please enter the file name with pyx extension: "
#read name
#usage: ./run.sh filename
echo -n "Begin to run the code, wait for a moment..."
printf "\n"
echo "========================="
cython $1.pyx
gcc -c -fPIC -I/usr/include/python2.7/ $1.c
gcc -shared $1.o -o $1.so -lpython2.7
python $2.py
# ====delete the temporary file=======
echo "========================="
rm  $1.c
rm  $1.o
rm  $1.so
if [ -e $1.pyc ]; then		#blank is needed in bracket [ ]
		rm $1.pyc
		rm $2.pyc
		echo "OK, $1.pyc is removed."
else
		echo "NO, $1.pyc doesn't exist. "
fi
echo -n "The running finished!"
printf "\n"

