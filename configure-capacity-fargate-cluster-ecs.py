import boto3

ecs = boto3.client('ecs')
response = ecs.create_capacity_provider(
    name='capacity-to-serverless-cluster',
    autoScalingGroupProvider={
        'autoScalingGroupArn': 'arn:aws:ecs:eu-west-3:111866276431:cluster/Fargate-cluster-ecs-stoic',
        'managedScaling': {
            'status': 'ENABLED',
        },
        'managedTerminationProtection': 'DISABLED'
    },
    tags=[
        {
            'key': 'env',
            'value': 'test'
        },
    ]
)