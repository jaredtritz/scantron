import lib.scantron_lib as slib
import random

class Exam_Answers(object):
    
    def __init__(self, items):
        self.items = items

    def deliver_latex(self):
        answers_tex = r"""
% Answers:
\begin{enumerate}"""
        for aa in self.items: 
            answers_tex += r"""
    \item """ + aa
        answers_tex += r"""
\end{enumerate}
        """
        return answers_tex

class Exam_Question(object):
    
    def __init__(self, latex):
        self.latex = latex

    def deliver_latex(self):
        return self.latex

class Exam_Solution(object):
    
    def __init__(self, latex):
        self.latex = latex

    def deliver_latex(self):
        return self.latex

class Exam_Problem(object):

    def __init__(self, name, question, answers, solution):
        self.name = name
        self.question = question
        self.answers = answers
        self.solution = solution

    def deliver_latex(self, version):
        latex = self.question.deliver_latex()
        latex += self.answers.deliver_latex()
        latex += self.solution.deliver_latex()
        return latex

class Exam_Document(object):

    def __init__(self, problems, output_dir):
        self.problems = problems
        self.output_dir = output_dir
        self.versions = dict()

    def write_maps(self, versions=1, qmix=False, amix=False):
        # scramble the questions
        q_map = dict()
        probs = range(1, len(self.problems)+1)
        for xnum in range(1, versions+1):
            tmp = probs[:]
            if xnum > 1 and qmix: # don't scramble first version
                random.shuffle(tmp)
            q_map[xnum] = tmp

        # scramble the answers
        a_map = dict()
        answers = []
        for xnum in range(1, versions+1):
            alist = []
            for pp in self.problems:
                tmp = range(1, len(pp.answers.items)+1)
                if xnum > 1 and amix: # don't scramble first version
                    random.shuffle(tmp)
                alist.append(tmp)
            a_map[xnum] = alist

        with open(self.output_dir+'/'+'map_scramble.py', 'w') as outfile:
            slib.write_json('q_map', q_map, outfile)
            slib.write_json('a_map', a_map, outfile)

    def read_maps(self):
        imports = {}
        tmp = dict()
        ofile = self.output_dir+'/'+'map_scramble.py'
        smap = dict()
        execfile((ofile), smap)
        return smap

    def write_exams(self):
        smap = self.read_maps()
        self.deliver_latex()

    def deliver_latex(self):
        problems = self.problems
        latex = r"""
\documentclass{article}
\usepackage{graphicx}
\begin{document}
        """
        for pp in problems:
            latex += pp.deliver_latex()
            latex += r"\pagebreak"
        latex += r"""
\end{document}
        """
        tex_file = self.output_dir+'/exam'++'.tex'
        with open(tex_file, "w") as myfile:
            myfile.write(latex)

        """
        import subprocess
        shell_cmd = 'rm ' + self.output_dir + '/' + self.ofile_name + '.aux'
        import pdb; pdb.set_trace() 
        #subprocess.call([shell_cmd])
        os.call(shell_cmd)
        """

