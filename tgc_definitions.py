
# Record types of surfaces
surfaces = {
    0: "bunker",
    1: "green",
    2: "fairway",
    3: "rough",
    4: "heavyrough",
    5: "clearobjects",
    6: "cleartrees",
    7: "surface1",
    8: "surface2",
    9: "water",
    10: "surface3"
}

featuresToSurfaces = {
    "bunker": 0,
    "green": 1,
    "fairway": 2,
    "rough": 3,
    "heavyrough": 4,
    "clearobjects": 5,
    "cleartrees": 6,
    "surface1": 7,
    "surface2": 8,
    "water": 9,
    "surface3": 10,
    "cartpath": 10,
}

brushes = {
    8: "firm_circle",
    9: "medium_circle",
    10: "soft_circle",
    15: "soft_square",
    54: "very_soft_circle",
    72: "hard_square",
    73: "hard_circle"
}

themes = {
    2: "desert",
    5: "boreal",
    6: "tropical",
    7: "countryside",
    8: "harvest",
    10: "delta",
    11: "rustic",
    12: "swiss",
    13: "steppe",
    14: "autumn",
    15: "highlands",
}

normal_trees = {
    2: [0, 1, 2, 3, 9],
    5: [0, 1],
    6: [0, 1, 2, 3, 4, 5, 6, 7],
    7: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16],
    8: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12],
    11: [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    12: [0, 1, 3, 4, 7, 8, 10],
    13: [0, 1, 2, 3, 4, 5, 6, 7],
    14: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    15: [0, 1, 6, 7],
}

skinny_trees = {
    2: [10, 11, 12, 13, 14, 15, 16],
    5: [3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16],
    6: [8, 9, 13, 14, 15, 16, 17, 18, 19],
    7: [13, 14],
    8: [0, 1, 2],
    10: [],
    11: [13, 14, 16],
    12: [2, 5, 9],
    13: [8, 9, 10, 11, 12, 13, 14, 15],
    14: [12, 13, 15],
    15: [2, 3, 8, 9, 10, 22],
}

# List all types to be included on settings page, one for each tree type number, "" to skip
tree_names = {
    2: ["Tree", "Tree", "Tree", "Tree", "", "", "", "", "", "Tree", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Dead Tree", "Dead Tree", "Dead Tree"],
    5: ["Cedar", "Cedar", "Cedar", "Pine", "Pine", "Pine", "Ponderosa", "Ponderosa", "Ponderosa", "Pine", "Pine", "Pine", "Pine", "Pine", "Pine", "Pine", "Pine", "Maple", "Birch", "Birch"],
    6: ["Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm"],
    7: ["Oak", "Oak", "Oak", "Oak", "Oak", "Elm", "Elm", "Elm", "Ash", "Ash", "Ash", "Poplar", "Poplar", "Sycamore", "Sycamore", "Birch", "Birch", "Willow", "Willow"],
    8: ["Aspen", "Aspen", "Aspen", "Birch", "Birch", "Birch", "Elm", "Elm", "Elm", "Sycamore", "Hickory", "Maple", "Maple", "Maple", "Ash", "Ash", "Oak", "Poplar", "Poplar", "Willow", "Willow"],
    10: ["Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Small Tree", "Small Tree", "Tree", "Small Tree", "Small Tree", "Small Tree", "Small Tree"],
    11: ["Poplar", "Poplar", "Birch", "", "Ash", "Ash", "Elm", "Elm", "Maple", "Sycamore", "Oak", "Oak", "Oak", "Pine", "Cedar", "Ponderosa", "Spruce"],
    12: ["Pine", "Pine", "Pine", "Pine", "Pine", "Pine", "Mini Spruce", "Spruce", "Spruce", "Pine", "Pine", "Bare", "Bare", "Bare", "Bare"],
    13: ["Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Palm", "Short Palm", "Short Palm"],
    14: ["Aspen", "Birch", "Oak", "Oak", "Oak", "Oak", "Oak", "Ash", "Elm", "Elm", "Birch", "Birch", "Pine", "Pine", "Bare", "Pine"],
    15: ["Birch", "Birch", "Cedar", "Cedar", "Oak", "Oak", "Elm", "Elm", "Spruce", "Spruce", "Pine", "", "", "", "", "", "", "", "", "", "", "", "Fir", "Ash", "Ash"],
}

tree_meters_to_tgc = {
    2: [0.1699, 0.1331, 0.1407, 0.0923, 0, 0, 0, 0, 0, 0.0534, 0.0507, 0.0801, 0.0697, 0.0857, 0.0417, 0.0512, 0.0621, 0.1769, 0.2024, 0.2807],
    5: [0.0421, 0.0291, 0.0781, 0.0647, 0.0357, 0.037, 0.024, 0.0458, 0.0836, 0.0259, 0.0396, 0.0688, 0.0299, 0.0556, 0.0311, 0.0278, 0.0274, 0.0328, 0.0483, 0.036, 0.0349],
    6: [0.0361, 0.0321, 0.0382, 0.0374, 0.03, 0.0356, 0.0372, 0.0391, 0.0311, 0.0334, 0.0349, 0.0413, 0.0417, 0.0329, 0.0393, 0.0342, 0.038, 0.0317, 0.0526, 0.0379],
    7: [0.0357, 0.0341, 0.0395, 0.0331, 0.0418, 0.0405, 0.046, 0.0381, 0.0309, 0.0374, 0.0344, 0.032, 0.0356, 0.0303, 0.0331, 0.0555, 0.0615, 0.0432, 0.0489],
    8: [0.0465, 0.0399, 0.0464, 0.0496, 0.0467, 0.0481, 0.0369, 0.0508, 0.0323, 0.0381, 0.0361, 0.0475, 0.0423, 0.0485, 0.0385, 0.039, 0.0375, 0.042, 0.0431, 0.0491],
    10: [0.0359, 0.033, 0.0394, 0.0378, 0.0294, 0.0356, 0.036, 0.0392, 0.0373, 0.0389, 0.0678, 0.0713, 0.0555, 0.06, 0.0619, 0.0916, 0.1094],
    11: [0.0321, 0.0353, 0.0535, 0, 0.0306, 0.0362, 0.0474, 0.0371, 0.0321, 0.0329, 0.0344, 0.0338, 0.0391, 0.0353, 0.0288, 0.0444, 0.0391],
    12: [0.1008, 0.0587, 0.055, 0.0529, 0.0692, 0.058, 0.1192, 0.0699, 0.0827, 0.0368, 0.0648, 0.0478, 0.042, 0.0416, 0.038],
    13: [0.1618, 0.1309, 0.0912, 0.0926, 0.1104, 0.0622, 0.0672, 0.0681, 0.0329, 0.0342, 0.0414, 0.0419, 0.0389, 0.0333, 0.0376, 0.0301, 0.0888, 0.1041],
    14: [0.0471, 0.0486, 0.0321, 0.0389, 0.0396, 0.0323, 0.0424, 0.0467, 0.0367, 0.0424, 0.0485, 0.0533, 0.0394, 0.0484, 0.0366, 0.0358],
    15: [0.0547, 0.0615, 0.0454, 0.0284, 0.0336, 0.0405, 0.0474, 0.0374, 0.0257, 0.041, 0.0241, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0247, 0.0317, 0.0371]
}

tee_colors = {
    4: "red",
    0: "green",
    3: "white",
    2: "blue",
    1: "black",
    5: "gold"
}
