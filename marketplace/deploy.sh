#!/usr/bin/env bash

STACK_NAME=$1

TEMPLATE_BODY="file://couchbase-byol.template"
REGION=$2

ServerInstanceCount=$3
ServerVersion=$4
ServerUrl="$5"
ServerDiskSize="100"
SyncGatewayInstanceCount="0"
InstanceType="m4.xlarge"
Username="Administrator"
Password="password"
KeyName="couchbase-qe"
SSHCIDR="0.0.0.0/0"

aws cloudformation create-stack \
--capabilities CAPABILITY_IAM \
--template-body ${TEMPLATE_BODY} \
--stack-name ${STACK_NAME} \
--region ${REGION} \
--parameters \
ParameterKey=ServerInstanceCount,ParameterValue=${ServerInstanceCount} \
ParameterKey=ServerVersion,ParameterValue=${ServerVersion} \
ParameterKey=ServerUrl,ParameterValue="${ServerUrl}" \
ParameterKey=ServerDiskSize,ParameterValue=${ServerDiskSize} \
ParameterKey=SyncGatewayInstanceCount,ParameterValue=${SyncGatewayInstanceCount} \
ParameterKey=InstanceType,ParameterValue=${InstanceType} \
ParameterKey=Username,ParameterValue=${Username} \
ParameterKey=Password,ParameterValue=${Password} \
ParameterKey=KeyName,ParameterValue=${KeyName} \
ParameterKey=SSHCIDR,ParameterValue=${SSHCIDR}
