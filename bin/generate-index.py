#!/usr/bin/env python2.7
from __future__ import print_function, division
import json
import sys
import argparse

from bs4 import BeautifulSoup


def make_section(soup, file):
    section = soup.new_tag('section')
    section['data-markdown'] = file
    section['data-separator'] = "^\\n\\n\\n"
    section['data-separator-vertical'] = "^\\n\\n"
    section['data-separator-notes'] = "^Note:"
    return section


def validate(f):
    try:
        conf = json.load(open(f))
        for key in ["presentation", "styles", "title", "slides"]:
            if not (key in conf):
                print("Could not find key {} in {}".format(key, f),
                      file=sys.stderr)
                return None
        return conf
    except json.decoder.JSONDecodeError as e:
        print("Failed to decode JSON file {}".format(f), file=sys.stderr)
        return None


def generate(config, template):
    """
    Generate a reveal.js index.html
    Args:
        - config (dict): Configuration options. Must contain keys:
            - presentation
            - styles
            - title
            - slides
        - template (BeautifulSoup): Template HTML
    """
    template.title.string = config['presentation']
    for style in config['styles']:
        template.head.append(
            template.new_tag(
                'link',
                rel='stylesheet',
                href=style))
    # There should only be one `slides` class; we use the first one
    # regardless of how many there are
    slides = template.find_all(class_='slides')[0]
    title = make_section(template, config['title'])
    title['class'] = 'title'
    slides.append(title)
    for slide in config['slides']:
        slides.append(make_section(template, slide))
    return template.prettify()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="JSON file to use for generating index")
    parser.add_argument("template", help="Base HTML template")
    parser.add_argument(
        '--output',
        '-o',
        action='store',
        help="Output of index generation. By default this is STDOUT.")

    args = parser.parse_args()

    config = validate(args.config)
    if config is None:
        print("Invalid config, exiting...")
        sys.exit(1)
    soup = BeautifulSoup(open(args.template), "lxml")
    output = generate(config, soup)

    if args.output is not None:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)
