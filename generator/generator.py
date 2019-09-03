import sys
import yaml
import json

def main():
    filename=sys.argv[1]
    print('Using parameter file: ' + filename)
    with open(filename, 'r') as stream:
        parameters = yaml.load(stream)
    print('Parameters: ' + str(parameters))

    template={
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": "AWS Deployment for Couchbase Enterprise",
        "Parameters": {
            "Username": {
                "Description": "Username for Couchbase administrator",
                "Type": "String"
            },
            "Password": {
                "Description": "Password for Couchbase administrator",
                "Type": "String",
                "NoEcho": True
            },
            "KeyName": {
                "Description": "Name of an existing EC2 KeyPair",
                "Type": "AWS::EC2::KeyPair::KeyName"
            }
        },
        "Mappings": {},
        "Resources": {}
    }

    serverVersion = parameters['serverVersion']
    syncGatewayVersion = parameters['syncGatewayVersion']
    cluster = parameters['cluster']

    template['Mappings'] = dict(template['Mappings'].items() + generateMappings().items())
    template['Resources'] = dict(template['Resources'].items() + generateMiscResources().items())
    template['Resources'] = dict(template['Resources'].items() + generateCluster(serverVersion, syncGatewayVersion, cluster).items())

    file = open('generated.template', 'w')
    file.write(json.dumps(template, sort_keys=True, indent=4, separators=(',', ': ')) + '\n')
    file.close()

def generateMappings():
      mappings = {  
        "CouchbaseServer":{  
            "ap-northeast-1":{  
                "BYOL":"ami-220376cf",
                "HourlyPricing":"ami-0f1f6ae2",
                "PrivateBYOL":"ami-09c8329c892efd3a4",
                "PrivateHourlyGold":"ami-0c0bc36ce1e451daf",
                "PrivateHourlyPlat":"ami-04030f1c6aed4a066"
            },
            "ap-northeast-2":{  
                "BYOL":"ami-b9893ed7",
                "HourlyPricing":"ami-8f8b3ce1",
                "PrivateBYOL":"ami-007a1600d278ba81a",
                "PrivateHourlyGold":"ami-022649a13b10b33ac",
                "PrivateHourlyPlat":"ami-03979fdd0236623c7"
            },
            "ap-south-1":{  
                "BYOL":"ami-658bb80a",
                "HourlyPricing":"ami-4e8fbc21",
                "PrivateBYOL":"ami-074cec37a6eb7cf0d",
                "PrivateHourlyGold":"ami-08209daec2fddc10e",
                "PrivateHourlyPlat":"ami-0964815bfdaa6777b"
            },
            "ap-southeast-1":{  
                "BYOL":"ami-8f85c265",
                "HourlyPricing":"ami-ce7b3c24",
                "PrivateBYOL":"ami-0dd139097e52846a2",
                "PrivateHourlyGold":"ami-06a0eab08bf25919e",
                "PrivateHourlyPlat":"ami-0c015b73d118d05a3"
            },
            "ap-southeast-2":{  
                "BYOL":"ami-953394f7",
                "HourlyPricing":"ami-cb298ea9",
                "PrivateBYOL":"ami-02357aff956a327b2",
                "PrivateHourlyGold":"ami-0ea48c87250b17e6f",
                "PrivateHourlyPlat":"ami-030ca7f3d0a4e9414"
            },
            "ca-central-1":{  
                "BYOL":"ami-92911cf6",
                "HourlyPricing":"ami-acaa27c8",
                "PrivateBYOL":"ami-06aa8345e3431af5b",
                "PrivateHourlyGold":"ami-0b3d92624e06e92db",
                "PrivateHourlyPlat":"ami-0e044a4cec664dbfc"
            },
            "eu-central-1":{  
                "BYOL":"ami-310201da",
                "HourlyPricing":"ami-3c7f7cd7",
                "PrivateBYOL":"ami-0c13f646fa1825554",
                "PrivateHourlyGold":"ami-07e63fc84e3cb0af3",
                "PrivateHourlyPlat":"ami-06bf51c3bc7be03ff"
            },
            "eu-west-1":{  
                "BYOL":"ami-3a7f64d0",
                "HourlyPricing":"ami-3c7f64d6",
                "PrivateBYOL":"ami-05ceb8de8f7e83c22",
                "PrivateHourlyGold":"ami-08b304d565d60788f",
                "PrivateHourlyPlat":"ami-053d4f39839c01cbb"
            },
            "eu-west-2":{  
                "BYOL":"ami-69ed070e",
                "HourlyPricing":"ami-48ea002f",
                "PrivateBYOL":"ami-0aaaef8ceb67a1a8a",
                "PrivateHourlyGold":"ami-0209ce30de6035dd0",
                "PrivateHourlyPlat":"ami-01e39d363307878ea"
            },
            "eu-west-3":{  
                "BYOL":"ami-9d8d3de0",
                "HourlyPricing":"ami-718f3f0c",
                "PrivateBYOL":"ami-0e8607978d272c693",
                "PrivateHourlyGold":"ami-089cce539024535e2",
                "PrivateHourlyPlat":"ami-04e5ae0c5576faaf2"
            },
            "sa-east-1":{  
                "BYOL":"ami-3e290852",
                "HourlyPricing":"ami-4151702d",
                "PrivateBYOL":"ami-086794c41a1eb31b9",
                "PrivateHourlyGold":"ami-0be2e1121d504b803",
                "PrivateHourlyPlat":"ami-0e5701affc2f066a2"
            },
            "us-east-1":{  
                "BYOL":"ami-40dcdf3f",
                "HourlyPricing":"ami-49e7e436",
                "PrivateBYOL":"ami-0f0cbdf64dac60912",
                "PrivateHourlyGold":"ami-03577010f4a21dfc1",
                "PrivateHourlyPlat":"ami-0265a23a6b334304c"
            },
            "us-east-2":{  
                "BYOL":"ami-99271dfc",
                "HourlyPricing":"ami-17271d72",
                "PrivateBYOL":"ami-08b217b8db1bb14f3",
                "PrivateHourlyGold":"ami-0aa9bc591250e6927",
                "PrivateHourlyPlat":"ami-03977a740555bf8ab"
            },
            "us-west-1":{  
                "BYOL":"ami-f5d13c96",
                "HourlyPricing":"ami-edd03d8e",
                "PrivateBYOL":"ami-0fb65c398310a0736",
                "PrivateHourlyGold":"ami-0fa8ad0dc9876b314",
                "PrivateHourlyPlat":"ami-0f0ede7fd152a93e2"
            },
            "us-west-2":{  
                "BYOL":"ami-70ca9408",
                "HourlyPricing":"ami-53ce902b",
                "PrivateBYOL":"ami-0ec331c14c38a4ae8",
                "PrivateHourlyGold":"ami-079b12a3f3173c3f2",
                "PrivateHourlyPlat":"ami-0cb1125d99968b8df"
            }
            }, 
        "CouchbaseSyncGateway":{  
            "ap-northeast-1":{  
                "BYOL":"ami-0b0174e6",
                "HourlyPricing":"ami-410b7eac",
                "PrivateBYOL":"ami-00142db2a4f18a091",
                "PrivateHourlyGold":"ami-0589e6f99c60e98dd",
                "PrivateHourlyPlat":"ami-09943a2b5dd01e50d"
            },
            "ap-northeast-2":{  
                "BYOL":"ami-ca8631a4",
                "HourlyPricing":"ami-37823559",
                "PrivateBYOL":"ami-0fc588e3c1d556971",
                "PrivateHourlyGold":"ami-0f12f12bd800f6562",
                "PrivateHourlyPlat":"ami-004cfbbd2265ea41a"
            },
            "ap-south-1":{  
                "BYOL":"ami-628bb80d",
                "HourlyPricing":"ami-4174462e",
                "PrivateBYOL":"ami-0f2fe809a9abece67",
                "PrivateHourlyGold":"ami-0e0ea2f0a58a01d98",
                "PrivateHourlyPlat":"ami-0d7e5b8ef15e1635d"
            },
            "ap-southeast-1":{  
                "BYOL":"ami-be7a3d54",
                "HourlyPricing":"ami-0a783fe0",
                "PrivateBYOL":"ami-0d666045b0dc3afa2",
                "PrivateHourlyGold":"ami-082d6f57bb9227fb7",
                "PrivateHourlyPlat":"ami-0d2a40fd679e1d368"
            },
            "ap-southeast-2":{  
                "BYOL":"ami-5833943a",
                "HourlyPricing":"ami-49288f2b",
                "PrivateBYOL":"ami-0a390aa0802353893",
                "PrivateHourlyGold":"ami-06bef34e9cfc712f1",
                "PrivateHourlyPlat":"ami-07f4a6a91413737ef"
            },
            "ca-central-1":{  
                "BYOL":"ami-13aa2777",
                "HourlyPricing":"ami-adaa27c9",
                "PrivateBYOL":"ami-06f7563110ac99a4e",
                "PrivateHourlyGold":"ami-0c42c043171159bab",
                "PrivateHourlyPlat":"ami-010d9004e963ea053"
            },
            "eu-central-1":{  
                "BYOL":"ami-7e070495",
                "HourlyPricing":"ami-3e7f7cd5",
                "PrivateBYOL":"ami-076d4930127526263",
                "PrivateHourlyGold":"ami-0bb9acb88d567a1ec",
                "PrivateHourlyPlat":"ami-03e73d94cc8e3c657"
            },
            "eu-west-1":{  
                "BYOL":"ami-836a7169",
                "HourlyPricing":"ami-8a170c60",
                "PrivateBYOL":"ami-0a44b20a65c7ae3c4",
                "PrivateHourlyGold":"ami-0fb8b03df4553d6ff",
                "PrivateHourlyPlat":"ami-090053756a1cb9e3d"
            },
            "eu-west-2":{  
                "BYOL":"ami-49ea002e",
                "HourlyPricing":"ami-d3eb01b4",
                "PrivateBYOL":"ami-0974d474cbefec841",
                "PrivateHourlyGold":"ami-0ff4d2f16077fb9fd",
                "PrivateHourlyPlat":"ami-0ac0cb9136be7092a"
            },
            "eu-west-3":{  
                "BYOL":"ami-9e8d3de3",
                "HourlyPricing":"ami-9f8d3de2",
                "PrivateBYOL":"ami-0bdb4dab356e43438",
                "PrivateHourlyGold":"ami-0bef1a36c3ac8d560",
                "PrivateHourlyPlat":"ami-034d54c2f686d384c"
            },
            "sa-east-1":{  
                "BYOL":"ami-14577678",
                "HourlyPricing":"ami-457a5b29",
                "PrivateBYOL":"ami-021dec08d0008bb83",
                "PrivateHourlyGold":"ami-0fd589dc9ec12fb5b",
                "PrivateHourlyPlat":"ami-036c3f608a9d55f93"
            },
            "us-east-1":{  
                "BYOL":"ami-f6e3e089",
                "HourlyPricing":"ami-2ce5e653",
                "PrivateBYOL":"ami-0e703c6d1f3e6e249",
                "PrivateHourlyGold":"ami-07913f4d354ecd472",
                "PrivateHourlyPlat":"ami-0bb39f184d87a1a17"
            },
            "us-east-2":{  
                "BYOL":"ami-10271d75",
                "HourlyPricing":"ami-bf251fda",
                "PrivateBYOL":"ami-0bbb19a0c0de97823",
                "PrivateHourlyGold":"ami-01bdb4c377a24a53b",
                "PrivateHourlyPlat":"ami-039ac453fbac58d5d"
            },
            "us-west-1":{  
                "BYOL":"ami-f4d13c97",
                "HourlyPricing":"ami-cbd13ca8",
                "PrivateBYOL":"ami-052024155dc3f7155",
                "PrivateHourlyGold":"ami-05587fe828189f355",
                "PrivateHourlyPlat":"ami-0d2454b76648a4127"
            },
            "us-west-2":{  
                "BYOL":"ami-dfcc92a7",
                "HourlyPricing":"ami-ddcc92a5",
                "PrivateBYOL":"ami-016143aba59553fe5",
                "PrivateHourlyGold":"ami-093ff23c63a9c670c",
                "PrivateHourlyPlat":"ami-08df627e3135466da"
            }
        }
    }
    return mappings

def generateMiscResources():
    resources = {
        "CouchbaseInstanceProfile": {
            "Type": "AWS::IAM::InstanceProfile",
            "Properties": {"Roles": [{"Ref": "CouchbaseRole"}]}
        },
        "CouchbaseRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Effect": "Allow",
                        "Principal": {"Service": ["ec2.amazonaws.com"]},
                        "Action": ["sts:AssumeRole"]
                    }]
                },
                "Policies": [{
                    "PolicyName": "CouchbasePolicy",
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [{
                            "Effect": "Allow",
                            "Action": [
                                "ec2:CreateTags",
                                "ec2:DescribeTags",
                                "ec2:DescribeInstances",
                                "autoscaling:DescribeAutoScalingGroups"
                            ],
                            "Resource": "*"
                        }]
                    }
                }]
            }
        },
        "CouchbaseSecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription" : "Enable SSH and Couchbase Ports",
                "SecurityGroupIngress": [
                    { "IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 4369, "ToPort": 4369, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 4984, "ToPort": 4985, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 8091, "ToPort": 8096, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 9100, "ToPort": 9105, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 9110, "ToPort": 9122, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 9998, "ToPort": 9999, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 11207, "ToPort": 11215, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 18091, "ToPort": 18096, "CidrIp": "0.0.0.0/0" },
                    { "IpProtocol": "tcp", "FromPort": 21100, "ToPort": 21299, "CidrIp": "0.0.0.0/0" }
                ]
            }
        }
    }
    return resources

def generateCluster(serverVersion, syncGatewayVersion, cluster):
    resources = {}
    rallyAutoScalingGroup=cluster[0]['group']
    for group in cluster:
        groupResources=generateGroup(serverVersion, syncGatewayVersion, group, rallyAutoScalingGroup)
        resources = dict(resources.items() + groupResources.items())
    return resources

def generateGroup(serverVersion, syncGatewayVersion, group, rallyAutoScalingGroup):
    resources = {}
    license=group['license']
    if 'syncGateway' in group['services']:
        resources = dict(resources.items() + generateSyncGateway(license, syncGatewayVersion, group, rallyAutoScalingGroup).items())
    else:
        resources = dict(resources.items() + generateServer(license, serverVersion, group, rallyAutoScalingGroup).items())
    return resources

def generateSyncGateway(license, syncGatewayVersion, group, rallyAutoScalingGroup):
    groupName = group['group']
    nodeCount = group['nodeCount']
    nodeType = group['nodeType']

    resources = {
        groupName + "AutoScalingGroup": {
            "Type": "AWS::AutoScaling::AutoScalingGroup",
            "Properties": {
                "AvailabilityZones": { "Fn::GetAZs": "" },
                "LaunchConfigurationName": { "Ref": groupName + "LaunchConfiguration" },
                "MinSize": 0,
                "MaxSize": 100,
                "DesiredCapacity": nodeCount
            }
        },
        groupName + "LaunchConfiguration": {
            "Type": "AWS::AutoScaling::LaunchConfiguration",
            "Properties": {
                "ImageId": { "Fn::FindInMap": [ "CouchbaseSyncGateway", { "Ref": "AWS::Region" }, license ] },
                "InstanceType": nodeType,
                "SecurityGroups": [ { "Ref": "CouchbaseSecurityGroup" } ],
                "KeyName": { "Ref": "KeyName" },
                "EbsOptimized": True,
                "IamInstanceProfile": { "Ref": "CouchbaseInstanceProfile" },
                "BlockDeviceMappings":
                [
                    {
                        "DeviceName" : "/dev/xvda",
                        "Ebs" : { "DeleteOnTermination" : True }
                    }
                ],
                "UserData": {
                    "Fn::Base64": {
                        "Fn::Join": [ "", [
                            "#!/bin/bash\n",
                            "echo 'Running startup script...'\n",
                            "stackName=", { "Ref": "AWS::StackName" }, "\n",
                            "syncGatewayVersion=" + syncGatewayVersion + "\n",
                            "baseURL=https://raw.githubusercontent.com/couchbase-partners/amazon-cloud-formation-couchbase/master/scripts/\n",
                            "wget ${baseURL}syncGateway.sh\n",
                            "chmod +x *.sh\n",
                            "./syncGateway.sh ${stackName} ${syncGatewayVersion}\n"
                        ]]
                    }
                }
            }
        }
    }
    return resources

def generateServer(license, serverVersion, group, rallyAutoScalingGroup):
    groupName = group['group']
    nodeCount = group['nodeCount']
    nodeType = group['nodeType']
    dataDiskSize = group['dataDiskSize']
    services = group['services']

    servicesParameter=''
    for service in services:
        servicesParameter += service + ','
    servicesParameter=servicesParameter[:-1]

    command = [
        "#!/bin/bash\n",
        "echo 'Running startup script...'\n",
        "adminUsername=", { "Ref": "Username" }, "\n",
        "adminPassword=", { "Ref": "Password" }, "\n",
        "services=" + servicesParameter + "\n",
        "stackName=", { "Ref": "AWS::StackName" }, "\n",
        "serverVersion=" + serverVersion + "\n",
        "baseURL=https://raw.githubusercontent.com/couchbase-partners/amazon-cloud-formation-couchbase/master/scripts/\n",
        "wget ${baseURL}server.sh\n",
        "wget ${baseURL}util.sh\n",
        "chmod +x *.sh\n",
    ]
    if groupName==rallyAutoScalingGroup:
        command.append("./server.sh ${adminUsername} ${adminPassword} ${services} ${stackName} ${serverVersion}\n")
    else:
        command.append("rallyAutoScalingGroup=")
        command.append({ "Ref": rallyAutoScalingGroup + "AutoScalingGroup" })
        command.append("\n")
        command.append("./server.sh ${adminUsername} ${adminPassword} ${services} ${stackName} ${serverVersion} ${rallyAutoScalingGroup}\n")

    resources = {
        groupName + "AutoScalingGroup": {
            "Type": "AWS::AutoScaling::AutoScalingGroup",
            "Properties": {
                "AvailabilityZones": { "Fn::GetAZs": "" },
                "LaunchConfigurationName": { "Ref": groupName + "LaunchConfiguration" },
                "MinSize": 0,
                "MaxSize": 100,
                "DesiredCapacity": nodeCount
            }
        },
        groupName + "LaunchConfiguration": {
            "Type": "AWS::AutoScaling::LaunchConfiguration",
            "Properties": {
                "ImageId": { "Fn::FindInMap": [ "CouchbaseServer", { "Ref": "AWS::Region" }, license ] },
                "InstanceType": nodeType,
                "SecurityGroups": [ { "Ref": "CouchbaseSecurityGroup" } ],
                "KeyName": { "Ref": "KeyName" },
                "EbsOptimized": True,
                "IamInstanceProfile": { "Ref": "CouchbaseInstanceProfile" },
                "BlockDeviceMappings":
                [
                    {
                        "DeviceName" : "/dev/xvda",
                        "Ebs" : { "DeleteOnTermination" : True }
                    },
                    {
                        "DeviceName" : "/dev/sdk",
                        "Ebs" : {
                            "VolumeSize": dataDiskSize,
                            "VolumeType": "gp2",
                            "Encrypted": True
                        }
                    }
                ],
                "UserData": {
                    "Fn::Base64": {
                        "Fn::Join": [ "", command]
                    }
                }
            }
        }
    }
    return resources

main()
