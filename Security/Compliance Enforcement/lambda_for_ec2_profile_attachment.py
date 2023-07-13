"""
This lambda function reviews instance profiles and replaces them with default
"""

import json
import sys
import os
import boto3
import base64
from botocore.exceptions import ClientError
import logging

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2_client = boto3.client('ec2')

def lambda_handler(event, context):

    instance = event
    logger.info(instance)

    try:
        response = ec2_client.associate_iam_instance_profile(
            IamInstanceProfile={
                'Name': 'LabInstanceProfile'
            },
            InstanceId=instance
        )    
        logger.info(response)
        return {
            "compliance_type": "COMPLIANT",
            "annotation": "This resource is compliant with the rule."
        }    
    except Exception as exp:
        logger.exception(exp)
