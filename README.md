You will need to create a self signed cert for this to run. It expects the cert to be located in the same directory as https_server.py.

Windows people: If you have GIT installed you can create certs using the openssl.exe located in "C:\Program Files\Git\usr\bin\openssl.exe" (e.g. "C:\Program Files\Git\usr\bin\openssl.exe" req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem
 -days 365 -nodes)
