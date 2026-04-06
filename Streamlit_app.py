# Import python packages.
import streamlit as st
#from snowflake.snowpark.context import  get_active_session
from snowflake.snowpark.functions import  col

# Write directly to the app.
st.title(f":cup_with_straw: Customize Your Smoothie:cup_with_straw:")
st.write(
  """Choose the fruits you want in custom smoothie
  """
)

#option = st.selectbox('What is the Fruit?', ('Banana' + ':banana:', 'Strawberries' + ':strawberries:','Peaches'+ ':peaches:'))

#st.write('Your favorite friut is ', option )
name_on_order = st.text_input('Name on Smoothie')
st.write(' The name on smoothie will be :', name_on_order)

#session = get_active_session()
cnx = st.connection('snowflake')
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options") .select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredient_list = st.multiselect('Choose up the ingredients', 
                                 my_dataframe,
                                 max_selections=5)
#st.write(ingredient_list)

if ingredient_list:
    ingredients_string = ''
    for fruits_choosen in ingredient_list:
        ingredients_string += fruits_choosen +' ';
    st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
                    values ('""" + ingredients_string + "" "', '""" + name_on_order + "" "')"""

    st.write(ingredient_list)
    
    time_to_insert = st.button('Submit Order')
    
    #st.write(my_insert_stmt)
    if time_to_insert:
        #st.write('inserted properly')
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
import requests  
#smoothiefroot_response = requests.get("[https://my.smoothiefroot.com/api/fruit/watermelon](https://my.smoothiefroot.com/api/fruit/watermelon)")  
try:
  smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
  st.text(smoothiefroot_response.status_code)
  st.text(smoothiefroot_response.json())
  sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
  st.write(sf_df)
except Exception as e:
  st.write('error is : ', {e})
    
  #st.write(ingredient_list)
  #st.text(ingredient_list)
    
    
      
      
