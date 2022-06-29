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
queries = []

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
                    queries.append(o.query)
            list_set = set(paths)
            unique_paths = (list(list_set))
            for url in unique_paths:
                url = url.split("/")
                for chare in url:
                    if len(chare) > 0:
                        words.append(chare)
                        s = ""
                        if len(chare) > 0:
                            for i in range(len(chare)):
                                if chare[i].islower():
                                    s += chare[i]
                                elif  chare[i].isupper():
                                    if len(s) > 1:
                                        words.append(s)
                                    s = chare[i]
                                elif chare[i] == '.' and len(s) > 0:
                                    words.append(s)
                                if len(s) > 0 and i == len(chare)-1 and re.search("[A-Z]", s) and not bool(re.search("[\.]", s)):
                                    words.append(s)
            list_set3 = set(queries)
            unique_queries = (list(list_set3))
            for query in unique_queries:
                a = query.split("&")
                for name in a:
                    words.append(name.split("=")[0])
            list_set2 = set(words)
            unique_words = (list(list_set2))
    else:
        print("Wrong Input!")

for x in unique_words:
    if len(x) > 0 and not bool(re.search("[\.]", x)):
        print(x)
