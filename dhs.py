import streamlit as st
from math import exp as e
import base64

page = st.sidebar.radio(

    'DHS Library:',
    ['Calculator', 'Example Calculation', 'DHS Tables', 'DHS- The One Solution', 'Complete Documentation']

    )

def calculator():

    global count_view, count_likePost, count_unlike, count_positiveComment
    global count_negativeComment, count_neutralComment, count_share
    global count_likePage, count_reach, count_follower, count_post
    
    box1_view, box2_likePost, box3_unlike = st.columns(3)
    
    box4_positiveComment, box5_negativeComment, box6_neutralComment = st.columns(3)

    box7_share, box8_likePage, box9_reach = st.columns(3)

    box10_follower, box11_post, box11 = st.columns(3)

    with box1_view:
        count_view = st.number_input('Number of Views:')

    with box2_likePost:
        count_likePost = st.number_input('Number of Likes (Post):')

    with box3_unlike:
            count_unlike = st.number_input('Number of Unlikes:')

    with box4_positiveComment:
        count_positiveComment = st.number_input('Number of Positive Comments:')

    with box5_negativeComment:
        count_negativeComment = st.number_input('Number of Negative Comments:')

    with box6_neutralComment:
        count_neutralComment = st.number_input('Number of Neutral Comments:')

    with box7_share:
        count_share = st.number_input('Number of Shares:')

    with box8_likePage:
            count_likePage = st.number_input('Number of Page Likes:')

    with box9_reach:
            count_reach = st.number_input('Number of Reach/Impression:')

    with box10_follower:
            count_follower = st.number_input('Number of Followers:')

    with box11_post:
            count_post = st.number_input('Number of Posts:')

    button_OK = st.button('Calculate DHS',
                          help = 'Press me to calculate the DHS :sunglasses:')

    if button_OK:
        st.write('Your DHS: ', dhs())

def dhs():

    # es = Engagement Score
    es = ((count_view + count_likePost - count_unlike + count_positiveComment -
          count_negativeComment + count_neutralComment + count_share +
          count_likePage) / (count_reach + count_follower) /  (count_post))

    return (e(es)/(1 + e(es))) * 100

def exampleCalculation():
    
    title = '<p style="font-family:calibri; color:Green; font-size: 20px;">Welcome to Example Calculation of DHS</p>'

    st.markdown(title, unsafe_allow_html=True)

    with open ('Example Calculation of DHS.pdf',"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="700" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html = True)


def dhsTables():

    title = '<p style="font-family:calibri; color:Green; font-size: 20px;">Welcome to DHS Tables</p>'

    st.markdown(title, unsafe_allow_html=True)

    with open ('DHS Tables.pdf',"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="700" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html = True)

def dhsTheSolution():

    title = '<p style="font-family:calibri; color:Green; font-size: 20px;">Welcome to DHS- The One Solution</p>'

    st.markdown(title, unsafe_allow_html=True)

    with open ('X:\Enteraction\DHS\DHS- Problem Statement with Proposed Solution.pdf',"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="700" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html = True)

def completeDocumentation():

    title = '<p style="font-family:calibri; color:Green; font-size: 20px;">Welcome to Complete Documentation of DHS</p>'

    st.markdown(title, unsafe_allow_html=True)

    with open ('X:\Enteraction\DHS\DHS Documentation.pdf',"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="700" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html = True)


def main():
    
    if page == 'Calculator':
        calculator()

    elif page == 'Example Calculation':
        exampleCalculation()

    elif page == 'DHS Tables':
            dhsTables()

    elif page == 'Complete Documentation':
        completeDocumentation()

    elif page == 'DHS- The One Solution':
        dhsTheSolution()
        
main()
