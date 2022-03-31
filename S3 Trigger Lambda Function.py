#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import urllib3
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    
    if event:
        print("event: ", event)
        file_obj = event["Records"][0]
        bucket_name = str(file_obj['s3']["bucket"]['name'])
        file_name = str(file_obj['s3']['object']['key'])
        print('Bucket: ', bucket_name)
        print('File Name: ', file_name)
    
    
    http = urllib3.PoolManager()
    
    data = {"text": "File Name: " + file_name + " URL: s3.amazonaws.com/" + bucket_name + "/" + file_name}
    
    r = http.request("POST", "https://hooks.slack.com/services/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",
                    body = json.dumps(data), 
                    headers = {"Content-Type": "application-json"})
                        
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

