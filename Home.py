# import stream lit
import streamlit as st



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
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "Data Analytics Center - Algonquin College"
        }
    )
    col1, col2, col3, col4 = st.columns(4)

    with col4:
        st.image('images/dac.png', width=500)





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
    uploaded_file = st.file_uploader("Upload your data")


##################################################
#
# entry point
#
##################################################
if __name__ == "__main__":
    main()

