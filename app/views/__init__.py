
from app.views.student_views import *
from app.views.auth_views import *
from app.views.busary_view import *


@flask_app.route('/')
def index():
    if 'student_data' in session:
        return redirect(url_for('orders'))
    
    elif 'staff_data' in session:
        return redirect(url_for('services'))

    return redirect(url_for('student_login'))

@flask_app.route('/staff')
def staff():
    if 'staff_data' in session:
        return redirect(url_for('index'))

    return redirect(url_for('staff_login'))

