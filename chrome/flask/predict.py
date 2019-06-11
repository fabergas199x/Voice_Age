from keras.models import load_model
import pandas as pd
import pickle
from sklearn.feature_selection import SelectFromModel

def predict(file):
	data = pd.read_csv(file)
	data = data.dropna(how='any',axis=0)

	X_pred = data.drop(columns=['Unnamed: 0']).values
	feature_selector = pickle.load(open('MLP_Model3_featureSelector.pickle','rb'), encoding='latin1')
	X_pred = feature_selector.transform(X_pred)
	scaler = pickle.load(open("MLP_Model3_standardScaler.pickle","rb"), encoding='latin1')
	X_pred = scaler.transform(X_pred)

	model_3 = load_model('MLP_Model3.h5')
	y_pred = model_3.predict_classes(X_pred)
	class_names = ['teens','twenties','thirties','fourties','fifties','sixties','seventies','eighties']


	return class_names[int(y_pred)]