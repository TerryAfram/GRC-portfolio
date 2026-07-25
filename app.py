import streamlit as st

st.set_page_config(
    page_title="Terry Afram-Kumi | GRC & Cloud Security Portfolio",
    layout="centered",
)

st.title("🛡️ Terry Afram-Kumi")
st.subheader("Cloud Security, GRC Automation & Compliance Portfolio")

st.write(
    "Welcome! Below are my active GitHub projects focusing on cloud security,"
    " compliance automation, and infrastructure as code."
)

st.divider()

# Project 1
st.markdown("### 📁 Azure Native Auditor")
st.write(
    "Automated compliance scripts to scan cloud storage environments and map"
    " controls to security frameworks."
)
st.markdown(
    "[View Repository on GitHub]"
    "(https://github.com/terryafram/azure-native-auditor)"
)

st.divider()

# Project 2
st.markdown("### 📁 Azure IAM Governance Tool")
st.write(
    "Tools and scripts to generate reports on privileged identity assignments and"
    " risk posture assessments."
)
st.markdown(
    "[View Repository on GitHub]"
    "(https://github.com/terryafram/azure-iam-governance-tool)"
)

st.divider()

# Project 3
st.markdown("### 📁 Azure Terraform Compliance")
st.write(
    "Infrastructure as Code modules and automated policy validations using"
    " Terraform for secure cloud deployments."
)
st.markdown(
    "[View Repository on GitHub]"
    "(https://github.com/terryafram/azure-iac-terraform)"
)
