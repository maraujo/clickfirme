__author__ = 'matheus'
import urllib2
import os
url = urllib2.urlopen("http://developers.agenciaideias.com.br/loterias/megasena/json")
content = url.read()
filename = "megasena.json"
file_ptr = open(os.path.abspath(os.path.dirname(__file__)) + "/raffle/" + filename, "w")
file_ptr.write(content)
file_ptr.close()




