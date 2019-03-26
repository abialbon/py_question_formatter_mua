import re

style_1 = ['(A)', '(B)', '(C)', '(D)', '(E)',
           '(F)', '(G)', '(H)', '(I)', '(J)',
           '(K)', '(L)', '(M)', '(N)', '(O)',
           '(P)', '(Q)', '(R)', '(S)', '(T)',
           '(U)', '(V)', '(W)', '(X)', '(Y)',
           '(Z)'
           ]

style_2 = ['A)', 'B)', 'C)', 'D)', 'E)',
           'F)', 'G)', 'H)', 'I)', 'J)',
           'K)', 'L)', 'M)', 'N)', 'O)',
           'P)', 'Q)', 'R)', 'S)', 'T)',
           'U)', 'V)', 'W)', 'X)', 'Y)',
           'Z)'
           ]


def is_a_question(line):
    indicator = line.split('.')[0].strip()
    if indicator.lower() == 'q':
        return True
    try:
        if int(indicator) > 0:
            return True
    except ValueError:
        return False
    return False


def is_answer(line):
    if line[0] == '*':
        return True
    else:
        return False


def strip_choice_text(line):
    p = r'\A\*?\(?.?\)+\.?'
    strip_text = re.sub(p, '', line, count=1).strip()
    return strip_text


def format_answer_choice(line, style_choice, option_number, dot=False, space=False):
    answer = '*' if is_answer(line) else ''
    style_choice = str(style_choice)
    choice_indicator = eval('style_' + style_choice)[option_number]
    dot_needed = '.' if dot else ''
    space_needed = ' ' if space else ''
    choice_text = strip_choice_text(line)
    f_ans = "{is_answer}{choice_indicator}{dot_needed}{space_needed}{choice_text}"
    return f_ans.format(is_answer=answer,
                        choice_indicator=choice_indicator,
                        dot_needed=dot_needed,
                        space_needed=space_needed,
                        choice_text=choice_text)


def q_roll_generator(n):
    return "{:03d}".format(n)


def strip_stem_text(line):
    p = r'\A.+\.{1}'
    strip_text = re.sub(p, '', line, count=1).strip()
    return strip_text


def format_question_stem(line, q_no, q_roll):
    stem_text = strip_stem_text(line)
    f_q_roll = q_roll_generator(q_roll)
    f_stem = "{question_no}. {question_roll}. {stem_text}"
    return f_stem.format(question_no=q_no,
                         question_roll=f_q_roll,
                         stem_text=stem_text)
