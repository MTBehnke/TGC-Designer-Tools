
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
    14: [12, 15],
    15: [2, 3, 8, 9, 10, 22],
}

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
    14: ["Aspen", "Birch", "Oak", "Oak", "Oak", "Oak", "Oak", "Ash", "Elm", "Elm", "Birch", "Birch", "Pine", "Bare", "Pine"],
    15: ["Birch", "Birch", "Cedar", "Cedar", "Oak", "Oak", "Elm", "Elm", "Spruce", "Spruce", "Pine", "", "", "", "", "", "", "", "", "", "", "", "Fir", "Ash", "Ash"],
}

tree_normalize = {
    2: [1.00, 0.78, 0.83, 0.54, 1.00, 1.00, 1.00, 1.00, 1.00, 0.31, 0.30, 0.47, 0.41, 0.50, 0.25, 0.30, 0.37, 1.04, 1.19, 1.65],
    5: [1.00, 0.69, 1.85, 1.54, 0.85, 0.88, 0.57, 1.09, 1.99, 0.62, 0.94, 1.63, 0.71, 1.32, 0.74, 0.66, 0.65, 0.78, 1.15, 0.85, 0.83],
    6: [1.00, 0.89, 1.06, 1.04, 0.83, 0.98, 1.03, 1.08, 0.86, 0.92, 0.97, 1.14, 1.15, 0.91, 1.09, 0.95, 1.05, 0.88, 1.45, 1.05],
    7: [1.00, 0.96, 1.11, 0.93, 1.17, 1.13, 1.29, 1.07, 0.87, 1.05, 0.96, 0.90, 1.00, 0.85, 0.93, 1.56, 1.72, 1.21, 1.37],
    8: [1.00, 0.86, 1.00, 1.07, 1.01, 1.03, 0.79, 1.09, 0.69, 0.82, 0.78, 1.02, 0.91, 1.04, 0.83, 0.84, 0.81, 0.90, 0.93, 1.06],
    10: [1.00, 0.92, 1.09, 1.05, 0.82, 0.99, 1.00, 1.09, 1.04, 1.08, 1.89, 1.98, 1.55, 1.67, 1.72, 2.55, 3.04],
    11: [1.00, 1.10, 1.67, 1.00, 0.95, 1.13, 1.48, 1.16, 1.00, 1.03, 1.07, 1.06, 1.22, 1.10, 0.90, 1.39, 1.22],
    12: [1.00, 0.58, 0.55, 0.52, 0.69, 0.58, 1.18, 0.69, 0.82, 0.37, 0.64, 0.47, 0.42, 0.41, 0.38],
    13: [1.00, 0.81, 0.56, 0.57, 0.68, 0.38, 0.42, 0.42, 0.20, 0.21, 0.26, 0.26, 0.24, 0.21, 0.23, 0.19, 0.55, 0.64],
    14: [1.00, 1.03, 0.68, 0.83, 0.84, 0.69, 0.90, 0.99, 0.78, 0.90, 1.03, 1.13, 0.84, 1.03, 0.78, 0.76],
    15: [1.00, 1.12, 0.83, 0.52, 0.61, 0.74, 0.87, 0.68, 0.47, 0.75, 0.44, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.45, 0.58, 0.68],
}

tee_colors = {
    4: "red",
    0: "green",
    3: "white",
    2: "blue",
    1: "black",
    5: "gold"
}
