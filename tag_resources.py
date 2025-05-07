import boto3
from resource_arns import resource_arn
# Initialize tagging client
client = boto3.client('resourcegroupstaggingapi')

# Tags to add/patch
tags_to_update = {
    'Environment': 'Production',
    'Owner': 'DevOps Team',
    'Project': 'CentralizedBackup'
}

# Patch tags for imported resources
response = client.tag_resources(
    ResourceARNList=resource_arn,
    Tags=tags_to_update
)

print("Tagging response:", response)
