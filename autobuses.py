# -*- coding: utf-8 -*-

from lxml import etree
from suds.client import Client

bus = raw_input("¿Que linea de autobuses quieres consutar? ")

cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)
respuesta = cliente.service.GetStatusLinea(bus)


raiz = etree.fromstring(respuesta.encode("utf-8"))
raiz2 = raiz[0][0]
pretty = etree.tostring(raiz2, pretty_print = True)
ns = "{http://tempuri.org/}"
nb = "GetStatusLineaResult/"
activos = raiz2.find(ns+nb+ns+"activos")
frecuencia = raiz2.find(ns+nb+ns+"frec_bien")
graves = raiz2.find(ns+nb+ns+"graves")

print "En la linea",bus,"existen",activos.text,"autobuses activos"""
print "De los",activos.text,"van en frecuencia",frecuencia.text,"autobuses"""
print "En esta linea existen un numero de",graves.text,"incidencias graves"