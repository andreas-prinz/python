#!/usr/bin/env python

import boto3

GROUP_NAME = "Bastion"

# Connect to the Amazon EC2 service
ec2 = boto3.resource('ec2')

# Retrieve the security group
security_groups = ec2.security_groups.filter(Filters=[{'Name':'group-name', 'Values':['Bastion']}])

# Delete all rules in the group
for group in security_groups:
    group.revoke_ingress(IpPermissions = group.ip_permissions)
