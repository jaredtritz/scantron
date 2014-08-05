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

    def deliver_latex(self):
        latex = r"""
\documentclass{article}
\usepackage{graphicx}
\begin{document}
        """
        for pp in self.problems:
            latex += pp.deliver_latex()
        latex += r"""
\end{document}
        """
        with open(self.output_dir+'/test.tex', "w") as myfile:
            myfile.write(latex)


