import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new  healthy diner.')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 - Omega3 and blueberry Oatmeal')
streamlit.text('🥗 - Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 - Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 - Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list  = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index("Fruit")

#streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index))
#streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected = streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#create a function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  #streamlit.text(fruityvice_response.json())
  # Take the json version response and normalize it
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  # output it the screen as a table
  #streamlit.dataframe(fruityvice_normalized)
  return fruityvice_normalized

# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
  if not fruit_choice:
    stream.error("Please select fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)  
except URLError as e:
  streamlit.error()


#snowflake

streamlit.header("View our fruit list - Add your favorites!")
#Snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
    
# Add a button to load the fruit
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
  
# Allow the end user to add a fruit
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding" + new_fruit
 
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
if streamlit.button("Add a fruit to the list"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text("back from function")
                     
  

streamlit.stop()





