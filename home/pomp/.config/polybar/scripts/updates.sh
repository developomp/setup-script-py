#!/usr/bin/env bash

# add flatpak and pamac update counts
if ! UPDATES=$(($(checkupdates 2>/dev/null | wc -l) + $(echo 'n' | flatpak update 2>/dev/null | tail -n +5 | head -2 | wc -l))); then
    UPDATES=0
fi

echo $UPDATES
