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

streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
