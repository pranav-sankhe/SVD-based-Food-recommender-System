import pandas as pd
import numpy as np
from sklearn.externals import joblib
from recsys.datamodel.item import Item
from recsys.datamodel.user import User
import recsys.algorithm
#recsys.algorithm.VERBOSE = True
 
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
from recsys.evaluation.prediction import RMSE, MAE
from collections import Counter


def setup():
	restaurant_data =  pd.DataFrame()
	user_data = pd.DataFrame()
	joblib.dump(restaurant_data,'restaurant_data.pkl')
	joblib.dump(user_data,'user_data.pkl')

def restaurant_details(input):
	#input = { 'rest_id':'None' 'food_id':None 'food_detail':None 'food_category_id':None }
	global restaurant_data
	restaurant_data = joblib.load('restaurant_data.pkl')
	rest_id = input['rest_id']
	food_id = input['food_id']
	food_detail = input['food_detail']
	food_category_id = input['food_category_id'] 
	list1 = [[rest_id,food_id,food_detail,food_category_id]]
	restaurant_data = restaurant_data.append(list1)
	joblib.dump(restaurant_data,'restaurant_data.pkl')
	return restaurant_data



def user_data(Input):
	#input = {'rest_id': 'None',  'user_id':'None' , 'food_id':'None'}
	global user_data
	user_data = joblib.load('user_data.pkl')
	rest_id = Input['rest_id']
	user_id = Input['user_id']
	food_id = Input['food_id']
	list1 = [[rest_id ,user_id ,food_id ]]
	user_data = user_data.append(list1)
	joblib.dump(user_data, 'user_data.pkl')
	return user_data



def train():
	global user_data
	user_data = joblib.load('user_data.pkl')
	user_data.insert(3, 3, 1)  
	users_data = user_data[[1,2,3]]
	users_data.to_csv('./data.csv')
	rest_id = user_data[0]
	for rest in rest_id	:
		data = Data()
		data.load('./data.csv', sep=',', format={'col':0, 'row':1, 'value':2})
		savefile = './' + 'models' + '/rest' + str(rest)      
		
		K=100
		svd = SVD()
		train = data
		svd.set_data(train)

		svd.compute(k=K, min_values=1, pre_normalize=None, mean_center=True, post_normalize=True,savefile=savefile)
		return 	
		


def predict(input):
	
	rest_id = input['rest_id']
	svd = SVD()
	svd.create_matrix()
	savefile = './models/rest' + str(rest_id)
	svd.load_model(savefile)
	
	try:
		user_id = input['user_id']
		l = svd.recommend(user_id, n=5, only_unknowns=False, is_row=False) 
		restaurant_data = joblib.load('restaurant_data.pkl') 
		food_id = restaurant_data[1].values

		for food in l:
			a = np.where(food_id[:] == food[0])
			print restaurant_data.as_matrix()[a[0][0]]  
	except KeyError:
		user_data = joblib.load('user_data.pkl')
		food = user_id[2].tolist()
		max_occur = Counter(food)
		val = max_occur.most_common(5)[0][0]
		a = np.where(food[:] == val)
		print restaurant_data.as_matrix()[a[0][0]]


