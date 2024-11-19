import streamlit as st
import langchain_backend

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian", "Chinese", "Italian", "Mexican","American"))


if cuisine:
    response = langchain_backend.generate_name_menu(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(",") #Because the menu has comman separated values. 
    st.write("**Menu Items**")
    
    for item in menu_items:
     st.write("-",item)
     
     
     #This is the main ui file.