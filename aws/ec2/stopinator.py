#!/usr/bin/env python

import boto3

# Connect to the Amazon EC2 service
ec2 = boto3.resource('ec2')

# Loop through each instance
for instance in ec2.instances.all():
  state = instance.state['Name']
  for tag in instance.tags:

    # Check for the 'stopinator' tag
    if tag['Key'] == 'stopinator':
      action = tag['Value'].lower()
      
      # Stop?
      if action == 'stop' and state == 'running':
        print "Stopping instance", instance.id
        instance.stop()
      
      # Terminate?
      elif action == 'terminate' and state != 'terminated':
        print "Terminating instance", instance.id
        instance.terminate()
