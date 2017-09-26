# Food recommender system 

## Steps: 

- **Run setup function. Need to run just once**

- **To enter the details of restaurant**: 
  - **Function** : _restaurant_details_
  - **input format** :   { _rest_id_:None _food_id_:None _food_detail_:None _food_category_id_:None }	 
  		where, 
  		-_rest_id_ represent a particular restaurant (data type : int)
  		-_food id_ represent the food item and is unique for each and every dish. (data type : int)
  		-in _food_details_, abstract food details can be added. (data type : strings,int)
  		-_food_category_ consists of the genres in which the particular dish falls in data type : strings, list)

- **To account for each transaction**:
	- **Function** : _user_data_
	- **input format**:  {_rest_id_: 'None',  _user_id_:'None' , _food_id_:'None'} 
		where, 
		- _rest_id_ represent a particular restaurant (data type : int)
		- _user_id_ represents the user 
		- _food_id_ is the dish he ordered. 

- **The system will update the training model every 12 hours. To update the system:**
	- **Function**: _update_
	  **input** : None

- **To recommend:** 
	- **Function**: _predict_
	- **Input format**: {_rest_id_: 'None', _user_id_:'None'}
		where, 
		- _rest_id_ represent a particular restaurant (data type : int)
		- _user_id_ represents the user (datatype : int)

