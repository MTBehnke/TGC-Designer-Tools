# TGC Golf Tools – Tree Settings Tutorial


This is a how-to guide on using the Tree Settings tab in the TGC-Designer-Tools available at: https://github.com/MTBehnke/TGC-Designer-Tools/releases

This app was forked from https://github.com/chadrockey/TGC-Designer-Tools and performs all the same functions as the original tool while adding the tree settings options.  For a tutorial on using the rest of the tool features, see https://chadrockey.github.io/TGC-Designer-Tools/TUTORIAL


If you have a problem related to the tree settings, please describe it the best you can, send screenshots, photos, and anything you can copy and paste and make a New Issue at https://github.com/MTBehnke/TGC-Designer-Tools/issues


## Starting the App

Download and run the exe files from releases: https://github.com/MTBehnke/TGC-Designer-Tools/releases


The file doesn't need to be installed, just double click it and it should run.


## Import Terrain and Features Tab
 ![image](https://user-images.githubusercontent.com/22116435/73792230-7ba88000-4769-11ea-9970-b0b4e9204321.png)

## Tree Settings Tab
 ![image](https://user-images.githubusercontent.com/22116435/73792040-1eacca00-4769-11ea-8f5d-a1df4f38d646.png)



# Quick Start Guide

1.	Process Lidar with Select Lidar and Generate Heightmap

2.	Run Select and Import Heightmap and OSM into Course, with:

    •	Import Mapped Woods/Trees:  unchecked

    •	Add Trees From Lidar (Experimental):  checked

    •	Tree Variety (Lidar and OSM):  checked

    •	Tree Settings tab:  default settings or modify if desired

    Note:  Tree Settings tab will be blank until you’ve imported a course, typically a blank course for the first run.

3.	Export .course file and view in TGC

    •	Examine trees, decide if any changes are desired.

4.	Modify Tree Settings as desired

5.	Rerun Select and Import Heightmap and OSM into Course, with:

    •	Import OpenStreetMap:  unchecked

    Note:  Once OSM has been imported, there isn’t a need to reimport it.

6.	Repeat step 3 through 5 until satisfied with trees.



# Tree Settings

## Tree Source Data

The tool generates its list of trees to add to a course based on one of two sources selected by the user:

   •	Lidar – includes position, height and radius of trees, automatically determined from Lidar data.

   •	OSM – position where manually located in OSM, height and radius assigned randomly.

To use Lidar trees, run the tool with Import Mapped Woods/Trees unchecked.

Note:  If you mapped wooded areas in OSM but still want Lidar trees, first run the tool with the Mapped Woods/Trees option checked, then all later runs with it unchecked.


## Default Tree Setting

If Use Default Settings is checked, the tool will use the settings displayed on the Tree Settings tab upon initial launch.


## Enforce TGC Minimum Tree Size

Trees added directly within TGC Designer are generally much larger than their real world sizes, even fully scaled down.  This tool allows much smaller trees to be added to match their real world heights.


The primary issue this can create occurs where lidar trees are nearby trees added manually, such as in masked areas.  The size difference can be quite apparent and may be undesireable.  Additionally, if you move any Lidar trees that are smaller than the TGC minimum size, TGC will automatically resized it to the minimum.


By selecting the Enforce TGC Minimum Tree Size option, no trees will be smaller than the normal minimum size.


## Tree Size Multiplier and Size Multipliers
These sliders allow you to scale the overall size of trees, the first one for all trees and the latter for specific types of trees.


## Tree Height Limits
This allows you to specify the minimum and maximum heights allowed for trees that are added.  These limits can be useful to increase the heights of shorter trees or decrease the heights of taller trees without impacting the reset of the trees.


After running the tool once, the heights of the shortest and tallest Lidar trees will display in the bottom right, which can help you decide appropriate ranges.  Note, it’s not uncommon for the tool to interpret buildings and other objects as trees, at times with heights outside the range of normal tree heights.


If using OSM trees, the heights for trees will be assigned randomly based on these limits.


## Tree Width Limits
Similar to the Tree Height Limits, the width limits allow you to set a minimum and maximum width range, but based on the variation from the default width of the tree.  You can modify this to keep tree widths more proportional to their heights if desired.


OSM trees default to their standard width based on their height, so this setting has no effect.


## Normal and Skinny Trees
For Lidar trees, the tool calculates the height to width ratio for each tree.  If the ratio is less than the split ratio, the tool selects a tree type from the designated normal trees.  If the ratio is greater than this number, the tool selects a tree type from the designated skinny trees.


As conifers are generally skinnier than deciduous trees, you can adjust the proportion of normal and skinny trees to better reflect the mix of real trees.


In addition to changing the height:width ratio, you can also change the list of normal and skinny trees as you’d like.  Additionally, you can set trees to None to prevent that type of tree from being used at all.


OSM trees don’t have any height or width data, so the tool will select a tree type from either list, excluding any marked none.


## My Typical Settings

I usually use the Rustic theme as that has a nice mix of deciduous trees and coniferous trees that better matches the trees in my area.  I might also uncheck a few of the tree types, including usually only including one or two of the conifers.  


Typically the lidar trees detected range from around 10-70 feet in my area, which is displayed at the bottom of the settings page after the first time you run the tool.  I usually set the minimum height to around 25-30 feet as most shorter trees look somewhat out of place in the game.  I usually keep the maximum set at 70 feet.


If a course has a lot of shorter trees, the minimum height setting can result in a bit too uniform look.  In this case, leaving Enforce TGC Minimum Size checked can help with a little variety for the shorter trees.


I usually narrow the width range, favoring wider a bit more.  I find setting the minimum width to around 80% and the maximum width to around 120-130% usually looks pretty good.


If a course has a lot of trees, especially thicker tree lined fairways, keeping the overall size multiplier set to 1.0 works pretty well.  For courses with smaller, fewer and more spaced out trees, increasing the sizes can help keep the trees from feeling too small.


I've noticed that trees with narrow peaks sometimes seem to be shorter than the other types of trees.  I think this may be because lidar has a harder time finding the true peak height of skinny trees.  If this is the case, I usually bump up the size multiplier for the skinny tree types until they look right.


Finally, I usually lower the Normal/Skinny Tree Split setting a bit, until the mix of trees better matches the real life mix of trees.  We have some courses with lots of pines and by adjusting this I can often get areas of the course with lots of pines to populate with pines.


Getting the trees right with the settings usually takes me 3-4 iterations.  While you can usually tell if you like the trees it generated with a quick view in TGC, I'd recommend play-testing a few holes or at least viewing the trees from ground level in the game.  After all, this is the angle you'll be viewing the trees from the vast majority of the time.  I find that I've kept the trees too short versus too tall more often than not.
