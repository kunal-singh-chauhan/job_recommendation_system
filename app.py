import pandas as pd
import streamlit as st
import pickle

df = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def user_page():
  def recommendation(title):
    idx = df[df['Title']==title].index[0]
    idx = df.index.get_loc(idx)
    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x)[1:20]

    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)
    return jobs
  

  st.title('Job Recommendation System')
  title = st.selectbox('Search Job',df['Title'])
  search_button = st.button("Search")
  if search_button:
    jobs = recommendation(title)
    if jobs:
      st.write(jobs)
  jobs = recommendation(title)

  if jobs:
    st.write(jobs)

  


def admin_page():
    st.title("Admin Page")
    st.title('CSV File Uploader')

    uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
    if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
      data = pd.read_csv(uploaded_file)
    
      st.write(data)
      serialized_data=pickle.dumps(data)
      with open('serialized_data.pkl','wb') as f:
        f.write(serialized_data)


def main():
    # Sidebar to select user type
    user_type = st.sidebar.radio("Select User Type", ("User", "Admin"))

    # Display page based on user selection
    if user_type == "User":
        user_page()
    elif user_type == "Admin":
        admin_page()

if __name__ == "__main__":
    main()


