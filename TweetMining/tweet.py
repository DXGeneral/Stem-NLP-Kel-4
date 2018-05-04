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
adjs = ['lambat', 'lemot', 'lelet']
customerWords = ['kenapa', 'tolong']
kataKasar = ['goblok', 'anjing', 'bego', 'cacat', 'maling']

kataOA = ['kait', 'info', 'pantau', 'ketidaknyamanan', 'kendala', 'kena', 'keluh', 'privasi']

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

#Gunakan kode berikut untuk validasi poin
#print(poin)
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
        if isKeluhan(data) is not True:
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
        'AXISgsm kenapa yah, jaringan lemot banget.. pusiiing dahh gua pake @ask_AXIS',
        '@AdhiHardiansyah Hai, Mas Adhi. Jika mengalami akses internet lambat kembali, coba menggunakan mode jaringan 3G only dahulu. Agar dapat dibantu cek status kartu serta data terjaga, infokan nomor dengan lengkap dan tipe HP via DM. Terima kasih. -Sakhi',
        'myXLCare hi XL, sudah beberapa hari ini lambat sekali ya. Hari ini yang paling parah di jaringan LTE nya. Youtube, browsing, twitter, instagram, dll lambat bgt. Kenapa?',
        'FirstMediaCares siang min, saya pelanggan 80844501 bbrp hari ini bahkan minggu lalu sempat terjadi hal yg sama. Jaringan sangat lambat (lemot). Mhn diperbaiki dalam waktu 2 jam atau akhir bulan ini kalian ambil kembali property kalian dari rumah saya. Tq',
        'Jaringan 4G dari @telkomsel di manokwari emang TOP BANGET! 48,71 KB. KILOBYTE LOH!!!! Untuk ukuran 4G itu lambat banget!!! AKU CINTA PRODUK INDONESIA!!! https://t.co/75xBLrpv0p',
        '@XLAxiata_Tbk @celath @myXLCare Ini provider isiny cm maling, jaringan kyk tai ngak stabil aja iklan di gedein goblok l xl. Maling pulsa, maling paket ckckckc anjing l xl kampret',
        '@myXLCare @hak_bersuara Provider bangsat, kerahasian tai l xl goblok. Sms ngak jelas,rbt nipu,fb nipi,jaringan nipu bangsat l xl. Ada jg ini provider lha maling sesungguhnya. Eh cs bangsat ganti l anjing kerugian2 konsumen kampret l xl maling.'
        'myXL fuck XL jaringan internet paling lemot! Lu liat nih kecepatan internet yang lu berikan 0,22 Mbps? Lu bilang speed dial up lu nyampe 50Mbps dari HONGKONG 50 Mbps https://t.co/gxm7Cp0EgY',
        'RT @hollyshit87: @IndosatCare @aurorasytr goblok! Bukannya diperkuat jaringan nya tapi masih ttp aja nyuruh konsumen pake cara bodoh kaya g…',
        'Anjing bangsat ngentot busuk jaringan lo ga bener bener najis goblok @TelkomCare'    
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

#prediction = classification(word)

#scoring(prediction, label)

# OUTPUT KE FILE CSV

result = filtering(word)

import numpy
a = numpy.asarray(result)
numpy.savetxt("output.csv", a, fmt="%s", delimiter=";", encoding="ISO-8859-1")

# Parameter result untuk array of tweet yang sudah terfilter

#for word in result:
#    print(word)

end = time.time()

print("Time: ", ("%.3f" % (end - start)))
# =============================================================================


    