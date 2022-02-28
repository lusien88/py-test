import boto3

ecs = boto3.client('ecs')
response = ecs.create_cluster(
    clusterName='Fargate-cluster-ecs-stoic',
    tags=[
        {
            'key': 'env',
            'value': 'test'
        },
    ],
    capacityProviders=[
        'FARGATE',
    ],
)