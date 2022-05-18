# aws-mfa
Tool to manage MFA credentials with multiple AWS profiles

## Installation
```
WORKING_DIRECTORY=$HOME
AWS_MFA_REPOSITORY=${WORKING_DIRECTORY}/aws-mfa

cd ${WORKING_DIRECTORY}
git clone https://github.com/nlangellier/aws-mfa.git

conda create --name aws-mfa python=3.10
conda activate aws-mfa
pip install git+https://github.com/nlangellier/aws-mfa.git@main

echo "alias aws-mfa=\"conda activate aws-mfa && python ${AWS_MFA_REPOSITORY}/aws_mfa/main.py && conda deactivate\"" >> $HOME/.bashrc
source $HOME/.bashrc
```

## Usage
```
aws-mfa
```
