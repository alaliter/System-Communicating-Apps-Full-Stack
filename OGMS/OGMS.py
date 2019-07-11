from flask import Flask, request, render_template, session, redirect, Session
from flask.json import jsonify
from lib.Database import Database
from lib.Student import Student
from lib.Admin import Admin
from lib.Department import Department

import requests
import json

app = Flask(__name__)
sess = Session()

@app.route('/')
def index():
    return redirect('/home/')

@app.route('/home/')
def home():
    return 'hello world'

@app.route('/dummy', methods=['GET'])
def dummy_data():
  ####################### GET local data from PAWS database in ##################
    data = [{"sid":1009, "email":"varshi@gmail.com", "fname":"Varshi", "lname":"Abeysinghe", "majordept":"CSC", "gradassistant":"Y"}]
    return jsonify(data)

# @app.route('/request/<string:dept>', methods=['GET'])
# def request_accepted(dept):
#   ####################### TBD change 'dummy' to GET from PAWS database ##################
#     data = json.loads(requests.get(f"http://tinman.cs.gsu.edu:5001/students/{dept}/").content)
#     Admin.accepted_req(data)
#     return 'student added'
@app.route('/request/students', methods=['GET'])
def request_student_accepted():
        ####################### TBD change 'dummy' to GET from PAWS database ##################
        data = json.loads(requests.get(f"http://tinman.cs.gsu.edu:5001/students/CSC/").content)
        Admin.accepted_student_req(data)
        return jsonify(data)

@app.route('/request/courses', methods=['GET'])
def request_course_accepted():
  ####################### TBD change 'dummy' to GET from PAWS database ##################
    data = json.loads(requests.get(f"http://tinman.cs.gsu.edu:5001/courses/CSC/").content)
    Admin.accepted_course_req(data)
    return jsonify(data)

@app.route('/request/enrollments/<string:term>/', methods=['GET'])
def request_enrollment_accepted(term):
  ####################### TBD change 'dummy' to GET from PAWS database ##################
    data = json.loads(requests.get(f"http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/{term}/").content)
    Admin.accepted_enrollment_req(data)
    return jsonify(data)


############ copy to my ossistantship database
@app.route('/request/assistantship/<string:term>/', methods=['GET'])
def request_assistantship_accepted(term):
  ####################### TBD change 'dummy' to GET from PAWS database ##################
    data = json.loads(requests.get(f"http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/{term}/").content)
    Admin.accepted_assistantship_req(data)
    return jsonify(data)

########## No need #############
@app.route('/request/grades', methods=['GET'])
def request_grade_accepted():
  ####################### TBD change 'dummy' to GET from PAWS database ##################
    data = Admin.accepted_grade_req()
    return jsonify(data)

# @app.route('/students/<string:dept>/', methods=['GET'])
# def students_dept(dept):
#     return jsonify(Student.student_list(dept))

# @app.route('/courses/<string:dept>/', methods=['GET'])
# def course_dept(dept):
#     return jsonify(Department.getcourses(dept))

# @app.route('/students/enrolled/<string:dept>/<string:term>/', methods=['GET'])
# def enrollment(dept, term):
#     return jsonify(Student.enrollment_list(dept, term))

############change create assistantship to ######################
# @app.route('/request/assistantship/', methods=['POST'])
# def create_assistantship():
#     if request.form:
#         Admin.create_assistantship(request.form['sid'], request.form['term'], request.form['year'], request.form['assistantship'])
#         return "update successfull"
#     else:
#         return str(request.form)

# @app.route('/student/assistantship/<int:sid>/')
# def check_assistantship(sid):
#     assis =  Admin.check_assistantship(sid)
#     return jsonify(assis)
#     # add update assistantship
@app.route('/student/assistantship/', methods=['PATCH'])
def update_assistantship():
#    if request.form:
#        Admin.update_grade(request.form['sid'], request.form['grade'])
#        return "update successfull"
     Admin.update_assistantship(request.json.get('sid'), request.json.get('assistantship'))
     return "update successful."

@app.route('/student/assistantship/<int:sid>/', methods=['GET'])
def get_assistantship(sid):
    assis =  Admin.check_assistantship(sid)
    return jsonify(assis)

@app.route('/student/assistantships/', methods=['GET'])
def get_assistantships():
    data = json.loads(requests.get('http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/FA/').content)
    Admin.accepted_assistantship_req(data)
    data = json.loads(requests.get('http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/SU/').content)
    Admin.accepted_assistantship_req(data)
    data = json.loads(requests.get('http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/SP/').content)
    Admin.accepted_assistantship_req(data)
    assis =  Admin.check_assistantships()
    return jsonify(assis)

@app.route('/request/enrollments/grade/', methods=['PATCH', 'GET'])
def update_grade():
#    if request.form:
#       Admin.update_grade(request.form['sid'], request.form['grade'])
#        return "update successfull"
     if request.method == 'PATCH':
             Admin.update_grade(request.json['sid'], request.json['grade'], request.json['term'], request.json['year'], request.json['crn'])
             return "update successful."
     elif request.method == "GET":
             data = Admin.get_student_grade()
             return jsonify(data)

if __name__ =='__main__':
    app.secret_key = 'super secret key here gghalfndfacvdaewa'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='tinman.cs.gsu.edu', debug=True, port=5020)
    #app.run(host='localhost', debug=True)
