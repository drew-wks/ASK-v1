import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from pathlib import Path
import os 
import base64
import utils

st.set_page_config(page_title="ASK Library", initial_sidebar_state="collapsed")

st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: visible;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("""
        <style>
                .block-container {
                    padding-top: 1rem;
                    padding-bottom: 1rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }
        </style>
        """, unsafe_allow_html=True)



def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()



st.image("https://raw.githubusercontent.com/drew-wks/ASK/v1/images/ASK_logotype_color.png?raw=true", use_column_width="always") # use_container_width=True instead in streamlit >1.4

back = st.button("< Back to App", type="primary")
if back:
    switch_page("ui")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Library", "FAQs", "Product Roadmap", "Feedback"])

with tab1:
    overview = read_markdown_file("docs/ask_overview.md")
    st.markdown(overview, unsafe_allow_html=True)
    

with tab2:
    try:
        df, last_update_date = utils.get_library_doc_catalog_excel_and_date()
    except Exception as e:
        os.write(1, f"Failed to read the Excel file: {e}\n".encode())
        
    overview = read_markdown_file("docs/library_overview.md")

    if df is not None:
        num_items = len(df)
        st.markdown("#### Library Overview")
        st.markdown(f"ASK is loaded with **{num_items}** national documents (almost 9000 pages) including USCG Directives, CHDIRAUX documents and documents issued by the USCG Auxiliary National leadership. All these documents are located in public sections of the USCG and USCG Auxiliary websites (cgaux.org uscg.mil).  No secure content is included (i.e., content requiring Member Zone or CAC access. All documents are national. Regional requirements may vary, so check with your local AOR leadership for the final word. ")
        st.markdown(f"{overview}")
        st.markdown("#### Library Catalog")
        st.markdown(f"{num_items} items. Last update: {last_update_date}")  

        # Display the DataFrame
        display_df = df[['title']]
        edited_df = st.data_editor(display_df, use_container_width=True, hide_index=False, disabled=True)
        isim = f'document_catalog_download_{last_update_date}.csv'
        indir = edited_df.to_csv(index=False)
        b64 = base64.b64encode(indir.encode(encoding='utf-8')).decode()
        linko_final = f'<a href="data:file/csv;base64,{b64}" download="{isim}">Click to download the catalog</a>'
        st.markdown(linko_final, unsafe_allow_html=True)

    else:
        # Display the original markdown file content if df is None
        overview = read_markdown_file("docs/library_overview.md")
        st.markdown(overview, unsafe_allow_html=True)


with tab3:
    overview = read_markdown_file("docs/faqs.md")
    st.markdown(overview, unsafe_allow_html=True)

with tab4:
    roadmap = read_markdown_file("docs/roadmap.md")
    st.markdown(roadmap, unsafe_allow_html=True)
    
with tab5:
    st.markdown("#### Feedback")
    st.markdown("ASK's mission is to provide USCG Auxiliary members efficient, accuracete and easy access to the authoritative source of knowledge on any topic in the Auxiliary.")
    st.markdown('If you would like to help ASK acheive this mission, **please reach out!**')
                
    st.markdown('''Presently, ASK works by analyzing documents that are the most current official policy that exists at a national level. 
            If you see a document missing from the libary or should be removed, please let us know.''')  
    
    st.markdown('''If you find an error or ommision in a response, please let me know. Be sure to include the exact question asked
            and a reference to the applicable policy (doc and page).''')  
                
    st.markdown('Send an email to uscgaux.drew@wks.us.''')
