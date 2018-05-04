import tweepy
import json
from tweepy import OAuthHandler
import numpy as np
 
consumer_key = 'OU4n6gpftucZHbF727ylx6pe3'
consumer_secret = '9G2RBxpTCQwXiUqhLlpvrnj4arzOLTKbAPhEhfSYJQs5Uv0onD'
access_token = '321787319GSH9sxzlA9qsJFp9NnWXu4aBJyjQFy5tIw49LOef'
access_secret = 'n4bub6B82yAfqTgzYm4vQLCb2a0JPas6aGPMtb2gX08Ly'
 
#auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)

"""
#TWEET MINING
api = tweepy.API(auth)
f = open('tweets.txt', 'w+', encoding="utf-8")
jumlah_data_yang_diinginkan = 1000
for i in list(['jaringan','4g','3g','koneksi','gsm','hdspa','edge']):
    for j in list(['lambat','lemot','lelet','goblok','anjing','bego','cacat']):
        for tweet in tweepy.Cursor(api.search, q=[i,j], tweet_mode='extended', geocode="-7.614529,110.712246,583km").items(jumlah_data_yang_diinginkan):
            obj = tweet._json
            #print(obj.keys())
            #print(obj['full_text'])
            f.write(obj['full_text'])
            f.write("\n")
f.close()
"""
    
# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import time

# create stemmer
#factory = StemmerFactory()
#stemmer = factory.create_stemmer()

# stem
#sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
#output   = stemmer.stem(sentence)
#
#print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

#print(stemmer.stem('koneksi'))
# mereka tiru

# ======================= Kelompok Kata & Bobot ===============================

nouns = ['jaring', '4g', '3g', 'koneksi', 'hsdpa', 'h+', 'edge']
adjs = ['lambat', 'lemot', 'lelet', 'lot']
customerWords = ['kenapa', 'tolong', 'banget']
kataKasar = ['goblok', 'anjing', 'bego', 'cacat', 'maling']

kataOA = ['kait', 'info', 'pantau', 'ketidaknyamanan', 'kendala', 'kena', 'keluh', 'privasi']

# =============================================================================

# =================== Fungsi Klasifikasi Data Keluhan =========================

def debug_isKeluhan (data):
# Menentukan data mengenai keluhan jaringan dari pelanggan    
    
    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    
    poin = 0
    output = stemmer.stem(data)#data.lower()
        
    words = output.split(' ')
    for word in words:
        if word in nouns:
            poin = poin +1                
        elif word in adjs:
            poin = poin +2                
        elif word in customerWords:
            poin = poin +2                
        elif word in kataKasar:
            poin = poin +3                
        elif word in kataOA:
            poin = poin -3
        else:
            poin = poin + 0
            
            print("Kata: ", word, "Poin: ", poin)

#Gunakan kode berikut untuk validasi poin
#    print(poin)
    if poin >= 3:
        return True;
    else:
        return False;

# =============================================================================


# =================== Fungsi Klasifikasi Data Keluhan =========================

def isKeluhan (data):
# Menentukan data mengenai keluhan jaringan dari pelanggan    
    
    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    
    poin = 0
    output = stemmer.stem(data)#data.lower()
        
    words = output.split(' ')
    for word in words:
        if word in nouns:
            poin = poin +1                
        elif word in adjs:
            poin = poin +2                
        elif word in customerWords:
            poin = poin +2                
        elif word in kataKasar:
            poin = poin +3                
        elif word in kataOA:
            poin = poin -3
        else:
            poin = poin + 0

#Gunakan kode berikut untuk validasi poin
#    print(poin)
    if poin >= 3:
        return True;
    else:
        return False;

# =============================================================================

# ========================= Fungsi Filtering Data =============================

def filtering (rawDatas):
# Mencari data mengenai keluhan jaringan dari pelanggan    
    filteredDatas = []
    
    for data in rawDatas:
        if isKeluhan(data):
            filteredDatas.append(data)
    
    return filteredDatas;

# =============================================================================

# ========================= Fungsi Scoring Data =============================

def classification (rawDatas):
# Mencari data mengenai keluhan jaringan dari pelanggan    
    classes = []
    
    for data in rawDatas:
        if isKeluhan(data):
            classes.append(1)
        else:
            classes.append(0)
    
    return classes;

# =============================================================================

# ========================= Fungsi Scoring Data =============================

def scoring (predicted, actual):
    
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(actual, predicted)
    
    print(cm)

#cm = [[6664, 209], [1398, 25267]]

    TN = cm[0][0]
    TP = cm[1][1]
    FP = cm[0][1]
    FN = cm[1][0]
    
    Akurasi = (TP+TN)/(TP+TN+FP+FN)
    Presisi = (TP)/(TP+FP)
    Recall = (TP)/(TP+FN)
    Spesitifitas = (TN)/(TN+FP)
    
    print("Akurasi: ", Akurasi)
    print("Presisi: ", Presisi)
    print("Recall: ", Recall)
    print("Spesitifitas: ", Spesitifitas)
    
    return 0;

# =============================================================================

# ================== Proses Filter mengunakan Stemming ========================
# 
start = time.time()

# Parameter word untuk array f tweet yang akan diproses
"""
word = [
        'https://t.co/l5DyhZMO0a @IndosatCare  masih lemot nih Indosat. Jaringan sudah 4G - Indosat Ooredoo..  Lemot cuma di rumah saya saja.',
        '@TelkomCare Mohon cek jaringan dong. Ini internet Indihome kok lemot LAGI ya???',
        'myXLCare hi XL, sudah beberapa hari ini lambat sekali ya. Hari ini yang paling parah di jaringan LTE nya. Youtube, browsing, twitter, instagram, dll lambat bgt. Kenapa?',
        '@IndosatCare indosat jaringan 4g tapi lemot parah',
        '@IndosatCare jaringan indosat hari ini lg lemot bgt apa gmn ya?',
        'Sepertinya jaringan internet indonesia lagi error. Yang pake ini itu pada ngeluh lemot',
        '@Telkomsel jaringan telkomsel d tangerang lg bermasalah kah? Lemot sekali internet 2 hari ini. Beli paketnya mahal lho d banding yg lain.',
        '@triindonesia jaringan 3 di Kebalen, Bekasi Utara, 2 hari ini untuk download, browsing lemot banget, sering putus, mohon dicek jaringannya',
        '@IndosatCare min kuota saya masih banyak tapi internetnya tidak bisa dipakai, lemot sejak semalam, ada perbaikan jaringan apa gimana?',
        '@MNCPlayID min ini jaringan net nya kok lemot bgt ya sering RTO . Pdhl bayar nya saya lancar tp internet nya lemot -_-'    
        ]
"""

import pandas as pd
csv_file = 'tweets-full.csv'
df = pd.read_csv(csv_file, sep=';', encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)

word = df.Tweet #you can also use df['column_name']
label = df.Label

#print(word)
#print(label)

#print(label.value_counts())

prediction = classification(word)

scoring(prediction, label)

# OUTPUT KE FILE CSV

#result = filtering(word)

#import numpy
#a = numpy.asarray(result)
#numpy.savetxt("output.csv", a, fmt="%s", delimiter=";", encoding="ISO-8859-1")

# Parameter result untuk array of tweet yang sudah terfilter

#for pala in word:
#    print(debug_isKeluhan(pala))

end = time.time()

print("Time: ", ("%.3f" % (end - start)))
# =============================================================================


    