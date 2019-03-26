from parsing_utils import format_question_stem, format_answer_choice


class QuestionParser:

    def __init__(self, parser, f_in_stream, q_stem, q_count, options):
        self.parse(parser, f_in_stream, q_stem, q_count, options)

    def parse(self, parent_parser, f_in, stem, q_count, options):
        print(format_question_stem(stem, q_count, options['q_roll_start']))
        i = 0
        while True:
            line = f_in.readline()
            if line != '\n' and line != '':
                print(format_answer_choice(line, options['style_choice'], i, options['dot'], options['space']))
                i += 1
            else:
                print("\n", end="")
                parent_parser.parse(f_in)
                break
