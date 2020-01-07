# Defining classes related to the university

class Professor:

	def __init__(self, firstname, lastname, email, room):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.room = room

	@property
	def fullname(self):
		return "{} {}".format(self.firstname, self.lastname)
	

class Subject:

	def __init__(self, name, professor, room, day, time, exam):
		self.name = name
		self.professor = professor
		self.room = room
		self.day = day
		self.time = time
		self.exam = exam

	@property
	def schedule(self):
		return "Class takes place {} at {}.".format(self.day, self.time)

	@property
	def isExam(self):
		if self.exam: return "This subject has an exam."
		else: return "This subject doesn't have an exam."

	@property
	def professorContactInfo(self):
		return "{}, email: {}, room: {}".format(self.professor.fullname, 
			self.professor.email, self.professor.room)

	def changeRoom(self, new_room):
		self.room = new_room
	