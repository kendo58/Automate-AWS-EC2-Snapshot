from datetime import datetime
import boto3

# ISO 8601 timestamp, i.e. 2019-01-31T14:01:58
timestamp = datetime.now()

def lambda_handler(event, context):
    
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        for tag in instance.tags:
            if tag['Key'] == 'Name':
                Names = tag['Value']
                for volume in instance.volumes.all():
                    desc = 'Backup of {} instance, volume {} created on {}'.format(Names, volume.id, timestamp )
                    snapshot = volume.create_snapshot(Description=desc)
                    print('Created snapshot of', Names)
