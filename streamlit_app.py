import streamlit as st
import sqlite3

conn = sqlite3.connect('diucse.db')


def teamview(id):

    cur= conn.cursor()
    cur.execute("select Team_Name,Leader_Name,Leader_Id,Leader_Image,Member_Name,Member_Id,Member_Image,Title,Supervisor,`Co-Supervisor` from defense where Leader_Id = '"+str(id)+"'")
    hol=cur.fetchone()
    st.header(hol[0])
    col1, col2 = st.columns(2)
    with col1:
        st.image(hol[3],width=150)
        st.write(hol[1]+" (Leader)")
        st.write("ID: "+hol[2])
    with col2:
        try:
            st.image(hol[6],width=150)
            st.write(hol[4])
            st.write("ID: "+hol[5])
        except:
            pass

    st.subheader("Title: "+hol[7])
    st.write("Supervisor: "+hol[8])
    st.write("Co-Supervisor: "+hol[9])
    return


m = range(2341,2774)
for n in m:
    try:
        teamview("191-15-"+str(n))
    except:
        pass
