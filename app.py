import os
api_key = os.getenv('API_KEY')
print('Application Started')
if api_key:
    print('API Key Found')
else:
    print('API Key Missing')
