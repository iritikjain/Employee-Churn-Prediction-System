import os
import json
import urllib.request
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("endpoint")
key = os.getenv("key")

def predict(satisfaction,evaluation,project,hours,time,accident,promotion,department,sal):
    satisfaction=float(satisfaction)/100
    evaluation=float(evaluation)/100
    data = {
        "Inputs": {
            "WebServiceInput0":
                [
                    {
                        'satisfaction_level': satisfaction,
                        'last_evaluation': evaluation,
                        'number_project': project,
                        'average_monthly_hours': hours,
                        'time_spend_company': time,
                        'work_accident': accident,
                        'promotion_last_5years': promotion,
                        'dept': department,
                        'salary': sal,
                    },
                ],
        },
        "GlobalParameters":  {
        }
    }

    body = str.encode(json.dumps(data))

    headers = {'Content-Type': 'application/json',
                 'Authorization': ('Bearer ' + key)}

    req = urllib.request.Request(endpoint, body, headers)

    try:
            response = urllib.request.urlopen(req)
            result = response.read()
            json_result = json.loads(result)
            output = json_result["Results"]["WebServiceOutput1"][0]
            results = int(output["Employee Churn Prediction"])
            return results

    except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))
