# rektin
automate mass emailing to employees of any company

#### Installation:
```sh
    git clone https://github.com/Wayne-X/rektin.git
    sudo rektin/setup.sh
```

#### Email Setup:
1. Fill in ~/email_credentials/config.json with your gmail credentials and email template
2. Enable gmail log in permissions as follows:

![In gmail, go to settings](img/allow1.png)
![In settings, go to Accounts and import tab, and click Other Account Settings](img/allow1.5.png)
![Click on the Sign in and security card](img/allow2.png)
![Scroll down and enable allow less secure apps](img/allow3.png)

#### Usage:
```sh
    python linkscrape.py -e YourLinkedInEmail -c CompanyName -d EmailDomainName
```
#### Example Usage:
```sh
    python linkscrape.py -e stew_dent@gmail.com -c DunderMifflin -d DunderMiffl.com
```
