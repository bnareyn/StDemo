# import stream lit
import streamlit as st
import streamlit.components.v1 as components

import numpy as np
import pandas as pd

import os

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    #MainMenu {visibility: hidden;}
</style>
"""

def cleanupFolder(folderName):
    try:
        files = os.listdir(path = folderName)

        for file in files:
            fileName = os.path.join(folderName, file)
            os.unlink(fileName)

    except Exception as e:
        print(e)


##################################################
#
# set configs
#
##################################################
def setAppConfigs():
    """
       arguments: None
       returns: None
    """
    st.set_page_config(
        page_title="DACBoard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "Data Analytics Center - Algonquin College"
        }
    )

    #st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    genre = st.radio("",("BYOD", "Kaggle", "DAC"), horizontal = True)

    col1, col2, col3, col6 = st.columns(4)
    #with col1:
        #st.write("🗃️ BYOD")
    
    #with col2:
    #    st.write("🇰 Kaggle")
    
    #with col3:
    #    st.write("DAC")

    with col6:
        st.image('images/dac.png', width=500)
    
    uploaded_file = None
    if genre == "BYOD":
        uploaded_file = st.file_uploader("Upload your data")
    elif genre == "Kaggle":
        st.write("Kaggle")
    else:
        st.write("DAC")
    
    from autoviz.AutoViz_Class import AutoViz_Class
    autoViz = AutoViz_Class()

    viz = None
    folderName = "./AutoViz_Plots/AutoViz"
    fileName = "uploaded.csv"
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file, encoding = 'latin1')
        #st.write(list(dataframe.columns))
        dataframe.to_csv(fileName)

        # cleanup plots folder
        cleanupFolder( folderName )

        # Create vizualizations
        avDF = autoViz.AutoViz( fileName, sep=",", 
        dfte=None, header=0, verbose=0, lowess=False, 
        chart_format="html", max_rows_analyzed=2000, max_cols_analyzed=20, )
        print(autoViz.overall)

        # Display visualizations
        
        files = os.listdir(path = folderName)

        #for file in files:
        #    fileName = os.path.join(folderName, file)
        #    with open( fileName ) as f:
        #        html = f.read()
        #        components.html(html, height = 200)
        tabNames = [ name.split('.')[0].title() for name in files]
        tabs = st.tabs(tabNames)
        for tab, file in zip(tabs, files):
            with tab:
                fileName = os.path.join(folderName, file)
                with open( fileName ) as f:
                    html = f.read()
                    components.html(html, height = 900)



                




    
    #files = os.listdir(path='.')
    #st.write(files)

    #files = os.listdir(path='./AutoViz_Plots/AutoViz')
    #st.write(files)
    
    #if viz == "Bar":
    #    st.write("bar")
    #elif viz == "Pie":
    #    st.write("Pie")
    #elif viz == "Map":
    #    st.write("Map")
    #else:
    #    pass

 




##################################################
#
# main method
#
##################################################
def main():
    """
       arguments: None
       returns: None
    """
    setAppConfigs()
    



    #st.image()


##################################################
#
# entry point
#
##################################################
if __name__ == "__main__":
    main()

