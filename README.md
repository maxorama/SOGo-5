# SOGo
Ansible compile and installing SOGo for postfix mail server. Also added LDAP bind for global Address Book.

Configuration:
- SOGo 5.x.x

Compilation:
- Compillation is building for CentOS 7.x/8.x using rpmbuild
- To fully working with remote Imaps/Pop3s protocol versions of mailserver you should install valid self-signed/CA root certificate or self-signed mailserver certificate to CA authority

Known issue:
- If you want to use SSL/TLS self-signed certificate of you mail server then you will need to place a mail server self-signed certificate to roles/sogo/files/ca-chain.cert.pem and setup the parameter mail_tls to "yes"

Backend backup - Bacula client

