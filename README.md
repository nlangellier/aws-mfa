# aws-mfa
Tool to manage MFA credentials with multiple AWS profiles

## Installation
```
conda create --name aws-mfa python=3.10
conda activate aws-mfa
pip install git+https://github.com/nlangellier/aws-mfa.git@main
curl https://raw.githubusercontent.com/nlangellier/aws-mfa/aws-mfa.sh -o $HOME/aws-mfa.sh
echo 'alias aws-mfa="$HOME/aws-mfa.sh"' >> $HOME/.zshrc
```
