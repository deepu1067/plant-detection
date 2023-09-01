classes_plant = {0: "tomato", 1: "potato", 2: "corn", 3: "grape"}
grape = {
    0: "black_measles",
    1: "leaf_blight_(isariopsis_leaf_spot)",
    2: "black_rot",
    3: "healthy",
}
corn = {0: "healthy", 1: "common_rust", 2: "gray_leaf_spot", 3: "northern_leaf_blight"}
tomato = {
    0: "septoria_leaf_spot",
    1: "healthy",
    2: "early_blight",
    3: "yellow_leaf_curl_virus",
    4: "target_spot",
    5: "bacterial_spot",
    6: "late_blight",
    7: "spider_mites_(two_spotted_spider_mite)",
    8: "leaf_mold",
    9: "mosaic_virus",
}
potato = {0: "healthy", 1: "early_blight", 2: "late_blight"}


def get_plant(plant):
    return classes_plant[plant]

def get_model(plant):
    if plant == 0:
        return 'models/tomate.h5' , tomato
    if plant == 1:
        return 'models/potato.h5', potato
    if plant == 2:
        return 'models/corn.h5' , corn
    if plant == 3:
        return 'models/grape.h5' , grape
