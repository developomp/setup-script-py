#!/usr/bin/env bash

case "$1" in
--reset) brightnessctl s 50% &>/dev/null ;;

--restore) brightnessctl --restore &>/dev/null ;;

--inc) brightnessctl s +10% &>/dev/null ;;

--dec) brightnessctl s 10%- &>/dev/null ;;

*) ;;
esac

percentage=$((100 * $(brightnessctl get) / $(brightnessctl max)))

if ((percentage >= 90)); then
    echo ""
elif ((percentage >= 60)); then
    echo ""
elif ((percentage >= 30)); then
    echo ""
elif ((percentage >= 0)); then
    echo ""
fi
