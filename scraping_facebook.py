

from facebook_scraper import get_posts , get_profile
import pandas as pd
import requests
from PIL import Image
import streamlit as st

st.title('Facebook Scraper')
st.subheader('Scrape posts from pages')

search_term = st.text_input('Enter Page name','nintendo')
num_pages = st.number_input('Enter number of pages of posts to request ',2)
if st.button('Show Posts'):  
	if search_term:
		for post in get_posts(search_term, pages=num_pages,cookies='cookies.txt'):
			st.markdown('Post content: ' + post['text'] )
			st.markdown('Count of Likes: ' + str(post['likes']))
			st.markdown('Count of Comments: ' + str(post['comments']))
			st.markdown('Count of Shares: ' + str(post['shares']))
			st.markdown('Post url: ' + post['post_url'])



st.subheader('Scrape accounts')
account = st.text_input('Enter account name','zuck')


if st.button('Show account details'):

	if account:
		try:
			my_dict = get_profile(account,cookies='cookies.txt')
			df = pd.DataFrame(list(my_dict.items()))
			st.image(Image.open(requests.get(my_dict.get('profile_picture'), stream=True).raw), width=300)
			st.markdown('ID number: ' + df[1][0])
			st.markdown('Name :' + df[1][4])
			

			st.markdown('Work :' + ' '.join(df[1][5].split('\n')))
			st.markdown('Education: ' + ' '.join(df[1][6].split('\n')))
			st.markdown('Places lived: ' + ' '.join(df[1][7].split('\n')))

			st.markdown('About :' + df[1][11])
			st.markdown('Favourite Quotes: ' + df[1][13])
		except:
			st.error('Please enter a valid account')
		


