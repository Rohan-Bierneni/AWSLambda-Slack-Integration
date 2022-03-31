# Lambda-Slack-Integration
Two different types of integration with slack. 

First part integrates an S3 bucket to slack via lambda function. When file is uploaded to an S3 bucket, invokes a lambda function to post message to Slack channel with url included. 

Second part sends a message to Slack channel when CPU Utilization of an EC2 instance goes above threshhold.

## Description
### S3 Integration:
Creates a new Slack application configured to a specific channel in a workspace. Activate incoming webhooks to allow POST message from external sources (AWS Lambda in this case). 
In AWS Console, create a lambda function with Python 3.9 and a role that has permissions to CloudWatch logs and S3 (read & write). The policy used in the role is AWSLambdaExecute.
In the function code, use urllib3 to send the POST request to the slack channel.

### CloudWatch Alarms Integration
The CloudWatch Alarm pushes an SNS notification that invokes a lambda function as well as pushes message to email. The lambda function takes the json data from SNS and reformats to a structured message and POSTS to the Slack channel via incoming webhooks. 

## Visuals

<img width="812" alt="Screen Shot 2022-03-31 at 4 31 19 PM" src="https://user-images.githubusercontent.com/102715043/161166043-e1d3e2fc-cc9d-4602-9b59-6ce964e95f62.png">
<img width="793" alt="Screen Shot 2022-03-31 at 4 33 01 PM" src="https://user-images.githubusercontent.com/102715043/161166209-b8e2607d-d851-40b9-b229-4e6a43bfe7fb.png">
