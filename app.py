import streamlit as st

# =========================================================
# ALLOY COMPOSITION ANALYZER
# Aluminium + Steel Grades
# =========================================================

st.set_page_config(
    page_title="Alloy Composition Analyzer",
    page_icon="⚙️",
    layout="wide"
)
st.title("⚙️ Alloy Composition Analyzer")

st.markdown("""
**Developed by:** Subham Sahu  
**B.Tech 4th Year | Metallurgical & Materials Engineering | IGIT Sarang**
""")

st.write(
    "Select a material type and grade, enter the chemical composition, "
    "then click Analyze."
)


# =========================================================
# GRADE DATABASE
# Values are approximate screening ranges in wt. %
# Always verify against the applicable material standard.
# =========================================================

ALUMINIUM = {

    "Aluminium 1050": {
        "Si": (0, 0.25), "Fe": (0, 0.40), "Cu": (0, 0.05),
        "Mn": (0, 0.05), "Mg": (0, 0.05), "Zn": (0, 0.05),
        "Ti": (0, 0.03), "Al": (99.50, 100.00)
    },

    "Aluminium 1100": {
        "Si": (0, 1.00), "Fe": (0, 1.00), "Cu": (0, 0.20),
        "Mn": (0, 0.05), "Mg": (0, 0.05), "Zn": (0, 0.10),
        "Ti": (0, 0.05), "Al": (99.00, 100.00)
    },

    "Aluminium 2024": {
        "Si": (0, 0.50), "Fe": (0, 0.50), "Cu": (3.80, 4.90),
        "Mn": (0.30, 1.00), "Mg": (1.20, 1.80),
        "Zn": (0, 0.25), "Ti": (0, 0.15), "Al": (90.70, 94.70)
    },

    "Aluminium 3003": {
        "Si": (0, 0.60), "Fe": (0, 0.70), "Cu": (0.05, 0.20),
        "Mn": (1.00, 1.50), "Mg": (0, 0.05),
        "Zn": (0, 0.10), "Ti": (0, 0.05), "Al": (96.80, 98.95)
    },

    "Aluminium 5052": {
        "Si": (0, 0.25), "Fe": (0, 0.40), "Cu": (0, 0.10),
        "Mn": (0, 0.10), "Mg": (2.20, 2.80),
        "Cr": (0.15, 0.35), "Zn": (0, 0.10),
        "Al": (96.00, 97.60)
    },

    "Aluminium 5083": {
        "Si": (0, 0.40), "Fe": (0, 0.40), "Cu": (0, 0.10),
        "Mn": (0.40, 1.00), "Mg": (4.00, 4.90),
        "Cr": (0.05, 0.25), "Zn": (0, 0.25),
        "Ti": (0, 0.15), "Al": (93.00, 95.60)
    },

    "Aluminium 6061": {
        "Si": (0.40, 0.80), "Fe": (0, 0.70), "Cu": (0.15, 0.40),
        "Mn": (0, 0.15), "Mg": (0.80, 1.20),
        "Cr": (0.04, 0.35), "Zn": (0, 0.25),
        "Ti": (0, 0.15), "Al": (95.85, 98.57)
    },

    "Aluminium 6063": {
        "Si": (0.20, 0.60), "Fe": (0, 0.35), "Cu": (0, 0.10),
        "Mn": (0, 0.10), "Mg": (0.45, 0.90),
        "Cr": (0, 0.10), "Zn": (0, 0.10),
        "Ti": (0, 0.10), "Al": (97.55, 99.25)
    },

    "Aluminium 6082": {
        "Si": (0.70, 1.30), "Fe": (0, 0.50), "Cu": (0, 0.10),
        "Mn": (0.40, 1.00), "Mg": (0.60, 1.20),
        "Cr": (0, 0.25), "Zn": (0, 0.20),
        "Ti": (0, 0.10), "Al": (95.85, 98.30)
    },

    "Aluminium 7075": {
        "Si": (0, 0.40), "Fe": (0, 0.50), "Cu": (1.20, 2.00),
        "Mn": (0, 0.30), "Mg": (2.10, 2.90),
        "Cr": (0.18, 0.28), "Zn": (5.10, 6.10),
        "Ti": (0, 0.20), "Al": (87.70, 91.41)
    },
}


STEEL = {

    "Carbon Steel A36": {
        "C": (0, 0.26), "Mn": (0, 1.20), "Si": (0, 0.40),
        "P": (0, 0.040), "S": (0, 0.050), "Fe": (97.00, 100.00)
    },

    "Carbon Steel 1018": {
        "C": (0.15, 0.20), "Mn": (0.60, 0.90),
        "P": (0, 0.040), "S": (0, 0.050),
        "Fe": (98.00, 99.25)
    },

    "Carbon Steel 1045": {
        "C": (0.43, 0.50), "Mn": (0.60, 0.90),
        "Si": (0, 0.40), "P": (0, 0.040),
        "S": (0, 0.050), "Fe": (97.50, 98.97)
    },

    "Stainless Steel 201": {
        "C": (0, 0.15), "Mn": (5.50, 7.50), "Si": (0, 1.00),
        "P": (0, 0.060), "S": (0, 0.030),
        "Cr": (16.00, 18.00), "Ni": (3.50, 5.50),
        "N": (0, 0.25), "Fe": (60.00, 75.00)
    },

    "Stainless Steel 301": {
        "C": (0, 0.15), "Mn": (0, 2.00), "Si": (0, 1.00),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (16.00, 18.00), "Ni": (6.00, 8.00),
        "N": (0, 0.10), "Fe": (70.00, 80.00)
    },

    "Stainless Steel 304": {
        "C": (0, 0.08), "Mn": (0, 2.00), "Si": (0, 0.75),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (18.00, 20.00), "Ni": (8.00, 10.50),
        "N": (0, 0.10), "Fe": (65.00, 74.00)
    },

    "Stainless Steel 304L": {
        "C": (0, 0.03), "Mn": (0, 2.00), "Si": (0, 0.75),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (18.00, 20.00), "Ni": (8.00, 12.00),
        "N": (0, 0.10), "Fe": (65.00, 74.00)
    },

    "Stainless Steel 316": {
        "C": (0, 0.08), "Mn": (0, 2.00), "Si": (0, 0.75),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (16.00, 18.00), "Ni": (10.00, 14.00),
        "Mo": (2.00, 3.00), "N": (0, 0.10),
        "Fe": (60.00, 72.00)
    },

    "Stainless Steel 316L": {
        "C": (0, 0.03), "Mn": (0, 2.00), "Si": (0, 0.75),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (16.00, 18.00), "Ni": (10.00, 14.00),
        "Mo": (2.00, 3.00), "N": (0, 0.10),
        "Fe": (60.00, 72.00)
    },

    "Stainless Steel 321": {
        "C": (0, 0.08), "Mn": (0, 2.00), "Si": (0, 0.75),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (17.00, 19.00), "Ni": (9.00, 12.00),
        "Ti": (0, 0.70), "N": (0, 0.10),
        "Fe": (65.00, 74.00)
    },

    "Stainless Steel 347": {
        "C": (0, 0.08), "Mn": (0, 2.00), "Si": (0, 0.75),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (17.00, 19.00), "Ni": (9.00, 13.00),
        "Nb": (0.30, 1.00), "N": (0, 0.10),
        "Fe": (65.00, 74.00)
    },

    "Stainless Steel 309S": {
        "C": (0, 0.08), "Mn": (0, 2.00), "Si": (0, 0.75),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (22.00, 24.00), "Ni": (12.00, 15.00),
        "Fe": (55.00, 65.00)
    },

    "Stainless Steel 310S": {
        "C": (0, 0.08), "Mn": (0, 2.00), "Si": (0, 1.50),
        "P": (0, 0.045), "S": (0, 0.030),
        "Cr": (24.00, 26.00), "Ni": (19.00, 22.00),
        "Fe": (50.00, 60.00)
    },

    "Stainless Steel 410": {
        "C": (0, 0.15), "Mn": (0, 1.00), "Si": (0, 1.00),
        "P": (0, 0.040), "S": (0, 0.030),
        "Cr": (11.50, 13.50), "Ni": (0, 0.75),
        "Fe": (84.00, 89.00)
    },

    "Stainless Steel 420": {
        "C": (0.15, 0.40), "Mn": (0, 1.00), "Si": (0, 1.00),
        "P": (0, 0.040), "S": (0, 0.040),
        "Cr": (12.00, 14.00), "Ni": (0, 0.75),
        "Fe": (83.00, 87.00)
    },

    "Stainless Steel 430": {
        "C": (0, 0.12), "Mn": (0, 1.00), "Si": (0, 1.00),
        "P": (0, 0.040), "S": (0, 0.030),
        "Cr": (16.00, 18.00), "Ni": (0, 0.75),
        "Fe": (80.00, 84.00)
    },

    "Tool Steel D2": {
        "C": (1.40, 1.60), "Si": (0, 0.60), "Mn": (0, 0.60),
        "P": (0, 0.030), "S": (0, 0.030),
        "Cr": (11.00, 13.00), "Mo": (0.70, 1.20),
        "V": (0.70, 1.20), "Fe": (80.00, 86.00)
    },

    "Alloy Steel 4140": {
        "C": (0.38, 0.43), "Si": (0.15, 0.35), "Mn": (0.75, 1.00),
        "P": (0, 0.035), "S": (0, 0.040),
        "Cr": (0.80, 1.10), "Mo": (0.15, 0.25),
        "Fe": (96.00, 98.00)
    },

    "Alloy Steel 4340": {
        "C": (0.38, 0.43), "Si": (0.15, 0.35), "Mn": (0.60, 0.80),
        "P": (0, 0.035), "S": (0, 0.040),
        "Ni": (1.65, 2.00), "Cr": (0.70, 0.90),
        "Mo": (0.20, 0.30), "Fe": (94.00, 97.00)
    },

    "Duplex Stainless Steel 2205": {
        "C": (0, 0.03), "Mn": (0, 2.00), "Si": (0, 1.00),
        "P": (0, 0.030), "S": (0, 0.020),
        "Cr": (22.00, 23.00), "Ni": (4.50, 6.50),
        "Mo": (3.00, 3.50), "N": (0.14, 0.20),
        "Fe": (60.00, 70.00)
    },

    "Super Duplex Stainless Steel 2507": {
        "C": (0, 0.03), "Mn": (0, 1.20), "Si": (0, 0.80),
        "P": (0, 0.035), "S": (0, 0.020),
        "Cr": (24.00, 26.00), "Ni": (6.00, 8.00),
        "Mo": (3.00, 5.00), "N": (0.24, 0.32),
        "Fe": (55.00, 65.00)
    },

    "17-4 PH Stainless Steel": {
        "C": (0, 0.07), "Mn": (0, 1.00), "Si": (0, 1.00),
        "P": (0, 0.040), "S": (0, 0.030),
        "Cr": (15.00, 17.50), "Ni": (3.00, 5.00),
        "Cu": (3.00, 5.00), "Nb": (0.15, 0.45),
        "Fe": (70.00, 80.00)
    },
}


# =========================================================
# MATERIAL TYPE
# =========================================================

material_type = st.selectbox(
    "🔩 Select Material Type",
    ["Aluminium", "Steel"]
)

if material_type == "Aluminium":
    database = ALUMINIUM
else:
    database = STEEL


# =========================================================
# GRADE SELECTION
# =========================================================

grade = st.selectbox(
    "📋 Select Grade",
    list(database.keys())
)

limits = database[grade]

st.info(f"**Selected:** {grade}")


# =========================================================
# INPUT SECTION
# =========================================================

st.subheader("🧪 Enter Chemical Composition (%)")

values = {}

columns = st.columns(3)

for index, (element, (minimum, maximum)) in enumerate(limits.items()):

    if minimum == maximum:
        default = minimum
    else:
        default = (minimum + maximum) / 2

    with columns[index % 3]:

        values[element] = st.number_input(
            f"{element} (%)",
            min_value=0.0,
            max_value=100.0,
            value=float(default),
            step=0.001,
            format="%.3f",
            key=f"{material_type}_{grade}_{element}"
        )


# =========================================================
# ANALYSIS
# =========================================================

if st.button("🔍 Analyze Composition", type="primary"):

    results = []
    passed = True

    st.subheader("📊 Analysis Result")

    for element, (minimum, maximum) in limits.items():

        value = values[element]

        if minimum <= value <= maximum:

            status = "PASS"
            results.append(
                f"✅ **{element}**: {value:.3f}% — "
                f"Within range ({minimum:.3f}–{maximum:.3f}%)"
            )

        else:

            status = "FAIL"
            passed = False

            results.append(
                f"❌ **{element}**: {value:.3f}% — "
                f"Outside range ({minimum:.3f}–{maximum:.3f}%)"
            )

    for result in results:
        st.write(result)

    st.divider()

    if passed:
        st.success(
            f"🎉 PASS — The entered composition matches the "
            f"screening ranges for **{grade}**."
        )
    else:
        st.error(
            f"⚠️ FAIL — The entered composition does not fully "
            f"match the screening ranges for **{grade}**."
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "⚠️ Screening tool only. Chemical limits can vary according "
    "to ASTM/EN/ISO/JIS standards, product form, heat analysis, "
    "product analysis and customer specification. Always verify "
    "against the applicable material standard before certification "
    "or engineering decisions."
)
