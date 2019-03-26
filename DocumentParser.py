from QuestionParser import QuestionParser


class DocumentParser:

    def __init__(self, file_path):
        # TODO: Catch exceptions
        self.filename = file_path
        self.parse(open(file_path))

    def parse(self, f_stream):
        while True:
            line = f_stream.readline()
            if line.startswith('Q') or line.startswith('q'):
                QuestionParser(self, f_stream, line)
                break
            elif line == '\n':
                pass
            else:
                break
