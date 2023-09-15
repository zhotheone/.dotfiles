#!/bin/bash

notify-send "Playing Video" "$(xclip -o)"
mpv --hwdec=auto "$(xclip -o)"
