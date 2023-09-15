# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage


from libqtile import bar, layout, widget, hook, qtile, extension
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen
from libqtile.lazy import lazy

import os
import subprocess
from os import path

home = path.expanduser('~')
startsc = home + "/.config/qtile/start.sh"
mod = "mod4"
terminal = "kitty"
rofi = "rofi -show drun"
screenshot_gui = "flameshot gui --clipboard"
screenshot_full = "flameshot full --clipboard"
ee = "easyeffects"
pv = home + "/.config/qtile/mpv.sh"
volmute = home + "/.config/qtile/vol.sh mute"
volup = home + "/.config/qtile/vol.sh up"
voldown = home + "/.config/qtile/vol.sh down"

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([startsc])

keys = [
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn(rofi), desc="Launch rofi -drun"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn(pv), desc="Play a video through mpv"),
    Key([mod], 's', lazy.spawn(screenshot_gui), desc="Screenshot to clipboard"),
    Key([], "XF86AudioMute", lazy.spawn(volmute), desc="Toggle mute"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(voldown), desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(volup), desc="Raise volume"),
    Key([mod], 'backspace', lazy.run_extension(extension.CommandSet(
    commands={
        'Suspend': 'systemctl suspend',
        'Reboot': 'systemctl reboot',
        'Shutdown': 'systemctl poweroff',
        'Log-out': 'loginctl terminate-session ${XDG_SESSION_ID-}',
        },
    ))),
]

groups = [Group(i) for i in "123456789"]

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "minus", "equal"]
group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "-", "="]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
            Group(
                name=group_names[i],
                layout=group_layouts[i].lower(),
                label=group_labels[i],
                )
            )

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Mod + Key to move to group"),
        Key([mod], "Tab", lazy.screen.next_group(), desc="Mod + Tab to move to next group"),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="Mod + Tab to move to previous group"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="Move focused window to new workspace"),
        ])
    
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

groups.append(ScratchPad("scratchpad", [
    DropDown("term", "kitty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("ee", "easyeffects", width=0.5, heigh=0.5, x=0.1, y=0.1),
    ]))

keys.extend([
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle("term")),
    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle("telegram")),
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle("ee"))
    ])

colors = []
cache = '/home/zhotheone/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
        colors.append('#ffffff')
        lazy.reload()
load_colors(cache)

layout_theme = {
        "margin": 2,
        "border_width": 2,
        "border_focus": colors[3],
        "border_normal": colors[1]
        }

layouts = [
        layout.MonadTall(**layout_theme),
        layout.Columns(**layout_theme),
        layout.Max(**layout_theme),
        ]

widget_defaults = dict(
    font="FiraCode Nerd Regular",
    fontsize=12,
    padding=3,
)

def init_widgets_list(monitor_num):
    widgets_list = [
            widget.GroupBox(
                font='FiraCode Nerd Regular',
                fontsize= 16,
                margin_y = 4,
                margin_x = 2,
                padding_y = 6,
                padding_x = 6,
                borderwidth = 2,
                disable_drag = True,
                active = colors[1],
                inacive = colors[1],
                hide_unused = True,
                rounded = False,
                highlight_method = "line",
                block_highlight_text_color = colors[4],
                highlight_color = [colors[0], colors[0]],
                this_current_screen_border = colors[7],
                this_screen_border = colors[4],
                other_screen_border = colors[3],
                other_current_screen_border = colors[3],
                urgent_alert_method = 'line',
                urgent_border = colors[6],
                urgent_text = colors[1],
                foreground = colors[0],
                background = colors[0],
                use_mouse_wheel = False,
                ),
                widget.Sep(linewidth=1, padding=10, foreground=colors[4], background=colors[0]),
                widget.TaskList(
                        icon_size = 0,
                        font = "FiraCode Nerd Regular",
                        fontsize = 16,
                        foreground = colors[8],
                        background = colors[0],
                        borderwidth = 0,
                        border = colors[0],
                        margin_y = 2,
                        padding = 0,
                        highlight_method = "block",
                        title_width_method = "uniform",
                        rounded = False,
                ),
                widget.Sep(linewidth=1, padding=10, foreground=colors[4], background=colors[0]),
                widget.TextBox(text = "", fontsize=14, foreground=colors[8]),
                widget.CPU(
                        update_interval = 1.0,
                        format = "{load_percent}%",
                        foreground = colors[2],
                        padding = 5,
                        ),
                widget.Sep(linewidth=1, padding=10, foreground=colors[4], background=colors[0]),
                widget.TextBox(text = "󰍛", fontsize=14, foreground=colors[8]),
                widget.Memory(
                        foreground = colors[6],
                        format = '{MemUsed: .0f} / {MemTotal:.0f}{mm}',
                        measure_mem = "G",
                        padding = 0,
                        ),
                widget.Sep(linewidth=1, padding=10, foreground=colors[4], background=colors[0]),
                widget.TextBox(text = "󰍛", fontsize=14, foreground=colors[8]),
                widget.Clock(
                        fomat = "%I:%M %p",
                        padding = 8,
                        foreground = colors[6],
                        ),
                widget.Sep(linewidth=1, padding=10, foreground=colors[4], background=colors[0]),
                ]
    return widgets_list

widgets_list = init_widgets_list('1')

screens = [
        Screen(top=bar.Bar(widgets=widgets_list, size=25, background=colors[0], margin=0, opacity=1))
        ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
