import lib.scantron_lib as slib

class Exam_Answers(object):
    
    def __init__(self, answers):
        self.answers = answers

    def deliver_latex(self):
        answers_tex = r"""
% Answers:
\begin{enumerate}"""
        for aa in self.answers: 
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

    def __init__(self, question, answers, solution):
        self.question = question
        self.answers = answers
        self.solution = solution

    def deliver_latex(self):
        latex = self.question.deliver_latex()
        latex += self.answers.deliver_latex()
        latex += self.solution.deliver_latex()
        return latex

class Exam_Document(object):

    def __init__(self, problems, output_dir):
        self.problems = problems
        self.output_dir = output_dir
        self.ofile_name = 'test'
        self.versions = dict()

    def scramble(self, extras=0, questions=False, answers=False):
        # create form 1
        # create extra scrambled forms
        # write the scramble key 
        q_map = {
            'A': [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20],
            'B': [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20],
            'C': [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20],
            'D': [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
            #'B': [ 5, 3, 8, 11, 6, 16, 13, 9, 20, 12, 14, 2, 19, 7, 4, 10, 1, 17, 18, 15],
            #'C': [ 3, 20, 14, 9, 16, 18, 17, 19, 12, 15, 10, 6, 1, 11, 5, 2, 8, 4, 13, 7],
            #'D': [ 3, 20, 14, 9, 16, 18, 17, 19, 12, 15, 10, 6, 1, 11, 5, 2, 8, 4, 13, 7]
        }
        a_map = {

            'A':[ 
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],

            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],

            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],

            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5]
            ],

            'B':[
            [3,4,5,1,2],
            [4,3,1,5,2],
            [4,3,1,5,2],
            [5,1,2,3,4],
            [4,3,1,5,2],
            
            [5,1,4,2,3],
            [2,3,5,1,4],
            [2,4,5,3,1],
            [2,5,4,1,3],
            [5,1,4,2,3],
            
            [5,1,2,3,4],
            [5,3,1,2,4],
            [4,5,2,3,1],
            [4,1,2,5,3],
            [4,5,1,2,3],
            
            [3,1,4,5,2],
            [5,1,4,2,3],
            [5,1,2,3,4],
            [3,4,5,1,2],
            [2,3,4,5,1]
            ],
            
            'C':[
            [4,1,2,5,3],
            [2,4,5,3,1],
            [2,4,5,3,1],
            [1,4,3,5,2],
            [5,2,4,3,1],
            
            [1,2,5,3,4],
            [5,1,4,2,3],
            [4,1,2,5,3],
            [4,2,1,3,5],
            [4,3,2,1,5],
            
            [4,2,3,1,5],
            [3,4,2,5,1],
            [1,2,4,5,3],
            [2,4,3,1,5],
            [1,2,5,3,4],
            
            [4,5,2,3,1],
            [2,4,5,3,1],
            [3,5,4,2,1],
            [1,5,3,2,4],
            [1,2,5,3,4]
            ],

            'D':[
            [4,1,2,5,3],
            [2,4,5,3,1],
            [2,4,5,3,1],
            [1,4,3,5,2],
            [5,2,4,3,1],
            
            [1,2,5,3,4],
            [5,1,4,2,3],
            [4,1,2,5,3],
            [4,2,1,3,5],
            [4,3,2,1,5],
            
            [4,2,3,1,5],
            [3,4,2,5,1],
            [1,2,4,5,3],
            [2,4,3,1,5],
            [1,2,5,3,4],
            
            [4,5,2,3,1],
            [2,4,5,3,1],
            [3,5,4,2,1],
            [1,5,3,2,4],
            [1,2,5,3,4]
            ]
        }

        with open(self.output_dir+'/'+'map_scramble.py', 'w') as outfile:
            slib.write_json('q_map', q_map, outfile)
            slib.write_json('a_map', a_map, outfile)

    def deliver_latex(self, versions):
        latex = r"""
\documentclass{article}
\usepackage{graphicx}
\begin{document}
        """
        for pp in self.problems:
            latex += pp.deliver_latex()
            latex += r"\pagebreak"
        latex += r"""
\end{document}
        """
        tex_file = self.output_dir+'/'+self.ofile_name+'.tex'
        with open(tex_file, "w") as myfile:
            myfile.write(latex)

        """
        import subprocess
        shell_cmd = 'rm ' + self.output_dir + '/' + self.ofile_name + '.aux'
        import pdb; pdb.set_trace() 
        #subprocess.call([shell_cmd])
        os.call(shell_cmd)
        """

