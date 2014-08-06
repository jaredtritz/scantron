import json

class Question(object):

    def __init__(self, eform, qpos, aval):
        self.eform = eform
        self.qpos = qpos
        self.aval = aval
        self.parse_answer()
    
    def parse_answer(self):
        possible_answers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] 
        self.avals = list(self.aval) # possibly more than one bubble filled in
        self.apos = []
        for vv in self.avals:
            self.apos.append(possible_answers.index(vv)) 

    def set_qid(self, qmap):
        self.qid = qmap[self.eform][self.qpos] - 1

    def unscramble_answers(self, amap):
        self.aids = []
        for pos in self.apos:
            self.aids.append(amap[self.eform][self.qid][pos])

class Exam(object):

    def __init__(self, sid, eform, alist):
        self.sid = sid
        self.eform = eform
        self.alist = alist  # relative to exam form

    def unscramble_questions(self, qmap):
        self.qlist = [] 
        qpos = 0
        for aa in self.alist:
            question = Question(self.eform, qpos=qpos, aval=aa)
            question.set_qid(qmap)
            self.qlist.append(question)
            qpos += 1
 
    def unscramble_answers(self, amap):
        for qq in self.qlist:
            qq.unscramble_answers(amap)

class Scantron(object):

    def __init__(self, sdata, idcol, acols, fcol):
        self.sdata = sdata # scantron data 
        self.idcol = idcol # student id column in scantron data 
        self.acols = acols # question columns in scantron data (indexed) [3,4,5..22]
        self.fcol = fcol   # exam form identifier column (A, or B, or C, etc)

    def init_exams(self):
        self.exams = []
        for row in self.sdata:
            # extract the bits for a student
            sid = row[self.idcol]
            eform = row[self.fcol]
            alist = []
            for qq in self.acols:
                alist.append(row[qq])
            exam = Exam(sid=sid, eform=eform, alist=alist)
            self.exams.append(exam)

    def unscramble_exams(self, qmap, amap):
        for exam in self.exams:
            exam.unscramble_questions(qmap)
            exam.unscramble_answers(amap)
      
    def score_exams(self, grader):
        scores = []
        scores.append(['who', 'exam form', 'question', 'selection', 'question form A', 'selections form A', 'score'])
        for exam in self.exams:
            for qq in exam.qlist:
                scores.append([exam.sid, exam.eform, qq.qpos+1, qq.aval, qq.qid+1, qq.aids, grader.score(qq)])
        return scores
      
    def translate_identity(self):
        ptable = []
        for exam in self.exams:
            alist = []
            alist.append(exam.sid)
            alist.append(exam.eform)
            for qq in exam.qlist:
                alist.append(str(qq.aval))
            ptable.append(alist)
        return ptable

    def translate_identity_position(self):
        ptable = []
        for exam in self.exams:
            alist = []
            alist.append(exam.sid)
            alist.append(exam.eform)
            for qq in exam.qlist:
                alist.append(str(qq.apos))
            ptable.append(alist)
        return ptable

    def translate_fomrA(self):
        ptable = []
        for exam in self.exams:
            alist = []
            alist.append(exam.sid)
            alist.append(exam.eform)
            for qq in exam.qlist:
                alist.append(str(qq.aids))
            ptable.append(alist)
        return ptable

class Grader(object):

    def __init__(self, score_key):
        self.score_key = score_key

    def score(self, qq):
        # print for debugging
        weights = self.score_key[qq.qid][1]
        num_selected = len(qq.aids)
        weight = 0
        if num_selected < len(weights):
            weight = weights[num_selected-1]
        possible = self.score_key[qq.qid][0]
        credits = [0]
        for aa in qq.aids:
            credits.append(possible[aa-1]) 
        credit = weight * max(credits)
        return credit


def print_table(tdata):
    maxes = [0 for ii in tdata[0]]
    for dat in tdata:
        for ii in range(0,len(dat)):
            if maxes[ii] < len(str(dat[ii])):
                maxes[ii] = len(str(dat[ii])) 
    for dat in tdata:
        tmp = []
        for ii in range(0,len(dat)):
            myformat = '{0: <'+str(maxes[ii])+'}'
            tmp.append(myformat.format(dat[ii]))
        pp = '| ' + ' | '.join(tmp) + ' |'
        print pp

def write_json(var, data, ofile):
    ofile.write('\n')
    ofile.write(var + ' = ')
    json.dump(data, ofile)
    ofile.write('\n')


