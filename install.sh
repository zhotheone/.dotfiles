#! /bin/bash

set -eu -o pipefail
prompt(){ read -p "$1" a; [ $a = "y" ]; }
prompt "Continue?[y/n]"  &&  {
    echo test
    # yes | LC_ALL=en_US.UTF-8 sudo pacman -S kitty dunst easyeffects neofetch qtile rofi
}

# create symlinks
"ln -s ~/.dotfiles/.zshrc ~/.zshrc
ln -s ~/.dotfiles/.gitconfig ~/.gitconfig
ln -s ~/.dotfiles/dunst ~/.config/dunst
ln -s ~/.dotfiles/easyeffects ~/.config/easyeffects
ln -s ~/.dotfiles/kitty ~/.config/kitty
ln -s ~/.dotfiles/neofetch ~/.config/neofetch
ln -s ~/.dotfiles/qtile ~/.config/qtile
ln -s ~/.dotfiles/rofi ~/.config/rofi
ln -s ~/.dotfiles/rofi-wallpaper-changer ~/.config/rofi-wallpaper-changer
ln -s ~/.dotfiles/spicetify ~/.config/spicetify
ln -s ~/.dotfiles/wal ~/.config/wal"

