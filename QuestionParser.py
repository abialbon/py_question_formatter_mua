class QuestionParser:

    def __init__(self, parser, f_in_stream, q_stem):
        self.parse(parser, f_in_stream, q_stem)

    def parse(self, parent_parser, f_in, stem):
        print(stem.strip())
        while True:
            line = f_in.readline()
            if line != '\n' and line != '':
                print(line.strip())
            else:
                print("\n", end="")
                parent_parser.parse(f_in)
                break
