import streamlit as st
import calendar
import datetime

# --- Helper: Initialize session state for pages ---
if 'pages' not in st.session_state:
    st.session_state['pages'] = {}  # key: (year, month, day), value: page data

if 'selected_date' not in st.session_state:
    st.session_state['selected_date'] = None

# --- Month/Year Selection ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Calendar", "Dashboard", "Pages"])

if page == "Calendar":
    st.title("Monthly Calendar")
    year = 2025
    months = list(calendar.month_name)[1:]
    month_idx = st.selectbox("Select Month", range(1, 13), format_func=lambda x: months[x-1])
    month_name = months[month_idx-1]

    st.write(f"## {month_name} {year}")

    # --- Calendar Table ---
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month_idx)
    day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    st.write("| " + " | ".join(day_names) + " |")
    st.write("|" + "|".join([" :---: "]*7) + "|")

    for week in month_days:
        row = []
        for i, day in enumerate(week):
            if day == 0:
                row.append(" ")
            else:
                key = (year, month_idx, day)
                if key in st.session_state['pages']:
                    # Page exists: show clickable day number
                    btn = st.button(f"{day}", key=f"day-{day}-{month_idx}", help="View Page")
                    if btn:
                        st.session_state['selected_date'] = key
                    row.append(f"**{day}**")
                else:
                    # No page: show + button
                    plus_btn = st.button(f"+", key=f"plus-{day}-{month_idx}", help="Add Page")
                    if plus_btn:
                        st.session_state['selected_date'] = key
                        st.session_state['pages'][key] = {}  # Create empty page
                    row.append(f"{day} [+]")
        st.write("| " + " | ".join(row) + " |")

    # --- Page Editor ---
    if st.session_state['selected_date']:
        key = st.session_state['selected_date']
        st.write("---")
        st.write(f"## Page for {key[0]}-{key[1]:02d}-{key[2]:02d}")
        title = st.text_input("Title", value=st.session_state['pages'][key].get('title', ''), key="title")
        st.session_state['pages'][key]['title'] = title
        st.write("### Properties")
        prop1 = st.text_input("Property 1 (Text)", value=st.session_state['pages'][key].get('prop1', ''), key="prop1")
        st.session_state['pages'][key]['prop1'] = prop1
        prop2 = st.checkbox("Property 2 (Checkbox)", value=st.session_state['pages'][key].get('prop2', False), key="prop2")
        st.session_state['pages'][key]['prop2'] = prop2
        st.write("### Content")
        content = st.text_area("Write your notes here...", value=st.session_state['pages'][key].get('content', ''), height=200, key="content")
        st.session_state['pages'][key]['content'] = content
        st.button("Save Page")
