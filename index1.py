import requests
import random
import json
import hmac
import hashlib
import base64
import datetime

date = datetime.datetime.now()
year = date.strftime('%Y')
month = date.strftime('%m')
day = date.strftime('%d')
hour = date.strftime('%H')
minute = date.strftime('%M')
second = date.strftime('%S')
requestTime = year + '-' + month + '-' + day + 'T' + hour + ':' + minute + ':' + second

status = 'status codes as per table below'
timeToLiveSeconds = 300
merchantId = 'test'
orderId = random.randint(1000000, 9999999)
merchantReferenceId = 'wavemerchant-' + str(random.randint(1000000, 9999999))
frontendResultUrl = 'https://wave-merchant.com'
backendResultUrl = 'https://wave-merchant.com/backend-callback'
initiatorMsisdn = '9400002678'
amount = 50
paymentDescription = 'Purchase of Item X'
currency = "MMK"
transactionId = 360
paymentRequestId = 360
hashValue = "29e9486e727ac0e4f185c3b757cf8892e59eb8d292c23f11d13926bb0bdae798"
merchant_name = 'Wave Merchant'

secret_key = 'secret-key-from-wave-money'.encode()
message = ''.join([
    status,
    str(timeToLiveSeconds),
    merchantId,
    str(orderId),
    str(amount),
    backendResultUrl,
    merchantReferenceId,
    initiatorMsisdn,
    str(transactionId),
    str(paymentRequestId),
    requestTime
]).encode()
signature = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
hashValue = signature.decode()

myobj = {
    'status': status,
    'merchantId': merchantId,
    'orderId': orderId,
    'merchantReferenceId': merchantReferenceId,
    'frontendResultUrl': frontendResultUrl,
    'backendResultUrl': backendResultUrl,
    'initiatorMsisdn': initiatorMsisdn,
    'amount': amount,
    'timeToLiveSeconds': timeToLiveSeconds,
    'paymentDescription': paymentDescription,
    'currency': currency,
    'hashValue': hashValue,
    'transactionId': transactionId,
    'paymentRequestId': paymentRequestId,
    'requestTime': requestTime
}
jsonObj = json.dumps(myobj)

url = 'https://testpayments.wavemoney.io/authenticate?transaction_id=' + str(transactionId)

x = requests.post(url, json = jsonObj, headers = {"Type": "application/json"})
