from turtle import pd

import requests

response = requests.get(url='http://taf-env.eba-mef6maah.us-east-2.elasticbeanstalk.com/taf/util'
                            '/getEmailReportTableData?historyId=633')

response.raise_for_status()

data = response.json()
print(data)
