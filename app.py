import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

/* Sidebar Background */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#eef5ff,#dfefff);
}

/* Sidebar Title */
[data-testid="stSidebar"] h1{
    color:#1565C0;
    text-align:center;
    font-weight:bold;
}

.nav-link{
    border-radius:12px !important;
    margin:8px;
    font-size:17px !important;
    font-weight:600;
}

.nav-link:hover{
    background:#42A5F5 !important;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

df=pd.read_csv("employess attrition.csv")

with st.sidebar:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#1565C0,#42A5F5);
        padding:18px;
        border-radius:15px;
        text-align:center;
        color:white;
        box-shadow:0 4px 12px rgba(0,0,0,0.2);
        margin-bottom:15px;
    ">
        <h2 style="margin:0;">🏢 IBM HR Analytics</h2>
        <p style="margin:5px 0 0 0;font-size:15px;">
            Employee Attrition Dashboard
        </p>
    </div>
    """, unsafe_allow_html=True)

    opt=option_menu("menu",["Home","Dataset","Pre-Processing","Visualization","HR Insights","About"],icons=["house","table","gear","bar-chart","lightbulb","person"])
    d=st.multiselect(
        "SelectDepartment",
        options=df['Department'].unique()
    )
    if d:
       filtered=df[df["Department"].isin(d)]
    else:
        filtered=df
if opt=="Home":

    total_employee = filtered.shape[0]
    total_department = filtered["Department"].nunique()
    total_attrition = filtered["Attrition"].value_counts().get("Yes", 0)
    avg_age = round(filtered["Age"].mean(), 1)
    avg_income = round(filtered["MonthlyIncome"].mean(), 0)
    col1, col2, col3, col4, col5 = st.columns(5)

    st.title("IBM HR Analytics Employee Attrition Dashboard")
    st.markdown("""
    ### 👋 Welcome to the IBM HR Analytics Dashboard

 This dashboard provides a simple overview of employee data.  
 It helps analyze employee attrition, departments, age, salary, and workforce trends
   through interactive charts and key performance indicators (KPIs).
""")
    st.markdown("""
<style>

/* KPI Cards */
.kpi-card{
    background: linear-gradient(135deg,#4CAF50,#2E7D32);
    color:white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,0.20);
    transition:all 0.35s ease;
    cursor:pointer;
    border:1px solid rgba(255,255,255,0.15);
}

.kpi-card:hover{
    transform:translateY(-8px) scale(1.05);
    box-shadow:0 15px 35px rgba(76,175,80,0.45);
    background:linear-gradient(135deg,#66BB6A,#388E3C);
}

.kpi-label{
    font-size:18px;
    font-weight:600;
    opacity:0.95;
    margin-bottom:10px;
}

.kpi-value{
    font-size:34px;
    font-weight:700;
    letter-spacing:1px;
}

/* Optional animation on page load */
.kpi-card{
    animation:fadeIn 0.8s ease;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)
    with col1:
        st.markdown(f"""
        <div class="kpi-card emp">
                <div class="kpi-title">👨‍💼 Total Employees</div>
                <div class="kpi-value">{total_employee}</div>
            </div>
            """,unsafe_allow_html=True)


    with col2:
        st.markdown(f"""
        <div class="kpi-card" style="background:linear-gradient(135deg,#2563eb,#3b82f6);">
                <div class="kpi-title">🏢 DEPARTMENTS</div>
                <div class="kpi-value">{total_department}</div>
            </div>
            """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card" style="background:linear-gradient(135deg,#f97316,#fb923c);">
                <div class="kpi-title">📉 ATTRITION</div>
                <div class="kpi-value">{total_attrition}</div>
            </div>
            """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card" style="background:linear-gradient(135deg,#9333ea,#c084fc);">
            <div class="kpi-title">👤 AVERAGE AGE</div>
            <div class="kpi-value">{avg_age:.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="kpi-card" style="background:linear-gradient(135deg,#e11d48,#f43f5e);">
            <div class="kpi-title">💰 AVERAGE INCOME</div>
            <div class="kpi-value">{avg_income:.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    .objective-card{
        background:linear-gradient(135deg,#e8f5e9,#ffffff);
        border-left:8px solid #28a745;
        border-radius:18px;
        padding:25px;
        margin-top:20px;
        margin-bottom:20px;
        box-shadow:0 8px 18px rgba(0,0,0,0.12);
        transition:0.4s;
    }

    .objective-card:hover{
        transform:translateY(-8px);
        box-shadow:0 15px 30px rgba(0,0,0,0.18);
    }

    .objective-title{
        font-size:28px;
        font-weight:bold;
        color:#198754;
        margin-bottom:12px;
    }

    .objective-text{
        font-size:17px;
        color:#444;
        line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="objective-card">

    <div class="objective-title">
    🎯 Project Objective
    </div>

    <div class="objective-text">

    The objective of this HR Analytics Dashboard is to analyze employee data and provide useful HR insights.
    It helps understand employee attrition, department performance, workforce distribution, age, salary, and job roles. 
    This dashboard supports better HR decisions through interactive visualizations.

    </div>

    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>

    .dataset-card{
        background:linear-gradient(135deg,#e3f2fd,#ffffff);
        border-left:8px solid #2196F3;
        border-radius:18px;
        padding:25px;
        margin-top:20px;
        margin-bottom:20px;
        box-shadow:0 8px 18px rgba(0,0,0,0.12);
        transition:0.4s;
    }

    .dataset-card:hover{
        transform:translateY(-8px);
        box-shadow:0 15px 30px rgba(0,0,0,0.18);
    }

    .dataset-title{
        font-size:28px;
        font-weight:bold;
        color:#1565C0;
        margin-bottom:12px;
    }

    .dataset-text{
        font-size:17px;
        color:#444;
        line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dataset-card">

    <div class="dataset-title">
    📊 About Dataset
    </div>

    <div class="dataset-text">

    The The IBM HR Analytics dataset contains employee details like age, gender,
    department, job role, education, salary, and attrition.
    This dashboard helps us understand employee data, compare departments, 
    attrition, and support better HR decisions through easy-to-understand charts.

    </div>

    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#fff8e1,#ffffff);
    padding:20px;
    border-left:6px solid #f39c12;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
    margin-top:20px;
    transition:0.3s;
    ">

    <h3 style="color:#f39c12;">⭐ Features</h3>

    <ul style="font-size:17px; line-height:2; color:#333;">

    <li>👨‍💼 Employee Workforce Overview</li>

    <li>🏢 Department-wise Analysis</li>

    <li>📉 Employee Attrition Analysis</li>

    <li>📊 Salary & Monthly Income Analysis</li>

    <li>⚙️ Data Pre-Processing</li>

    <li>📄 Employee Dataset Overview</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#ede7f6,#ffffff);
    padding:20px;
    border-left:6px solid #673ab7;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
    margin-top:20px;
    transition:0.3s;
    ">

    <h3 style="color:#673ab7;">🛠️ Tools & Technologies</h3>

    <ul style="font-size:17px; line-height:2; color:#333;">

    <li>🐍 Python</li>

    <li>📊 Pandas</li>

    <li>📈 Plotly</li>

    <li>🌐 Streamlit</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)

elif opt == "Dataset":

    st.title("📊 IBM HR Analytics Employee Attrition Dataset")
    st.markdown("### Explore, Understand & Discover Your Employee Data")
    st.write(
        "Get a clear view of your IBM HR Analytics dataset, employee records, "
        "data quality and important information."
    )

    # ============================================================
    # CUSTOM CSS
    # ============================================================

    st.markdown("""
    <style>

    /* Main page spacing */
    .block-container {
        padding-top: 2rem;
    }

    /* KPI CARD */
    .kpi-card {
        padding: 22px 18px;
        border-radius: 18px;
        color: white;
        min-height: 125px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        margin-bottom: 10px;
    }

    .kpi-title {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .kpi-value {
        font-size: 32px;
        font-weight: 800;
        color: white;
    }

    /* Section heading */
    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* Information box */
    .info-box {
        padding: 18px;
        border-radius: 16px;
        background: linear-gradient(135deg,#eef2ff,#fdf2f8);
        border-left: 6px solid #7c3aed;
        margin-bottom: 15px;
    }

    /* Download button */
    .download-text {
        font-size: 22px;
        font-weight: 700;
    }

    </style>
    """, unsafe_allow_html=True)


    # ============================================================
    # BASIC DATASET INFORMATION
    # ============================================================

    total_employees = len(df)
    total_columns = len(df.columns)

    if "Department" in df.columns:
        total_departments = df["Department"].nunique()
    else:
        total_departments = 0

    if "JobRole" in df.columns:
        total_job_roles = df["JobRole"].nunique()
    else:
        total_job_roles = 0


    # ============================================================
    # QUICK DATASET OVERVIEW
    # ============================================================

    st.markdown("## 🌈 Quick Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="kpi-card"
        style="background:linear-gradient(135deg,#7c3aed,#a855f7);">
            <div class="kpi-title">👥 Total Employees</div>
            <div class="kpi-value">{total_employees:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card"
        style="background:linear-gradient(135deg,#2563eb,#38bdf8);">
            <div class="kpi-title">📋 Total Columns</div>
            <div class="kpi-value">{total_columns}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card"
        style="background:linear-gradient(135deg,#16a34a,#4ade80);">
            <div class="kpi-title">🏢 Departments</div>
            <div class="kpi-value">{total_departments}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card"
        style="background:linear-gradient(135deg,#f97316,#f43f5e);">
            <div class="kpi-title">💼 Job Roles</div>
            <div class="kpi-value">{total_job_roles}</div>
        </div>
        """, unsafe_allow_html=True)


    # ============================================================
    # EXPLORE EMPLOYEE RECORDS
    # ============================================================

    st.markdown("## 👨‍💼 Explore Employee Records")
    st.write("Search and explore employee information from the dataset.")

    search = st.text_input(
        "🔎 Search employee information",
        placeholder="Search Department, Job Role, Gender, Education..."
    )

    display_df = df.copy()

    if search:
        search_text = search.lower()

        mask = display_df.astype(str).apply(
            lambda column: column.str.lower().str.contains(
                search_text,
                na=False
            )
        ).any(axis=1)

        display_df = display_df[mask]

    st.caption(f"Showing {len(display_df):,} employee records")


    # ============================================================
    # COLOURFUL EMPLOYEE TABLE
    # ============================================================

    def style_employee_table(data):

        return data.style.background_gradient(
            subset=[
                col for col in [
                    "Age",
                    "DailyRate",
                    "DistanceFromHome",
                    "MonthlyIncome",
                    "TotalWorkingYears",
                    "YearsAtCompany"
                ]
                if col in data.columns
            ],
            cmap="PuBu"
        ).set_properties(
            **{
                "text-align": "center",
                "font-size": "13px"
            }
        )


    st.dataframe(
        style_employee_table(display_df.head(100)),
        use_container_width=True,
        height=420,
        hide_index=True
    )

    st.info(
        "💡 The table shows the first 100 matching employee records. "
        "Use the search box above to find specific employees or categories."
    )


    # ============================================================
    # UNDERSTANDING YOUR DATASET
    # ============================================================

    st.markdown("## 🔍 Understanding Your Dataset")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🏗️ Structure",
            "🔤 Data Types",
            "⚠️ Missing Values",
            "♻️ Duplicates"
        ]
    )


    # ============================================================
    # STRUCTURE
    # ============================================================

    with tab1:

        structure_df = pd.DataFrame({
            "Information": [
                "Total Employees",
                "Total Columns",
                "Departments",
                "Job Roles",
                "Total Cells"
            ],
            "Value": [
                total_employees,
                total_columns,
                total_departments,
                total_job_roles,
                total_employees * total_columns
            ]
        })

        st.dataframe(
            structure_df.style
            .background_gradient(cmap="Purples")
            .set_properties(
                **{
                    "font-size": "15px",
                    "text-align": "center"
                }
            ),
            use_container_width=True,
            hide_index=True
        )


    # ============================================================
    # DATA TYPES
    # ============================================================

    with tab2:

        dtype_df = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str).values
        })

        st.dataframe(
            dtype_df.style
            .background_gradient(cmap="Blues")
            .set_properties(
                **{
                    "font-size": "14px",
                    "text-align": "center"
                }
            ),
            use_container_width=True,
            hide_index=True
        )


    # ============================================================
    # MISSING VALUES
    # ============================================================

    with tab3:

        missing_df = pd.DataFrame({
            "Column Name": df.columns,
            "Missing Values": df.isnull().sum().values
        })

        missing_df["Missing %"] = (
            missing_df["Missing Values"] /
            len(df) * 100
        ).round(2)

        st.dataframe(
            missing_df.style
            .background_gradient(
                subset=["Missing Values"],
                cmap="Reds"
            )
            .set_properties(
                **{
                    "font-size": "14px",
                    "text-align": "center"
                }
            ),
            use_container_width=True,
            hide_index=True
        )

        total_missing = int(df.isnull().sum().sum())

        if total_missing == 0:
            st.success("🎉 Great! No missing values were found.")
        else:
            st.warning(
                f"⚠️ Total missing values found: {total_missing}"
            )


    # ============================================================
    # DUPLICATES
    # ============================================================

    with tab4:

        duplicate_count = df.duplicated().sum()

        duplicate_df = pd.DataFrame({
            "Information": [
                "Total Duplicate Rows",
                "Unique Rows"
            ],
            "Value": [
                duplicate_count,
                len(df.drop_duplicates())
            ]
        })

        st.dataframe(
            duplicate_df.style
            .background_gradient(cmap="Oranges")
            .set_properties(
                **{
                    "font-size": "15px",
                    "text-align": "center"
                }
            ),
            use_container_width=True,
            hide_index=True
        )

        if duplicate_count == 0:
            st.success("✅ No duplicate records found.")
        else:
            st.warning(
                f"⚠️ {duplicate_count} duplicate records found."
            )


    # ============================================================
    # NUMERICAL INFORMATION
    # ============================================================

    st.markdown("## 🔢 Numerical Information")

    numeric_columns = df.select_dtypes(
        include=["int64", "float64", "int32", "float32"]
    ).columns.tolist()

    if numeric_columns:

        selected_numeric = st.selectbox(
            "Select a numerical column",
            numeric_columns
        )

        selected_data = df[selected_numeric].dropna()

        average_value = selected_data.mean()
        minimum_value = selected_data.min()
        maximum_value = selected_data.max()
        median_value = selected_data.median()


        ncol1, ncol2, ncol3, ncol4 = st.columns(4)

        with ncol1:
            st.markdown(f"""
            <div class="kpi-card"
            style="background:linear-gradient(135deg,#7c3aed,#c084fc);">
                <div class="kpi-title">📊 Average</div>
                <div class="kpi-value">{average_value:.2f}</div>
            </div>
            """, unsafe_allow_html=True)

        with ncol2:
            st.markdown(f"""
            <div class="kpi-card"
            style="background:linear-gradient(135deg,#0284c7,#38bdf8);">
                <div class="kpi-title">⬇️ Minimum</div>
                <div class="kpi-value">{minimum_value:.2f}</div>
            </div>
            """, unsafe_allow_html=True)

        with ncol3:
            st.markdown(f"""
            <div class="kpi-card"
            style="background:linear-gradient(135deg,#16a34a,#4ade80);">
                <div class="kpi-title">⬆️ Maximum</div>
                <div class="kpi-value">{maximum_value:.2f}</div>
            </div>
            """, unsafe_allow_html=True)

        with ncol4:
            st.markdown(f"""
            <div class="kpi-card"
            style="background:linear-gradient(135deg,#ea580c,#fb923c);">
                <div class="kpi-title">📌 Median</div>
                <div class="kpi-value">{median_value:.2f}</div>
            </div>
            """, unsafe_allow_html=True)


    # ============================================================
    # STATISTICAL SUMMARY
    # ============================================================

    st.markdown("## 📈 Statistical Summary")

    numeric_summary = df.select_dtypes(
        include=["int64", "float64", "int32", "float32"]
    ).describe().T

    numeric_summary = numeric_summary.round(2)

    st.dataframe(
        numeric_summary.style
        .background_gradient(cmap="BuPu")
        .set_properties(
            **{
                "font-size": "13px",
                "text-align": "center"
            }
        ),
        use_container_width=True
    )


    # ============================================================
    # CATEGORY ANALYSIS
    # ============================================================

    st.markdown("## 🏷️ Explore Employee Categories")

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if categorical_columns:

        selected_category = st.selectbox(
            "Select a categorical column",
            categorical_columns
        )

        category_count = (
            df[selected_category]
            .value_counts()
            .reset_index()
        )

        category_count.columns = [
            selected_category,
            "Employee Count"
        ]

        c1, c2 = st.columns([1, 1])

        with c1:

            st.dataframe(
                category_count.style
                .background_gradient(
                    subset=["Employee Count"],
                    cmap="PuRd"
                )
                .set_properties(
                    **{
                        "font-size": "14px",
                        "text-align": "center"
                    }
                ),
                use_container_width=True,
                hide_index=True
            )

        with c2:
             
    #          st.markdown("### 📊 Employee Distribution")

    # category_counts = filtered["Attrition"].value_counts()

    # st.dataframe(
    #     category_counts.reset_index(),
    #     use_container_width=True,
    #     hide_index=True
    # )

    # st.bar_chart(
    #     category_counts,
    #     use_container_width=True
    # ) 
            st.markdown("### 📌 Dataset Highlights")

    st.markdown("#### 👩‍💼 Employee Overview")

    total_emp = len(filtered)
    avg_age = filtered["Age"].mean()
    avg_income = filtered["MonthlyIncome"].mean()

    st.metric(
        "Total Employees",
        f"{total_emp:,}"
    )

    st.metric(
        "Average Age",
        f"{avg_age:.1f} years"
    )

    st.metric(
        "Average Monthly Income",
        f"₹{avg_income:,.0f}"
    )

    st.markdown("#### 🏢 Department Overview")

    dept_count = filtered["Department"].value_counts()

    st.dataframe(
        dept_count.reset_index(name="Employee Count"),
        use_container_width=True,
        hide_index=True
    )
    
    # ============================================================
    # DOWNLOAD DATASET
    # ============================================================

    

    st.write(
        "Download the complete IBM HR Analytics employee dataset."
    )

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Complete Dataset",
        data=csv_data,
        file_name="IBM_HR_Analytics_Employee_Attrition.csv",
        mime="text/csv",
        use_container_width=False
    )

    st.success(
        "✅ Dataset explorer is ready. You can search, understand, "
        "analyse and download your employee data."
    )
    
    
elif opt=="Pre-Processing":
    st.title("⚙️ Data Pre-Processing")

    st.markdown("""
    <style>

    /* ---------- PAGE BACKGROUND ---------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #f8f9ff 0%,
            #fdfbff 45%,
            #f5f9ff 100%
        );
    }

    /* ---------- MAIN TITLE ---------- */

    .prep-title {
        background: linear-gradient(
            90deg,
            #6a11cb,
            #2575fc,
            #00b09b
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .prep-subtitle {
        color: #64748b;
        font-size: 18px;
        margin-bottom: 25px;
    }

    /* ---------- SECTION HEADINGS ---------- */

    .section-heading {
        padding: 13px 18px;
        border-radius: 14px;
        background: linear-gradient(
            90deg,
            #eef2ff,
            #f5f3ff,
            #ecfeff
        );
        border-left: 5px solid #6366f1;
        color: #312e81;
        font-size: 23px;
        font-weight: 750;
        margin-top: 25px;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(99,102,241,0.08);
    }

    /* ---------- DESCRIPTION BOX ---------- */

    .description-box {
        padding: 18px 22px;
        border-radius: 16px;
        background: rgba(255,255,255,0.82);
        border: 1px solid #e5e7eb;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
        color: #475569;
        line-height: 1.7;
        margin-bottom: 22px;
    }

    /* ---------- KPI CARDS ---------- */

    .kpi-card {
        padding: 20px 12px;
        border-radius: 20px;
        text-align: center;
        color: white;
        min-height: 125px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow:
            0 8px 20px rgba(0,0,0,0.12),
            inset 0 1px 0 rgba(255,255,255,0.3);
        transition: 0.25s ease;
        margin-bottom: 18px;
    }

    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow:
            0 12px 28px rgba(0,0,0,0.17);
    }

    .kpi-label {
        font-size: 15px;
        font-weight: 600;
        letter-spacing: 0.3px;
    }

    .kpi-value {
        font-size: 30px;
        font-weight: 800;
        color: white;
        margin-top: 8px;
    }

    /* ---------- DIFFERENT KPI COLORS ---------- */

    .purple {
        background: linear-gradient(
            135deg,#7c3aed,#4f46e5
        );
    }

    .pink {
        background: linear-gradient(
            135deg,#ec4899,#db2777
        );
    }

    .green {
        background: linear-gradient(
            135deg,#10b981,#059669
        );
    }

    .orange {
        background: linear-gradient(
            135deg,#f59e0b,#ea580c
        );
    }

    .blue {
        background: linear-gradient(
            135deg,#2563eb,#06b6d4
        );
    }

    .red {
        background: linear-gradient(
            135deg,#ef4444,#e11d48
        );
    }

    .teal {
        background: linear-gradient(
            135deg,#14b8a6,#0f766e
        );
    }

    .violet {
        background: linear-gradient(
            135deg,#8b5cf6,#7c3aed
        );
    }

    /* ---------- INFORMATION BOX ---------- */

    .info-box {
        padding: 18px 20px;
        border-radius: 16px;
        background: linear-gradient(
            135deg,
            #ffffff,
            #f5f3ff
        );
        border-left: 5px solid #6366f1;
        box-shadow: 0 5px 16px rgba(0,0,0,0.06);
        margin: 15px 0 20px 0;
    }

    /* ---------- SUCCESS BOX ---------- */

    .success-box {
        padding: 18px 20px;
        border-radius: 16px;
        background: linear-gradient(
            135deg,
            #ecfdf5,
            #f0fdf4
        );
        border-left: 5px solid #10b981;
        box-shadow: 0 5px 16px rgba(16,185,129,0.08);
        margin: 15px 0 20px 0;
    }

    /* ---------- REMOVED COLUMN BOX ---------- */

    .removed-box {
        padding: 18px 20px;
        border-radius: 16px;
        background: linear-gradient(
            135deg,
            #fff1f2,
            #fdf2f8
        );
        border-left: 5px solid #e11d48;
        box-shadow: 0 5px 16px rgba(225,29,72,0.08);
        margin: 15px 0 15px 0;
    }

    /* ---------- STREAMLIT DATAFRAME ---------- */

    div[data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #e2e8f0;
        box-shadow: 0 5px 18px rgba(0,0,0,0.07);
        background: white;
    }

    /* ---------- METRIC BOXES ---------- */

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.85);
        border-radius: 16px;
        padding: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.06);
    }

    /* ---------- SUCCESS / WARNING ---------- */

    div[data-testid="stAlert"] {
        border-radius: 14px;
    }

    /* ---------- DIVIDER ---------- */

    hr {
        margin-top: 30px;
        margin-bottom: 30px;
        border: none;
        height: 2px;
        background: linear-gradient(
            90deg,
            transparent,
            #c4b5fd,
            #93c5fd,
            transparent
        );
    }

    </style>
    """, unsafe_allow_html=True)


    # =========================================================
    # PAGE TITLE
    # =========================================================

    st.markdown(
        '<div class="prep-title">🧹 HR Employee Data Pre-Processing</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="prep-subtitle">'
        '🔄 Clean, Check & Prepare Your Employee Dataset'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="description-box">
        📌 This section checks the quality of the HR dataset,
        removes unnecessary columns, checks missing values and
        duplicates, and prepares the cleaned dataset for analysis.
    </div>
    """, unsafe_allow_html=True)


    # =========================================================
    # 1. ORIGINAL DATASET
    # =========================================================

    st.markdown(
        '<div class="section-heading">📂 1. Original Dataset</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )


    # =========================================================
    # 2. DATASET INFORMATION
    # =========================================================

    st.markdown(
        '<div class="section-heading">📊 2. Dataset Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="kpi-card purple">
            <div class="kpi-label">📋 Rows</div>
            <div class="kpi-value">{df.shape[0]:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card blue">
            <div class="kpi-label">📊 Columns</div>
            <div class="kpi-value">{df.shape[1]:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card green">
            <div class="kpi-label">🔢 Total Cells</div>
            <div class="kpi-value">
                {df.shape[0] * df.shape[1]:,}
            </div>
        </div>
        """, unsafe_allow_html=True)


    # =========================================================
    # 3. MISSING VALUES
    # =========================================================

    st.markdown(
        '<div class="section-heading">🔍 3. Missing Values</div>',
        unsafe_allow_html=True
    )

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    missing_df["Missing %"] = (
        missing_df["Missing Values"]
        / len(df)
        * 100
    ).round(2)

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True
    )

    total_missing = df.isnull().sum().sum()

    if total_missing == 0:
        st.success(
            "✅ No missing values found in the dataset."
        )
    else:
        st.warning(
            f"⚠️ Total missing values: {total_missing:,}"
        )


    # =========================================================
    # 4. DUPLICATES
    # =========================================================

    st.markdown(
        '<div class="section-heading">♻️ 4. Duplicate Records</div>',
        unsafe_allow_html=True
    )

    duplicate_count = df.duplicated().sum()

    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown(f"""
        <div class="kpi-card orange">
            <div class="kpi-label">♻️ Duplicate Rows</div>
            <div class="kpi-value">{duplicate_count:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        if duplicate_count == 0:
            st.success(
                "✅ No duplicate records found."
            )
        else:
            st.warning(
                f"⚠️ {duplicate_count:,} duplicate records found."
            )


    # =========================================================
    # 5. DATA TYPES
    # =========================================================

    st.markdown(
        '<div class="section-heading">🔤 5. Data Types</div>',
        unsafe_allow_html=True
    )

    datatype_df = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Unique Values": [
            df[col].nunique()
            for col in df.columns
        ]
    })

    st.dataframe(
        datatype_df,
        use_container_width=True,
        hide_index=True
    )


    # =========================================================
    # 6. COLUMN CLEANING
    # =========================================================

    st.markdown(
        '<div class="section-heading">🧼 6. Data Cleaning</div>',
        unsafe_allow_html=True
    )

    cleaned_df = df.copy()

    # ---------------------------------------------------------
    # Columns to remove
    # ---------------------------------------------------------

    columns_to_remove = [
        "EmployeeCount",
        "Over18",
        "StandardHours"
    ]

    removed_columns = [
        col
        for col in columns_to_remove
        if col in cleaned_df.columns
    ]

    cleaned_df.drop(
        columns=removed_columns,
        inplace=True
    )


    # =========================================================
    # 7. BEFORE VS AFTER COLUMNS
    # =========================================================

    st.markdown(
        '<div class="section-heading">🔄 7. Before vs After Cleaning</div>',
        unsafe_allow_html=True
    )

    before_columns = df.shape[1]
    removed_count = len(removed_columns)
    after_columns = cleaned_df.shape[1]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="kpi-card pink">
            <div class="kpi-label">🔵 Before Cleaning</div>
            <div class="kpi-value">{before_columns}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card red">
            <div class="kpi-label">🗑️ Columns Removed</div>
            <div class="kpi-value">{removed_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card teal">
            <div class="kpi-label">🟢 After Cleaning</div>
            <div class="kpi-value">{after_columns}</div>
        </div>
        """, unsafe_allow_html=True)


    # =========================================================
    # 8. REMOVED COLUMNS
    # =========================================================

    st.markdown(
        '<div class="section-heading">🗑️ 8. Removed Columns</div>',
        unsafe_allow_html=True
    )

    if removed_columns:

        st.markdown("""
        <div class="removed-box">
            ✅ The following unnecessary columns were removed:
        </div>
        """, unsafe_allow_html=True)

        removed_df = pd.DataFrame({
            "Removed Column": removed_columns
        })

        st.dataframe(
            removed_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.error(
            "❌ The specified columns were not found."
        )

        st.write(
            "Available columns are:"
        )

        st.write(
            df.columns.tolist()
        )


    # =========================================================
    # 9. REMOVE DUPLICATES
    # =========================================================

    st.markdown(
        '<div class="section-heading">♻️ 9. Remove Duplicate Records</div>',
        unsafe_allow_html=True
    )

    duplicates_before = cleaned_df.duplicated().sum()

    cleaned_df.drop_duplicates(
        inplace=True
    )

    duplicates_after = cleaned_df.duplicated().sum()

    st.write(
        f"🧹 Duplicate rows removed: "
        f"**{duplicates_before:,}**"
    )


    # =========================================================
    # 10. HANDLE MISSING VALUES
    # =========================================================

    st.markdown(
        '<div class="section-heading">🩹 10. Missing Value Handling</div>',
        unsafe_allow_html=True
    )

    missing_before = (
        cleaned_df.isnull()
        .sum()
        .sum()
    )

    # Numeric columns → Median
    numeric_columns = (
        cleaned_df
        .select_dtypes(include=["number"])
        .columns
    )

    for col in numeric_columns:

        if cleaned_df[col].isnull().sum() > 0:

            cleaned_df[col] = cleaned_df[col].fillna(
                cleaned_df[col].median()
            )

    # Categorical columns → Mode
    categorical_columns = (
        cleaned_df
        .select_dtypes(
            include=["object", "category"]
        )
        .columns
    )

    for col in categorical_columns:

        if cleaned_df[col].isnull().sum() > 0:

            if not cleaned_df[col].mode().empty:

                cleaned_df[col] = cleaned_df[col].fillna(
                    cleaned_df[col].mode().iloc[0]
                )

    missing_after = (
        cleaned_df.isnull()
        .sum()
        .sum()
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="kpi-card orange">
            <div class="kpi-label">🔍 Missing Before</div>
            <div class="kpi-value">{missing_before:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card green">
            <div class="kpi-label">✨ Missing After</div>
            <div class="kpi-value">{missing_after:,}</div>
        </div>
        """, unsafe_allow_html=True)

    if missing_after == 0:
        st.success(
            "✅ No missing values remain after cleaning."
        )


    # =========================================================
    # 11. RESET INDEX
    # =========================================================

    cleaned_df.reset_index(
        drop=True,
        inplace=True
    )


    # =========================================================
    # 12. CLEANED DATASET
    # =========================================================

    st.markdown(
        '<div class="section-heading">✨ 12. Cleaned Dataset</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="success-box">
        🎉 <b>Cleaned Dataset Ready!</b><br>
        The cleaned dataset contains
        <b>{cleaned_df.shape[0]:,} rows</b>
        and
        <b>{cleaned_df.shape[1]} columns</b>.
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        cleaned_df.head(10),
        use_container_width=True,
        hide_index=True
    )


    # =========================================================
    # 13. FINAL DATA QUALITY CHECK
    # =========================================================

    st.markdown(
        '<div class="section-heading">✅ 13. Final Data Quality Check</div>',
        unsafe_allow_html=True
    )

    final_missing = (
        cleaned_df.isnull()
        .sum()
        .sum()
    )

    final_duplicates = (
        cleaned_df.duplicated()
        .sum()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="kpi-card purple">
            <div class="kpi-label">👥 Final Rows</div>
            <div class="kpi-value">
                {cleaned_df.shape[0]:,}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card blue">
            <div class="kpi-label">📊 Final Columns</div>
            <div class="kpi-value">
                {cleaned_df.shape[1]:,}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card green">
            <div class="kpi-label">🔍 Missing Values</div>
            <div class="kpi-value">
                {final_missing:,}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card pink">
            <div class="kpi-label">♻️ Duplicate Rows</div>
            <div class="kpi-value">
                {final_duplicates:,}
            </div>
        </div>
        """, unsafe_allow_html=True)


    # =========================================================
    # 14. FINAL STATUS
    # =========================================================

    st.markdown(
        '<div class="section-heading">🎯 14. Final Status</div>',
        unsafe_allow_html=True
    )

    if (
        cleaned_df.shape[1] == 32
        and final_missing == 0
        and final_duplicates == 0
    ):

        st.success(
            "🎉 Pre-Processing Completed Successfully!"
        )

        st.info(
            "The dataset has been successfully reduced "
            "from 35 columns to 32 columns."
        )

    else:

        st.info(
            f"Current cleaned dataset contains "
            f"{cleaned_df.shape[1]} columns."
        )


    # =========================================================
    # 15. SAVE CLEANED DATA
    # =========================================================

    st.session_state["cleaned_data"] = cleaned_df
elif opt=="Visualization":
    st.title("📊 HR Analytics Visualizations")

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#4f46e5,#7c3aed);
        padding: 28px;
        border-radius: 20px;
        margin-bottom: 25px;
        text-align: center;
    ">
        <h1 style="color:white; margin:0;">
            📊 HR Analytics Visualizations
        </h1>
        <p style="color:#e0e7ff; font-size:17px; margin-top:8px;">
            Explore workforce, attrition, compensation and employee satisfaction patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)


    # =========================================================
    # FILTERS
    # =========================================================

    st.markdown("### 🔍 Dashboard Filters")

    col1, col2 = st.columns(2)

    with col1:
        department_filter = st.selectbox(
            "Department",
            ["All"] + sorted(df["Department"].dropna().unique().tolist())
        )

    with col2:
        gender_filter = st.selectbox(
            "Gender",
            ["All"] + sorted(df["Gender"].dropna().unique().tolist())
        )


    filtered_df = df.copy()

    if department_filter != "All":
        filtered_df = filtered_df[
            filtered_df["Department"] == department_filter
        ]

    if gender_filter != "All":
        filtered_df = filtered_df[
            filtered_df["Gender"] == gender_filter
        ]


    st.success(
        f"Showing {len(filtered_df):,} employees"
    )

    st.divider()


    # =========================================================
    # TOPIC 1 — WORKFORCE & DEMOGRAPHICS
    # =========================================================

    st.markdown("## 👥 Workforce & Demographics")

    st.caption(
        "Understand employee distribution across departments, age groups, "
        "job roles and marital status."
    )

    col1, col2 = st.columns(2)

    # ---------------------------------------------------------
    # GRAPH 1 — TOTAL EMPLOYEES BY DEPARTMENT
    # ---------------------------------------------------------

    with col1:

        depar_count = (
            filtered_df.groupby("Department")
            .size()
            .reset_index(name="Total Employees")
        )

        fig = px.bar(
            depar_count,
            x="Department",
            y="Total Employees",
            color="Department",
            text="Total Employees",
            title="<b>Total Employees by Department</b>",
            hover_data={
                "Department": True,
                "Total Employees": True
            }
        )

        fig.update_traces(
            textposition="outside",
            marker_line_color="black",
            marker_line_width=1.5
        )

        fig.update_layout(
            template="plotly_white",
            title_x=0.5,
            title_font=dict(size=22),
            height=500,
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 2 — AGE DISTRIBUTION
    # ---------------------------------------------------------

    with col2:

        fig = px.histogram(
            filtered_df,
            x="Age",
            nbins=10,
            title="<b>Age Distribution of the Workforce</b>",
            color_discrete_sequence=px.colors.qualitative.Pastel1,
            text_auto=True,
            hover_data={"Age": True}
        )

        fig.update_traces(
            marker_line_color="black",
            marker_line_width=1.9
        )

        fig.update_layout(
            template="plotly_white",
            title_font=dict(size=22),
            height=500,
            title_x=0.5,
            showlegend=False,
            yaxis_title="Count of Employees",
            xaxis_title="Age"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    col3, col4 = st.columns(2)


    # ---------------------------------------------------------
    # GRAPH 3 — GENDER DISTRIBUTION ACROSS JOB ROLES
    # ---------------------------------------------------------

    with col3:

        fig = px.treemap(
            filtered_df,
            path=["JobRole", "Gender"],
            title="<b>Gender Distribution Across Job Roles</b>",
            color="Gender",
            color_discrete_sequence=["blue", "pink"],
            hover_data={
                "JobRole": True,
                "Gender": True
            }
        )

        fig.update_traces(
            textfont=dict(size=15),
            marker_line_width=3,
            marker_line_color="black",
            root_color="lightgrey",
            textinfo="label+value"
        )

        fig.update_layout(
            template="plotly_white",
            title_font=dict(size=22),
            height=600,
            title_x=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 4 — MARITAL STATUS BREAKDOWN
    # ---------------------------------------------------------

    with col4:

        marital_count = (
            filtered_df.groupby("MaritalStatus")
            .size()
            .reset_index(name="Count")
        )

        fig = px.pie(
            marital_count,
            names="MaritalStatus",
            values="Count",
            title="<b>Marital Status Breakdown</b>",
            color="MaritalStatus",
            color_discrete_sequence=px.colors.qualitative.Dark24
        )

        fig.update_traces(
            textinfo="label+percent",
            hole=0.4
        )

        fig.update_layout(
            title_font_size=26,
            height=600,
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.divider()


    # =========================================================
    # TOPIC 2 — ATTRITION ANALYSIS
    # =========================================================

    st.markdown("## 🚪 Employee Attrition Analysis")

    st.caption(
        "Analyze employee turnover and identify departments, job roles "
        "and experience levels associated with attrition."
    )

    col1, col2 = st.columns(2)


    # ---------------------------------------------------------
    # GRAPH 5 — EMPLOYEE ATTRITION OVERVIEW
    # ---------------------------------------------------------

    with col1:

        attrition_count = (
            filtered_df.groupby("Attrition")
            .size()
            .reset_index(name="Count")
        )

        fig = px.bar(
            attrition_count,
            x="Attrition",
            y="Count",
            title="<b>Employee Attrition Overview</b>",
            color="Attrition",
            text_auto=True
        )

        fig.update_layout(
            title_x=0.5,
            xaxis_title="Attrition",
            yaxis_title="Number of Employees",
            template="plotly_white",
            height=500
        )

        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 6 — ATTRITION BY DEPARTMENT & JOB ROLE
    # ---------------------------------------------------------

    with col2:

        employees_left = filtered_df[
            filtered_df["Attrition"] == "Yes"
        ]

        fig = px.sunburst(
            employees_left,
            path=["Department", "JobRole"],
            color="Department",
            color_discrete_sequence=px.colors.qualitative.Dark24,
            title="<b>Employee Attrition by Department and Job Role</b>"
        )

        fig.update_traces(
            textinfo="label+value",
            textfont_size=14,
            textfont_color="black"
        )

        fig.update_layout(
            title_x=0.5,
            template="plotly_dark",
            height=600,
            hoverlabel=dict(
                bgcolor="white",
                font_color="blue",
                font_size=12
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    col3, col4 = st.columns(2)


    # ---------------------------------------------------------
    # GRAPH 7 — EMPLOYEES LEFT BY JOB ROLE
    # ---------------------------------------------------------

    with col3:

        employees_left = filtered_df[
            filtered_df["Attrition"] == "Yes"
        ]

        jobs = (
            employees_left.groupby("JobRole")
            .size()
            .reset_index(name="Count")
        )

        fig = px.bar(
            jobs,
            x="JobRole",
            y="Count",
            title="<b>Employees Left by Job Role</b>",
            text_auto=True,
            color="JobRole",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig.update_traces(
            textfont_size=12,
            marker_line_color="black",
            marker_line_width=2
        )

        fig.update_layout(
            title_x=0.5,
            xaxis_title="Job Role",
            yaxis_title="Number of Employees",
            height=550,
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 8 — ATTRITION TREND BY YEARS AT COMPANY
    # ---------------------------------------------------------

    with col4:

        employees_left = filtered_df[
            filtered_df["Attrition"] == "Yes"
        ]

        years = (
            employees_left.groupby("YearsAtCompany")
            .size()
            .reset_index(name="count")
        )

        fig = px.line(
            years,
            x="YearsAtCompany",
            y="count",
            title="<b>Attrition Trend by Years at Company</b>",
            markers=True
        )

        fig.update_traces(
            line_color="green",
            line_width=3,
            marker=dict(
                size=7,
                color="red"
            )
        )

        fig.update_layout(
            title_x=0.5,
            xaxis_title="Years at Company",
            yaxis_title="Employees Left",
            height=550,
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.divider()


    # =========================================================
    # TOPIC 3 — COMPENSATION & INCOME
    # =========================================================

    st.markdown("## 💰 Compensation & Income Analysis")

    st.caption(
        "Explore how monthly income varies with age, job role, department and gender."
    )

    col1, col2 = st.columns(2)


    # ---------------------------------------------------------
    # GRAPH 9 — MONTHLY INCOME VS AGE
    # ---------------------------------------------------------

    with col1:

        fig = px.scatter(
            filtered_df,
            x="Age",
            y="MonthlyIncome",
            color="Attrition",
            color_discrete_sequence=px.colors.qualitative.Dark24,
            title="<b>Monthly Income vs Age by Attrition Status</b>",
            hover_data=["JobRole", "Department"]
        )

        fig.update_traces(
            marker=dict(
                size=7,
                opacity=1,
                symbol="star"
            )
        )

        fig.update_layout(
            title_x=0.5,
            xaxis_title="Age",
            yaxis_title="Monthly Income",
            template="plotly_white",
            height=550
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 10 — MONTHLY INCOME BY JOB ROLE
    # ---------------------------------------------------------

    with col2:

        fig = px.box(
            filtered_df,
            x="JobRole",
            y="MonthlyIncome",
            title="<b>Monthly Income Distribution by Job Role</b>",
            color="JobRole",
            points="outliers",
            color_discrete_sequence=px.colors.qualitative.Bold
        )

        fig.update_layout(
            title_x=0.5,
            title_font_size=23,
            xaxis_title="Job Role",
            yaxis_title="Monthly Income",
            template="plotly_dark",
            height=550,
            showlegend=False
        )

        fig.update_traces(
            hoverlabel=dict(
                bgcolor="white",
                font_color="black"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    col3, col4 = st.columns(2)


    # ---------------------------------------------------------
    # GRAPH 13 — MONTHLY INCOME BY GENDER
    # ---------------------------------------------------------

    with col3:

        fig = px.box(
            filtered_df,
            x="Gender",
            y="MonthlyIncome",
            title="<b>Monthly Income by Gender</b>",
            color="Gender",
            color_discrete_map={
                "Male": "blue",
                "Female": "red"
            },
            points="outliers"
        )

        fig.update_layout(
            title_x=0.5,
            template="plotly_dark",
            height=550
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 14 — MONTHLY INCOME BY DEPARTMENT
    # ---------------------------------------------------------

    with col4:

        fig = px.violin(
            filtered_df,
            x="Department",
            y="MonthlyIncome",
            color="Department",
            box=True,
            points="all",
            title="<b>Monthly Income by Department</b>",
            color_discrete_sequence=px.colors.qualitative.Bold
        )

        fig.update_traces(
            marker=dict(size=4),
            line=dict(width=2)
        )

        fig.update_layout(
            title_x=0.5,
            title_font_size=25,
            height=550,
            xaxis_title="Department",
            yaxis_title="Monthly Income",
            template="plotly_dark",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.divider()


    # =========================================================
    # TOPIC 4 — SATISFACTION & WORK-LIFE
    # =========================================================

    st.markdown("## 😊 Satisfaction & Work-Life Analysis")

    st.caption(
        "Explore employee satisfaction, performance, distance from home and overtime patterns."
    )

    col1, col2 = st.columns(2)


    # ---------------------------------------------------------
    # GRAPH 11 — JOB SATISFACTION VS PERFORMANCE
    # ---------------------------------------------------------

    with col1:

        fig = px.violin(
            filtered_df,
            x="PerformanceRating",
            y="JobSatisfaction",
            box=True,
            points="all",
            title="<b>Job Satisfaction Across Performance Ratings</b>"
        )

        fig.update_traces(
            line_color="black",
            fillcolor="yellow",
            box_line_color="red",
            box_fillcolor="pink"
        )

        fig.update_layout(
            xaxis_title="Performance Rating",
            yaxis_title="Job Satisfaction",
            template="plotly_dark",
            title_x=0.5,
            height=550
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 15 — DISTANCE FROM HOME VS JOB SATISFACTION
    # ---------------------------------------------------------

    with col2:

        fig = px.scatter(
            filtered_df,
            x="DistanceFromHome",
            y="JobSatisfaction",
            color="DistanceFromHome",
            title="<b>Distance From Home vs Job Satisfaction</b>",
            color_discrete_sequence=px.colors.qualitative.Bold,
            hover_data=[
                "Department",
                "JobRole",
                "MonthlyIncome"
            ]
        )

        fig.update_traces(
            marker=dict(size=10)
        )

        fig.update_layout(
            title_x=0.5,
            title_font_size=24,
            xaxis_title="Distance From Home",
            yaxis_title="Job Satisfaction",
            template="plotly_dark",
            height=550,
            hoverlabel=dict(
                bgcolor="white",
                font_color="black",
                font_size=14
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 16 — OVERTIME
    # ---------------------------------------------------------

    fig = px.pie(
        filtered_df,
        names="OverTime",
        title="<b>Employees Working Overtime</b>",
        color="OverTime",
        color_discrete_sequence=px.colors.qualitative.Set1
    )

    fig.update_traces(
        textinfo="percent+label",
        textfont_size=15,
        pull=[0, 0.08]
    )

    fig.update_layout(
        title_x=0.5,
        title_font_size=30,
        template="plotly_dark",
        height=550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.divider()


    # =========================================================
    # TOPIC 5 — EDUCATION & EMPLOYEE FACTORS
    # =========================================================

    st.markdown("## 🎓 Education & Employee Factors")

    st.caption(
        "Compare employee education fields and examine relationships between key numerical HR metrics."
    )

    col1, col2 = st.columns(2)


    # ---------------------------------------------------------
    # GRAPH 17 — EDUCATION FIELD BY GENDER
    # ---------------------------------------------------------

    with col1:

        data = (
            filtered_df
            .groupby(["EducationField", "Gender"])
            .size()
            .reset_index(name="Count of Employees")
        )

        fig = px.bar(
            data,
            x="EducationField",
            y="Count of Employees",
            color="Gender",
            color_discrete_sequence=px.colors.qualitative.Bold,
            title="<b>Male and Female Employees by Education Field</b>"
        )

        fig.update_layout(
            title_x=0.5,
            title_font_size=22,
            xaxis_title="Education Field",
            yaxis_title="Number of Employees",
            template="plotly_dark",
            height=550
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------------------------------------------------
    # GRAPH 12 — CORRELATION HEATMAP
    # ---------------------------------------------------------

    with col2:

        num_df = filtered_df[
            [
                "Age",
                "MonthlyIncome",
                "DistanceFromHome",
                "PercentSalaryHike",
                "WorkLifeBalance"
            ]
        ]

        corr_matrix = num_df.corr()

        fig = px.imshow(
            corr_matrix,
            text_auto=True,
            color_continuous_scale=px.colors.sequential.Viridis,
            title="<b>Correlation of Numerical Metrics</b>"
        )

        fig.update_layout(
            title_x=0.5,
            xaxis_title="Numerical Columns",
            yaxis_title="Numerical Columns",
            template="plotly_white",
            font=dict(size=14),
            height=550
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # =========================================================
    # END NOTE
    # =========================================================

    st.markdown("""
    <div style="
        margin-top:30px;
        padding:22px;
        border-radius:18px;
        background:linear-gradient(135deg,#eef2ff,#fdf2f8);
        border:1px solid #ddd6fe;
        text-align:center;
    ">
        <h3>💡 HR Analytics Visualization Summary</h3>
        <p>
        These visualizations help identify workforce structure, employee attrition,
        compensation patterns, satisfaction levels and important relationships
        within the HR dataset.
        </p>
    </div>
    """, unsafe_allow_html=True)
    

elif opt=="HR Insights":
    st.title("💡 HR Insights")

    st.markdown("""
    <style>

    /* ================= KPI CARDS ================= */

    .kpi-card {
        padding: 20px 18px;
        border-radius: 18px;
        min-height: 120px;
        margin-bottom: 18px;
        text-align: left;
        color: #111827;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 22px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }

    .kpi-card:hover {
        transform: translateY(-7px);
        box-shadow: 0 16px 30px rgba(0,0,0,0.15);
    }

    /* Different KPI colors */

    .kpi-blue {
        border-left: 7px solid #2563eb;
        background: linear-gradient(135deg, #eff6ff, #ffffff);
    }

    .kpi-purple {
        border-left: 7px solid #7c3aed;
        background: linear-gradient(135deg, #f5f3ff, #ffffff);
    }

    .kpi-green {
        border-left: 7px solid #16a34a;
        background: linear-gradient(135deg, #f0fdf4, #ffffff);
    }

    .kpi-orange {
        border-left: 7px solid #f97316;
        background: linear-gradient(135deg, #fff7ed, #ffffff);
    }

    .kpi-pink {
        border-left: 7px solid #ec4899;
        background: linear-gradient(135deg, #fdf2f8, #ffffff);
    }

    .kpi-cyan {
        border-left: 7px solid #06b6d4;
        background: linear-gradient(135deg, #ecfeff, #ffffff);
    }

    .kpi-title {
        font-size: 15px;
        font-weight: 650;
        color: #4b5563;
        margin-bottom: 10px;
    }

    .kpi-value {
        font-size: 28px;
        font-weight: 800;
        color: #111827;
    }

    .kpi-subtitle {
        font-size: 13px;
        color: #6b7280;
        margin-top: 5px;
    }

    </style>
    """, unsafe_allow_html=True)


    # =========================================================
    # TITLE
    # =========================================================

    st.markdown("# 📊 HR Insights")

    st.markdown(
        "### Explore employee patterns, workforce structure and factors related to attrition."
    )


    # =========================================================
    # PROJECT HEADLINE
    # =========================================================

    st.markdown("""
    ### 🌟 HR Analytics Employee Attrition Dashboard

    This section highlights important workforce patterns from the employee dataset.

    Use these insights to understand:

    - Employee attrition patterns
    - Department-wise workforce structure
    - Job role behaviour
    - Business travel patterns
    - Education and experience
    - Employee satisfaction
    - Income and work-life balance
    - Factors associated with employee turnover
    """)


    # =========================================================
    # CALCULATE VALUES
    # =========================================================

    total_employees = len(df)

    avg_age = df["Age"].mean()

    max_age = df["Age"].max()

    avg_years = df["YearsAtCompany"].mean()

    max_years = df["YearsAtCompany"].max()

    attrition_count = (df["Attrition"] == "Yes").sum()

    attrition_rate = (attrition_count / total_employees) * 100


    # =========================================================
    # WORKFORCE SNAPSHOT
    # =========================================================

    st.markdown("## 📌 Workforce Snapshot")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="kpi-card kpi-blue">
            <div class="kpi-title">👥 Total Employees</div>
            <div class="kpi-value">{total_employees:,}</div>
            <div class="kpi-subtitle">Employees in dataset</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi-card kpi-purple">
            <div class="kpi-title">🎂 Average Age</div>
            <div class="kpi-value">{avg_age:.1f}</div>
            <div class="kpi-subtitle">Average employee age</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi-card kpi-green">
            <div class="kpi-title">📈 Average Years at Company</div>
            <div class="kpi-value">{avg_years:.1f}</div>
            <div class="kpi-subtitle">Average company tenure</div>
        </div>
        """, unsafe_allow_html=True)


    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown(f"""
        <div class="kpi-card kpi-orange">
            <div class="kpi-title">🚪 Employees Left</div>
            <div class="kpi-value">{attrition_count:,}</div>
            <div class="kpi-subtitle">Employees with attrition</div>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown(f"""
        <div class="kpi-card kpi-pink">
            <div class="kpi-title">📉 Attrition Rate</div>
            <div class="kpi-value">{attrition_rate:.1f}%</div>
            <div class="kpi-subtitle">Overall attrition percentage</div>
        </div>
        """, unsafe_allow_html=True)

    with c6:
        st.markdown(f"""
        <div class="kpi-card kpi-cyan">
            <div class="kpi-title">🏆 Maximum Years at Company</div>
            <div class="kpi-value">{max_years}</div>
            <div class="kpi-subtitle">Highest company tenure</div>
        </div>
        """, unsafe_allow_html=True)


    # =========================================================
    # DEPARTMENT INSIGHTS
    # =========================================================

    st.markdown("## 🏢 Department Insights")

    department_counts = df["Department"].value_counts()

    cols = st.columns(len(department_counts))

    for i, (department, count) in enumerate(department_counts.items()):

        with cols[i]:

            st.metric(
                f"🏢 {department}",
                f"{count:,}",
                "Employees"
            )


    # =========================================================
    # JOB ROLE INSIGHTS
    # =========================================================

    st.markdown("## 💼 Job Role Insights")

    top_roles = df["JobRole"].value_counts().head(6)

    cols = st.columns(3)

    for i, (role, count) in enumerate(top_roles.items()):

        with cols[i % 3]:

            st.metric(
                f"💼 {role}",
                f"{count:,}",
                "Employees"
            )


    # =========================================================
    # BUSINESS TRAVEL
    # =========================================================

    st.markdown("## ✈️ Business Travel Insights")

    travel_counts = df["BusinessTravel"].value_counts()

    cols = st.columns(len(travel_counts))

    for i, (travel, count) in enumerate(travel_counts.items()):

        with cols[i]:

            st.metric(
                f"✈️ {travel}",
                f"{count:,}",
                "Employees"
            )


    # =========================================================
    # EDUCATION
    # =========================================================

    st.markdown("## 🎓 Education Insights")

    education_counts = df["EducationField"].value_counts().head(5)

    cols = st.columns(5)

    for i, (education, count) in enumerate(education_counts.items()):

        with cols[i]:

            st.metric(
                f"🎓 {education}",
                f"{count:,}",
                "Employees"
            )


    # =========================================================
    # EXPERIENCE
    # =========================================================

    st.markdown("## ⏳ Experience Insights")

    experience_metrics = [
        (
            "🕐 Average Experience",
            f"{df['TotalWorkingYears'].mean():.1f} years"
        ),
        (
            "🏆 Maximum Experience",
            f"{df['TotalWorkingYears'].max()} years"
        ),
        (
            "🏢 Average Company Tenure",
            f"{df['YearsAtCompany'].mean():.1f} years"
        )
    ]

    cols = st.columns(3)

    for i, (label, value) in enumerate(experience_metrics):

        with cols[i]:

            st.metric(label, value)


    # =========================================================
    # WHAT DASHBOARD HELPS IDENTIFY
    # =========================================================

    st.markdown("## 🔍 What This Dashboard Helps Identify")

    st.markdown("""
    ### 📌 Key Areas of Analysis

    - **Employee Attrition Patterns** — Understand how many employees leave the organization and where attrition is higher.
    - **Department Trends** — Compare employee distribution and attrition across departments.
    - **Job Role Patterns** — Identify roles with larger workforce sizes or higher employee turnover.
    - **Business Travel Impact** — Understand how travel frequency relates to employee attrition.
    - **Age & Experience** — Explore employee age, experience and years spent with the company.
    - **Education Patterns** — Compare employees across different educational backgrounds.
    - **Income & Compensation** — Understand salary-related patterns across employees.
    - **Job Satisfaction** — Explore satisfaction levels and their relationship with employee behaviour.
    - **Work-Life Balance** — Examine how work-life balance may relate to employee retention.
    """)


    # =========================================================
    # HR TAKEAWAYS
    # =========================================================

    st.markdown("## 💡 HR Takeaways")

    st.markdown("""
    ### What HR teams can learn from this dashboard

    - Identify departments with higher employee turnover.
    - Find job roles that may require additional attention.
    - Understand employee demographics and workforce composition.
    - Monitor business travel patterns.
    - Compare employee experience levels.
    - Explore compensation and satisfaction patterns.
    - Use data-driven insights to support employee retention strategies.
    """)


    # =========================================================
    # PROJECT OUTCOME
    # =========================================================

    st.markdown("## 🎯 Project Outcome")

    st.markdown("""
    This dashboard converts employee data into clear and interactive HR insights.

    It helps transform raw data into meaningful information that can support
    better understanding of workforce behaviour, employee attrition and
    organizational patterns.
    """)


    # =========================================================
    # FINAL MESSAGE
    # =========================================================

    

elif opt=="About":
    st.title("About The Dataset")
    st.markdown("""
    <style>

    /* ================================
       PAGE BACKGROUND
       ================================ */

    .stApp {
        background:
        linear-gradient(
            135deg,
            #f8f9ff 0%,
            #eef4ff 35%,
            #f8f0ff 70%,
            #fff5fb 100%
        );
    }


    /* ================================
       MAIN TITLE
       ================================ */

    h1 {
        color: #172554 !important;
        font-weight: 850 !important;
    }

    h2 {
        color: #1e1b4b !important;
        font-weight: 800 !important;
        margin-top: 25px !important;
    }

    h3 {
        color: #312e81 !important;
        font-weight: 750 !important;
    }


    /* ================================
       ALL METRIC CARDS
       ================================ */

    div[data-testid="stMetric"] {
        min-height: 135px;
        padding: 20px 18px;
        border-radius: 22px;

        background: linear-gradient(
            135deg,
            #ffffff,
            #f8faff
        );

        border: 1px solid #e0e7ff;

        box-shadow:
            0 8px 25px rgba(79, 70, 229, 0.12);

        transition:
            transform 0.35s ease,
            box-shadow 0.35s ease,
            border-color 0.35s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-9px) scale(1.025);

        box-shadow:
            0 18px 40px rgba(79, 70, 229, 0.25);

        border-color: #818cf8;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 15px !important;
        font-weight: 750 !important;
        color: #475569 !important;
    }

    div[data-testid="stMetricValue"] {
        font-size: 24px !important;
        font-weight: 850 !important;
        color: #312e81 !important;
    }


    /* ================================
       COLOURFUL METRIC CARDS
       ================================ */

    div[data-testid="stHorizontalBlock"] > div:nth-child(1)
    div[data-testid="stMetric"] {
        background: linear-gradient(
            135deg,
            #eef2ff,
            #ddd6fe
        );
        border-color: #a5b4fc;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(2)
    div[data-testid="stMetric"] {
        background: linear-gradient(
            135deg,
            #ecfeff,
            #cffafe
        );
        border-color: #67e8f9;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(3)
    div[data-testid="stMetric"] {
        background: linear-gradient(
            135deg,
            #fdf2f8,
            #fbcfe8
        );
        border-color: #f9a8d4;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(4)
    div[data-testid="stMetric"] {
        background: linear-gradient(
            135deg,
            #f0fdf4,
            #bbf7d0
        );
        border-color: #86efac;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(5)
    div[data-testid="stMetric"] {
        background: linear-gradient(
            135deg,
            #fff7ed,
            #fed7aa
        );
        border-color: #fdba74;
    }


    /* ================================
       SECTION INTRO BOX
       ================================ */

    div[data-testid="stAlert"] {
        border-radius: 18px !important;
    }


    /* ================================
       TECHNOLOGY CARDS
       ================================ */

    div[data-testid="stHorizontalBlock"] > div:nth-child(1)
    div[data-testid="stMetric"] {
        transition: all 0.35s ease;
    }


    /* ================================
       SUCCESS MESSAGE
       ================================ */

    div[data-testid="stAlert"][data-baseweb="notification"] {
        border-radius: 18px;
        font-weight: 600;
    }


    /* ================================
       FINAL THANK YOU METRIC
       ================================ */

    div[data-testid="stVerticalBlock"] div[data-testid="stMetric"] {
        transition: all 0.35s ease;
    }

    </style>
    """, unsafe_allow_html=True)


    # =====================================================
    # MAIN TITLE
    # =====================================================

    st.title(
        "📊 HR Analytics Employee Attrition Dashboard"
    )

    st.markdown(
        "### ✨ Explore • Analyze • Visualize • Understand • Improve"
    )

    st.write(
        "An interactive HR analytics project designed to "
        "explore employee information and understand "
        "the factors associated with employee attrition."
    )


    # =====================================================
    # PROJECT AT A GLANCE
    # =====================================================

    st.header("✨ Project At a Glance")

    st.write(
        "A quick overview of the HR Analytics project."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Employees",
            "1,470"
        )

    with col2:
        st.metric(
            "📋 Original Columns",
            "35"
        )

    with col3:
        st.metric(
            "🧹 Cleaned Columns",
            "32"
        )

    with col4:
        st.metric(
            "🎯 Main Focus",
            "Attrition"
        )


    # =====================================================
    # ABOUT THE PROJECT
    # =====================================================

    st.header("📌 About The Project")

    st.write(
        "This project is an HR Analytics Employee Attrition "
        "Dashboard developed to explore, analyze and understand "
        "employee information and the factors associated with "
        "employee attrition."
    )

    st.write(
        "The dashboard transforms employee data into meaningful "
        "insights through data preprocessing, analysis, "
        "interactive visualizations and dashboard-based reporting."
    )


    # =====================================================
    # PROJECT OBJECTIVE
    # =====================================================

    st.header("🎯 Project Objective")

    st.write(
        "The main objective is to analyze employee data, "
        "identify important patterns and understand workforce "
        "factors related to employee attrition."
    )

    obj1, obj2, obj3, obj4 = st.columns(4)

    with obj1:
        st.metric(
            "🧹 Data Cleaning",
            "Clean & Prepare"
        )

    with obj2:
        st.metric(
            "🔎 Data Analysis",
            "Analyze Patterns"
        )

    with obj3:
        st.metric(
            "📊 Visualization",
            "Interactive Charts"
        )

    with obj4:
        st.metric(
            "💡 HR Insights",
            "Understand Attrition"
        )


    # =====================================================
    # TECHNOLOGIES USED
    # =====================================================

    st.header("🛠️ Technologies Used")

    st.write(
        "The project uses Python-based tools for data processing, "
        "analysis, visualization and dashboard development."
    )

    tech1, tech2, tech3, tech4, tech5 = st.columns(5)

    with tech1:
        st.metric(
            "🐍 Python",
            "Programming"
        )

    with tech2:
        st.metric(
            "🐼 Pandas",
            "Data Analysis"
        )

    with tech3:
        st.metric(
            "📊 Plotly",
            "Interactive Charts"
        )

    with tech4:
        st.metric(
            "📈 Matplotlib",
            "Visualization"
        )

    with tech5:
        st.metric(
            "💻 VS Code",
            "Development"
        )


    # =====================================================
    # DATASET
    # =====================================================

    st.header("🗂️ Dataset")

    st.write(
        "The project uses the IBM HR Analytics Employee Attrition "
        "dataset containing detailed information about employees, "
        "demographics, departments, job roles, income, experience, "
        "satisfaction levels and attrition status."
    )

    data1, data2, data3, data4 = st.columns(4)

    with data1:
        st.metric(
            "📁 Dataset",
            "IBM HR Analytics"
        )

    with data2:
        st.metric(
            "👥 Records",
            "1,470"
        )

    with data3:
        st.metric(
            "📋 Before Cleaning",
            "35 Columns"
        )

    with data4:
        st.metric(
            "✨ After Cleaning",
            "32 Columns"
        )


    # =====================================================
    # CLEANING SUMMARY
    # =====================================================

    st.subheader("🧼 Data Cleaning Summary")

    st.write(
        "During preprocessing, three unnecessary columns "
        "were removed from the original dataset:"
    )

    clean1, clean2, clean3 = st.columns(3)

    with clean1:
        st.metric(
            "EmployeeCount",
            "Removed"
        )

    with clean2:
        st.metric(
            "Over18",
            "Removed"
        )

    with clean3:
        st.metric(
            "StandardHours",
            "Removed"
        )

    st.success(
        "✅ Final cleaned dataset contains 32 useful columns "
        "for analysis and visualization."
    )


    # =====================================================
    # ANALYTIC FOCUS
    # =====================================================

    st.header("🔍 Analytic Focus")

    st.write(
        "The dashboard focuses on important employee and "
        "HR-related patterns."
    )

    focus1, focus2, focus3, focus4 = st.columns(4)

    with focus1:
        st.metric(
            "👥 Workforce",
            "Demographics"
        )

    with focus2:
        st.metric(
            "📉 Attrition",
            "Employee Trends"
        )

    with focus3:
        st.metric(
            "💰 Compensation",
            "Income Analysis"
        )

    with focus4:
        st.metric(
            "😊 Satisfaction",
            "Performance"
        )


    # =====================================================
    # PROJECT WORKFLOW
    # =====================================================

    st.header("🔄 Project Workflow")

    st.write(
        "The project follows a structured data analytics "
        "workflow from raw data to meaningful HR insights."
    )

    flow1, flow2, flow3, flow4, flow5 = st.columns(5)

    with flow1:
        st.metric(
            "01",
            "Load Data"
        )

    with flow2:
        st.metric(
            "02",
            "Clean Data"
        )

    with flow3:
        st.metric(
            "03",
            "Analyze"
        )

    with flow4:
        st.metric(
            "04",
            "Visualize"
        )

    with flow5:
        st.metric(
            "05",
            "Generate Insights"
        )


    # =====================================================
    # PROJECT OUTCOME
    # =====================================================

    st.header("🏆 Project Outcome")

    st.write(
        "The final dashboard provides an interactive way "
        "to explore employee data, identify attrition patterns "
        "and understand important HR factors."
    )

    out1, out2, out3 = st.columns(3)

    with out1:
        st.metric(
            "📊 Data Driven",
            "HR Analysis"
        )

    with out2:
        st.metric(
            "📈 Interactive",
            "Visual Insights"
        )

    with out3:
        st.metric(
            "💡 Actionable",
            "HR Understanding"
        )


    # =====================================================
    # WHAT THIS PROJECT HELPS TO UNDERSTAND
    # =====================================================

    st.header("💡 What This Project Helps To Understand")

    st.write(
        "• Employee demographics and workforce structure"
    )

    st.write(
        "• Employee attrition patterns"
    )

    st.write(
        "• Department and job-role trends"
    )

    st.write(
        "• Age and gender-based patterns"
    )

    st.write(
        "• Business travel behaviour"
    )

    st.write(
        "• Income and compensation patterns"
    )

    st.write(
        "• Job satisfaction and performance"
    )

    st.write(
        "• HR-focused insights through interactive visualizations"
    )


    # =====================================================
    # THANK YOU SECTION
    # =====================================================

    st.header("💜 Thank You For Exploring This Project")

    thank1, thank2, thank3 = st.columns(3)

    with thank1:
        st.metric(
            "🔎 Explore",
            "Employee Data"
        )

    with thank2:
        st.metric(
            "📊 Analyze",
            "HR Patterns"
        )

    with thank3:
        st.metric(
            "💡 Understand",
            "HR Insights"
        )

    st.success(
        "✨ Data helps us understand people, patterns and possibilities."
    )

    st.write(
        "This dashboard turns employee data into meaningful "
        "HR insights through analysis, visualization and "
        "interactive reporting."
    )

    
    st.write(
        "Explore • Analyze • Visualize • Understand"
    )
    


    st.write(
    "Data Cleaning • Data Analysis • Data Visualization • HR Insights"
)
    st.header("✨ Project Creator")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown(
        """
        <style>
        .rupam-card {
            background: linear-gradient(
                135deg,
                #7C3AED,
                #EC4899,
                #F97316
            );
            padding: 30px;
            border-radius: 25px;
            text-align: center;
            box-shadow: 0 12px 35px rgba(124, 58, 237, 0.30);
            transition: all 0.35s ease;
        }

        .rupam-card:hover {
            transform: translateY(-8px) scale(1.03);
            box-shadow: 0 20px 45px rgba(236, 72, 153, 0.40);
        }

        .rupam-title {
            color: white;
            font-size: 18px;
            font-weight: 600;
        }

        .rupam-name {
            color: white;
            font-size: 34px;
            font-weight: 800;
            margin: 8px 0;
        }

        .rupam-work {
            color: white;
            font-size: 14px;
            font-weight: 500;
        }
        </style>

        <div class="rupam-card">
            <div class="rupam-title">👩‍💻 Designed & Developed By</div>
            <div class="rupam-name">Rupam</div>
            <div class="rupam-work">
                🧹 Data Cleaning &nbsp; • &nbsp;
                📊 Data Analysis &nbsp; • &nbsp;
                📈 Visualization &nbsp; • &nbsp;
                💡 HR Insights
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    