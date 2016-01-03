#!/bin/bash
udisks --unmount /dev/fd0
udisks --mount /dev/fd0

if [ -w /media/floppy ]
then
nautilus /media/floppy
else
if [ "$(ls -A /media/floppy)" ]
then
nautilus /media/floppy
fi

fi


