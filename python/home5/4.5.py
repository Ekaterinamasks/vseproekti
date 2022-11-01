# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
line = 'абв абвбп абвырыр аабврпв ырырфп првапф рвапр абв'
words = line.split(' ')
fragment = 'абв'
new_words = []
for word in words:
     if fragment not in word:
         new_words.append(word)
new_words = ' '.join(new_words)
print (new_words)