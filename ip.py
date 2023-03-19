# -*- coding: utf-8 -*-
"""ip.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14BUoaG_idrggeQvWCn8pLSLjGBGtRHUJ
"""

#importação de biblioteca nativa do Python 3
import ipaddress

#Criação do objeto para receber qualquer número de ip.
ip = '192.168.0.1'

#Criação do objeto endereço para passagem do número do ip informado
endereco = ipaddress.ip_address(ip)
print(endereco)

"""Cálculos de IP´s"""

#somar +100 no ip
endereco = ipaddress.ip_address(ip)
print(endereco+100)

#somar +257 no ip
endereco = ipaddress.ip_address(ip)
print(endereco+257)

#somar +256 no ip
endereco = ipaddress.ip_address(ip)
print(endereco+256)

#somar +2000 no ip
endereco = ipaddress.ip_address(ip)
print(endereco+2000)

#trabalhar com redes

rede = ipaddress.ip_network(ip)
print(rede)

#impressão de ip's com redes e utilizando o módulo strict
ip = '192.168.0.0/24'
rede = ipaddress.ip_network(ip, strict=False)
for ip in rede:
    print(ip)

#trabalhar ip's com redes
ip = '192.168.0.0/32'
rede = ipaddress.ip_network(ip, strict=False)
for ip in rede:
    print(ip)