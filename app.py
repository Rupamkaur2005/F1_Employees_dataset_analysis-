import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded"
)
df=pd.read_csv("employess attrition.csv")
with st.sidebar:
    opt=option_menu("menu",["Home","Dataset","Pre-Processing","Visualization","About"],icons=["house","table","gear","bar-chart","person"])
    d=st.multiselect(
        "SelectDepartment",
        options=df['Department'].unique()
    )
    if d:
       filtered=df[df["Department"].isin(d)]
    else:
        filtered=df
if opt=="Home":total_employee = filtered.shape[0]
total_department = filtered["Department"].nunique()
total_attrition = filtered["Attrition"].value_counts().get("Yes", 0)
avg_age = round(filtered["Age"].mean(), 1)
avg_income = round(filtered["MonthlyIncome"].mean(), 0)
col1, col2, col3, col4, col5 = st.columns(5)

st.title("🏠HR Analytics Department")
st.markdown("### Welcome! Explore HR Analytics Dashboard.")
# st.markdown("""
# 📊 HR Analytics Dashboard

# Welcome to the **HR Analytics Dashboard**.

# ✨ Features

# - 👥 Employee Workforce Overview
# - 🏢 Department-wise Analysis
# - 📉 Employee Attrition Insights
# - 📊 Interactive Data Visualization
# - ⚙️ Data Pre-Processing
# - 📋 Employee Dataset Explorer
# - 📈 Key Performance Metrics (KPIs)

# ---
# 💡 **Use the sidebar to navigate between different sections of the dashboard.**

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

st.markdown("""
<style>

.kpi-card{
background:#fff;
border-radius:18px;
padding:20px;
text-align:center;
color:white;
box-shadow:0px 8px 20px rgba(0,0,0,0.15);
transition:0.3s;
margin-top:10px;
}

.kpi-card:hover{
transform:translateY(-5px) scale(1.03);
}

.kpi-title{
font-size:14px;
font-weight:600;
margin-bottom:8px;
}

.kpi-value{
font-size:32px;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# st.title("🏠HR Analytics Department")
# st.markdown("### Welcome! Explore HR Analytics Dashboard.")
# st.markdown("""
# ## 📊 HR Analytics Dashboard

# Welcome to the **HR Analytics Dashboard**.

# ### ✨ Features

# - 👥 Employee Workforce Overview
# - 🏢 Department-wise Analysis
# - 📉 Employee Attrition Insights
# - 📊 Interactive Data Visualization
# - ⚙️ Data Pre-Processing
# - 📋 Employee Dataset Explorer
# - 📈 Key Performance Metrics (KPIs)

# ---
# 💡 **Use the sidebar to navigate between different sections of the dashboard.**
# """)
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

total_employee = filtered.shape[0]
total_department = filtered["Department"].nunique()
total_attrition = filtered["Attrition"].value_counts().get("Yes", 0)
avg_age = filtered["Age"].mean()
avg_income = filtered["MonthlyIncome"].mean()
col1, col2, col3, col4, col5 = st.columns(5)

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
 📊 HR Analytics Dashboard

Welcome to the **HR Analytics Dashboard**.

 ✨ Features

 - 👥 Employee Workforce Overview
 - 🏢 Department-wise Analysis
 - 📉 Employee Attrition Insights
 - 📊 Interactive Data Visualization
 - ⚙️ Data Pre-Processing
 - 📋 Employee Dataset Explorer
 - 📈 Key Performance Metrics (KPIs)

 
 💡 **Use the sidebar to navigate between different sections of the dashboard.**
""")
    

if opt=="Dataset":
    st.title("📋Employee Dataset")
if opt=="Pre-Processing":
    st.title("⚙️ Data Pre-Processing")
if opt=="Visualization":
    st.title("📊Data Visualization")
if opt=="About":
    st.title("⚙️About Project")   