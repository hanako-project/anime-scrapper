import json

from file_parser import get_data_array, get_link
from fetcher import fetch_content, source_checker
from content_parser import parse_content
from merger import merge_data


def main():
    new_data_array = []
    anime = get_data_array('example.json')
    for idx, data in enumerate(anime):
        url_dict = get_link(data)
        source, url = source_checker(url_dict)
        content = fetch_content(url)
        if content is not None:
            new_data = parse_content(content, source)
            data = merge_data(data, new_data)
            new_data_array.append(data)

    with open('result.json', 'w') as fp:
        json.dump(new_data_array, fp, indent=4)


if __name__ == '__main__':
    main()
