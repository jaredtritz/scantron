#!/usr/bin/env python2
import lib.latex_lib as tlib
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creates scrambled exams from latex pieces with unscrambling keys/maps.')
    parser._optionals.title = "arguments"
    parser.add_argument('-pdir', required=True, help='directory where python problem files are found')
    parser.add_argument('-versions', type=int, required=True, help='number of versions to make')
    parser.add_argument('-qmix', required=True, choices=['no', 'yes'], help='mix the questions')
    parser.add_argument('-amix', required=True, choices=['no', 'yes'], help='mix the answers')
    args = parser.parse_args() # go get args

probs_path = os.path.abspath(args.pdir)
pfiles = [fn for fn in os.listdir(args.pdir) if (fn.endswith('.py') and fn.find('prob') > -1)]

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
    problem = tlib.Exam_Problem(prob, question, answers, solution)
    problems.append(problem)

problems = sorted(problems, key=lambda prob: prob.name)

doc = tlib.Exam_Document(problems, probs_path)
qmix = args.qmix == 'yes'
amix = args.amix == 'yes'
doc.write_maps(versions=args.versions, qmix=qmix, amix=amix)
doc.write_exams()

#import subprocess
#subprocess.call(['./test.sh'])

