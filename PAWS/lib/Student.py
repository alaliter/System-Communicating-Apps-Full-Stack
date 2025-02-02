from lib.Database import Database, dbl
import hashlib

class Student():
    """
    handles a student for PAWS system
    """
    def __init__(self, sid):
        self.sid = sid
        self.connection = Database.getconnection()

    def getdata(self):
        """
        returns viewable data of a student
        """
        with self.connection.cursor() as cur:
            try:
                cur.execute(f'SELECT email, fname, lname FROM student WHERE sid={self.sid}')
                #since only one student
                return cur.fetchone() 
            except (Exception, dbl.DatabaseError) as e:
                print(e)

    
    @staticmethod
    def student_list(dept):
        connection = Database.getconnection()
        with connection.cursor() as cur:
            try:
                cur.execute(f"SELECT * FROM student WHERE majordept LIKE '{dept}%'")
                return cur.fetchall()
            except (Exception, dbl.DatabaseError) as e:
                print(e)


    @staticmethod
    def enrollment_list(dept, term):
        connection = Database.getconnection()
        with connection.cursor() as cur:
            try:
                cur.execute(f"SELECT enroll.* FROM enroll INNER JOIN section ON(enroll.crn=section.crn) WHERE section.cprefix LIKE '{dept}%' and section.term='{term}'")
                return cur.fetchall()
            except (Exception, dbl.DatabaseError) as e:
                print(e)
