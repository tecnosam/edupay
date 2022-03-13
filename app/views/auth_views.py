from app import flask_app

from app.models.student_models import Student
from app.models.busary_models import BusaryStaff

from app.all_fields import student_fields, staff_fields

from flask import render_template, request, flash, redirect, session, url_for
from flask_restful import marshal


@flask_app.route("/students/login", methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        matric = request.form.get('matric', '')
        pwd = request.form.get('pass', '')

        _student = Student.auth(matric, pwd)

        if _student is not None:

            if 'staff_data' in session:
                session.pop('staff_data')

            session['student_data'] = marshal(_student, student_fields)
            return redirect('/')

        flash("Invalid Matric no or password")

    return render_template('pages/student-login.html')

@flask_app.route("/staff/login", methods=['GET', 'POST'])
def staff_login():
    if request.method == 'POST':

        email = request.form.get('email', '')
        pwd = request.form.get('pwd', '')

        _staff = BusaryStaff.auth(email, pwd)

        if _staff is not None:

            if 'student_data' in session:
                session.pop('student_data')

            session['staff_data'] = marshal(_staff, staff_fields)

            return redirect('/receipts')

        flash("Invalid Authentication details")

    return render_template("pages/staff-login.html")

@flask_app.route('/change-password', methods=['POST'])
def change_pwd():
    password = request.form['pwd']

    if 'student_data' in session:

        _student: Student = Student.change_pwd(session['student_data']['id'], password)
        if _student is not None:
            session['student_data']['pwd'] = _student.pwd
            flash("Password changed successfully")
        else:
            flash("Error locating student data (NOT FOUND)")

    elif 'staff_data' in session:

        _staff: BusaryStaff = BusaryStaff.change_pwd(session['staff_data']['id'], password)

        if _staff is not None:
            session['staff_data']['pwd'] = _staff.pwd
            flash("Password changed successfully")
        else:
            flash("Error locating bursary staff data (NOT FOUND)")

    return redirect(url_for('index'))


@flask_app.route('/logout')
def logout():
    if 'student_data' in session:
        session.pop('student_data')
        return redirect(url_for('student_login'))
    if 'staff_data' in session:
        session.pop('staff_data')
        return redirect(url_for('staff_login'))

    return redirect('/')
