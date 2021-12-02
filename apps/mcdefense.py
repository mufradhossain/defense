import streamlit as st
import sqlite3
def app():
    conn = sqlite3.connect('diucse.db')


    def teamview(id):

        cur= conn.cursor()
        cur.execute("select Team_Name,Leader_Name,Leader_Id,Leader_Image,Member_one_Name,Member_one_Id,Member_one_Image,Member_two_Name,Member_two_Id,Member_two_Image,Title,Supervisor,`Co-Supervisor`,Description,Objective,Motivation from mcdefense where Leader_Id = '"+str(id)+"'")
        hol=cur.fetchone()
        #st.header(hol[0])
        #
        with st.expander(hol[0], expanded=True):
            st.subheader("Title: "+hol[10])
            col1, col2, col3 = st.columns(3)
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
            with col3:
                try:
                    st.image(hol[9],width=200)
                    st.write(hol[7])
                    st.write("ID: "+hol[8])
                except:
                    pass
            st.info("**Supervisor** : "+hol[11])
            st.info("**Co-Supervisor** : "+hol[12])
            st.write("**Description** : "+hol[13])
            st.write("**Objective** : "+hol[14])
            st.write("**Motivation** : "+hol[15])
        return


    m = range(12059,13028)
    for n in m:
        try:
            teamview("191-15-"+str(n))
        except:
            pass