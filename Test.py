import requests
from rest_framework import status

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNDcwOTk3LCJpYXQiOjE3MjM0NzA2OTcsImp0aSI6ImI1MDQ3ODM2YWYwNTRhYjZhYzhhZGE4M2JmZWVhZGQ0IiwidXNlcl9pZCI6MX0.-8mVtypj6NkLJFCwMnRjb13HOfrKTvDhcas7XTxQ1R0"
}
try:
    endpoint = "http://127.0.0.1:8000/Admin/Student/"

    result = requests.get(endpoint, headers=headers)

    print(result.status_code)  
    print(result.json()) 
except Exception as e:
    print(e)