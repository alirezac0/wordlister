import argparse
import os.path
from urllib.parse import urlparse
import os
import re


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help = "Target File",action="store")

args = parser.parse_args()

paths = []
words = []


if args.target:
    if (os.path.exists(args.target)):
        with open(args.target, 'r') as f:
            sitemap = f.read().split()
            for url in sitemap:
                if url.count('] - ') == 2:
                    url = url.split(" - ")[2]
                elif url.count('] - ') == 1:
                    url = url.split(" - ")[1]
                if url[0:3] == '://':
                    url = "http" + url
                elif url[0:2] == '//':
                    url = "http:" + url
                elif url[0:1] == '/':
                    url = "http:/" + url
                if url[-1:] == ']':
                    url = url[:-1]
                if url[0:7] == "http://" or url[0:8] == "https://":
                    o = urlparse(url)
                    paths.append(o.path)
            list_set = set(paths)
            unique_paths = (list(list_set))
            for url in unique_paths:
                url = url.split("/")
                for peyman in url:
                    if len(peyman) > 0:
                        words.append(peyman)
                        s = ""
                        if len(peyman) > 0:
                            for i in range(len(peyman)):
                                if peyman[i].islower():
                                    s += peyman[i]
                                elif  peyman[i].isupper():
                                    if len(s) > 1:
                                        words.append(s)
                                    s = peyman[i]
                                elif peyman[i] == '.' and len(s) > 0:
                                    words.append(s)
                                if len(s) > 0 and i == len(peyman)-1 and re.search("[A-Z]", s) and not bool(re.search("[\.]", s)):
                                    words.append(s)
            list_set2 = set(words)
            unique_words = (list(list_set2))
    else:
        print("Wrong Input!")

for x in unique_words:
    if len(x) > 1 and not bool(re.search("[\.]", x)):
        print(x)
