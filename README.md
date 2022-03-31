# Lambda-Slack-Integration-w-S3-Trigger
Invokes a lambda function when file is uploaded to S3 that posts message to Slack channel

## Description
Creates a new Slack application configured to a specific channel in a workspace. Activate incoming webhooks to allow POST message from external sources (AWS Lambda in this case). 
In AWS Console, create a lambda function with Python 3.9 and a role that has permissions to CloudWatch logs and S3 (read & write). The policy used in the role is AWSLambdaExecute.
In the function code, use urllib3 to send the POST request to the slack channel
