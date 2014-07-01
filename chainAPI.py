import random, os, json, sys
import requests

API_KEY = 'Enter API key here'
BASE_URL = 'https://%s@api.chain.com/v1/bitcoin/' % API_KEY

def send_request(endpoint):
    url = "%s/%s" % (BASE_URL,endpoint)
    response = requests.get(url,auth=(API_KEY, ''))
    return response.json()
    

def get_address(address):
    endpoint = 'addresses/%s' % (address)
    res = send_request(endpoint)
    return res

def get_address_transactions(address,limit=50):
    endpoint = 'addresses/%s/transactions?limit=%d' % (address,limit)
    res = send_request(endpoint)
    return res

def get_unspent(address):
    endpoint = 'addresses/%s/unspents' % (address)
    res = send_request(endpoint)
    return res


def get_transaction_details(txid):
    endpoint = 'transactions/%s' % (txid)
    res = send_request(endpoint)
    return res


def pushtx(txn):
    endpoint = 'transactions' % (txn)
    res = send_request(endpoint)
    return res
