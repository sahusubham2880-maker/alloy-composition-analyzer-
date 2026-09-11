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

# =========================================================
# HEADER
# =========================================================

st.title("⚙️ Alloy Composition Analyzer")

st.markdown("""
**Developed by:** Subham Sahu  
**B.Tech - 4th Year | Metallurgical & Materials Engineering | IGIT , Sarang**
""")

st.write(
    "Enter the chemical composition of an unknown alloy sample. "
    "The analyzer compares it with the available grades and identifies "
    "the closest matching grade."
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
# SELECT MATERIAL TYPE
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
# SAMPLE COMPOSITION INPUT
# =========================================================

st.subheader("🧪 Enter Unknown Sample Composition (%)")

st.info(
    "Enter the measured chemical composition of your sample. "
    "Use 0.000 for an element that is not detected or is not present."
)

# Get all elements available for the selected material
all_elements = sorted(
    set(
        element
        for grade_data in database.values()
        for element in grade_data
    )
)

values = {}

columns = st.columns(3)

for index, element in enumerate(all_elements):

    with columns[index % 3]:

        values[element] = st.number_input(
            f"{element} (%)",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.001,
            format="%.3f",
            key=f"{material_type}_{element}"
        )


# =========================================================
# ANALYSIS FUNCTION
# =========================================================

def calculate_grade_match(sample, grade_limits):

    scores = []

    for element, sample_value in sample.items():

        # Ignore elements that were not entered/detected
        if sample_value == 0:
            continue

        # If the element is not part of the grade,
        # it is considered a mismatch.
        if element not in grade_limits:
            scores.append(0.0)
            continue

        minimum, maximum = grade_limits[element]

        # Perfect match if value is inside the allowed range
        if minimum <= sample_value <= maximum:
            scores.append(1.0)

        else:
            # Calculate distance from the acceptable range
            if sample_value < minimum:
                distance = minimum - sample_value
            else:
                distance = sample_value - maximum

            # Avoid division by zero
            range_width = max(maximum - minimum, 0.001)

            penalty = distance / range_width

            # Convert distance into a score
            score = max(0.0, 1.0 - penalty)

            scores.append(score)

    if not scores:
        return 0.0

    return sum(scores) / len(scores)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button("🔍 Analyze Composition", type="primary"):

    # Check whether the user entered any composition
    entered_elements = {
        element: value
        for element, value in values.items()
        if value > 0
    }

    if not entered_elements:

        st.warning(
            "⚠️ Please enter the measured chemical composition "
            "of the sample before analysis."
        )

    else:

        # -------------------------------------------------
        # Compare sample with every grade
        # -------------------------------------------------

        grade_scores = []

        for grade_name, grade_limits in database.items():

            score = calculate_grade_match(
                entered_elements,
                grade_limits
            )

            grade_scores.append(
                (grade_name, score)
            )

        # Sort grades from highest to lowest match
        grade_scores.sort(
            key=lambda x: x[1],
            reverse=True
        )

        best_grade = grade_scores[0][0]
        best_score = grade_scores[0][1] * 100

        best_limits = database[best_grade]

        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        st.divider()
        st.subheader("📊 Analysis Result")

        if best_score >= 80:

            st.success(
                f"🎯 **Most Likely Grade: {best_grade}**"
            )

        elif best_score >= 60:

            st.warning(
                f"⚠️ **Possible Grade: {best_grade}**"
            )

        else:

            st.error(
                f"❌ **No strong grade match found**"
            )

        st.metric(
            "Matching Score",
            f"{best_score:.1f}%"
        )

        # -------------------------------------------------
        # ELEMENT-WISE ANALYSIS
        # -------------------------------------------------

        st.subheader(
            f"🔬 Element-wise Comparison — {best_grade}"
        )

        passed = 0
        failed = 0

        for element, sample_value in entered_elements.items():

            if element not in best_limits:

                st.error(
                    f"❌ **{element}**: {sample_value:.3f}% — "
                    f"Element is not specified for {best_grade}"
                )

                failed += 1
                continue

            minimum, maximum = best_limits[element]

            if minimum <= sample_value <= maximum:

                st.success(
                    f"✅ **{element}**: {sample_value:.3f}% — "
                    f"Within range "
                    f"({minimum:.3f}–{maximum:.3f}%)"
                )

                passed += 1

            else:

                st.error(
                    f"❌ **{element}**: {sample_value:.3f}% — "
                    f"Outside range "
                    f"({minimum:.3f}–{maximum:.3f}%)"
                )

                failed += 1

        # -------------------------------------------------
        # FINAL DECISION
        # -------------------------------------------------

        st.divider()

        if failed == 0 and best_score >= 80:

            st.success(
                f"🎉 **PASS — The sample composition is "
                f"consistent with {best_grade}.**"
            )

        elif best_score >= 60:

            st.warning(
                f"⚠️ **REVIEW REQUIRED — {best_grade} is the "
                f"closest match, but the composition should be "
                f"verified against the applicable material standard.**"
            )

        else:

            st.error(
                "❌ **FAIL — The sample does not show a strong "
                "match with the available grades.**"
            )

        # -------------------------------------------------
        # OTHER CLOSE MATCHES
        # -------------------------------------------------

        st.subheader("📋 Other Possible Grades")

        for grade_name, score in grade_scores[1:4]:

            st.write(
                f"• **{grade_name}** — "
                f"{score * 100:.1f}% match"
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
