import streamlit as st
import src.pages.home
import src.pages.data
import src.pages.dashboard
import src.pages.contribute
import src.pages.about


PAGES = {
    "Home": src.pages.home,
    "Data": src.pages.data,
    "Dashboard": src.pages.dashboard
}

def main():
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
    PAGES[choice].main()
    
if __name__ == "__main__":
    main()
