#!/bin/bash

# On lid close show lock screen and suspend laptop.

. /usr/share/acpi-support/power-funcs

grep -q closed /proc/acpi/button/lid/*/state
if [ $? = 0 ]; then
    for x in /tmp/.X11-unix/*; do
        displaynum=`echo $x | sed s#/tmp/.X11-unix/X##`
        getXuser;
        if [ x"$XAUTHORITY" != x"" ]; then
            export DISPLAY=":$displaynum"
            su $user -c 'gnome-screensaver-command --lock'
        fi
    done
    pm-suspend
fi
