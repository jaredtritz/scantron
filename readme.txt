scrambler.py
    Compiles input python file containing latex strings into multiple versions of latex output where questions and answers are scrambled.
    Produces key/map files for unscambling, used by grader below.

grader.py 
    Merges scantron output from multiple exam formats where questions and answers were scrambled into one exam result summary.
    Uses auto generated key/map file from scrambler above to unscramble and remerge the exam data.
    Flexible exam scoring allows multiple answers/guesses to be entered per problem, with credit discounting based on number of guesses.

Usage examples (with output below):

$ scrambler.py -pdir scrambler/example_probs/ -ver 2 -qmix no -amix yes
$ grader.py -if grader/example_quiz.csv -sid 0 -form 1 -ans_cols 3 4 5 6 -sfile grader/example_sfile.py -cfile grader/example_cfile.py

--------------------------------------------------------------------------

files:

├── grader.py                   <<< executable script for grading exams ***use this***
├── grader                      
│   ├── example_cfile.py        <<< example config/map file for question and answer scrambleing
│   ├── example_sfile.py        <<< example config/map file for problem scoring
│   └── example_quiz.csv        <<< example output from scantron
│                               
│
├── scrambler.py                <<< executable script for creating scrambled exams ***use this***
├── scrambler                   
│   ├── compile.sh              <<< example complile script
│   └── example_probs          
│        ├── prob1.py           <<< latex for problem1
│        ├── prob2.py           <<< latex for problem2
│        ├── prob3.py           <<< latex for problem3
│        ├── prob4.py           <<< latex for problem4
│        ├── prob5.py           <<< latex for problem5
│        └── prob6.py           <<< latex for problem6
│                               
└── lib
    ├── latex_lib.py             <<< classes for printing latex exams
    └── scantron_lib.py          <<< classes for reading scantron output


--------------------------------------------------------------------------

The help menu should produce something like this:

[ezacademic jtritz: scantron]$ ./grader.py -h
usage: grader.py [-h] -ifile IFILE -sid_col SID_COL -form_col FORM_COL
                 -ans_cols ANS_COLS [ANS_COLS ...] -sfile SFILE -cfile CFILE

Grades multiple form exams from scantron output with custom grading stategies.

arguments:
  -h, --help            show this help message and exit
  -ifile IFILE          csv file from scantron
  -sid_col SID_COL      student id column in ifile
  -form_col FORM_COL    exam form column in ifile
  -ans_cols ANS_COLS [ANS_COLS ...]
                        list of answer columns
  -sfile SFILE          python file with question and answer scrambling map
  -cfile CFILE          python file with credit/scoring map


--------------------------------------------------------------------------

Example output:

| who      | exam form | question | selection | question form A | selections form A | score |
| jwcrimms | A         | 1        | C         | 1               | [3]               | 0     |
| jwcrimms | A         | 2        | C         | 2               | [3]               | 0     |
| jwcrimms | A         | 3        | C         | 3               | [3]               | 0     |
| jwcrimms | A         | 4        | B         | 4               | [2]               | 0     |
| phzang   | B         | 1        | E         | 5               | [2]               | 0     |
| phzang   | B         | 2        | C         | 3               | [1]               | 6     |
| phzang   | B         | 3        | C         | 8               | [5]               | 0     |
| phzang   | B         | 4        | B         | 11              | [1]               | 6     |
| eeshatz  | C         | 1        | AB        | 3               | [2, 4]            | 0     |
| eeshatz  | C         | 2        | D         | 20              | [3]               | 0     |
| eeshatz  | C         | 3        | E         | 14              | [5]               | 0     |
| eeshatz  | C         | 4        | B         | 9               | [2]               | 0     |
| sadlakha | B         | 1        | D         | 5               | [5]               | 0     |
| sadlakha | B         | 2        | C         | 3               | [1]               | 6     |
| sadlakha | B         | 3        | C         | 8               | [5]               | 0     |
| sadlakha | B         | 4        | D         | 11              | [3]               | 0     |
| anuaekka | B         | 1        | CD        | 5               | [1, 5]            | 0     |
| anuaekka | B         | 2        | C         | 3               | [1]               | 6     |
| anuaekka | B         | 3        | C         | 8               | [5]               | 0     |
| anuaekka | B         | 4        | CD        | 11              | [2, 3]            | 0     |

--------------------------------------------------------------------------

[ezacademic jtritz: scantron]$ ./scrambler.py -h
usage: scrambler.py [-h] -pdir PDIR -versions VERSIONS -qmix {no,yes} -amix
                    {no,yes}

Creates scrambled exams from latex pieces with unscrambling keys/maps.

arguments:
  -h, --help          show this help message and exit
  -pdir PDIR          directory where python problem files are found
  -versions VERSIONS  number of versions to make
  -qmix {no,yes}      mix the questions
  -amix {no,yes}      mix the answers

find output inside pdir, for example:

└── scrambler
    └── example_probs
        ├── map_scramble.py
        ├── exam1.tex
        ├── exam2.tex
        ├── exam3.tex
        └── exam4.tex

