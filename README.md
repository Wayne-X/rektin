# RektIn
Fully automated recruiting growth hack: set up once, and reach recruiters' inboxes with a single command.
<p align="center">
<img src="https://github.com/Wayne-X/rektin/blob/master/img/success1.PNG?raw=true" width="400">
<img src="https://github.com/Wayne-X/rektin/blob/master/img/success2.PNG?raw=true" width="400">
<br>
<i>example of the code at work, these are fake names</i>
</p>

Leverages data mining and a portion of the SMTP protocol to collect email addresses of recruiters at top companys, and automates sending emails to selected email addresses. This code is provided as-is, use at your own discretion. Go easy on the data mining part, if you query too fast your LinkedIn account might get flagged.

Our submission to Wildhacks 2016: 
[Wayne Xun](https://www.linkedin.com/in/waynexun) (CS '17), [Hayley Hu](https://www.linkedin.com/in/hayley-hu) (CS '16)

#### Motivation:
GeekedIn recently leaked information on 8 million developers that was crawled from Github [(link)](https://www.troyhunt.com/8-million-github-profiles-were-leaked-from-geekedins-mongodb-heres-how-to-see-yours/). Corporations have begun to mass email developers with recruitment spam.

We bring you revenge. Now you can can crawl for information from LinkedIn, and mass email corporations with recruitment spam.

#### Installation:
```sh
    git clone https://github.com/Wayne-X/rektin.git
    chmod u+x rektin/setup.sh
    sudo rektin/setup.sh
```

#### Email Setup:
1. Fill in ~/email_credentials/config.json with your gmail credentials and email template
2. Enable gmail log in permissions as follows:

![In gmail, go to settings](https://github.com/Wayne-X/rektin/blob/master/img/allow1.PNG?raw=true)
![In settings, go to Accounts and import tab, and click Other Account Settings](https://github.com/Wayne-X/rektin/blob/master/img/allow1.5.PNG?raw=true)
![Click on the Sign in and security card](https://github.com/Wayne-X/rektin/blob/master/img/allow2.PNG?raw=true)
![Scroll down and enable allow less secure apps](https://github.com/Wayne-X/rektin/blob/master/img/allow3.PNG?raw=true)

#### Usage:
```sh
    python linkScrape.py -e YourLinkedInEmail -c CompanyName -d EmailDomainName
```
#### Example Usage:
```sh
    python linkScrape.py -e stew_dent@gmail.com -c DunderMifflin -d DunderMiffl.com
```
#### Feature Queue:
Features that would be nice to have in the future
- more robust credentials handling: support system keychain
- async queries, multiple SMTP querying workers
- get emails mode, only get emails but does not send anything
- user adjustable settings for linked scrape speed
- "costco mode", input list of companies with conservative scrape speed and run silently "always-on", email new people not seen before



