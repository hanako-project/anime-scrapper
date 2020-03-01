import json
import re

URL_MATCHER = {
    "MAL": r'https:\/\/myanimelist.net\/anime\/\d{1,10}',
    "ANILIST": r'https:\/\/anilist.co\/anime\/\d{1,10}',
    "ANIDB": r'https:\/\/anidb.net\/anime\/\d{1,10}',
    "KITSU": r'https:\/\/kitsu.io\/anime\/\d{1,10}',
    "NMOE": r'^https:\/\/notify.moe\/anime\/'
}


# SOURCE_LIST = ["MAL", "KITSU", "ANIDB", "ANILIST"]


def get_data_array(name):
    with open(name) as f:
        return json.load(f).get('data')


def get_link(data):
    link_dict = {}
    sources = data.get('sources')
    for url in sources:
        mal = re.match(URL_MATCHER["MAL"], url)
        anidb = re.match(URL_MATCHER["ANIDB"], url)
        kitsu = re.match(URL_MATCHER["KITSU"], url)
        anilist = re.match(URL_MATCHER["ANILIST"], url)
        nmore = re.match(URL_MATCHER["NMOE"], url)
        if mal:
            link_dict["MAL"] = mal.group(0)
        if anidb:
            link_dict["ANIDB"] = anidb.group(0)
        if kitsu:
            link_dict["KITSU"] = kitsu.group(0)
        if anilist:
            link_dict["ANILIST"] = anilist.group(0)
        if nmore:
            link_dict["NMOE"] = nmore.group(0)

    return link_dict
