import boto3

ecs = boto3.client('ecs')

response = ecs.create_task_set(
    service='nginx-service',
    cluster='Fargate-cluster-ecs-stoic',
    externalId='id-externe',
    taskDefinition='nginx-task',
    networkConfiguration={
        'awsvpcConfiguration': {
            'assignPublicIp': 'ENABLED',
            'subnets': [
                '10.0.0.2/16',
            ],            
        }
    },
    serviceRegistries=[
        {
            'registryArn': 'arn:aws:ecr-public::111866276431:registry/111866276431',
            'port': 80,
            'containerName': 'public.ecr.aws/x9h1o7p1/registry-alex:latest',
            'containerPort': 80
        },
    ],
    launchType='FARGATE',
    platformVersion='1',
    scale={
        'value': 2,
        'unit': 'PERCENT'
    },
    tags=[
        {
            'key': 'env',
            'value': 'test'
        },
    ]
)