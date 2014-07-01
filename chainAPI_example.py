from chainAPI import *

print get_address('142zKLqjx7BsEQPnveWNNfDYeNfJZWK5KG')
print '-' * 50
print get_address_transactions('142zKLqjx7BsEQPnveWNNfDYeNfJZWK5KG')
print '-' * 50
unspent = get_unspent('142zKLqjx7BsEQPnveWNNfDYeNfJZWK5KG')
print unspent
print '-' * 50
for each_u in unspent:
    print each_u['transaction_hash']
    print '-' * 50
    print get_transaction_details(each_u['transaction_hash'])