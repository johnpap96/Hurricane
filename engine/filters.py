#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.error
import urllib.robotparser
from urllib.parse import urlparse


def gather_robots_txt(domain):
    domain = url_to_domain(domain)
    robots = http_checker(domain) + "/robots.txt"
    try:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots)
        rp.read()
    except urllib.error.HTTPError:
        return None
    else:
        return rp


def gather_words_around_search_word(given_description, given_word, length):
    position = given_description.find(given_word)
    return given_description[position - length // 2 : position + length // 2]


def url_validator(url):
    try:
        result = urlparse(url)
        return True if result.scheme and result.netloc and result.path else False
    except Exception as exem:
        print(exem)
        return False


def crop_fragment_identifier(url_path):
    if "#" in url_path:
        return url_path.split("#")[0]
    return url_path


def complete_domain(url_path, current_domain):
    try:
        if url_path[0] == "/":
            return "{0}{1}".format(http_checker(current_domain), url_path)
    except IndexError:
        pass
    return url_path


def http_checker(url):
    if ("http://" in url) or ("https://" in url):
        return url
    else:
        if url[:2] == "//":
            return ("http:" + url)
        return ("http://" + url)


def url_to_domain(url_path):
    return urlparse(url_path).netloc
