# aws-mfa
Tool to manage MFA credentials with multiple AWS profiles

## Installation
###Step 1 (Optional)
Create and activate a virtual environment to install `aws-mfa` into. For example with `conda` this may look like
```
conda create --name aws-mfa python=3.10
conda activate aws-mfa
```
### Step 2
Install `aws-mfa`
```
pip install git+https://github.com/nlangellier/aws-mfa.git@main
```
### Step 3 (Optional)
If a virtual environment was created in step 1, an alias can be added to your `.bashrc` or `.zshrc` file to execute `aws-mfa` from anywhere in any environment. Using the example in step 1, append the following to your `.bashrc` or `.zshrc` file:
```
alias aws-mfa="conda activate aws-mfa && aws-mfa && conda deactivate || conda deactivate"
```
Then source your `.bashrc` or `.zshrc` file
```
source $HOME/.bashrc
```

## Command Line Usage
```
aws-mfa
```
