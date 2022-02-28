import boto3

ecs = boto3.client('ecs')
response = ecs.delete_cluster(
    cluster='Fargate-cluster-ecs-stoic'
)