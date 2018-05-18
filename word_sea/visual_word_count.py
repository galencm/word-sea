# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2018, Galen Curwen-McAdams
import sys
import collections
import argparse
import fileinput
import numpy

def print_rgb(to_print, rgb, mode="fg", bg_textcolor=(255, 255, 255)):
    if mode == "fg":
        print("\x1b[38;2;{0};{1};{2}m{3}\x1b[0m".format(*rgb, to_print), end='')
    elif mode == "bg":
        print("\x1b[48;2;{0};{1};{2}m\x1b[38;2;{3};{4};{5}m{6}\x1b[0m".format(*rgb, *bg_textcolor, to_print), end='')

def display_words(corpus, beige_list=None, length_threshold=None, count_threshold=None, display_key=False, display_key_only=False):
    if beige_list is None:
        beige_list = set()

    wc = collections.Counter()
    printable_corpus = corpus
    corpus = corpus.replace("\n", " ")
    for word in corpus.split(" "):
        if word:
            wc[word.lower()] += 1

    if length_threshold is not None:
        for k, v in wc.items():
            if len(k) < length_threshold:
                beige_list.add(k)

    if count_threshold is not None:
        for k, v in wc.items():
            if v < count_threshold:
                beige_list.add(k)

    # use the beige list to filter out words
    for item in beige_list:
        try:
            del wc[item]
        except KeyError:
            pass

    corpus_min = min(wc.items(), key=lambda v: v[1])
    corpus_max = max(wc.items(), key=lambda v: v[1])
    corpus_count = len(wc.keys())

    palette = {}
    # min_step = int(255 / corpus_max[1])

    # script takes almost twice as long to run
    # if importing numpy
    freq, bins = numpy.histogram(numpy.array(list(wc.values())), numpy.arange(0, 255))
    min_step = int(255 / len([ s for s in freq if s > 0]))

    if min_step < 1:
        min_step = 1
    for i, step in enumerate(reversed(range(0, 255, min_step))):
        palette[i+1] = step

    printable_corpus = printable_corpus.replace("\n", " \n ")

    if display_key_only is False:
        for word in printable_corpus.split(" "):
            if word.lower() in wc:
                try:
                    rgb = [palette[wc[word.lower()]]] * 3
                except KeyError:
                    rgb = (0, 0, 0)

                print_rgb(word + " ",
                          rgb,
                          mode="bg",
                          bg_textcolor=(128, 128, 128))

            else:
                if word == "\n":
                    print()
                else:
                    # beigelisted
                    print_rgb(word + " ",
                              (245, 245, 220),
                              mode="bg",
                              bg_textcolor=(235, 235, 210))

    if display_key or display_key_only:
        print()
        for k, v in wc.most_common():
            try:
                rgb = [palette[wc[k]]] * 3
            except KeyError:
                rgb=(0, 0, 0)
            print_rgb("{:>4}".format(v),
                              rgb,
                              mode="bg",
                              bg_textcolor=(0, 128, 128)
                      )
            print("  {}".format(k))

def main():

    corpus = ""
    # handle stdin first
    if not sys.stdin.isatty():
        corpus = sys.stdin.read()

    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    parser.add_argument('--key', action='store_true')
    parser.add_argument('--key-only', action='store_true')
    parser.add_argument('--length-threshold', type=int)
    parser.add_argument('--count-threshold', type=int)
    parser.add_argument('--beige-list', nargs='+', default=[])
    args = parser.parse_args()

    with fileinput.input(files=args.files) as f:
        for line in f:
            if line:
                corpus += line

    display_words(corpus, beige_list=set(args.beige_list), length_threshold=args.length_threshold, count_threshold=args.count_threshold, display_key=args.key, display_key_only=args.key_only)

if __name__ == "__main__":
    main()
