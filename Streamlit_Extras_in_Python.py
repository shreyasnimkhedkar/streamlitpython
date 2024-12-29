import streamlit as stm
from streamlit_extras import add_vertical_space as avs

# 1). CREATE A SIMPLE STREAMLIT WEB APP

stm.set_page_config(page_title="This is a simple sreamlit web app")
stm.title("Ths is the Home page of Shreyas Project.")
stm.text("Project Home page")

# 2). Adding vertical space in our WebApp
# We will now add ‘n’ amount of vertical spaces in our web app using the add_vertical_space() function.

# Text before putting space 

stm.write("The text after which we will put spaces")
avs.add_vertical_space(5)
stm.write("The text after putting spaces")

# 3). Adding annotated strings in our WebApp

# Need to import librarys (import annotated_text as ant,  from annotated_text import annotation)

import annotated_text as ant
from annotated_text import annotation

ant.annotated_text(
    "Hey",
    annotation("Shreyas Project",color='#07a631'),
    ('is', 'The', 'Blue'),
    annotation("Best",border='3px groove yellow'),
    annotation("for", "EVERYTHING", color='#f7f8fa'))


# 4). Add buymeacoffee button in our WebApp


from streamlit_extras.buy_me_a_coffee import button

button(username="Shreyas", floating=False, width=250)

# 5). Add a clickable card in your WebApp

from streamlit_card import card

card(
    title="Shreyas Project",
    text="click this card Shreyas Project",
    image="shreyas_project.jpg",
    url = "https://shreyas.home.blog/",
)


# 6). Adding Filter to our DataFrame

# from streamlit_extras.dataframe_explorer import dataframe_explorer 
# import pandas as pd

# df = pd.read_csv('iris_dataset.csv')
# filtered_df = dataframe_explorer(df)
# stm.dataframe(filtered_df,use_container_width=True)



# from streamlit_extras.keyboard_url import keyboard_to_url 
# from streamlit_extras.keyboard_text import key 


# keyboard_to_url(key='G', url="https://shreyas.home.blog/")
# stm.write(
#     f"""Now hit {key("G", False)} on your keyboard....!""",
#     unsafe_allow_html=True,
# )


# # 7). create emoji

# from streamlit_extras.let_it_rain import rain 
  
  
# stm.set_page_config(page_title="This is a Simple Streamlit WebApp") 
# stm.title("This is the Home Page Geeks.") 
# stm.text("Geeks Home Page") 
  
  
# # Raining Emoji 
  
# rain( 
#     emoji="<copy paste an emoji from any site like emojipedia or iemoji>", 
#     font_size=40,  # the size of emoji 
#     falling_speed=3,  # speed of raining 
#     animation_length="infinite",  # for how much time the animation will happen 
# ) 


