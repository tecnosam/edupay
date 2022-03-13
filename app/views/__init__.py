
from app.views.student_views import *
from app.views.auth_views import *
from app.views.busary_view import *


@flask_app.route('/')
def index():
    if 'student_data' in session:
        return redirect(url_for('orders'))
    
    elif 'staff_data' in session:
        return redirect(url_for('products'))
    
    return redirect(url_for('student_login'))


