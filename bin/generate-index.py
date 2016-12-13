#!/usr/bin/env python2.7
from __future__ import print_function, division
import json
import sys

from bs4 import BeautifulSoup

HELPSTR = """
Usage: generate-index.py CONFIG TEMPLATE [OUTPUT]
Generate a reveal.js index file using configuration in CONFIG and base
template TEMPLATE. By default outputs to 'index.html', instead can output
to OUTPUT.
"""

def make_section(soup, file):
    section = soup.new_tag('section')
    section['data-markdown'] = file
    section['data-separator'] = "^\\n\\n\\n"
    section['data-separator-vertical'] = "^\\n\\n"
    section['data-separator-notes'] = "^Note:"
    return section

def generate(config, template):
    soup = BeautifulSoup(open(template).read(), "lxml")
    config = json.loads(open(config).read().strip())
    soup.title.string = config['presentation']
    for style in config['styles']:
        soup.head.append(soup.new_tag('link', rel='stylesheet', href=style))
    # There should only be one `slides` class; we use the first one
    # regardless of how many there are
    slides = soup.find_all(class_='slides')[0]
    slides.append(make_section(soup, config['title_slide']))
    for slide in config['slides']:
        slides.append(make_section(soup, slide))
    return soup.prettify()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Missing positional arguments")
        print(HELPSTR)
        sys.exit(1)
    print(generate(sys.argv[1], sys.argv[2]))
