import os
from configparser import ConfigParser
from getpass import getpass
from pathlib import Path

import boto3


def main():
    fpath_default_aws_credentials = Path.home() / '.aws' / 'credentials'
    fpath_aws_credentials = input('AWS credentials file '
                                  f'[{fpath_default_aws_credentials}]: ')
    if not fpath_aws_credentials:
        fpath_aws_credentials = fpath_default_aws_credentials

    config = ConfigParser()
    config.read(fpath_aws_credentials)

    profile_name = input('Profile name: ')
    if 'aws_mfa_serial_number' in config[profile_name]:
        aws_mfa_serial_number = config[profile_name]['aws_mfa_serial_number']
    else:
        aws_mfa_serial_number = getpass('AWS MFA serial number: ')
    aws_mfa_one_time_token = input('MFA one time token: ')

    aws_session = boto3.Session(profile_name=profile_name)
    sts_client = aws_session.client(service_name='sts')
    response = sts_client.get_session_token(SerialNumber=aws_mfa_serial_number,
                                            TokenCode=aws_mfa_one_time_token)
    credentials = response['Credentials']

    profile = input('Profile to write temporary credentials to [default]: ')
    if not profile:
        profile = 'default'
    if not config.has_section(profile):
        config.add_section(profile)
    elif profile != 'default':
        ok_to_overwrite = input('Are you sure you want to overwrite profile '
                                f'{profile} (y/[n])? ')
        if not ok_to_overwrite or ok_to_overwrite.upper() == 'N':
            print('Exiting. No credentials saved. Please try again.')
            return

    config[profile]['aws_access_key_id'] = credentials['AccessKeyId']
    config[profile]['aws_secret_access_key'] = credentials['SecretAccessKey']
    config[profile]['aws_session_token'] = credentials['SessionToken']

    with open(fpath_aws_credentials, 'w') as aws_credentials:
        config.write(aws_credentials)

    set_env = input(f'Set AWS_PROFILE env variable to {profile} (y/[n])? ')
    if set_env.upper() == 'Y':
        os.environ['AWS_PROFILE'] = profile
    elif set_env not in ['', 'n', 'N']:
        raise ValueError('Invalid response. Skipping env variable setting.')


if __name__ == '__main__':
    main()
