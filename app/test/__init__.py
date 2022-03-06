from app.models.student_models import Student
from app.models.product_models import Product
from app import db
import sqlalchemy
import csv


def csv_load_wrapper(fn, func):

    with open(fn, 'r') as f:
        rows = f.readlines()
        rows.pop(0)  # remove header
        for row in csv.reader(rows):
            func(row)
    
    return


def load_test_students(row):
    try:
        Student.add(*row)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()


def load_test_products(row):
    try:
        Product.add(*row)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()


def load_all():
    csv_load_wrapper("app/test/products.csv", load_test_products)
    csv_load_wrapper("app/test/students.csv", load_test_students)
