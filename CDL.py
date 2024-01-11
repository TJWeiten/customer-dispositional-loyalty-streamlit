import streamlit as st
import random


class SurveyCDL:
    """
    A class for managing the user's progress through the CDL survey.
    """

    CDL_MEAN = 3.87
    CDL_STD_DEV = 0.66

    def __init__(self: object):
        """
        Initialize the survey with shuffled questions and reset the current question and answers.
        """
        
        self.survey_questions = [
            "Generally, I am someone who likes to be a regular customer of a company or service.",
            "Generally, I am someone who wants to be a steady customer of the same company or service.",
            "I intend to remain loyal to the products or services I like now.",
            "In general, it is easy for me to stay loyal to a brand, product, or service.",
            "Once I have found a product or service that I truly like, I tend to stay with that product or service.",
            "Once I make a commitment to a certain brand, product, or service, I tend to stick with it."
        ]
        random.shuffle(self.survey_questions) # shuffle the survey each time it is taken

        self.current_question = 0
        self.survey_answers = [0] * len(self.survey_questions)


    def build_survey_question(self, question_index: int):
        """
        Builds the Streamlit DOM for presenting a survey question at the given index.

        Args:
            question_index (int): The index of the question to present in the survey.
        """

        st.header(self.survey_questions[question_index], anchor = False)
        st.markdown("---")

        col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])

        with col1:
            answered = st.button(
                "Strongly Disagree", 
                on_click = self.answer_btn_callback, args = (question_index, 1), 
                use_container_width = True
            )
        with col2:
            answered = st.button(
                "Disagree", 
                on_click = self.answer_btn_callback, args = (question_index, 2), 
                use_container_width = True
            )
        with col3:
            answered = st.button(
                "Neutral", 
                on_click = self.answer_btn_callback, args = (question_index, 3), 
                use_container_width = True
            )
        with col4:
            answered = st.button(
                "Agree", 
                on_click = self.answer_btn_callback, args = (question_index, 4), 
                use_container_width = True
            )
        with col5:
            answered = st.button(
                "Strongly Agree", 
                on_click = self.answer_btn_callback, args = (question_index, 5), 
                use_container_width = True
            )

    
    def answer_btn_callback(self, question_index: int, answer: int):
        """
        Called whenever a user clicks on a survey answer button. 
        Takes the user's answer and stores it in the CDL object at the appropriate index.

        Args:
            question_index (int): The index of the question to present in the survey.
            answer (int): The coded value of the user's answer to the question.
        """
        self.survey_answers[question_index] = answer
        self.current_question += 1
        st.empty()
