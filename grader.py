#!/usr/bin/env python2
#from lib.scantron_lib import *
import lib.scantron_lib as slib
import lib.latex_lib as tlib
import csv
import argparse
import imp
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform matching analysis using home grown \'resampling\' algorithm.')
    parser._optionals.title = "arguments"
    parser.add_argument('-ifile', required=True, help='csv file from scantron')
    parser.add_argument('-sid_col', type=int, required=True, help='student id column in ifile')
    parser.add_argument('-form_col', type=int, required=True, help='exam form column in ifile')
    parser.add_argument('-ans_cols', nargs='+', type=int, required=True, help='list of answer columns')
    parser.add_argument('-sfile', required=True, help='python file with question and answer scrambling map')
    parser.add_argument('-cfile', required=True, help='python file with credit/scoring map')
    args = parser.parse_args() # go get args

sdata = []
with open(args.ifile, 'rb') as csvfile: 
    datareader = csv.reader(csvfile, delimiter=',')
    sheads = datareader.next()
    for row in datareader:
        sdata.append(row)

imports = dict()
execfile(os.path.abspath(args.sfile), imports)
if 'q_map' in imports and 'a_map' in imports:
    q_map = imports['q_map']
    a_map = imports['a_map']
else:
    print "oops!  please check your -sfile format"
    exit()

imports = dict()
execfile(os.path.abspath(args.cfile), imports)
if 's_map' in imports:
    s_map = imports['s_map']
else:
    print "oops!  please check your -sfile format"
    exit()

scantron = slib.Scantron(sdata=sdata, idcol=args.sid_col, acols=args.ans_cols, fcol=args.form_col)

scantron.init_exams()
scantron.unscramble_exams(q_map, a_map)

# print statements for debugging
#print_table(scantron.translate_identity())
#print_table(scantron.translate_identity_position())
#print_table(scantron.translate_fomrA())

slib.print_table(scantron.score_exams(slib.Grader(s_map)))
