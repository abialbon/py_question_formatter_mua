from QuestionParser import QuestionParser
from parsing_utils import is_a_question


class DocumentParser:

    def __init__(self, file_path, options):
        # TODO: Catch exceptions
        self.filename = file_path
        self.q_count = 0
        self.options = options
        self.parse(open(file_path, 'r', encoding='utf-8-sig'))

    def parse(self, f_stream):
        while True:
            line = f_stream.readline()
            if is_a_question(line):
                self.q_count += 1
                QuestionParser(self, f_stream, line, self.q_count, self.options)
                break
            elif line == '\n':
                pass
            else:
                break
