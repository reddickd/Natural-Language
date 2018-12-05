#from .nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
import sys
import logging

# from keras.layers import Input, Embedding, merge
# from keras.models import Model
# import tensorflow as tf
# import numpy as np

# import urllib.request
# import os
# import zipfile


warnings.filterwarnings(action = 'ignore') 
  
import gensim 
from gensim.models import word2vec,KeyedVectors 



# def maybe_download(filename, url, expected_bytes):
#     """Download a file if not present, and make sure it's the right size."""
#     if not os.path.exists(filename):
#         filename, _ = urllib.request.urlretrieve(url + filename, filename)
#     statinfo = os.stat(filename)
#     if statinfo.st_size == expected_bytes:
#         print('Found and verified', filename)
#     else:
#         print(statinfo.st_size)
#         raise Exception(
#             'Failed to verify ' + filename + '. Can you get to it with a browser?')
#     return filename

print("Takes a minute to load depending on the system . . .")

filename = '/Users/DavidsMac/Desktop/434naturallanguage/GoogleNews-vectors-negative300.bin.gz'
model = KeyedVectors.load_word2vec_format(filename, binary=True)

print("Model loaded\n")
# result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
# print(result)


#get the sentences to train the model
# url = 'http://mattmahoney.net/dc/'
# filename = maybe_download('text8.zip', url, 31344016)
# root_path = "/Users/DavidsMac/Documents/" 

# if not os.path.exists((root_path + filename).strip('.zip')):
# 	zipfile.ZipFile(root_path+filename).extractall()

# #word2vec = Word2Vec()

# sentences = word2vec.Text8Corpus((root_path + filename).strip('.zip'))

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# model = word2vec.Word2Vec(sentences, iter=10, min_count=4, size=5, workers=4)

# print(model.wv['the'])


print("Word embedding algorithm used: Word2Vec\nModel Used: Google News Vectors\n")



# Turn on [lamp, camera]

# Turn up [thermostat]

# Lock [bolt]

# Unlock [bolt]
while True:
	userInput = input("Enter your command: " + '\n')
	inputList = userInput.split(' ')
	output = "This will be overwritten"

	#initial prints of specs
	

	#scrub input to make sure valid command
	if userInput == "quit" : #quit entered
		sys.exit()

	if len(inputList) < 2 : 
		print("no compatible command found")
		sys.exit()

	elif(len(inputList) == 2 and inputList[0] == "lock"): #lock command
		#output = "lock command"
		result = model.similarity('bolt', inputList[1])
		print(result)
		if(result > .25):
			print("Input: " + userInput + '\n' + "Output: " + output)

	elif(len(inputList) == 2 and inputList[0] == "unlock"): #unlock command
		#output = "unlock command"
		result = model.similarity('bolt', inputList[1])
		print(result)
		if(result > .25):
		 	print("Input: " + userInput + '\n' + "Output: " + output)

	elif(len(inputList) == 3 and inputList[0] == "turn" and  inputList[1] == "on"): #turn on command
		#output = "turn on command"  
		result = model.similarity('lamp', inputList[2]) 
		result2 = model.similarity('camera', inputList[2])
		print(result+' | '+result2)
		if(result>result2):
			if(result > .3):
		 		print("Input: " + userInput + '\n' + "Output: " + output)
		else:
			if(result2 > .3):
				print("Input: " + userInput + '\n' + "Output: " + output)
		

	# elif(len(inputList) == 3 and inputList[0] == "turn" and  inputList[1] == "off"): #turn off command
	# 	output = "turn off command"
	# 	result = model.similarity('lamp', inputList[2]) #or camera
	# 	print(result)

	elif(len(inputList) == 3 and inputList[0] == "turn" and  inputList[1] == "up"): #turn up command
		#output = "turn up command"
		result = model.similarity('thermostat', inputList[2])
		print(result)
		if(result > .4):
		 	print("Input: " + userInput + '\n' + "Output: " + output)

	else:
		output = "no compatible command found"
	print('\n')
	#input word embedding shit













