# RekIn
automate mass emailing to employees of any company

#### Installation:
```sh
    git clone https://github.com/Wayne-X/rektin.git
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
    python linkscrape.py -e YourLinkedInEmail -c CompanyName -d EmailDomainName
```
#### Example Usage:
```sh
    python linkscrape.py -e stew_dent@gmail.com -c DunderMifflin -d DunderMiffl.com
```
