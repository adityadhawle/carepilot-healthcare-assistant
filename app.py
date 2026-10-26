import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date
import uuid

# -----------------------------
# App configuration
# -----------------------------
st.set_page_config(
    page_title="CarePilot | Healthcare Assistant",
    page_icon="🏥",
    layout="wide",
)

# -----------------------------
# Data configuration
# -----------------------------
DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "appointments.csv"

DATA_DIR.mkdir(exist_ok=True)

COLUMNS = [
    "appointment_id",
    "patient_name",
    "email",
    "appointment_date",
    "reason",
    "status",
]


def load_appointments():
    """Load appointment records from the CSV file."""
    if not DATA_FILE.exists():
        return pd.DataFrame(columns=COLUMNS)

    try:
        df = pd.read_csv(DATA_FILE, dtype=str)
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame(columns=COLUMNS)

    for column in COLUMNS:
        if column not in df.columns:
            df[column] = ""

    return df[COLUMNS].fillna("")


def save_appointment(patient_name, email, appointment_date, reason):
    """Save a new appointment to the CSV file."""
    df = load_appointments()

    new_appointment = pd.DataFrame(
        [
            {
                "appointment_id": str(uuid.uuid4())[:8].upper(),
                "patient_name": patient_name.strip(),
                "email": email.strip(),
                "appointment_date": str(appointment_date),
                "reason": reason.strip(),
                "status": "Pending",
            }
        ],
        columns=COLUMNS,
    )

    df = pd.concat([df, new_appointment], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)


def update_appointment_status(appointment_id, new_status):
    """Update an appointment status and save the CSV."""
    df = load_appointments()

    if appointment_id not in df["appointment_id"].values:
        return False

    df.loc[
        df["appointment_id"] == appointment_id,
        "status",
    ] = new_status

    df.to_csv(DATA_FILE, index=False)
    return True


# -----------------------------
# Navigation
# -----------------------------
PAGES = [
    "Home",
    "Health Guidance",
    "Book Appointment",
    "Dashboard",
]


def navigate_to(page):
    st.session_state["selected_page"] = page


if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Home"

if "page_nav" not in st.session_state:
    st.session_state["page_nav"] = st.session_state["selected_page"]


def sync_navigation():
    st.session_state["selected_page"] = st.session_state["page_nav"]


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🏥 CarePilot")
    st.caption("Your healthcare companion")
    st.divider()

    st.radio(
        "Navigation",
        PAGES,
        key="page_nav",
        on_change=sync_navigation,
    )

    st.divider()
    st.caption("Organize appointments and explore general health guidance.")


page = st.session_state["selected_page"]


# -----------------------------
# Home page
# -----------------------------
if page == "Home":
    st.markdown(
        """
        <div style="
            padding: 35px;
            border-radius: 18px;
            background: linear-gradient(120deg, #123B66, #2878A8);
            color: white;
            margin-bottom: 25px;
        ">
            <p style="font-size: 14px; margin-bottom: 8px;">
                YOUR PERSONAL HEALTHCARE COMPANION
            </p>
            <h1 style="color: white; margin: 0;">
                Welcome to CarePilot
            </h1>
            <p style="font-size: 17px; margin-top: 12px;">
                A simpler way to explore health guidance and
                manage appointment requests.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    appointments = load_appointments()

    total = len(appointments)
    pending = int(appointments["status"].eq("Pending").sum())
    confirmed = int(appointments["status"].eq("Confirmed").sum())
    completed = int(appointments["status"].eq("Completed").sum())

    st.subheader("Your Overview")
    st.caption("A quick snapshot of your appointment records.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Appointments", total)
    col2.metric("Pending", pending)
    col3.metric("Confirmed", confirmed)
    col4.metric("Completed", completed)

    st.divider()

    st.subheader("Explore CarePilot")
    st.write("Choose a section to get started.")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 🩺 Health Guidance")
            st.write(
                "Explore general wellness information and "
                "basic health guidance."
            )

            if st.button(
                "Explore Health Guidance →",
                key="home_health_button",
                use_container_width=True,
            ):
                navigate_to("Health Guidance")
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("### 📅 Book an Appointment")
            st.write(
                "Submit an appointment request and keep "
                "your details organized."
            )

            if st.button(
                "Book Appointment →",
                key="home_appointment_button",
                use_container_width=True,
            ):
                navigate_to("Book Appointment")
                st.rerun()

    st.divider()

    st.subheader("Designed for Simplicity")
    info1, info2, info3 = st.columns(3)

    with info1:
        st.markdown("#### 📋 Organized Records")
        st.caption("Keep appointment requests together in one dashboard.")

    with info2:
        st.markdown("#### 📊 Clear Overview")
        st.caption("Review appointment totals and status summaries.")

    with info3:
        st.markdown("#### 🔒 Local Data Storage")
        st.caption("This demo stores appointment records in a local CSV file.")

    st.info(
        "CarePilot is a demonstration application. Health guidance "
        "is educational only and does not replace a qualified "
        "healthcare professional. Appointment requests submitted "
        "here are not sent to a clinic."
    )



# -----------------------------
# Health Guidance page
# -----------------------------
elif page == "Health Guidance":
    st.title("🩺 Health Guidance")

    st.write(
        "Select a topic to explore general wellness information."
    )

    topic = st.selectbox(
        "Choose a health topic",
        [
            "Healthy Lifestyle",
            "Nutrition and Hydration",
            "Sleep and Rest",
            "Stress Management",
            "Common Symptoms",
        ],
    )

    if topic == "Healthy Lifestyle":
        st.subheader("Healthy Lifestyle")
        st.markdown(
            """
            - Stay physically active according to your ability.
            - Maintain a consistent daily routine.
            - Avoid tobacco and limit alcohol consumption.
            - Attend recommended health check-ups.
            """
        )

    elif topic == "Nutrition and Hydration":
        st.subheader("Nutrition and Hydration")
        st.markdown(
            """
            - Eat a balanced variety of foods.
            - Include fruits, vegetables, and whole grains.
            - Drink water regularly throughout the day.
            - Follow individualized dietary advice when needed.
            """
        )

    elif topic == "Sleep and Rest":
        st.subheader("Sleep and Rest")
        st.markdown(
            """
            - Maintain a consistent sleep schedule.
            - Create a quiet and comfortable sleeping environment.
            - Reduce screen use before bedtime.
            - Seek professional advice for persistent sleep problems.
            """
        )

    elif topic == "Stress Management":
        st.subheader("Stress Management")
        st.markdown(
            """
            - Try slow breathing or relaxation exercises.
            - Take regular breaks during work.
            - Stay connected with supportive people.
            - Consider professional support if stress persists.
            """
        )

    elif topic == "Common Symptoms":
        st.subheader("Understanding Common Symptoms")

        st.write(
            "Symptoms can have many different causes. "
            "Consider their severity, duration, and any changes."
        )

        st.warning(
            "Seek urgent medical care for severe or rapidly "
            "worsening symptoms, including difficulty breathing, "
            "severe chest pain, or signs of a stroke."
        )

    st.divider()

    st.caption(
        "CarePilot uses simple predefined guidance, not an AI model. "
        "This information is educational and is not a diagnosis "
        "or a substitute for professional medical advice."
    )

    if st.button("Back to Home"):
        navigate_to("Home")
        st.rerun()

# -----------------------------
# Book Appointment page
# -----------------------------
# -----------------------------
# Book Appointment page
# -----------------------------
elif page == "Book Appointment":
    st.markdown(
        """
        <div style="
            padding: 28px;
            border-radius: 18px;
            background: linear-gradient(120deg, #123B66, #2878A8);
            color: white;
            margin-bottom: 24px;
        ">
            <p style="font-size: 13px; letter-spacing: 2px; margin-bottom: 8px;">
                CAREPILOT HEALTH SERVICES
            </p>
            <h1 style="color: white; margin: 0;">
                Book an Appointment
            </h1>
            <p style="font-size: 16px; margin-top: 10px; margin-bottom: 0;">
                Share your details and preferred date to submit
                your appointment request.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left_info, right_info = st.columns(2)

    with left_info:
        st.info(
            "**Easy Booking**\n\n"
            "Enter your details and preferred appointment date."
        )

    with right_info:
        st.info(
            "**Request Tracking**\n\n"
            "Your request is saved with Pending status until updated."
        )

    st.markdown("### Your Details")
    st.caption("Fields marked as required must be completed.")

    with st.form("appointment_form", clear_on_submit=True):
        patient_name = st.text_input(
            "Full Name *",
            placeholder="Enter your full name",
        )

        email = st.text_input(
            "Email Address *",
            placeholder="you@example.com",
        )

        appointment_date = st.date_input(
            "Preferred Appointment Date *",
            value=date.today(),
            min_value=date.today(),
            format="DD/MM/YYYY",
        )

        reason = st.text_area(
            "Reason for Appointment *",
            placeholder=(
                "Briefly describe the reason for your visit..."
            ),
            height=120,
        )

        st.caption(
            "Please provide accurate information before submitting."
        )

        submitted = st.form_submit_button(
            "Submit Appointment Request →",
            use_container_width=True,
            type="primary",
        )

        if submitted:
            clean_name = patient_name.strip()
            clean_email = email.strip()
            clean_reason = reason.strip()

            if not clean_name:
                st.error("Please enter your full name.")

            elif (
                not clean_email
                or "@" not in clean_email
                or "." not in clean_email.split("@")[-1]
            ):
                st.error("Please enter a valid email address.")

            elif not clean_reason:
                st.error("Please enter the reason for your appointment.")

            else:
                save_appointment(
                    clean_name,
                    clean_email,
                    appointment_date,
                    clean_reason,
                )

                st.success(
                    "Your appointment request has been saved successfully!"
                )

                st.info(
                    "Current status: Pending. This prototype does not "
                    "contact a clinic or confirm an actual medical appointment. "
                    "You can view your saved request on the Dashboard."
                )


# -----------------------------
# Dashboard page
# -----------------------------
elif page == "Dashboard":
    st.markdown(
        """
        <div style="
            padding: 28px;
            border-radius: 18px;
            background: linear-gradient(120deg, #123B66, #2878A8);
            color: white;
            margin-bottom: 24px;
        ">
            <p style="font-size: 13px; letter-spacing: 2px; margin-bottom: 8px;">
                CAREPILOT ANALYTICS
            </p>
            <h1 style="color: white; margin: 0;">
                Appointment Dashboard
            </h1>
            <p style="font-size: 16px; margin-top: 10px; margin-bottom: 0;">
                Monitor requests, review appointment trends, and manage statuses.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    df = load_appointments()

    total = len(df)
    pending = int(df["status"].eq("Pending").sum())
    confirmed = int(df["status"].eq("Confirmed").sum())
    completed = int(df["status"].eq("Completed").sum())
    cancelled = int(df["status"].eq("Cancelled").sum())

    st.subheader("Your Overview")
    st.caption("A live summary of the appointment records stored in your CSV.")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Requests", total)
    col2.metric("Pending", pending)
    col3.metric("Confirmed", confirmed)
    col4.metric("Completed", completed)
    col5.metric("Cancelled", cancelled)

    st.divider()

    st.subheader("Appointment Analytics")

    if df.empty:
        st.info(
            "No appointments available yet. "
            "Use Book Appointment to create your first request."
        )
    else:
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown("#### Requests by Status")

            status_counts = (
                df["status"]
                .replace("", "Unspecified")
                .value_counts()
            )

            st.bar_chart(status_counts)

        with chart_col2:
            st.markdown("#### Completion Progress")

            if total:
                st.progress(
                    completed / total,
                    text=f"{completed} of {total} requests completed",
                )

            st.write(f"🟡 Pending: **{pending}**")
            st.write(f"🟢 Confirmed: **{confirmed}**")
            st.write(f"🔵 Completed: **{completed}**")
            st.write(f"🔴 Cancelled: **{cancelled}**")

    st.divider()

    st.subheader("Appointment Records")
    st.caption("Search, filter, review and download your appointment requests.")

    search_col, filter_col = st.columns([2, 1])

    with search_col:
        search = st.text_input(
            "Search appointments",
            placeholder="Search by patient name, email or appointment ID...",
            key="dashboard_search",
        )

    with filter_col:
        status_filter = st.selectbox(
            "Filter by status",
            ["All statuses", "Pending", "Confirmed", "Completed", "Cancelled"],
            key="dashboard_status_filter",
        )

    filtered_df = df.copy()

    if search.strip():
        query = search.strip()

        mask = (
            filtered_df["patient_name"].str.contains(
                query, case=False, na=False, regex=False
            )
            | filtered_df["email"].str.contains(
                query, case=False, na=False, regex=False
            )
            | filtered_df["appointment_id"].str.contains(
                query, case=False, na=False, regex=False
            )
        )

        filtered_df = filtered_df[mask]

    if status_filter != "All statuses":
        filtered_df = filtered_df[
            filtered_df["status"] == status_filter
        ]

    st.caption(
        f"Showing {len(filtered_df)} of {total} appointment records"
    )

    display_columns = [
        "appointment_id",
        "patient_name",
        "email",
        "appointment_date",
        "reason",
        "status",
    ]

    st.dataframe(
        filtered_df[display_columns],
        use_container_width=True,
        hide_index=True,
        column_config={
            "appointment_id": st.column_config.TextColumn("Appointment ID"),
            "patient_name": st.column_config.TextColumn("Patient Name"),
            "email": st.column_config.TextColumn("Email"),
            "appointment_date": st.column_config.TextColumn("Appointment Date"),
            "reason": st.column_config.TextColumn("Reason"),
            "status": st.column_config.TextColumn("Status"),
        },
    )

    st.download_button(
        label="⬇️ Download Filtered Appointments CSV",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="appointments.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.divider()

    st.subheader("Manage Appointment Status")
    st.caption(
        "Select a request below to update its status. "
        "Changes are saved to your existing appointment CSV."
    )

    if df.empty:
        st.info("There are no appointment statuses to update yet.")
    else:
        appointment_ids = df["appointment_id"].tolist()

        selected_id = st.selectbox(
            "Select Appointment ID",
            appointment_ids,
            format_func=lambda appointment_id: (
                f"{appointment_id} — "
                f"{df.loc[df['appointment_id'] == appointment_id, 'patient_name'].iloc[0]}"
            ),
            key="dashboard_selected_appointment",
        )

        current_row = df[
            df["appointment_id"] == selected_id
        ].iloc[0]

        detail_col1, detail_col2 = st.columns(2)

        with detail_col1:
            st.markdown("**Patient**")
            st.write(current_row["patient_name"])

            st.markdown("**Email**")
            st.write(current_row["email"])

        with detail_col2:
            st.markdown("**Appointment Date**")
            st.write(current_row["appointment_date"])

            st.markdown("**Current Status**")
            st.write(current_row["status"] or "Unspecified")

        statuses = [
            "Pending",
            "Confirmed",
            "Completed",
            "Cancelled",
        ]

        current_status = current_row["status"]
        default_index = (
            statuses.index(current_status)
            if current_status in statuses
            else 0
        )

        new_status = st.selectbox(
            "Choose New Status",
            statuses,
            index=default_index,
            key=f"dashboard_new_status_{selected_id}",
        )

        if st.button(
            "Save Status Changes",
            use_container_width=True,
            type="primary",
            key="dashboard_save_status",
        ):
            if update_appointment_status(selected_id, new_status):
                st.success("Appointment status updated successfully!")
                st.rerun()
            else:
                st.error("Could not find the selected appointment.")


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "CarePilot | Healthcare Appointment Management Demo"
)