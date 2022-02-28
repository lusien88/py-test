import boto3

#List clusters ECS existing on AWS
#Prerequisites:
# * In order to do that you need a ROLE on AWS granted to do this task

ecs = boto3.client('ecs')
response = ecs.list_clusters()
