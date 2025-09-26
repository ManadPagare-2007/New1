import pandas as pd
import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
   
    user="root",
    password="Manad@2007",
    database="hackathondata"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM studentdata")

columns = [desc[0] for desc in cursor.description]
rows = cursor.fetchall()

main_data = pd.DataFrame(rows, columns=columns)

cursor.close()
conn.close()

def metric_card(title: str, value, color: str = "#4E79A7"):
    st.markdown(f"""
        <div style="
            background-color: {color};
            padding: 18px 16px;
            border-radius: 16px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.12);
            text-align: center;
            color: white;
            font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
        ">
            <div style="font-size: 14px; opacity: 0.95; margin-bottom: 6px;">{title}</div>
            <div style="font-size: 26px; font-weight: 700;">{value}</div>
        </div>
    """, unsafe_allow_html=True)

if "main_data" not in st.session_state:
    st.session_state.main_data=pd.DataFrame(main_data)
main_data=st.session_state.main_data

if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = "2"

admin_data = pd.DataFrame({
    "USERNAME":["manad@paruluniversity","yash@paruluniversity","shaurya@paruluniversity",
    "parth@paruluniversity","srishti@paruluniversity","bhumi@paruluniversity"],
    "PASSWORD":["25UG033170","25UG031719","25UG035603","25UG033842","25UG036617","25UG035785"
    ]})

staff_members = list(admin_data["USERNAME"])
staff_passwords = list(admin_data["PASSWORD"])

if st.session_state.selected_tab == "2":
    import streamlit as st

    # Custom CSS for the futuristic box
    st.markdown(
        """
        <style>
        .login-box {
            background-color: rgba(20, 20, 30, 0.95);
            border-radius: 20px;
            padding: 30px;
            margin: auto;
            width: 400px;
            box-shadow: 0 0 20px #00f7ff, 0 0 40px #00f7ff;
        }
        .login-title {
            color: white;
            text-align: center;
            font-family: "Orbitron", sans-serif;
            letter-spacing: 2px;
            text-shadow: 0 0 10px #00f7ff, 0 0 20px #00f7ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<h1 style="text-align:center; color:white;">🔐 Login</h1>', unsafe_allow_html=True)

    a = st.radio("", options=("Student","Faculty","Admin"), horizontal=True)

    if a == "Student":
        st.header("Welcome Student...")
    elif a == "Admin":
        st.header("Welcome Admin...")
    elif a == "Faculty":
        st.header("Welcome Faculty...")

    with st.form("Form 1", clear_on_submit=False):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        if a == "Admin":
            if username=="" or password=="":
                st.error("Invalid username or password")
            elif username == staff_members[idx:=int(staff_members.index(username))] and password == staff_passwords[idx]:
                
                st.success("Click 'login' again..")
                st.session_state.selected_tab = "1"
            else:
                st.error("Invalid username or password")



elif st.session_state.selected_tab == "1":
    radio1=st.sidebar.radio("Go to",options=("Admissions","Hostels","Fees","Student Data"))
    
    if radio1 == "Admissions":

        st.header("🎓 Admissions Management")

        with st.form("admission_form"):
            
            in_name=st.text_input("Name")
            in_branch=st.selectbox("Department", ["Computer Science & Engineering", "Electrical Engineering", 
                                            "Mechanical Engineering","Civil Engineering","Chemical Engineering"])
            in_year=st.selectbox("Year of Acadamics",options=("1st","2nd","3rd","4th"))
            in_gender=st.radio("Gender",options=("Male","Female"),horizontal=True)
            in_age=int(st.number_input("Age",value=17,min_value=17,max_value=99))
            in_contact=st.text_input("Contact")
            in_email=st.text_input("Email")
            submitted = st.form_submit_button("Confirm Admission")
            if submitted:
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Manad@2007",
                database="hackathondata"
                )
                cursor = conn.cursor()
                sql = """
                    INSERT INTO studentdata (Name, Branch, Year, Gender, Age, Contact, Email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                values = (in_name, in_branch, in_year, in_gender, in_age, in_contact, in_email)
                cursor.execute(sql, values)
                cursor.execute("SELECT * FROM studentdata")
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                st.session_state.main_data = pd.DataFrame(rows, columns=columns)



                conn.commit()
                cursor.close()
                st.success("✅ Admission recorded successfully!")

    elif radio1=="Student Data":
        st.title("📊 Students Spreadsheet")
        st.dataframe(main_data)

    


    

