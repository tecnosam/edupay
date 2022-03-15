from requests import get
from dotenv import load_dotenv
import os
from app.models.service_models import Service
from app.models.order_models import Order


load_dotenv()


def validate_payment(reference, service_id):

    url = f"https://api.paystack.co/transaction/verify/{reference}"

    secret = os.getenv('PAYSTACK_SECRET')
    headers = {"Authorization": f'Bearer {secret}'}

    response = get(url, headers=headers)

    if response.status_code != 200:
        return False
    
    data = response.json()['data']

    service = Service.query.get(service_id)

    if service is None:
        return False

    if (data['amount']/100 != service.price) or (data['status'] != 'success'):
        return False

    return True
