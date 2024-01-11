import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from statistics import mean

from styles import css_overrides
from CDL import CDL


# if the home page has not yet been viewed in this session, take them to the introduction page
if "intro_viewed" not in st.session_state:
    switch_page("home")


def main():
    css_overrides()
    survey = st.session_state.survey

    # if survey is not yet complete, ask the current question
    if survey.current_question < len(survey.survey_questions):
        survey.build_survey_question(survey.current_question)

    # otherwise, display the results
    else: 
        survey_results(survey)


def survey_results(survey: CDL):
    """
    Displays the results of the survey.

    Args:
        survey (CDL): The survey object that contains details about the user's progress through the survey.
    """

    # z-score categories
    cdl_categories = ["very low", "low", "slightly below average", "average", "slightly above average", "high", "very high"]

    cdl_mean = mean(survey.survey_answers)
    z_score = round((cdl_mean - CDL.CDL_MEAN) / CDL.CDL_STD_DEV, 2)

    # pick an index in the middle of the list and adjust by z-score
    z_score_index = (len(cdl_categories) // 2) + int(z_score/0.5) 
    if z_score_index < 0:
        z_score_index = 0
    elif z_score_index >= len(cdl_categories):
        z_score_index = len(cdl_categories) - 1
    
    # display results
    st.header(f"Your Dispositional Loyalty score is *{cdl_categories[z_score_index]}*!")
    st.markdown(
        """
        ---
        **What does this mean?**

        """
    )
    st.markdown(f"You scored **{cdl_mean:.2f}** on our Dispositional Loyalty scale! \
                Based on results from our scale development and validation study, \
                we determined you fell into a category {z_score:.2f} standard deviations away from the mean. \
                This means that you are **{cdl_categories[z_score_index]}** in terms of your \
                dispositional loyalty relative to our study averages.")
    st.markdown("---")
    
    # return the user to the home page and reset state
    if st.button("Return to the home page!", type="primary", use_container_width = True):
        st.session_state.survey = CDL()
        switch_page("home")


if __name__ == "__main__":
    main()
