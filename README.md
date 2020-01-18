# TGC-Designer-Tools

Tools to support course creation and Lidar/Terrain Creation in The Golf Club 2019.

This app was originally developed by https://github.com/chadrockey/TGC-Designer-Tools

The versions here add additional features to the original, such as the Tree Settings tab.


## Windows EXE Download

Github is intended for software developers.  If you just want to run the software, view the latest releases here: [https://github.com/MTBehnke/TGC-Designer-Tools/releases](https://github.com/MTBehnke/TGC-Designer-Tools/releases)

Be sure to read the Tutorial! [https://chadrockey.github.io/TGC-Designer-Tools/TUTORIAL](https://chadrockey.github.io/TGC-Designer-Tools/TUTORIAL)

Developers and others can look through and run the code.  The main entry points are tgc_gui, lidar_map_api, and tgc_image_terrain.


## Software Developer Installation

Currently targeting Python 3.7

Get the dependencies with:

python -m pip install -r requirements.txt

## Distribution

pyinstaller -F --add-binary="./laszip/laszip-cli.exe;laszip" --additional-hooks-dir="./PyInstaller/hooks/" tgc_gui.py

In some cases you may need to include paths to certain directories (e.g. using venv for IDE, but not for pyinstaller):
pyinstaller -F --clean --add-binary="./laszip/laszip-cli.exe;laszip" --additional-hooks-dir="./PyInstaller/hooks/" --paths="./venv/Lib/site-packages/" --paths="./venv/src/" --paths="./venv/src/laspy/" tgc_gui.py
