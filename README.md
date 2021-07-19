![horus-shield](docs/img/security.svg)

# TR-PhishingList

It is aimed to detect and prevent access to resources such as attacks, abuse, command and control centers, Javascript-based cryptocurrency mining, websites spreading malware and etc.


# Attention

List type: **Aggressive**

False-Positive Ratio is high. Our list is under development, Please report any f/p

## The detection methods

- Kaspersky Abuse
- DNS Zone
- Google Safebrowsing
- Normshield
- RiskIQ
- UrlScan
- Alienvault
- Any Run
- Certificate Transparency
- DNS Twist
- Phishing NG
- Brandefense

# How to use?

### Linux

```bash
sort url-lists.txt | uniq | sed 's/\./\\\\./g' | while read host; 
do 
    echo "0.0.0.0 $host" >> /etc/hosts
done;
```

### Pi-hole and others

```
https://raw.githubusercontent.com/HorusTeknoloji/TR-PhishingList/master/url-lists.txt
```
