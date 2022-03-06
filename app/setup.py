from app.models.status_models import Status

neutral_status = ['PROCESSING', 'COLLECTED']
positive_status = ['APPROVED', 'READY']
negative_status = ['DISAPPROVED', 'CANCELLED']

def setup_status_rows():
    statuses = neutral_status + positive_status + negative_status

    for status in statuses:
        Status.add(status)

    return
