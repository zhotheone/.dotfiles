#!/bin/bash

source ~/.config/wal/generate-theme.sh
wal-telegram --wal
ln -sf ~/.cache/wal/dunstrc ~/.config/dunst/dunstrc
ln -sf ~/.cache/wal/colors.Xresources ~/.Xresources
xrdb ~/.Xresources
spicetify update
pkill dunst
dunst &
pkill -SIGUSR1 qtile
notify-send "Theme has changed!"
