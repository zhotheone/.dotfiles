#!/bin/bash

#AUTHOR: ABDELRHMAN NILE (PIRATE)
#github: https://github.com/AbdelrhmanNile

# this script WILL NOT WORK if you don't have feh and rofi, please install them first
# EDITED BY ZHOTHEONE
#


dir="/home/$USER/Pictures/" # wallpapers folder, change it to yours, make sure that it ends with a /
cd $dir
wallpaper="none is selected" 
view="feh"

########################-FUNCTION FOR SELECTING A WALLPAPER-###################
selectpic(){
    wallpaper=$(ls $dir | rofi -dmenu -p "select a wallpaper: ($wallpaper)")

    if [[ $wallpaper == "q" || $wallpaper == "" ]]; then
        killall feh && exit 
    else
        action
    fi
}
###############################################################################

#########################-FUNCTION FOR TAKING AN ACTION ON THE SELECTED WALLPAPER-#########################
action(){
  $view $wallpaper
  whattodo=$(echo -e "set\nclose" | rofi -dmenu -p "whatcha wanna do with it? ($wallpaper)")
    if [[ $whattodo == "set" ]]; then
        set_wall
    else
        killall wch
    fi
}
#############################################################################################################

########-FUNCTION TO SET THE SELECTED WALLPAPER, BUT IT IS NOT PERMANANT, THE CHANGE WILL BE UNDONE AFTER LOGOUT OR REBOOT-#######
set_wall(){
    # $set $wallpaper && killall feh &
    wal -i $wallpaper -n
    feh --bg-center "$(< "${HOME}/.cache/wal/wal")"
    source ~/.config/wal/allwal.sh
}
###################################################################################################################################

###################-MAIN-####################
selectpic

