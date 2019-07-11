import psycopg2 as pg

class Admin():
        """ 
        Handles administrative service
        """

        @staticmethod
        def check_assistantship(sid):
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        try:
                                sql = f"SELECT assistantship FROM oassistantship WHERE sid={sid}"
                                cur.execute(sql)
                                return cur.fetchone()
                        except (Exception, pg.DatabaseError) as e:
                                print(e)

########## add a method to fetch all assistantship###########
###     @staticmethod
        def check_assistantships():
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        try:
                                sql = f"SELECT * FROM oassistantship"
                                cur.execute(sql)
                                rows = cur.fetchall()
                                rets = []
                                for row in rows:
                                        columns = ['sid','term','year','assistantship']
                                        ret = dict(zip(columns, row))
                                        rets.append(ret)
                                return rets
                        except (Exception, pg.DatabaseError) as e:
                                print(e)
      
        @staticmethod
        def accepted_student_req(alldata):
                """
                gets the accepted students into database
                """
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        for data in alldata:
                                try:
                                        sql = f"INSERT INTO ostudent (sid, fname, lname) VALUES({data['sid']}, '{data['fname']}', '{data['lname']}')"
                                        cur.execute(sql)
                                        connection.commit()
                                except (Exception, pg.DatabaseError) as e:
                                        connection.rollback()
                                        print(e)

########### get courses ##############
        @staticmethod
        def accepted_course_req(alldata):
                """
                gets the accepted students into database
                """
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        for data in alldata:
                                try:
                                        sql = f"INSERT INTO ocourse (cprefix, cno, ctitle, hours) VALUES('CSC', {data['cno']}, '{data['ctitle']}', {data['chours']})"
                                        cur.execute(sql)
                                        connection.commit()
                                except (Exception, pg.DatabaseError) as e:
                                        connection.rollback()
                                        print(e)

########### get enrollment ##############
        @staticmethod
        def accepted_enrollment_req(alldata):
                """
                gets the accepted students into database
                """
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        for data in alldata:
                                try:
                                        sql = f"INSERT INTO oenroll (cprefix,sid, term, year, crn) VALUES('CSC', {data['sid']}, '{data['term']}', {data['year']}, {data['crn']})"
                                        cur.execute(sql)
                                        connection.commit()
                                except (Exception, pg.DatabaseError) as e:
                                        connection.rollback()
                                        print(e)

########### copy enrollment to assistantship ##############
        @staticmethod
        def accepted_assistantship_req(alldata):
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        for data in alldata:
                                try:
                                        sql = f"INSERT INTO oassistantship (sid, term, year, assistantship) VALUES({data['sid']}, '{data['term']}', {data['year']}, 'N')"
                                        cur.execute(sql)
                                        connection.commit()
                                except (Exception, pg.DatabaseError) as e:
                                        connection.rollback()
                                        print(e)

#### update assistantship ##############
        @staticmethod
        def update_assistantship(sid, assistantship):
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        try:
                                sql = f"UPDATE oassistantship SET assistantship='{assistantship}' WHERE sid={sid}"
                                cur.execute(sql)
                                connection.commit()
                        except (Exception, pg.DatabaseError) as e:
                                connection.rollback()
                                print(e)

########### update grade ##############
        @staticmethod
        def update_grade(sid, grade, term, year, crn):
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        try:
                                sql = f"UPDATE oenroll SET grade='{grade}' WHERE sid={sid} AND term='{term}' AND year={year} AND CRN={crn}"
                                cur.execute(sql)
                                connection.commit()
                        except (Exception, pg.DatabaseError) as e:
                                connection.rollback()
                                print(e)
        @staticmethod
        def get_student_grade():
                connection = pg.connect(dbname='llin15', user='llin15')
                with connection.cursor() as cur:
                        try:
                                sql = f"SELECT * FROM oenroll"
                                cur.execute(sql)
                                rows = cur.fetchall()
                                rets = []
                                for row in rows:
                                        columns = ['sid','term','year','cprefix', 'grade', 'crn']
                                        ret = dict(zip(columns, row))
                                        rets.append(ret)
                                return rets
                        except (Exception, pg.DatabaseError) as e:
                                print(e)
