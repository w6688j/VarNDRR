#! /usr/bin/python

import sys

prefix = sys.argv[1]

out_arg1 = file(prefix + '.arg1', 'w')
out_arg2 = file(prefix + '.arg2', 'w')
out_lbl = file(prefix + '.lbl', 'w')


def getIdByLabID(lab_id):
    labs = {
        'Comparison': '1',
        'Contingency': '2',
        'Temporal': '3',
        'Expansion': '4',
    }

    return labs[lab_id]


for line in file(sys.argv[2], 'rU'):
    segs = line.strip().split('|||')

    lbl = segs[0]
    arg1 = segs[1]
    arg2 = segs[2]

    lbl = getIdByLabID(lbl)
    if lbl != '1':
        lbl = '0'

    print >> out_arg1, arg1
    print >> out_arg2, arg2
    print >> out_lbl, lbl

out_arg1.close()
out_arg2.close()
out_lbl.close()
