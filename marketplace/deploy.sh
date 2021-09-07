#!/usr/bin/env bash

STACK_NAME=$1

TEMPLATE_BODY="file://couchbase-byol.template"
REGION=$2

ServerInstanceCount=$3
ServerDiskSize="100"
InstanceType="m4.xlarge"
KeyName=$4
SSHCIDR="0.0.0.0/0"

echo $ServerUrl

aws cloudformation create-stack \
--capabilities CAPABILITY_IAM \
--template-body ${TEMPLATE_BODY} \
--stack-name ${STACK_NAME} \
--region ${REGION} \
--parameters \
ParameterKey=ServerInstanceCount,ParameterValue=${ServerInstanceCount} \
ParameterKey=ServerDiskSize,ParameterValue=${ServerDiskSize} \
ParameterKey=InstanceType,ParameterValue=${InstanceType} \
ParameterKey=KeyName,ParameterValue=${KeyName} \
ParameterKey=SSHCIDR,ParameterValue=${SSHCIDR}
