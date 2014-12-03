#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import string
import unicodedata
import codecs
import csv
import cPickle as pickle
import csv

fin = codecs.open("olam-enml.csv", "rb", "utf-8")
malayalam_dict = dict()
pre_data = ""
definition = ""
a=0
for row in fin:
    a+=1
    print a
    data = row.split('\t')
    data[3] = data[3].replace('\r',";")
    if data[1] != pre_data:
        malayalam_dict[data[1].lower()] = data[3]
        definition = ""
    else:
        malayalam_dict[data[1].lower()] += data[3] 
    pre_data = data[1]



for item in malayalam_dict:
	malayalam_dict[item] = malayalam_dict[item].replace('\n',';')
	malayalam_dict[item] = malayalam_dict[item].replace(';;',';')
	splitml = malayalam_dict[item].split(";")
	uniqml = set(splitml)
	listml = list(uniqml)
	malayalam_dict[item] = ";".join(listml)
	malayalam_dict[item] = malayalam_dict[item].replace(';;',';')
	if malayalam_dict[item][0] == ";":
		malayalam_dict[item] = malayalam_dict[item][1:]
	if malayalam_dict[item][len(malayalam_dict[item])-1] == ";":
		malayalam_dict[item] = malayalam_dict[item][:-1]



out1 = codecs.open("database.dat", "wb", "utf-8")
out2 = codecs.open("pickledatabase.dat", "wb")
pickle.dump(malayalam_dict, out2)
for key in malayalam_dict:
	out1.write("%s\t%s\n" % (key,malayalam_dict[key]))
out1.close()
out2.close()
fin.close()
