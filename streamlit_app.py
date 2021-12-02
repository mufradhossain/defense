import streamlit as st
import sqlite3

conn = sqlite3.connect('diucse.db')


def teamview(id):

    cur= conn.cursor()
    cur.execute("select Team_Name,Leader_Name,Leader_Id,Leader_Image,Member_Name,Member_Id,Member_Image,Title,Supervisor,`Co-Supervisor`,Description,Objective,Motivation from defense where Leader_Id = '"+str(id)+"'")
    hol=cur.fetchone()
    #st.header(hol[0])
    #
    with st.expander(hol[0],expanded=True):
        st.subheader("Title: "+hol[7])
        col1, col2 = st.columns(2)
        with col1:
            st.image(hol[3],width=200)
            st.write(hol[1]+" (Leader)")
            st.write("ID: "+hol[2])
        with col2:
            try:
                st.image(hol[6],width=200)
                st.write(hol[4])
                st.write("ID: "+hol[5])
            except:
                pass
        st.info("**Supervisor** : "+hol[8])
        st.info("**Co-Supervisor** : "+hol[9])
        st.info("**Description** : "+hol[10])
        st.info("**Objective**: "+hol[11])
        st.info("**Motivation**: "+hol[12])
    return


m = range(2341,2774)
for n in m:
    try:
        teamview("191-15-"+str(n))
    except:
        pass
