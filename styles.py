import streamlit as st


def css_overrides():
    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none;
            }
            .block-container {
                max-width: 60em;
            }
            .pseudo-h1 {
                font-weight: 700;
                padding: 1.25rem 0px 1rem;
                margin: 0px;
                line-height: 1.2;
                font-size: calc(2rem + 1.8vw);
                text-align: center;
            }
            .pseudo-h2 {
                font-weight: 700;
                padding: 1.25rem 0px 1rem;
                margin: 0px;
                line-height: 1.2;
                font-size: calc(1.2rem + 1.8vw);
                text-align: center;
            }
            .pseudo-h3 {
                font-weight: 700;
                padding: 1.25rem 0px 1rem;
                margin: 0px;
                line-height: 1.2;
                font-size: calc(1.4rem);
            }
            .justified {
                text-align: justify;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
