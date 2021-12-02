import streamlit as st
from multiapp import MultiApp
from apps import dscdefense, mcdefense

app = MultiApp()


# Add all your application here
app.add_app("DSC", dscdefense.app)
app.add_app("CITY", mcdefense.app)
# The main app
app.run()
