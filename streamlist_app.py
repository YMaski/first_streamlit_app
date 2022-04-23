import streamlit
streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
# Let's put a Pick list here so that they can pick a fruit they want

fruits_selected = streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.index), ['Avacado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the table on the page
streamlit.dataframe(fruits_to_show)

