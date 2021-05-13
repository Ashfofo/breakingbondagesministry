from paynow import Paynow


paynow = Paynow(
    '11987',
    '4dcf61fe-fb17-4b45-b18f-2b0d12963661',
    'http://google.com',
    'http://google.com'
)

print('stat')
payment = paynow.create_payment('Order', 'anesumukanya@gmail.com')

payment.add('Payment for stuff', 1)

response = paynow.send_mobile(payment, '0774233510', 'ecocash')
print(response)


if(response.success):
    poll_url = response.poll_url

    print("Poll Url: ", poll_url)

    status = paynow.check_transaction_status(poll_url)

    time.sleep(30)

    print("Payment Status: ", status.status)