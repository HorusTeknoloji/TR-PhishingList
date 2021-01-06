![horus-shield](docs/img/security.svg)

# Türkiye'ye Yönelik Zararlı Bağlantı Erişim Engelleme Listesi

Saldırı, kötüye kullanma, komuta kontrol merkezleri, Javascript tabanlı kripto para madenciliği, zararlı yazılım yayan web siteleri vb kaynakların tespit edilmesi ve erişime engellenmesi amaçlanmaktadır.

## Kullanılan tespit yöntemleri

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


# DİKKAT, Kullandığınız bu liste geliştirilme aşamasındadır. Yer yer hatalar olabileceğini lütfen unutmayınız.

## Linux

```bash
sort url-lists.txt | uniq | sed 's/\./\\\\./g' | while read host; 
do 
    echo "0.0.0.0 $host" >> /etc/hosts
done;
```

## Pi-hole

Admin alanına giriş yaparak `Settings` altında yer alan `Blocklist` sekmesine gelerek listemizi ekleyin ve veritabanınızı güncelleyin

```
https://raw.githubusercontent.com/HorusTeknoloji/TR-PhishingList/master/url-lists.txt
```
