import streamlit
streamlit.title('My parents new  healthy diner.')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 - Omega3 and blueberry Oatmeal')
streamlit.text('🥗 - Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 - Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 - Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list  = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index("Fruit")

#streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index))
#streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected = streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

