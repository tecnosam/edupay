from app import flask_app
from app.models.student_models import Student
from app.all_fields import student_fields
from flask import render_template, request, flash, redirect, session
from flask_restful import marshal


@flask_app.route("/login", methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        matric = request.form.get('matric', '')
        pwd = request.form.get('pass', '')

        _student = Student.auth(matric, pwd)

        if _student is not None:
            session['student_data'] = marshal(_student, student_fields)
            return redirect('/')

        flash("Invalid Matric no or password")

    return render_template('pages/login.html')

@flask_app.route('/logout')
def logout():
    if 'student_data' in session:
        session.pop('student_data')
    return redirect('/')
