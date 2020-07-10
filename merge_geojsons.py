# merging multiple geojsons into one file without any fancy libraries
# only tested with same geom type (eg point) and properties fields

import os
import time
import json

start_time = time.time()

geojsons_in_folder = "data/state_geojsons/"
out_folder = "data/"


features_list = []
for root, dirs, files in os.walk(geojsons_in_folder):
    for gj in files:
        if gj.endswith(".geojson"):
            gj_path = geojsons_in_folder + gj
            print(gj_path)
            with open(gj_path) as data_file:
                data = json.load(data_file)
                x = data["features"]
                features_list = features_list + x

merged_geojson = {
    "type":"FeatureCollection",
    # optional crs
    #"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::4269" }
    #},
    "features": features_list
}

with open(out_folder + "merge_test.geojson", 'w') as fp:
    json.dump(merged_geojson, fp)

print("--------------")
print("%s seconds" % (time.time() - start_time))
