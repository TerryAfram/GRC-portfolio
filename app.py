import streamlit as st

st.set_page_config(
    page_title="Terry Afram-Kumi | GRC & Cloud Security Portfolio",
    page_icon="🛡️",
    layout="centered",
)

# ---------------------------------------------------------
# Custom CSS for UI Enhancement
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* Main Background & Font Styling */
    .stApp {
        background-color: #0e1117;
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom Project Card Styling */
    .project-card {
        background-color: #1e222d;
        border: 1px solid #2e364f;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .project-card:hover {
        border-color: #4da6ff;
        transform: translateY(-2px);
    }
    
    .project-title {
        color: #ffffff;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .project-desc {
        color: #b0b8c8;
        font-size: 0.95rem;
        line-height: 1.5;
        margin-bottom: 15px;
    }
    
    .tag {
        background-color: #263352;
        color: #4da6ff;
        padding: 4px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-right: 6px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Header Section
# ---------------------------------------------------------
st.title("🛡️ Terry Afram-Kumi")
st.subheader("Cloud Security, GRC Automation & Infrastructure Portfolio")

st.write(
    "Welcome! Below are my active technical security projects focusing on "
    "cloud security compliance, IAM risk assessments, and automated governance."
)

st.divider()

# ---------------------------------------------------------
# Key Credentials & Highlights (Columns)
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Primary Focus", value="Cloud GRC")
with col2:
    st.metric(label="Automation", value="Python / Azure")
with col3:
    st.metric(label="IaC Security", value="Terraform")

st.divider()

# ---------------------------------------------------------
# Projects Section (Styled Cards)
# ---------------------------------------------------------
st.subheader("📌 Featured Repositories")

# Project 1
st.markdown(
    """
    <div class="project-card">
        <div class="project-title">🔍 Azure Native Auditor</div>
        <div class="project-desc">
            Automated compliance scripts designed to scan cloud storage environments and automatically map technical controls to NIST SP 800-53 and COBIT frameworks.
        </div>
        <div>
            <span class="tag">Python</span>
            <span class="tag">Azure</span>
            <span class="tag">NIST 800-53</span>
        </div>
        <br>
        <a href="https://github.com/terryafram/azure-native-auditor" target="_blank" style="color: #4da6ff; text-decoration: none; font-weight: 600;">View Repository on GitHub →</a>
    </div>
""",
    unsafe_allow_html=True,
)

# Project 2
st.markdown(
    """
    <div class="project-card">
        <div class="project-title">🔑 Azure IAM Governance Tool</div>
        <div class="project-desc">
            Automated identity auditing suite to evaluate privileged assignments, track role-based access control (RBAC) drift, and generate risk assessment reports.
        </div>
        <div>
            <span class="tag">Identity & Access</span>
            <span class="tag">Governance</span>
            <span class="tag">Azure AD / Entra</span>
        </div>
        <br>
        <a href="https://github.com/terryafram/azure-iam-governance-tool" target="_blank" style="color: #4da6ff; text-decoration: none; font-weight: 600;">View Repository on GitHub →</a>
    </div>
""",
    unsafe_allow_html=True,
)

# Project 3
st.markdown(
    """
    <div class="project-card">
        <div class="project-title">🏗️ Azure Terraform Compliance</div>
        <div class="project-desc">
            Infrastructure as Code (IaC) templates and policy-as-code validations leveraging Terraform to enforce baseline compliance for cloud infrastructure deployments.
        </div>
        <div>
            <span class="tag">Terraform</span>
            <span class="tag">IaC Security</span>
            <span class="tag">Policy-as-Code</span>
        </div>
        <br>
        <a href="https://github.com/terryafram/azure-iac-terraform" target="_blank" style="color: #4da6ff; text-decoration: none; font-weight: 600;">View Repository on GitHub →</a>
    </div>
""",
    unsafe_allow_html=True,
)
