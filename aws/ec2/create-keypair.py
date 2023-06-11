#!/usr/bin/env python

import boto3

# Connect to the Amazon EC2 service
ec2_client = boto3.client('ec2')

# Create a Key Pair
key = ec2_client.create_key_pair(KeyName = 'SDK')

# Print the private Fingerprint of the private key
print(key.get('KeyFingerprint'))
