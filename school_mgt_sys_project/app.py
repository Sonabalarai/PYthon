import json
from abc import ABC, abstractmethod
from pathlib import Path
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Main title */
    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 25px;
    }

    /* Dashboard cards */
    .card {
        background-color: white;
        padding: 22px;
        border-radius: 15px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }

    .card-title {
        font-size: 15px;
        color: #6b7280;
        margin-bottom: 8px;
    }

    .card-value {
        font-size: 30px;
        font-weight: 700;
    }

    /* Section headings */
    .section-title {
        font-size: 25px;
        font-weight: 650;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATABASE
# =========================================================

database = "school_data.json"

data = {
    "student": [],
    "teacher": []
}


if Path(database).exists():

    try:
        with open(database, "r") as f:
            content = f.read()

            if content:
                data = json.loads(content)

    except json.JSONDecodeError:
        data = {
            "student": [],
            "teacher": []
        }


def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)


# =========================================================
# ABSTRACT CLASS
# =========================================================

class Persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):

        if "@" in email and "." in email:
            return True

        return False


# =========================================================
# STUDENT CLASS
# =========================================================

class Student(Persons):

    def get_roles(self):
        return "Student"

    def register(self, name, age, email, roll_no):

        if not Persons.validate_email(email):
            return False, "Invalid email address."

        for student in data["student"]:

            if student["roll_no"] == roll_no:
                return False, "Student with this roll number already exists."

        data["student"].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grade": {}
        })

        save()

        return True, f"Student {name} registered successfully."

    def show_details(self, roll_no):

        for student in data["student"]:

            if student["roll_no"] == roll_no:

                grades = student["grade"]

                average = (
                    sum(grades.values()) / len(grades)
                    if grades else 0
                )

                return student, average

        return None, None

    def add_grades(self, roll_no, subject, marks):

        for student in data["student"]:

            if student["roll_no"] == roll_no:

                student["grade"][subject] = marks

                save()

                return True, "Grade added successfully."

        return False, "Student not found."


# =========================================================
# TEACHER CLASS
# =========================================================

class Teacher(Persons):

    def get_roles(self):
        return "Teacher"

    def register(self, name, age, email, subject, emp_id):

        if not Persons.validate_email(email):
            return False, "Invalid email address."

        for teacher in data["teacher"]:

            if teacher["emp_id"] == emp_id:
                return False, "Teacher with this employee ID already exists."

        data["teacher"].append({
            "name": name,
            "age": age,
            "email": email,
            "subject": subject,
            "emp_id": emp_id
        })

        save()

        return True, f"Teacher {name} registered successfully."

    def show_details(self, emp_id):

        for teacher in data["teacher"]:

            if teacher["emp_id"] == emp_id:
                return teacher

        return None


# =========================================================
# OBJECTS
# =========================================================

student_obj = Student()
teacher_obj = Teacher()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    "<h1 style='text-align:center;'>🎓 SMS</h1>",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<p style='text-align:center;'>Student Management System</p>",
    unsafe_allow_html=True
)

st.sidebar.divider()

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👨‍🎓 Register Student",
        "👨‍🏫 Register Teacher",
        "📝 Add Grades",
        "🔍 Student Details",
        "🔍 Teacher Details"
    ]
)

st.sidebar.divider()

st.sidebar.write("📊 System Statistics")

st.sidebar.write(f"Students: {len(data['student'])}")
st.sidebar.write(f"Teachers: {len(data['teacher'])}")


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">🎓 Student Management System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Manage students, teachers and academic grades easily.</div>',
        unsafe_allow_html=True
    )

    # Statistics

    total_students = len(data["student"])
    total_teachers = len(data["teacher"])

    total_grades = sum(
        len(student["grade"])
        for student in data["student"]
    )

    total_subjects = len(
        set(
            subject
            for student in data["student"]
            for subject in student["grade"]
        )
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">👨‍🎓 Total Students</div>
                <div class="card-value">{total_students}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">👨‍🏫 Total Teachers</div>
                <div class="card-value">{total_teachers}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">📝 Grades Recorded</div>
                <div class="card-value">{total_grades}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">📚 Subjects</div>
                <div class="card-value">{total_subjects}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">📋 Registered Students</div>',
        unsafe_allow_html=True
    )

    if data["student"]:

        for student in data["student"]:

            grades = student["grade"]

            average = (
                sum(grades.values()) / len(grades)
                if grades else 0
            )

            with st.container(border=True):

                col1, col2, col3, col4 = st.columns(4)

                col1.write(f"**👤 {student['name']}**")
                col2.write(f"Roll No: {student['roll_no']}")
                col3.write(f"Subjects: {len(grades)}")
                col4.write(f"Average: {average:.1f}")

    else:

        st.info("No students registered yet.")


# =========================================================
# REGISTER STUDENT
# =========================================================

elif menu == "👨‍🎓 Register Student":

    st.markdown(
        '<div class="main-title">👨‍🎓 Register Student</div>',
        unsafe_allow_html=True
    )

    st.write("Enter the student's information below.")

    with st.form("student_registration"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter student name"
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=18
            )

        with col2:

            email = st.text_input(
                "Email",
                placeholder="student@example.com"
            )

            roll_no = st.text_input(
                "Roll Number",
                placeholder="Enter roll number"
            )

        submit = st.form_submit_button(
            "➕ Register Student",
            use_container_width=True
        )

        if submit:

            if not name or not email or not roll_no:

                st.error("Please fill all required fields.")

            else:

                success, message = student_obj.register(
                    name,
                    age,
                    email,
                    roll_no
                )

                if success:
                    st.success(message)
                    st.rerun()

                else:
                    st.error(message)


# =========================================================
# REGISTER TEACHER
# =========================================================

elif menu == "👨‍🏫 Register Teacher":

    st.markdown(
        '<div class="main-title">👨‍🏫 Register Teacher</div>',
        unsafe_allow_html=True
    )

    st.write("Enter the teacher's information below.")

    with st.form("teacher_registration"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter teacher name"
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=25
            )

            email = st.text_input(
                "Email",
                placeholder="teacher@example.com"
            )

        with col2:

            subject = st.text_input(
                "Subject",
                placeholder="e.g. Mathematics"
            )

            emp_id = st.text_input(
                "Employee ID",
                placeholder="Enter employee ID"
            )

        submit = st.form_submit_button(
            "➕ Register Teacher",
            use_container_width=True
        )

        if submit:

            if not name or not email or not subject or not emp_id:

                st.error("Please fill all required fields.")

            else:

                success, message = teacher_obj.register(
                    name,
                    age,
                    email,
                    subject,
                    emp_id
                )

                if success:
                    st.success(message)
                    st.rerun()

                else:
                    st.error(message)


# =========================================================
# ADD GRADES
# =========================================================

elif menu == "📝 Add Grades":

    st.markdown(
        '<div class="main-title">📝 Add Student Grade</div>',
        unsafe_allow_html=True
    )

    if not data["student"]:

        st.warning("No students are registered yet.")

    else:

        roll_numbers = [
            student["roll_no"]
            for student in data["student"]
        ]

        selected_roll = st.selectbox(
            "Select Student",
            roll_numbers
        )

        selected_student = next(
            s for s in data["student"]
            if s["roll_no"] == selected_roll
        )

        st.info(
            f"Student: **{selected_student['name']}**"
        )

        with st.form("grade_form"):

            subject = st.text_input(
                "Subject",
                placeholder="e.g. Mathematics"
            )

            marks = st.number_input(
                "Marks",
                min_value=0.0,
                max_value=100.0,
                value=0.0
            )

            submit = st.form_submit_button(
                "💾 Save Grade",
                use_container_width=True
            )

            if submit:

                if not subject:

                    st.error("Please enter a subject.")

                else:

                    success, message = student_obj.add_grades(
                        selected_roll,
                        subject,
                        marks
                    )

                    if success:

                        st.success(message)
                        st.rerun()

                    else:

                        st.error(message)


# =========================================================
# STUDENT DETAILS
# =========================================================

elif menu == "🔍 Student Details":

    st.markdown(
        '<div class="main-title">🔍 Student Details</div>',
        unsafe_allow_html=True
    )

    if not data["student"]:

        st.warning("No students registered.")

    else:

        roll_numbers = [
            student["roll_no"]
            for student in data["student"]
        ]

        roll_no = st.selectbox(
            "Select Roll Number",
            roll_numbers
        )

        student, average = student_obj.show_details(
            roll_no
        )

        if student:

            st.markdown(
                '<div class="section-title">👤 Student Information</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Student Name",
                    student["name"]
                )

            with col2:

                st.metric(
                    "Roll Number",
                    student["roll_no"]
                )

            with col3:

                st.metric(
                    "Average Marks",
                    f"{average:.1f}"
                )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.write("### 📧 Contact Information")

                st.write(
                    f"**Email:** {student['email']}"
                )

                st.write(
                    f"**Age:** {student['age']}"
                )

            with col2:

                st.write("### 📚 Grades")

                if student["grade"]:

                    for subject, marks in student["grade"].items():

                        st.progress(
                            marks / 100,
                            text=f"{subject}: {marks:.1f}"
                        )

                else:

                    st.info("No grades recorded.")


# =========================================================
# TEACHER DETAILS
# =========================================================

elif menu == "🔍 Teacher Details":

    st.markdown(
        '<div class="main-title">🔍 Teacher Details</div>',
        unsafe_allow_html=True
    )

    if not data["teacher"]:

        st.warning("No teachers registered.")

    else:

        emp_ids = [
            teacher["emp_id"]
            for teacher in data["teacher"]
        ]

        emp_id = st.selectbox(
            "Select Employee ID",
            emp_ids
        )

        teacher = teacher_obj.show_details(emp_id)

        if teacher:

            st.markdown(
                '<div class="section-title">👨‍🏫 Teacher Information</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Teacher Name",
                    teacher["name"]
                )

            with col2:

                st.metric(
                    "Employee ID",
                    teacher["emp_id"]
                )

            with col3:

                st.metric(
                    "Subject",
                    teacher["subject"]
                )

            st.divider()

            st.write("### 📋 Personal Information")

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Name:** {teacher['name']}"
                )

                st.write(
                    f"**Age:** {teacher['age']}"
                )

            with col2:

                st.write(
                    f"**Email:** {teacher['email']}"
                )

                st.write(
                    f"**Subject:** {teacher['subject']}"
                )