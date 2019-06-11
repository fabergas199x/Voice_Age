import pandas as pd
import dataclean
import record
import predict

def age():
	lst = []
	features = dataclean.pyaudio_featurize('audio.wav')
	labels = features[1]
	row = list(features[0])
	lst.append(row)
	df = pd.DataFrame(lst, columns=labels)
	df.to_csv('data.csv')

	age = predict.predict('data.csv')
	return age