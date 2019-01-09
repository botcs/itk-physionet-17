#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import argparse
from math import floor


def main(args):
    # class foo(object):
    #   pass
    # args = foo()
    # args.ref='raw/training2017/REFERENCE.csv'
    annot_lines = open(args.ref, 'r').read().splitlines()
    np.random.shuffle(annot_lines)
    annot_dict = {s: s.split(',')[1] for s in annot_lines}
    index_dict = {'N': [], 'A': [], 'O': [], '~': []}
    for idx, line in enumerate(annot_lines):
        index_dict[annot_dict[line]].append(idx)


    def fp(x): return os.path.normpath(os.path.dirname(args.ref) + '/' + x)
    
    for k in range(args.K):
        crossval_reference = open(fp('VALIDATION%02d.csv'%k), 'w')

        for idxs in index_dict.values():
            l = len(idxs)
            crossval_reference.writelines(
                '%s\n' % annot_lines[i] for i in idxs[k::args.K])
        print('References written succesfully to:', crossval_reference.name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--ref', help='location of reference file',
        default='./raw/training2017/REFERENCE.csv')
    parser.add_argument(
        '--K', help='K for K-fold crossvalidation',
        type=int, default=10)
    args = parser.parse_args()
    main(args)
