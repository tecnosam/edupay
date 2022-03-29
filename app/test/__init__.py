from app.models.student_models import Student
from app.models.service_models import Service
from app.models.busary_models import BusaryStaff
from app import db
import sqlalchemy
import csv


def csv_load_wrapper(fn, table):

    with open(fn, 'r') as f:
        rows = f.readlines()
        rows.pop(0)  # remove header
        print("Table - ", table)
        for row in csv.reader(rows):
            load_test(row, table)
    
    return


tables = {'student': Student, 'staff': BusaryStaff, 'service': Service}

def load_test(row, table):
    try:
        tables[table].add(*row)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()


def load_all():
    csv_load_wrapper("app/test/services.csv", "service")
    csv_load_wrapper("app/test/students.csv", "student")
    csv_load_wrapper("app/test/staff.csv", "staff")
