#!/bin/bash

source $HOME/opt/anaconda3/etc/profile.d/conda.sh || exit 1
conda activate aws-mfa || exit 1
$HOME/aws-mfa || exit 1
