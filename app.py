import streamlit as st

st.set_page_config(
    page_title="Terry Afram-Kumi | GRC & Cloud Security Portfolio",
    page_icon="🛡️",
    layout="centered",
)

# ---------------------------------------------------------
# Custom Colorful CSS Styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        font-family: 'Inter', sans-serif;
        color: #f8fafc;
    }
    
    .project-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #3b82f6;
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 22px;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .project-card:hover {
        border-color: #60a5fa;
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(96, 165, 250, 0.25);
    }
    
    .project-title {
        color: #60a5fa;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .project-desc {
        color: #cbd5e1;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .tag-python { background-color: #1e3a8a; color: #93c5fd; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-right: 6px; display: inline-block; }
    .tag-azure { background-color: #0369a1; color: #bae6fd; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-right: 6px; display: inline-block; }
    .tag-sec { background-color: #581c87; color: #e9d5ff; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-right: 6px; display: inline-block; }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Header Section with Profile Picture & Bio Side-by-Side
# ---------------------------------------------------------
col_img, col_text = st.columns([1, 2])

with col_img:
    # Points directly to your uploaded image filename
    st.image("IMG_3675.jpeg", width=200)

with col_text:
    st.title("🛡️ Terry Afram-Kumi")
    st.caption("CISA | PMP | MSc | Cloud Security & GRC Professional")

# Professional Summary Bio
st.write("---")
st.markdown("### 📌 About Me")
st.write(
    "Certified Information Systems Auditor (CISA) and Project Management"
    " Professional (PMP) specializing in cloud security, Governance, Risk, AI Audit,"
    " and Compliance (GRC), and automated control validation. I bridge the gap"
    " between technical infrastructure and regulatory frameworks, designing"
    " automated solutions that map technical controls to standards like NIST SP"
    " 800-53 and COBIT."
)
st.write(
    "My technical work focuses on building Python-based compliance automation"
    " tools, securing cloud resource groups in Microsoft Azure, and enforcing"
    " Infrastructure as Code (IaC) governance through Terraform and"
    " policy-as-code validations."
)

st.divider()

# ---------------------------------------------------------
# Key Metrics / Highlights
# ---------------------------------------------------------
m1, m2, m3 = st.columns(3)
with m1:
    st.metric(label="🎯 Focus", value="Cloud GRC")
with m2:
    st.metric(label="⚡ Core Stack", value="Python / Azure")
with m3:
    st.metric(label="🏗️ Infrastructure", value="Terraform")

st.divider()

# ---------------------------------------------------------
# Projects Section
# ---------------------------------------------------------
st.subheader("📂 Featured Repositories")

# Project 1
st.markdown(
    """
    <div class="project-card">
        <div class="project-title">🔍 Azure Native Auditor</div>
        <div class="project-desc">
            Automated compliance scripts engineered to scan cloud storage environments and automatically map technical controls to NIST SP 800-53 and COBIT frameworks.
        </div>
        <div>
            <span class="tag-python">🐍 Python</span>
            <span class="tag-azure">☁️ Azure</span>
            <span class="tag-sec">🔒 NIST 800-53</span>
        </div>
        <br><br>
        <a href="https://github.com/terryafram/azure-native-auditor" target="_blank" style="color: #60a5fa; text-decoration: none; font-weight: 700;">View Repository on GitHub →</a>
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
            Automated identity auditing suite designed to evaluate privileged assignments, track role-based access control (RBAC) drift, and generate risk assessment reports.
        </div>
        <div>
            <span class="tag-sec">🛡️ Identity Access</span>
            <span class="tag-azure">☁️ Azure Entra</span>
            <span class="tag-python">📊 Governance</span>
        </div>
        <br><br>
        <a href="https://github.com/terryafram/azure-iam-governance-tool" target="_blank" style="color: #60a5fa; text-decoration: none; font-weight: 700;">View Repository on GitHub →</a>
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
            Infrastructure as Code (IaC) templates and policy-as-code validations leveraging Terraform to enforce baseline compliance for secure cloud deployments.
        </div>
        <div>
            <span class="tag-azure">⚡ Terraform</span>
            <span class="tag-sec">🛡️ IaC Security</span>
            <span class="tag-python">📋 Policy-as-Code</span>
        </div>
        <br><br>
        <a href="https://github.com/terryafram/azure-iac-terraform" target="_blank" style="color: #60a5fa; text-decoration: none; font-weight: 700;">View Repository on GitHub →</a>
    </div>
""",
    unsafe_allow_html=True,
)
