# https://github.com/stefanb/gurs-obcine

import json

js = open('OB.geojson', 'r').read()
gj = json.loads(js)

for feature in gj['features']:

    xfeature = {"type": "Feature", "properties": feature["properties"], "bbox": feature["bbox"],
                "geometry": {"type": "Polygon"}}
    xfeature['geometry']['coordinates'] = feature['geometry']['coordinates']
    output = {"type": "FeatureCollection", "features": [xfeature]}
    name = "{mid}.geojson".format(
        mid=feature["properties"]["OB_MID"], name=feature["properties"]["OB_UIME"])
    open("data/"+name, 'w').write(json.dumps(output))
