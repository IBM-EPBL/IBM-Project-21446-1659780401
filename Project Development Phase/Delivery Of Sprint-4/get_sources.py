import json

import requests


def get_sources():
    json_sources = requests.get("https://newsapi.org/v1/sources").json()
    sources = []
    counter = 1
    for source in json_sources["sources"]:
        sources.append({
            "id": source['id'],
            "name": source['name'],
            "num": counter
        })
        counter += 1


    with open("sources.json", 'w') as out:
        json.dump(sources, out, indent=4)

    return sources

get_sources()
