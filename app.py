import streamlit as st
from pathlib import Path
from file_manager import (
    create_file,
    read_file,
    append_file,
    overwrite_file,
    rename_file,
    delete_file,
    get_files,
    FILE_DIR
)


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="File Manager",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Cards */
    .card {
        background-color: white;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 15px;
        color: #6b7280;
    }

    .card-value {
        font-size: 30px;
        font-weight: 700;
        margin-top: 5px;
    }

    /* File item */
    .file-item {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        margin-bottom: 8px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
    }

    /* Text areas */
    textarea {
        border-radius: 10px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    '<div class="main-title">📁 File Manager</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Simple, powerful and modern file handling system built with Python & Streamlit</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown("## 📁 File Manager")

    st.markdown("---")

    menu = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "➕ Create File",
            "📖 Read File",
            "✏️ Update File",
            "🗑️ Delete File"
        ]
    )

    st.markdown("---")

    st.caption("Python File Handling Project")
    st.caption("Built with Streamlit")


# ---------------------------------------------------
# GET FILES
# ---------------------------------------------------

files = get_files()


# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

if menu == "🏠 Dashboard":

    st.subheader("Dashboard")
    st.write("Manage your files from one place.")

    # Statistics
    total_files = len(files)

    total_size = sum(
        file.stat().st_size
        for file in files
    )

    total_size_kb = total_size / 1024

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">📄 Total Files</div>
                <div class="card-value">{total_files}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">💾 Storage Used</div>
                <div class="card-value">{total_size_kb:.2f} KB</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">⚡ Status</div>
                <div class="card-value">Active</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("📂 Your Files")

    if files:

        search = st.text_input(
            "🔍 Search files",
            placeholder="Type a filename..."
        )

        filtered_files = [
            file for file in files
            if search.lower() in file.name.lower()
        ]

        for file in filtered_files:

            size_kb = file.stat().st_size / 1024

            col1, col2, col3 = st.columns([5, 2, 1])

            with col1:
                st.markdown(
                    f"""
                    <div class="file-item">
                        📄 <strong>{file.name}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.write(f"{size_kb:.2f} KB")

            with col3:
                if st.button(
                    "View",
                    key=f"view_{file.name}"
                ):
                    success, content = read_file(file.name)

                    if success:
                        st.code(content)
                    else:
                        st.error(content)

    else:
        st.info("📂 No files created yet. Create your first file!")


# ---------------------------------------------------
# CREATE FILE
# ---------------------------------------------------

elif menu == "➕ Create File":

    st.subheader("➕ Create New File")

    st.write(
        "Create a new text file and add content to it."
    )

    with st.form("create_form"):

        filename = st.text_input(
            "File Name",
            placeholder="example.txt"
        )

        content = st.text_area(
            "File Content",
            placeholder="Write something here...",
            height=250
        )

        submitted = st.form_submit_button(
            "Create File",
            use_container_width=True
        )

        if submitted:

            if not filename.strip():
                st.error("Please enter a filename.")

            elif not Path(filename).suffix:
                st.error(
                    "Please provide a file extension, e.g. .txt"
                )

            else:

                success, message = create_file(
                    filename,
                    content
                )

                if success:
                    st.success(message)
                    st.balloons()

                else:
                    st.error(message)


# ---------------------------------------------------
# READ FILE
# ---------------------------------------------------

elif menu == "📖 Read File":

    st.subheader("📖 Read File")

    if not files:

        st.info("No files available.")

    else:

        selected_file = st.selectbox(
            "Select a file",
            [file.name for file in files]
        )

        if st.button(
            "📖 Read File",
            use_container_width=True
        ):

            success, content = read_file(
                selected_file
            )

            if success:

                st.success(
                    f"Reading: {selected_file}"
                )

                st.text_area(
                    "File Content",
                    content,
                    height=400
                )

            else:
                st.error(content)


# ---------------------------------------------------
# UPDATE FILE
# ---------------------------------------------------

elif menu == "✏️ Update File":

    st.subheader("✏️ Update File")

    if not files:

        st.info("No files available.")

    else:

        selected_file = st.selectbox(
            "Select file",
            [file.name for file in files]
        )

        operation = st.radio(
            "Choose Operation",
            [
                "🔄 Rename",
                "➕ Append Content",
                "✍️ Overwrite Content"
            ],
            horizontal=True
        )

        st.markdown("---")

        # -----------------------------
        # RENAME
        # -----------------------------

        if operation == "🔄 Rename":

            new_name = st.text_input(
                "New File Name",
                placeholder="new_name.txt"
            )

            if st.button(
                "🔄 Rename File",
                use_container_width=True
            ):

                if not new_name.strip():

                    st.error(
                        "Please enter the new filename."
                    )

                else:

                    success, message = rename_file(
                        selected_file,
                        new_name
                    )

                    if success:
                        st.success(message)
                        st.rerun()

                    else:
                        st.error(message)

        # -----------------------------
        # APPEND
        # -----------------------------

        elif operation == "➕ Append Content":

            content = st.text_area(
                "Content to Append",
                height=250,
                placeholder="Write content to append..."
            )

            if st.button(
                "➕ Append Content",
                use_container_width=True
            ):

                if not content.strip():

                    st.warning(
                        "Please enter some content."
                    )

                else:

                    success, message = append_file(
                        selected_file,
                        content
                    )

                    if success:
                        st.success(message)

                    else:
                        st.error(message)

        # -----------------------------
        # OVERWRITE
        # -----------------------------

        elif operation == "✍️ Overwrite Content":

            st.warning(
                "⚠️ This will replace the existing content."
            )

            content = st.text_area(
                "New Content",
                height=250,
                placeholder="Write the new content..."
            )

            confirm = st.checkbox(
                "I understand that the existing content will be replaced."
            )

            if st.button(
                "✍️ Overwrite File",
                use_container_width=True
            ):

                if not confirm:

                    st.warning(
                        "Please confirm the overwrite operation."
                    )

                else:

                    success, message = overwrite_file(
                        selected_file,
                        content
                    )

                    if success:
                        st.success(message)

                    else:
                        st.error(message)


# ---------------------------------------------------
# DELETE FILE
# ---------------------------------------------------

elif menu == "🗑️ Delete File":

    st.subheader("🗑️ Delete File")

    if not files:

        st.info("No files available.")

    else:

        selected_file = st.selectbox(
            "Select file to delete",
            [file.name for file in files]
        )

        st.warning(
            f"⚠️ You are about to permanently delete `{selected_file}`."
        )

        confirm = st.checkbox(
            "Yes, I want to permanently delete this file."
        )

        if st.button(
            "🗑️ Delete File",
            use_container_width=True
        ):

            if not confirm:

                st.warning(
                    "Please confirm deletion first."
                )

            else:

                success, message = delete_file(
                    selected_file
                )

                if success:
                    st.success(message)
                    st.rerun()

                else:
                    st.error(message)