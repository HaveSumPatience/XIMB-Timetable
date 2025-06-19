import streamlit as st
import pandas as pd
import datetime

# Data for subjects, faculty, and classrooms
subjects_data = {
    "Semester": [
        "4", "4", "4", "4", "4", "4", "4", "4",  # 4th Semester
        "5", "5", "5", "5", "5",                 # 5th Semester
        "6", "6", "6"                            # 6th Semester
    ],
    "Abbreviation": [
        "SCAS", "ETSU", "PROM", "SDM", "B2BM", "PAW", "CORE", "SAPM",
        "CRM", "DVM", "VIB", "FISM", "SCM",
        "FAME", "RM", "ASCM"
    ],
    "Subject Name": [
        "Strategy Capstone Simulation",
        "Ethics and Sustainability",
        "Project Management",
        "Sales and Distribution Management",
        "B2B Marketing",
        "Project Appraisal and Working Capital Management",
        "Corporate Restructuring",
        "Security Analysis and Portfolio Management",
        "Customer Relation Management",
        "Data Visualization for Managers",
        "Valuation and Investment Banking",
        "Fixed Income Securities and Markets",
        "Supply Chain Management",
        "Financial Analysis with Modeling in Excel",
        "Retail Management",
        "Advanced Supply Chain Management"
    ],
    "Room": [
        "CR-56", "CR-164", "CR-56", "CR-56", "CR-404", "CR-404", "CR-403", "CR-144",
        "NA", "NA", "NA", "NA", "NA",
        "NA", "NA", "NA"
    ],
    "Faculty": [
        "Prof. Anshuman Tripathy",
        "Prof. SS Ganesh",
        "Prof. Arun K Paul",
        "Prof. Punyashlok Dhall",
        "Prof. Soumya Sarkar",
        "Prof. Punam Prasad",
        "Prof. Prince Bhatia",
        "Prof. PC Pati",
        "Prof. Rajesh Panda, Prof. KD Gupta",
        "Prof. Shabana Chandrasekaran",
        "Prof. Punam Prasad",
        "Prof. RK Dubey",
        "Prof. AK Paul, Prof. Arijit Mitra",
        "Prof. RK Dubey",
        "Prof. Nirali Shah",
        "Prof. Sarat Kumar Jena"
    ]
}

# Create a DataFrame for display
subjects_df = pd.DataFrame(subjects_data)

st.title("2nd Year Schedule")

# Define time slots and days
time_slots = [
    "8:00 - 9:30 AM",
    "10:00 - 11:30 AM",
    "12:00 - 1:30 PM",
    "3:00 - 4:30 PM",
    "5:00 - 6:30 PM",
    "7:00 - 8:30 PM",
    "8:45 - 10:15 PM"
]

days = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

# Timetable data (7 days x 7 slots) for 4th semester
timetable = [
    # Monday
    ["", "", "CORE", "SDM", "", "PAW", ""],
    # Tuesday
    ["", "SAPM", "", "", "", "B2BM", ""],
    # Wednesday
    ["", "", "", "PROM", "ETSU", "SCAS", ""],
    # Thursday
    ["", "", "CORE", "SDM", "", "PAW", ""],
    # Friday
    ["", "SAPM", "", "", "", "B2BM", ""],
    # Saturday
    ["", "", "", "PROM", "ETSU", "SCAS", ""],
    # Sunday
    ["RESERVED", "RESERVED", "RESERVED", "RESERVED", "RESERVED", "RESERVED", "RESERVED"]
]

# Tabs for semesters
tab4, tab5, tab6, tab_subjects = st.tabs(["4th Semester", "5th Semester", "6th Semester", "Subjects"])

# Function to get current slot index based on current time
def get_current_slot_index():
    now = datetime.datetime.now()
    current_time = now.time()
    slot_times = [
        (8, 0, 9, 30),
        (10, 0, 11, 30),
        (12, 0, 13, 30),
        (15, 0, 16, 30),
        (17, 0, 18, 30),
        (19, 0, 20, 30),
        (20, 45, 22, 15)
    ]
    for idx, (start_h, start_m, end_h, end_m) in enumerate(slot_times):
        start = datetime.time(start_h, start_m)
        end = datetime.time(end_h, end_m)
        if start <= current_time <= end:
            return idx
    return None

# Function to get current day index (Monday=0, ..., Sunday=6)
def get_current_day_index():
    return datetime.datetime.now().weekday()

with tab4:
    st.subheader("Weekly Timetable")
    timetable_df = pd.DataFrame(timetable, columns=time_slots)
    timetable_df.insert(0, "Day", days)
    st.dataframe(timetable_df, hide_index=True)  # Removes row numbers

    # --- Where do I need to be now? ---
    slot_idx = get_current_slot_index()
    day_idx = get_current_day_index()
    if day_idx < len(timetable) and slot_idx is not None:
        subject = timetable[day_idx][slot_idx]
        if subject and subject != "RESERVED":
            st.success(f"Current subject: **{subject}**")
        elif subject == "RESERVED":
            st.info("All slots are reserved today.")
        else:
            st.info("No class scheduled for the current slot.")
    else:
        st.info("No class scheduled for the current time.")

with tab5:
    st.markdown("<h2 style='text-align: center; color: red;'>Semester not started yet</h2>", unsafe_allow_html=True)

with tab6:
    st.markdown("<h2 style='text-align: center; color: red;'>Semester not started yet</h2>", unsafe_allow_html=True)

with tab_subjects:
    st.subheader("Subjects, Faculty, and Classrooms")
    st.dataframe(subjects_df, hide_index=True)

# Get current date and time
now = datetime.datetime.now()

# Get current day name (e.g., 'Monday')
current_day = now.strftime("%A")

# Get current time (e.g., '14:35')
current_time = now.strftime("%H:%M")

st.write(f"Today is {current_day}, current time: {current_time}")