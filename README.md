# aws-mfa
Tool to manage MFA credentials with multiple AWS profiles

## Installation
### Step 1 (Optional)
Create and activate a virtual environment to install `aws-mfa` into. For example with `conda` this may look like
``` bash
conda create --name aws-mfa-env python=3.10
conda activate aws-mfa-env
```
### Step 2
Install `aws-mfa`
``` bash
pip install git+https://github.com/nlangellier/aws-mfa.git@main
```
### Step 3 (Optional)
If a virtual environment was created in step 1, an alias can be added to your `.bashrc` file to allow execution of `aws-mfa` from anywhere in any environment. Using the example in step 1, run the following command to append to your `.bashrc` file:
``` bash
echo 'alias aws-mfa="conda run --name aws-mfa-env --live-stream aws-mfa"' >> $HOME/.bashrc
source $HOME/.bashrc
```
If you used another virtual environment manager besides `conda`, then replace `"conda run --name aws-mfa-env --live-stream aws-mfa"` above with a relevant shell command to run `aws-mfa` in the environment created in step 1. If you use another shell, replace `.bashrc` with the relevant file. E.g. if you use zsh, then replace `.bashrc` with `.zshrc`.

## Command Line Usage
```
aws-mfa
```
