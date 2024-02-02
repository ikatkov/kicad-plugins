# Installation

Symlink folders into `/Users/%name%/Documents/kicad/7.0/scripting/plugins/`

Example `ln -s %path_to_source%/kicad-plugins/show_values/ /Users/%name%/Documents/kicad/7.0/scripting/plugins/show_values`

Refresh plugins.

![alt text](image.png)

# Development

For API refer to `/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pcbnew.py`

1. Run `/Applications/KiCad/KiCad.app/Contents/Applications/pcbnew.app/Contents/MacOS/pcbnew` in a console
2. After each code changes - need to manually refresh plugins in Kicad menu
3. Can use simple `print("stuff)` debug. There is no breakpoints or anything.