#!/usr/bin/env python2
import lib.latex_lib as tlib
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform matching analysis using home grown \'resampling\' algorithm.')
    parser._optionals.title = "arguments"
    parser.add_argument('-pdir', required=True, help='directory where python problem files are found')
    args = parser.parse_args() # go get args

probs_path = os.path.abspath(args.pdir)
pfiles = [fn for fn in os.listdir(args.pdir) if (fn.endswith('.py') and fn.find('prob') > 0)]

imports = {}
for pfile in pfiles:
    tmp = dict()
    execfile((probs_path+'/'+pfile), tmp)
    imports[pfile] = tmp

problems = []
for prob in imports:
    #print imports[prob]['answers']
    question = tlib.Exam_Question(imports[prob]['question_tex'])
    answers = tlib.Exam_Answers(imports[prob]['answers'])
    solution = tlib.Exam_Solution(imports[prob]['solution_tex'])
    problem = tlib.Exam_Problem(question, answers, solution)
    problems.append(problem)

doc = tlib.Exam_Document(problems, probs_path)
doc.scramble(self, extras=0, questions=False, answers=False):
import pdb; pdb.set_trace() 
doc.deliver_latex()

#import subprocess
#subprocess.call(['./test.sh'])

