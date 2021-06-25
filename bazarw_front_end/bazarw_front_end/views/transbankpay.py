from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime as dt
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction

import random

def webpay_plus_create(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = request.GET.get('total')
    return_url = 'http://localhost:8000/' + 'commit-pay/'

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }
    print(create_request)
    response = Transaction.create(buy_order, session_id, amount, return_url) 
    print('response: {0}'.format(response))

    return render(request, 'send-pay.html', {'response': response, 'amount': amount})    
 
@csrf_exempt
def commitpay(request):
    print('commitpay')
    print("request: {}".format(request.POST))    
    token = request.POST.get('token_ws')
    response = Transaction.commit(token=token)
    print("response: {}".format(response)) 
    state = ''
    if response.status == 'AUTHORIZED':
        state = 'Aceptado'
    pay_type = ''
    if response.payment_type_code == 'VD':
        pay_type = 'Tarjeta de Débito'

    amount = int(response.amount)
    amount = f'{amount:,.0f}'.replace(',', '.')
    transaction_date = dt.datetime.strptime(response.transaction_date, '%Y-%m-%dT%H:%M:%S.%fZ')
    transaction_date = '{:%d-%m-%Y %H:%M:%S}'.format(transaction_date)
    transaction_detail = {  'card_number': response.card_detail.card_number,
                            'transaction_date': transaction_date,
                            'state': state,
                            'pay_type': pay_type,
                            'amount': amount,
                            'authorization_code': response.authorization_code,
                            'buy_order': response.buy_order,
                        }   
    return render(request, 'commit-pay.html', {'transaction_detail': transaction_detail})    
