from contextlib import closing

import requests
from requests import RequestException


def source_checker(url_dict: dict):
    """Prioritize some source if more than one source is available"""
    try:
        return "MAL", url_dict.get("MAL")
    except Exception as e:
        try:
            "KITSU", url_dict.get("KITSU")
        except Exception as e:
            try:
                "NMOE", url_dict.get("NMOE")
            except Exception as e:
                try:
                    "ANILIST", url_dict.get("ANILIST")
                except Exception as e:
                    return "ANIDB", url_dict.get("ANIDB")


def fetch_content(url):
    # TODO add randomize user agent header
    try:
        print("Fetching {0}".format(url))
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)
