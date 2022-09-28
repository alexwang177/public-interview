import requests 
from requests.exceptions import HTTPError
from datetime import datetime
from dateutil import parser

'''
{'data': 
    [
        {
            'company': 'Brex', 
            'created_at': '2017-01-01T01:13:36Z', 
            'name': 'Pedro Franceschi'
        }, 
        {
            'company': 'Apple', 
            'created_at': '1976-04-01T01:13:36Z', 
            'name': 'Steve Jobs'
        }
    ]
}
'''

def test_request():

    try:
        res = requests.get('https://platform.brexapis.com/interview/test', params={"foo": "bar"}, headers={'Accept': 'application/json'})
        return res.json()
    except HTTPError as http_e:
        print(http_e)
    except Exception as e:
        print(e)

    # print("Headers:", res.headers)
    # print("Status code: ", res.status_code)
    # print("Content: ", res.content)
    # print("Text: ", res.text)
    # print("Request headers: ", res.request.headers)

def parse_iso_util(iso_str):
    return parser.isoparse(iso_str)

def parse_iso_native(iso_str):
    # datetime.strptime("2022-04-07T08:53:42.06717+02:00", "%Y-%m-%dT%H:%M:%S.%f%z")
    return datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S%z")

def parse_company(company):
    dt = parse_iso_native(company['created_at'])
    dt_formatted = dt.strftime("%A %B %d, %Y %I:%M %p")
    print(f"{company['company']} was founded by {company['name']} at time: {dt_formatted}")

def main():

    json_data = test_request()

    for company in json_data['data']:
        parse_company(company)

main()

