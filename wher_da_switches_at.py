#!/usr/local/bin/python3

import argparse
import os
import json
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from twilio.rest import Client

parser = argparse.ArgumentParser()

parser.add_argument('--chromedriver', required=True,
                                      help='path to your chromedriver')

parser.add_argument('--url', required=True,
                             help='insert gamestop url')

parser.add_argument('--account_SID', default=os.environ.get('ACCOUNT_SID'),
                                     help='Twilio account SID')

parser.add_argument('--auth_token', default=os.environ.get('AUTH_TOKEN'),
                                    help='Twilio auth Token')

parser.add_argument('--twilio_number', default=os.environ.get('TWILIO_NUMBER'),
                                       help='Twilio number')

parser.add_argument('--recipient', default=os.environ.get('RECIPIENT'),
                                   help='number to message')

args = parser.parse_args()

def driver_setup(path, url):

    # path set within env variable. make sure it's directed to the right place.
    driver = webdriver.Chrome(path)

    # list of URL extensions within the text file.
    driver.get(args.url)

    return driver

def twilio_signin(account_sid, auth_token):

    client = Client(account_sid, auth_token)

    return client

def extract_info(driver):

    content = driver.page_source

    # features added to get rid of warning message.
    soupy = BeautifulSoup(content, features = 'lxml')

    # json because it's easier.
    data = json.loads(str(soupy.text))

    checker = []

    productinfo = data['gtmData']['productInfo']

    filtered = { k : productinfo[k] for k in ('name', 'condition', 'availability') }

    checker.append(filtered)

    df = pd.DataFrame(checker)

    df.set_index('name')

    return df

def notify_client(client, df, twilio_number, recipient):

    for i in df['availability']:

        if i == 'Not Available':

            print('switches nowhere to be found. goodbye')
            exit()

        else:

            avail_message = client.messages \
                .create(
                    body=f"{df['name'].to_string(index=False)} is available! See {args.url} to purchase.",
                    from_=twilio_number,
                    to=recipient
                )

            print(avail_message.sid)

def main():

    args = parser.parse_args()

    retrieve_url = driver_setup(args.chromedriver, args.url)

    client = twilio_signin(args.account_SID, args.auth_token)

    extracted_info = extract_info(retrieve_url)

    print(extracted_info)

    notify_client(client, extracted_info, args.twilio_number, args.recipient)

if __name__ == '__main__':
    main()