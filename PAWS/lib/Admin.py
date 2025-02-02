import psycopg2 as pg

class Admin():
	""" 
	Handles administrative service
	"""

	@staticmethod
	def accepted_student_req(alldata):
		"""
		gets the accepted students into database
		"""
		connection = pg.connect(dbname='lina_sample_db_project', user='lina')
		with connection.cursor() as cur:
			for data in alldata:
				try:
					sql = f"INSERT INTO ostudent (sid, fname, lname) VALUES('{data[0]}', '{data[3]}', '{data[4]}')"
					cur.execute(sql)
					connection.commit()
				except (Exception, pg.DatabaseError) as e:
					connection.rollback()
					print(e)

########### get courses ##############
	def accepted_course_req(alldata):
		"""
		gets the accepted students into database
		"""
		connection = pg.connect(dbname='lina_sample_db_project', user='lina')
		with connection.cursor() as cur:
			for data in alldata:
				try:
					sql = f"INSERT INTO ostudent (cno, ctitle, chours) VALUES('{data[1]}', '{data[2]}', '{data[3]}')"
					cur.execute(sql)
					connection.commit()
				except (Exception, pg.DatabaseError) as e:
					connection.rollback()
					print(e)
########### get enrollment ##############
	def request_enrollment_accepted(alldata):
		"""
		gets the accepted students into database
		"""
		connection = pg.connect(dbname='lina_sample_db_project', user='lina')
		with connection.cursor() as cur:
			for data in alldata:
				try:
					sql = f"INSERT INTO ostudent (sid, term, year, crn, grade) VALUES('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')"
					cur.execute(sql)
					connection.commit()
				except (Exception, pg.DatabaseError) as e:
					connection.rollback()
					print(e)


########### get grade ##############
	def accepted_grade_req(alldata):
		"""
		gets the accepted students into database
		"""
		connection = pg.connect(dbname='lina_sample_db_project', user='lina')
		with connection.cursor() as cur:
			for data in alldata:
				try:
					sql = f"INSERT INTO ograde (sid, fname, lname) VALUES({data[0]}, '{data[1]}', '{data[2]}')"
					cur.execute(sql)
					connection.commit()
				except (Exception, pg.DatabaseError) as e:
					connection.rollback()
					print(e)


	@staticmethod
	def update_update_assistantship(sid, term, year, crn, update_assistantship):
		"""
		update a grade of a given student
		"""
		connection = pg.connect(dbname='lina_sample_db_project', user='lina')
		with connection.cursor() as cur:
			try:
				sql = f"UPDATE enroll SET update_assistantship='{update_assistantship}' WHERE sid={sid} AND term='{term}' AND year={year} AND crn={crn}"
				cur.execute(sql)
				connection.commit()
			except (Exception, pg.DatabaseError) as e:
				connection.rollback()
				print(e)

	@staticmethod
	def update_grade(sid, term, year, crn, grade):
		"""
		update a grade of a given student
		"""
		connection = pg.connect(dbname='lina_sample_db_project', user='lina')
		with connection.cursor() as cur:
			try:
				sql = f"UPDATE enroll SET grade='{grade}' WHERE sid={sid} AND term='{term}' AND year={year} AND crn={crn}"
				cur.execute(sql)
				connection.commit()
			except (Exception, pg.DatabaseError) as e:
				connection.rollback()
				print(e)

