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
    conf = json.load(open(f))
    for key in ["presentation", "styles", "title", "slides"]:
        if not (key in conf):
            print("Could not find key {} in {}".format(key, f), 
                file=sys.stderr)
            return None
    return conf

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
    parser.add_argument("directory", 
            help="Directory containing template and configuration.")
    parser.add_argument(
        '--config',
        '-c', 
        action='store',
        help="JSON file to use for generating index")
    parser.add_argument(
        '--template'
        '-t', 
        action='store',
        help="Base HTML template")
    parser.add_argument(
        '--output',
        '-o',
        action='store',
        help="Output of index generation. \
                By default this is [directory]/index.html.")

    args = parser.parse_args()

    config = validate(args.config or args.directory + '/config.json')
    if config is None:
        print("Invalid config, exiting...")
        sys.exit(1)
    soup = BeautifulSoup(
        open(args.template_t or args.directory + '/index.template'), 
        'lxml')
    output = generate(config, soup)

    with open(args.output or args.directory + '/index.html', 'w') as f:
        f.write(output)
