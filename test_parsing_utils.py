import unittest
from parsing_utils import *


class TestParsingUtils(unittest.TestCase):

    def test_is_a_question(self):
        self.assertTrue(is_a_question("q. this is a question"))
        self.assertTrue(is_a_question("Q. this is a question"))
        self.assertTrue(is_a_question("2. this is a question"))
        self.assertTrue(is_a_question("023. this is a question"))
        self.assertTrue(is_a_question("1. 023. this is a question"))
        self.assertFalse(is_a_question("A. this is not a question"))
        self.assertFalse(is_a_question("this is not a question"))

    def test_is_answer(self):
        self.assertTrue(is_answer("*(B) this is the answer"))
        self.assertTrue(is_answer("*B) this is the answer"))
        self.assertFalse(is_answer("N) this is not the answer"))

    def test_strip_choice_text(self):
        self.assertEqual(strip_choice_text("(A) this is an option"), "this is an option")
        self.assertEqual(strip_choice_text("*(A) this is an option"), "this is an option")
        self.assertEqual(strip_choice_text("*A) this is an option"), "this is an option")
        self.assertEqual(strip_choice_text("A) this is an option"), "this is an option")
        self.assertEqual(strip_choice_text("A) This is an option (this)"), "This is an option (this)")
        self.assertEqual(strip_choice_text("*(B) This is an option (A)"), "This is an option (A)")
        self.assertEqual(strip_choice_text("*This is an option"), "This is an option")

    def test_format_answer_choice(self):
        self.assertEqual(format_answer_choice("(A) this is an option", 1, 0), "(A)this is an option")
        self.assertEqual(format_answer_choice("*A) this is an option", 1, 0), "*(A)this is an option")
        self.assertEqual(format_answer_choice("(C) this is an option", 1, 2), "(C)this is an option")
        self.assertEqual(format_answer_choice("(E) this is an option", 2, 4, True, True), "E). this is an option")

    def test_q_roll_generator(self):
        self.assertEqual(q_roll_generator(20), "020")
        self.assertEqual(q_roll_generator(0), "000")
        self.assertEqual(q_roll_generator(1), "001")
        self.assertEqual(q_roll_generator(999), "999")

    def test_strip_stem_text(self):
        self.assertEqual(strip_stem_text("3. this question"), "this question")
        self.assertEqual(strip_stem_text("Q. this question"), "this question")
        self.assertEqual(strip_stem_text("22 . this question"), "this question")
        self.assertEqual(strip_stem_text("q. this question  "), "this question")
        self.assertEqual(strip_stem_text("q. this question.  "), "this question.")

    def test_format_question_stem(self):
        self.assertEqual(format_question_stem("this question", 1, 23), "1. 024. this question")
        self.assertEqual(format_question_stem("this question", 23, 23), "23. 046. this question")

