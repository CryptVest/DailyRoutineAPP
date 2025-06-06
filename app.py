import streamlit as st
import calendar
import datetime

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Calendar", "Dashboard", "Pages"])

# --- Helper: Calendar Grid ---
def calendar_grid(year, month):
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    st.write(f"### {calendar.month_name[month]} {year}")
    for week in month_days:
        cols = st.columns(7)
        for i, day in enumerate(week):
            if day == 0:
                cols[i].empty()
            else:
                if cols[i].button(str(day), key=f"day-{day}"):
                    st.session_state['selected_day'] = day

# --- Main Area ---
if 'selected_day' not in st.session_state:
    st.session_state['selected_day'] = None

if page == "Calendar":
    today = datetime.date.today()
    calendar_grid(today.year, today.month)
    if st.session_state['selected_day']:
        st.write("---")
        st.write(f"## Page for {today.year}-{today.month:02d}-{st.session_state['selected_day']:02d}")
        # Page Editor UI
        title = st.text_input("Title")
        st.write("### Properties")
        # Example: Add/Remove properties (dynamic in future)
        prop1 = st.text_input("Property 1 (Text)")
        prop2 = st.checkbox("Property 2 (Checkbox)")
        st.write("### Content")
        content = st.text_area("Write your notes here...", height=200)
        st.button("Save Page")

elif page == "Dashboard":
    st.write("# Dashboard")
    st.info("Progress tracking and analytics will appear here.")
    # Example: Streaks, charts, etc.

elif page == "Pages":
    st.write("# All Pages")
    st.info("List and search all pages here.")
    # Example: List of pages, search/filter, create new page

# --- Footer ---
st.markdown("---")
st.caption("Notion-like Daily Routine App (Streamlit UI Prototype)")
