# Unit tests for university classes

import unittest
import university

class TestUniversity(unittest.TestCase):

	# @classmethod
	# def setUpClass(cls):
	# 	print('setUpClass')

	# @classmethod
	# def tearDownClass(cls):
	# 	print('tearDownClass')

	def setUp(self):
		print('setUp')
		self.professor = university.Professor("Ryan", "Reynolds", "deptul@yahoo.com", 42)
		self.subject = university.Subject(name = "Acting in Romantic Comedies", 
			professor = self.professor, 
			room = 666, 
			day = "Friday",
			time = "16:20",
			exam = True)

	# def tearDown(self):
	# 	print('tearDown')

	def test_subject_professor(self):
		self.assertIsInstance(self.subject.professor, university.Professor)
		self.assertIs(self.subject.professor, self.professor)

	def test_professor_fullname(self):
		self.assertEqual(self.professor.fullname, "Ryan Reynolds")
		self.assertEqual(self.subject.professor.fullname, "Ryan Reynolds")

	def test_subject_properties(self):
		self.assertEqual(self.subject.schedule,
			"Class takes place Friday at 16:20.")
		self.assertEqual(self.subject.isExam, 
			"This subject has an exam.")
		self.assertEqual(self.subject.professorContactInfo, 
			"Ryan Reynolds, email: deptul@yahoo.com, room: 42")

	def test_changeRoom(self):
		self.assertEqual(self.subject.room, 666)
		self.subject.changeRoom(777)
		self.assertEqual(self.subject.room, 777)
		
		
if __name__ == '__main__':
	unittest.main()