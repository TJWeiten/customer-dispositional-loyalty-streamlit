import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from styles import css_overrides
from CDL import SurveyCDL


# initialize the CDL object in the session state
st.set_page_config(page_title="Customer Dispositional Loyalty", initial_sidebar_state="collapsed")
if "intro_viewed" not in st.session_state:
    st.session_state.intro_viewed = True
    st.session_state.survey = SurveyCDL()


def main():
    """
    Build the DOM of the home page.
    """
    css_overrides()
    home_content()


def home_content():
    """
    Displays home page content.
    """

    st.markdown(
        """                                                     
        <p class='pseudo-h1'>How Loyal Are <em>You</em>?</p>
        <p class='pseudo-h2'>A Scale for Measuring a Customer's</br><em>Dispositional Loyalty</em></p>
        <hr>
        """, 
        unsafe_allow_html = True
    )

    st.markdown(
        """
        <p class='pseudo-h3'>Overview</h3>

        <p class='justified'>
        Despite the importance of customer loyalty and considerable research attention accorded to it, 
        findings concerning the origins of loyalty are inconsistent. 
        We reason that loyalty stems from not only firm-specific antecedents, 
        but also a customer-specific trait that we name <b>dispositional loyalty</b>. 
        </p>

        <p class='justified'>
        In our research project, we not only define dispositional loyalty, 
        but also develop and validate a scale for its measurement.
        </p>
        
        <p class='justified'>
        In conceptualizing dispositional loyalty, we extend the discipline's knowledge of brand loyalty. 
        Unlike the attitudinal and behavioral dimensions of loyalty, which are specific to a firm/brand, 
        dispositional loyalty is generalizable across consumption domains 
        and can be useful for market research and consulting firms in segmenting markets.
        </p>

        <p class='justified'>
        We present this accomanying website to provide a brief overview of our research project 
        and to allow you to take the scale we developed to measure dispositional loyalty.
        </p>
        <hr>
        """,
        unsafe_allow_html = True
    )

    if st.button("See how you fall on the dispositional loyalty scale!", type="primary", use_container_width = True):
        switch_page("survey")


if __name__ == "__main__":
    main()
    