# WhEr dA sWitCHEs @??

This is to help u/melonbred find where all dem switches are.

![](img/istockphoto-968279248-1024x1024.jpg)

## Requirements
- python3.7/pip
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium WebDriver for Chrome](https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.69/)
- [Twilio and your own trial account](https://www.twilio.com/)

## Installation

`brew install python3`
`pip install beautifulsoup4`
`pip install selenium`
Then go to [this link](https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.69/) to download the ChromeDriver to your working directory.
`pip install twilio`

...and default crontab for Mac.

## How to Use

1. Create your ever-so-precious environment file (hide it from the world, please) and format it as such:

```bash
export ACCOUNT_SID='<account SID for twilio>'
export AUTH_TOKEN='<auth token for twilio>'
export TWILIO_NUMBER='<+1 twilio account number setup>'
export RECIPIENT='<+1 verified phone number of recipient>'
export CHROMEDRIVER_PATH='/path/to/chromedriver/'
```

2. Source your new env file.

3. Run the scraper using `./entrypoint.sh` from the terminal if you want to watch it run live. Otherwise, set up a job or list of jobs on your Mac machine using crontab.

## Using Crontab

From the terminal, run `crontab -e` to start the text editor for job management.

```bash
crontab -e
```

Crontab requires a specific format.

```bash
* * * * * command

* - minute (0-59)
* - hour (0-23)
* - day of the month (1-31)
* - month (1-12)
* - day of the week (0-6, 0 is Sunday)

command - command to execute
```

Once you input your intervals of when you want the program to run, save and exit crontab.

Mine is set up to run every 5 hours in the day like so:

```bash
0 0 * * * cd ~/path/to/wherdaswitchesat/ && source <envfile> && ./entrypoint.sh
0 5 * * * cd ~/path/to/wherdaswitchesat/ && source <envfile> && ./entrypoint.sh
0 10 * * * cd ~/path/to/wherdaswitchesat/ && source <envfile> && ./entrypoint.sh
0 15 * * * cd ~/path/to/wherdaswitchesat/ && source <envfile> && ./entrypoint.sh
0 20 * * * cd ~/path/to/wherdaswitchesat/ && source <envfile> && ./entrypoint.sh
```

Set up any interval you'd like. You can view message outputs of the job(s) from the directory your terminal prompts you. Mine prompts me to check /var/mail/<username>.
