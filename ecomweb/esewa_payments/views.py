from django.shortcuts import render

# Create your views here.
import hmac
import hashlib
import uuid

def genSha256(key, message):
    key = key.encode('utf-8')
    message = message.encode('utf-8')

    hmac_sha256 = hmac.new(key, message, hashlib.sha256)
    digest = hmac_sha256.digest()

    secret_key = "8gBm/:&EnhH.1/q"
    data_to_sign = f"total_amount={total_amount},transaction_uuid={uid},product_code=EPAYTEST"

    result = genSha256(secret_key, data_to_sign)