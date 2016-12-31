#Food recommender system 

Steps: 

- Run setup function. Need to run just once. 

- To enter the details of restaurant: 
  - Function : restaurant_details
  - input format :   { 'rest_id':'None' 'food_id':None 'food_detail':None 'food_category_id':None }	 
  		where, 
  		-rest_id represent a particular restaurant (data type : int)
  		-food id represent the food item and is unique for each and every dish. (data type : int)
  		-in food details, abstract food details can be added. (data type : strings,int)
  		- food category consists of the genres in which the particular dish falls in data type : strings, list)

- To account for each transaction:
	- Function : user_data
	- input format:  {'rest_id': 'None',  'user_id':'None' , 'food_id':'None'} 
		where, 
		- rest_id represent a particular restaurant (data type : int)
		- user_id represents the user 
		- food_id is the dish he ordered. 

- The system will update the training model every 12 hours. To update the system :
	- function: update
	  input : None

- To recommend : 
	- Function: predict
	- Input format: {'rest_id': 'None', 'user_id':'None'}
		where, 
		- rest_id represent a particular restaurant (data type : int)
		- user_id represents the user (datatype : int)

