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
        <p class='pseudo-h3'>Overview</p>

        <p class='justified'>
        <em><b>Customer loyalty</b></em> is a “collection of attitudes aligned with a series of purchase behaviors 
        that systematically favor one entity over competing entities” (Watson et al. 2015, p. 733).
        </p>
        
        <p class='justified'>
        While academics and practitioners have defined and measured a customer's loyalty 
        in terms of their attitudes and behaviors, we reason that loyalty is also a trait or disposition variable. 
        That is, a customer has a dispositional loyalty toward marketplace offerings. 
        Formally, we define <em><b>customer dispositional loyalty</b></em> as a stable disposition that drives some 
        customers to be more inclined to commit to a brand, product, or service, and remain committed to it, 
        despite situational factors that might otherwise lead to switching behavior.
        </p>
        
        <p class='justified'>
        This website accompanies our research manuscript, 
        which conceptualizes customer dispositional loyalty, 
        provides a six-item scale to measure an individual customer's dispositional loyalty, 
        and offers experimental evidence on the effect of a customer's dispositional loyalty 
        on their likelihood of forgiving a transgressor brand.
        </p>
        
        <p class='justified'>
        You can use this website to 
        <b>(1)</b> answer the six items that comprise the dispositional loyalty scale and 
        <b>(2)</b> score yourself on dispositional loyalty.
        </p>

        <b>References:</b>

        Watson, George F, Joshua T Beck, Conor M Henderson, and Robert W Palmatier (2015), "Building, measuring, and profiting from customer loyalty," Journal of the Academy of Marketing Science, 43 (6), 790-825. https://link.springer.com/article/10.1007/s11747-015-0439-4

        <hr>
        """,
        unsafe_allow_html = True
    )

    if st.button("See how you fall on the dispositional loyalty scale!", type="primary", use_container_width = True):
        switch_page("survey")


if __name__ == "__main__":
    main()
    