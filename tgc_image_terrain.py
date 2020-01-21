import cv2
import itertools
import json
import math
import numpy as np
from pathlib import Path
import random
import sys
import time

from GeoPointCloud import GeoPointCloud
from infill_image import infill_image_scipy
import OSMTGC
import tgc_definitions
import tgc_tools

status_print_duration = 1.0 # Print progress every n seconds

def get_pixel(x_pos, z_pos, height, scale, brush_type=72):
    output = json.loads('{"tool":0,"position":{"x":0.0,"y":"-Infinity","z":0.0},"rotation":{"x":0.0,"y":0.0,"z":0.0},"_orientation":0.0,"scale":{"x":1.0, \
                         "y":1.0,"z":1.0},"type":0,"value":0.0,"holeId":-1,"radius":0.0,"orientation":0.0}')
    output['type'] = brush_type
    output['position']['x'] = x_pos
    output['position']['z'] = z_pos
    output['value'] = height
    output['scale']['x'] = scale
    output['scale']['z'] = scale
    return output

def get_object_item(x_pos, z_pos, rotation_degrees):
    output = json.loads('{"position":{"x":0.0,"y":"-Infinity","z":0.0},"rotation":{"x":0.0,"y":0.0,"z":0.0},"scale":{"x":1.0,"y":1.0,"z":1.0}}')
    output['position']['x'] = x_pos
    output['position']['z'] = z_pos
    output['rotation']['y'] = rotation_degrees
    return output

def get_placed_object():
    output = json.loads('{"Key":{"category":0,"type":0,"theme":true},"Value":{"items":[],"clusters":[]}}')
    return output

def get_trees(theme, tree_variety, trees, tree_settings_dict, tree_category):
    # Default-Lidar:
	#   Height: Use lidar heights within default height range
	#   Radius: lidar radius within default radius range, no multipliers

    # Default-OSM:
	#   Height: Use random height within default height range
	#   Radius: Equal to height scale, no multipliers

    # Custom-Lidar:
	#   Height: Use lidar heights within settings height range
	#   Radius: lidar radius within settings radius range, use multipliers

    # Custom-OSM:
	#   Height: Use random heights within settings height range
	#   Radius: Equal to height scale, including multipliers

    # Tree Height/Radius Settings
    min_tree_height = min(trees, key=lambda x: x[3])[3]
    max_tree_height = max(trees, key=lambda x: x[3])[3]
    min_tree_radius = min(trees, key=lambda x: x[2])[2]
    max_tree_radius = max(trees, key=lambda x: x[2])[2]
    tree_height_range = max_tree_height - min_tree_height
    tree_radius_range = max_tree_radius - min_tree_radius
    real_height_factor = tgc_definitions.tree_meters_to_tgc.get(theme, [0])   # converts height in meters to TGC scale
    default_trees = tree_settings_dict.get('default_trees').get()
    enforce_tgc_size = tree_settings_dict.get('enforce_tgc_limit').get()

    # Add lidar tree height info to settings page
    tree_settings_dict.get('tallest_tree').set(value="Tallest Tree Height:  " + '{:.1f}'.format(max_tree_height) + " m / " + '{:.1f}'.format(max_tree_height*3.28) + " ft")
    tree_settings_dict.get('shortest_tree').set(value="Shortest Tree Height:  " + '{:.1f}'.format(min_tree_height) + " m / " + '{:.1f}'.format(min_tree_height*3.28) + " ft")

    # Get list of normal and skinny tree types based on selected options.
    if not tree_variety:
        normal_tree_ids = [0]
        skinny_tree_ids = []
    elif default_trees is True:
        normal_tree_ids = tgc_definitions.normal_trees.get(theme, [0])
        skinny_tree_ids = tgc_definitions.skinny_trees.get(theme, [])
    else:
        normal_tree_ids = []
        skinny_tree_ids = []
        for i, x in enumerate(tree_category[0]):
            x_value = x.get()
            if (x_value==1) or (tree_height_range < 0.1):   # If using OSM trees make all normal
                normal_tree_ids.append(i)
            elif x_value==2:
                skinny_tree_ids.append(i)
        if len(normal_tree_ids) == 0:
            if len(skinny_tree_ids) == 0:                   # No trees selected
                normal_tree_ids = [0]
            else:                                           # Only skinny trees selected
                normal_tree_ids = skinny_tree_ids.copy()
                skinny_tree_ids = []

    # Make an group for each type of tree, even if they may not be used
    normal_trees = []
    skinny_trees = []
    for tree_id in normal_tree_ids:
        p = get_placed_object()
        p['Key']['category'] = 0
        p['Key']['type'] = tree_id
        normal_trees.append(p)
    for tree_id in skinny_tree_ids:
        p = get_placed_object()
        p['Key']['category'] = 0
        p['Key']['type'] = tree_id
        skinny_trees.append(p)

    # Scale trees based on relative sizes, settings
    if default_trees is True:
        min_height = 10 / 3.28  # min default height in meters (first number is feet)
        max_height = 70 / 3.28  # max default height in meters (first number is feet)
        min_radius_scale = 50 / 100 # min radius scale as a percent of tree specific height scale
        max_radius_scale = 150 / 100 # max radius scale as a percent of tree specific height scale
        radius_scale_range = max_radius_scale - min_radius_scale
        skinny_h_r_ratio = 2.5  # Height to Radius Ratio to determine whether tree is a normal or skinny tree
        size_multiplier_all = 1.0
        size_multiplier = [1.0] * (len(tgc_definitions.tree_names.get(theme)) + 1)
    else:
        min_height = tree_settings_dict.get('tree_min_height').get() / 3.28
        max_height = tree_settings_dict.get('tree_max_height').get() / 3.28
        min_radius_scale = tree_settings_dict.get('tree_min_radius').get() / 100
        max_radius_scale = tree_settings_dict.get('tree_max_radius').get() / 100
        radius_scale_range = max_radius_scale - min_radius_scale
        skinny_h_r_ratio = tree_settings_dict.get('skinny_ratio').get()
        size_multiplier_all = tree_settings_dict.get('size_multiplier_all').get()
        size_multiplier = []
        for i, x in enumerate(tree_category[1]):
            size_multiplier.append(x.get())

    for tree in trees:
        easting, northing, r, h = tree
        t = get_object_item(easting, northing, random.randrange(0, 359))

        if h / r < skinny_h_r_ratio or len(skinny_trees) == 0:
            group = random.choice(normal_trees)
        else:
            group = random.choice(skinny_trees)
        tree_type = group['Key']['type']

        # Tree Height Scale
        if tree_height_range < 0.1:     # OSM tree
            h = random.uniform(min_height, max_height)
        else:                           # Lidar tree
            h = h * size_multiplier_all * size_multiplier[tree_type]
            if h < min_height: h = min_height
            elif h > max_height: h = max_height
        h_scale = h * real_height_factor[tree_type]
        if (enforce_tgc_size is True) or (default_trees is True): h_scale = max(h_scale, 0.5)
        t['scale']['y'] = h_scale

        # Tree Radius Scale
        if tree_height_range < 0.1:     # OSM tree
            r_scale = h_scale
        else:                           # Lidar tree
            r_scale = h_scale * (min_radius_scale + radius_scale_range * (r - min_tree_radius) / tree_radius_range)
        if (enforce_tgc_size is True) or (default_trees is True): r_scale = max(r_scale, 0.5)
        t['scale']['x'] = r_scale
        t['scale']['z'] = r_scale
        group['Value']['items'].append(t)

    # Remove empty groups
    output = []
    for g in itertools.chain(normal_trees, skinny_trees):
        if len(g['Value']['items']) > 0:
            output.append(g)
    return output

def get_lidar_trees(theme, tree_variety, lidar_trees, tree_settings_dict, tree_category, pc, mask, mask_pc, image_scale):
    # Convert to TGC coordinates
    trees = []
    tree_settings_dict.get('num_trees').set(value="Lidar Tree Count:  " + str(len(lidar_trees)))
    for tree in lidar_trees:
        easting, northing, r, h = tree
        # Use mask to only add trees on desired areas
        row, column = mask_pc.projToCV2(easting, northing, image_scale)
        mask_color = mask[(row, column)]
        # Color order is BGR, support both MS Paint Red Colors
        if not (mask_color[0] < 40 and mask_color[1] < 40 and mask_color[2] > 130):
            # Use standard pointcloud tp project trees into final TGC coordinates
            x, y, z = pc.projToTGC(easting, northing, 0.0)
            trees.append((x, z, r, h))

    return get_trees(theme, tree_variety, trees, tree_settings_dict, tree_category)

# Set various constants that we need
def set_constants(course_json, flatten_fairways=False, flatten_greens=False, course_latitude=None, printf=print):
    # These only work if the terrain is made from scult (red brushes) rather than landscape (blue brushes)
    course_json["flattenFairways"] = flatten_fairways # Needed to not flatten under fairway splines
    course_json["flattenGreens"] = flatten_greens # Needed to not flatten under green splines

    # Slow down and soften greens a bit by default.   A lot of real world courses are not as firm as fast as TGC defaults
    course_json["greenSpeed"] = 0.136312455
    course_json["greenFirmness"] = 0.20308432

    # Set all hole sizes to 0.0 so that you can add holes without the autogenerated features appearing
    # This lets a designer manually specifcy or delete and readd a hole without the teebox, green, bunkers appearing over their OSM.
    course_json["roughRadius"] = 0.0
    course_json["heavyRoughRadius"] = 0.0
    course_json["fairwayRadius"] = 0.0
    course_json["greenRadius"] = 0.0
    course_json["teeRadius"] = 0.0
    course_json["hazardGreenCount"] = 0.0
    course_json["hazardFairwayCount"] = 0.0

    # Set lighting parameters based on the actual position of the course
    course_json["sunOrientation"] = 0.0 # Set so in game North aligns to true North
    course_json["sunInclination"] = 45.0 # Default halfway position
    # Try to set inclination based on latitude, if provided
    # Based on: http://www.physicalgeography.net/fundamentals/6h.html
    if course_latitude is not None:
        earth_declination = 23.5
        if course_latitude >= earth_declination: # Above the Tropic of Cancer, use June Solstice position
            course_json["sunInclination"] = 90.0 - float(course_latitude) + earth_declination
        elif course_latitude >= 0.0: # Equation to the Tropic of Cancer, use Equinox position
            course_json["sunInclination"] = 90.0 - float(course_latitude)
        elif course_latitude >= -1.0*earth_declination: # Equation to the Tropic of Capricorn, use Equinox position
            # You can't set above 90 in game, but we can here.  Do this so that North and Sunrise to the East are still correct.
            course_json["sunInclination"] = 90.0 - float(course_latitude)
        else: # Below the Tropic of Caprion.  Use December Solstice position
            # You can't set above 90 in game, but we can here.  Do this so that North and Sunrise to the East are still correct.
            course_json["sunInclination"] = 90.0 + -1.0*float(course_latitude) - earth_declination
        printf("For latitude " + str(course_latitude) + ": Setting sun angle to: " + str(course_json["sunInclination"]))

    # Add our own JSON element so the courses could be filtered easily
    # Am choosing an organization name so that TGC-Desinger-Tools could be forked
    course_json["gis"] = "ChadRockeyDevelopment"

    return course_json

def generate_course(course_json, heightmap_dir_path, options_dict={}, tree_settings_dict={}, tree_category=[], printf=print):
    printf("Loading data from " + heightmap_dir_path)

    # Infill data to prevent holes and make the data nice and smooth
    hm_file = Path(heightmap_dir_path) / '/heightmap.npy'
    try:
        read_dictionary = np.load(heightmap_dir_path + '/heightmap.npy').item()
        im = read_dictionary['heightmap'].astype('float32')

        mask = cv2.imread(heightmap_dir_path + '/mask.png', cv2.IMREAD_COLOR)
        # Turn mask into matrix order from image order
        mask = np.flip(mask, 0)

        # Process Image
        printf("Filling holes in heightmap")
        image_scale = read_dictionary['image_scale']
        printf("Map scale is: " + str(image_scale) + " meters")
        background_ratio = None
        if options_dict.get('add_background', False):
            background_scale = float(options_dict.get('background_scale', 16.0))
            background_ratio = background_scale/image_scale
            printf("Background requested with scale: " + str(background_scale) + " meters")
            
        heightmap, background, holeMask = infill_image_scipy(im, mask, background_ratio=background_ratio, fill_water=options_dict.get('fill_water', False), purge_water=options_dict.get('purge_water', False), printf=printf)
    except FileNotFoundError:
        printf("Could not find heightmap or mask at: " + heightmap_dir_path)
        return course_json

    # Clear existing terrain
    course_json = set_constants(course_json, options_dict.get('flatten_fairways', False), options_dict.get('flatten_greens', False), read_dictionary['origin'][0], printf=printf)
    course_json["userLayers"]["height"] = []
    course_json["userLayers"]["terrainHeight"] = []
    course_json["placedObjects2"] = []

    # Construct high resolution model
    pc = GeoPointCloud()
    pc.addFromImage(heightmap, image_scale, read_dictionary['origin'], read_dictionary['projection'])

    # Add low resolution background
    if background is not None:
        background_pc = GeoPointCloud()
        background_pc.addFromImage(background, background_scale, read_dictionary['origin'], read_dictionary['projection'])
        num_points = len(background_pc.points())
        last_print_time = time.time()

        for n, i in enumerate(background_pc.points()):
            if time.time() > last_print_time + status_print_duration:
                last_print_time = time.time()
                printf(str(round(100.0*float(n) / num_points, 2)) + "% through heightmap")

            # Convert to projected coordinates, then project to TGC using the high resolution pointcloud to ensure alignment
            easting, northing = background_pc.enuToProj(i[0], i[1])
            x, y, z = pc.projToTGC(easting, northing, 0.0)
            # Using 10 - the very soft circles means we need to scale 2.5x more to fill and smooth the terrain
            course_json["userLayers"]["height"].append(get_pixel(x, z, i[2], 2.5*background_scale, brush_type=10))

    # Convert the pointcloud into height elements
    num_points = len(pc.points())
    last_print_time = time.time()
    for n, i in enumerate(pc.points()):
        if time.time() > last_print_time + status_print_duration:
            last_print_time = time.time()
            printf(str(round(100.0*float(n) / num_points, 2)) + "% through heightmap")

        x, y, z = pc.enuToTGC(i[0], i[1], 0.0) # Don't transform y, it's inverted from elevation
        course_json["userLayers"]["height"].append(get_pixel(x, z, i[2], image_scale))

    if options_dict.get('lidar_trees', False) and len(read_dictionary.get('trees', [])) > 0:
        printf("Adding trees from lidar data")
        # Need separate mask geopointcloud because pc is cropped
        mask_pc = GeoPointCloud()
        mask_pc.addFromImage(im, image_scale, read_dictionary['origin'], read_dictionary['projection'])
        for o in get_lidar_trees(course_json['theme'], options_dict.get('tree_variety', False), read_dictionary['trees'], tree_settings_dict, tree_category, pc, mask, mask_pc, image_scale):
            course_json["placedObjects2"].append(o)

    # Download OpenStreetMaps Data for this smaller area
    if options_dict.get('use_osm', True):
        printf("Adding golf features to lidar data")

        # Get spline configuration file, if present
        spline_json = tgc_tools.get_spline_configuration_json(heightmap_dir_path)

        # Use this data to create playable courses automatically
        upper_left_enu = pc.ulENU()
        lower_right_enu = pc.lrENU()
        upper_left_latlon = pc.enuToLatLon(*upper_left_enu)
        lower_right_latlon = pc.enuToLatLon(*lower_right_enu)
        # Order is South, West, North, East
        result = OSMTGC.getOSMData(lower_right_latlon[0], upper_left_latlon[1], upper_left_latlon[0], lower_right_latlon[1], printf=printf)
        osm_trees = OSMTGC.addOSMToTGC(course_json, pc, result, x_offset=float(options_dict.get('adjust_ew', 0.0)), y_offset=float(options_dict.get('adjust_ns', 0.0)), \
                                                         options_dict=options_dict, spline_configuration_json=spline_json, printf=printf)

        if len(osm_trees) > 0:
            printf("Adding trees from OpenStreetMap")
            for o in get_trees(course_json['theme'], options_dict.get('tree_variety', False), osm_trees, tree_settings_dict, tree_category):
                course_json["placedObjects2"].append(o)

    # Automatically adjust course elevation
    if options_dict.get('auto_elevation', True):
        printf("Moving course to lowest valid elevation")
        course_json = tgc_tools.elevate_terrain(course_json, None, printf=printf)

    # Automatic rotate to fit if needed
    if options_dict.get('auto_position', True):
        printf("Adjusting course to fit on map")
        course_json = tgc_tools.auto_position_course(course_json, printf=printf)

    printf("Course Description Complete")

    return course_json

def generate_flat_course(course_json, xml_data, options_dict={}, tree_settings_dict={}, tree_category=[], printf=print):
    course_json, osm_trees = OSMTGC.addOSMFromXML(course_json, xml_data, options_dict=options_dict, printf=printf)
    if len(osm_trees) > 0:
        printf("Adding trees from OpenStreetMap")
        for o in get_trees(course_json['theme'], options_dict.get('tree_variety', False), osm_trees, tree_settings_dict, tree_category):
            course_json["placedObjects2"].append(o)

    return course_json

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python program.py COURSE_DIRECTORY HEIGHTMAP_DIRECTORY")
        sys.exit(0)
    else:
        course_dir_path = sys.argv[1]
        heightmap_dir_path = sys.argv[2]

    print("Getting course description")
    course_json = tgc_tools.get_course_json(course_dir_path)

    print("Generating course")
    course_json = generate_course(course_json, heightmap_dir_path)

    print("Saving new course description")
    tgc_tools.write_course_json(course_dir_path, course_json)
