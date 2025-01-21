import streamlit as st

#stremlist UI
st.title("Example uI as in streamlit")
st.write("Enter a number to calcualte its square, cube and fifth power.")


#Get user Input
n = st.number_input("Enter an Integer",value=1,step=1)

# caluate results
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The square of {n} : {square}")
st.write(f"The cube of {n} : {cube}")
st.write(f"The fifth power of {n} : {fifth_power}")
