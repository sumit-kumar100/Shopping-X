 
from instamojo_wrapper import Instamojo

API_KEY = "test_00fdfd80a82bdae553372ec546b"
AUTH_TOKEN = "test_26343b0f40ae03f99bba48b3a58"

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

# Create a new Payment Request
response = api.payment_request_create(
    amount='3499',
    purpose='FIFA 16',
    send_email=True,
    email="foo@example.com",
    redirect_url="http://www.example.com/handle_redirect.py"
    )
# print the long URL of the payment request.
print(response['payment_request']['longurl'])