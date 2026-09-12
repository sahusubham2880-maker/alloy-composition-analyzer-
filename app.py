import streamlit as st

# ============================================================
# ALLOY COMPOSITION ANALYZER
# Preliminary Industrial Alloy Identification Tool
# ============================================================

st.set_page_config(
    page_title="Alloy Composition Analyzer",
    page_icon="⚙️",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================

st.title("⚙️ Alloy Composition Analyzer")

st.markdown("""
**Developed by:** Subham Sahu  
**B.Tech - 4th Year | Metallurgical & Materials Engineering | IGIT, Sarang**
""")

st.write(
    "Enter the chemical composition of an unknown alloy sample. "
    "The analyzer compares it with industrial alloy grades and "
    "identifies the closest composition match."
)

st.info(
    "⚠️ Preliminary screening tool only. "
    "Final material acceptance must be verified using the applicable "
    "ASTM / SAE / UNS / EN / ISO specification and certified analysis."
)


# ============================================================
# ALUMINIUM ALLOYS
# ============================================================

ALUMINIUM = {

    "Aluminium 1050": {
        "Al": (99.50, 100.00),
        "Si": (0.00, 0.25),
        "Fe": (0.00, 0.40),
        "Cu": (0.00, 0.05),
        "Mn": (0.00, 0.05),
        "Mg": (0.00, 0.05),
        "Zn": (0.00, 0.05),
        "Ti": (0.00, 0.05)
    },

    "Aluminium 1100": {
        "Al": (99.00, 100.00),
        "Si": (0.00, 1.00),
        "Fe": (0.00, 1.00),
        "Cu": (0.00, 0.20),
        "Mn": (0.00, 0.05),
        "Mg": (0.00, 0.05),
        "Zn": (0.00, 0.10)
    },

    "Aluminium 2024": {
        "Al": (90.70, 94.70),
        "Cu": (3.80, 4.90),
        "Mg": (1.20, 1.80),
        "Mn": (0.30, 1.00),
        "Si": (0.00, 0.50),
        "Fe": (0.00, 0.50),
        "Zn": (0.00, 0.25),
        "Ti": (0.00, 0.15)
    },

    "Aluminium 3003": {
        "Al": (96.80, 98.95),
        "Mn": (1.00, 1.50),
        "Cu": (0.05, 0.20),
        "Si": (0.00, 0.60),
        "Fe": (0.00, 0.70),
        "Mg": (0.00, 0.05),
        "Zn": (0.00, 0.10)
    },

    "Aluminium 5052": {
        "Al": (96.00, 97.60),
        "Mg": (2.20, 2.80),
        "Cr": (0.15, 0.35),
        "Si": (0.00, 0.25),
        "Fe": (0.00, 0.40),
        "Cu": (0.00, 0.10),
        "Mn": (0.00, 0.10),
        "Zn": (0.00, 0.10)
    },

    "Aluminium 5083": {
        "Al": (93.00, 95.60),
        "Mg": (4.00, 4.90),
        "Mn": (0.40, 1.00),
        "Cr": (0.05, 0.25),
        "Si": (0.00, 0.40),
        "Fe": (0.00, 0.40),
        "Cu": (0.00, 0.10),
        "Zn": (0.00, 0.25),
        "Ti": (0.00, 0.15)
    },

    "Aluminium 6061": {
        "Al": (95.80, 98.60),
        "Mg": (0.80, 1.20),
        "Si": (0.40, 0.80),
        "Cu": (0.15, 0.40),
        "Cr": (0.04, 0.35),
        "Fe": (0.00, 0.70),
        "Mn": (0.00, 0.15),
        "Zn": (0.00, 0.25),
        "Ti": (0.00, 0.15)
    },

    "Aluminium 7075": {
        "Al": (87.00, 91.00),
        "Zn": (5.10, 6.10),
        "Mg": (2.10, 2.90),
        "Cu": (1.20, 2.00),
        "Cr": (0.18, 0.28),
        "Fe": (0.00, 0.50),
        "Si": (0.00, 0.40),
        "Mn": (0.00, 0.30),
        "Ti": (0.00, 0.20)
    }
}


# ============================================================
# STEEL
# ============================================================

STEEL = {

    "SAE 1020": {
        "C": (0.18, 0.23),
        "Mn": (0.30, 0.60),
        "Si": (0.15, 0.35),
        "P": (0.00, 0.040),
        "S": (0.00, 0.050),
        "Fe": (98.00, 99.30)
    },

    "SAE 1045": {
        "C": (0.43, 0.50),
        "Mn": (0.60, 0.90),
        "Si": (0.15, 0.35),
        "P": (0.00, 0.040),
        "S": (0.00, 0.050),
        "Fe": (97.00, 98.50)
    },

    "SAE 4140": {
        "C": (0.38, 0.43),
        "Mn": (0.75, 1.00),
        "Si": (0.15, 0.35),
        "Cr": (0.80, 1.10),
        "Mo": (0.15, 0.25),
        "P": (0.00, 0.035),
        "S": (0.00, 0.040),
        "Fe": (95.00, 97.00)
    },

    "SAE 4340": {
        "C": (0.38, 0.43),
        "Mn": (0.60, 0.80),
        "Si": (0.15, 0.35),
        "Cr": (0.70, 0.90),
        "Ni": (1.65, 2.00),
        "Mo": (0.20, 0.30),
        "Fe": (94.00, 97.00)
    },

    "Stainless Steel 304": {
        "C": (0.00, 0.08),
        "Mn": (0.00, 2.00),
        "Si": (0.00, 1.00),
        "P": (0.00, 0.045),
        "S": (0.00, 0.030),
        "Cr": (17.50, 19.50),
        "Ni": (8.00, 10.50),
        "Fe": (66.00, 74.00)
    },

    "Stainless Steel 304L": {
        "C": (0.00, 0.030),
        "Mn": (0.00, 2.00),
        "Si": (0.00, 1.00),
        "P": (0.00, 0.045),
        "S": (0.00, 0.030),
        "Cr": (17.50, 19.50),
        "Ni": (8.00, 12.00),
        "Fe": (66.00, 74.00)
    },

    "Stainless Steel 316": {
        "C": (0.00, 0.08),
        "Mn": (0.00, 2.00),
        "Si": (0.00, 1.00),
        "P": (0.00, 0.045),
        "S": (0.00, 0.030),
        "Cr": (16.00, 18.00),
        "Ni": (10.00, 14.00),
        "Mo": (2.00, 3.00),
        "Fe": (60.00, 72.00)
    },

    "Stainless Steel 316L": {
        "C": (0.00, 0.030),
        "Mn": (0.00, 2.00),
        "Si": (0.00, 1.00),
        "P": (0.00, 0.045),
        "S": (0.00, 0.030),
        "Cr": (16.00, 18.00),
        "Ni": (10.00, 14.00),
        "Mo": (2.00, 3.00),
        "Fe": (60.00, 72.00)
    },

    "Stainless Steel 410": {
        "C": (0.00, 0.15),
        "Mn": (0.00, 1.00),
        "Si": (0.00, 1.00),
        "P": (0.00, 0.040),
        "S": (0.00, 0.030),
        "Cr": (11.50, 13.50),
        "Ni": (0.00, 0.75),
        "Fe": (84.00, 88.00)
    },

    "Stainless Steel 430": {
        "C": (0.00, 0.12),
        "Mn": (0.00, 1.00),
        "Si": (0.00, 1.00),
        "P": (0.00, 0.040),
        "S": (0.00, 0.030),
        "Cr": (16.00, 18.00),
        "Ni": (0.00, 0.75),
        "Fe": (80.00, 85.00)
    },

    "17-4 PH Stainless Steel": {
        "C": (0.00, 0.07),
        "Mn": (0.00, 1.00),
        "Si": (0.00, 1.00),
        "P": (0.00, 0.040),
        "S": (0.00, 0.030),
        "Cr": (15.00, 17.50),
        "Ni": (3.00, 5.00),
        "Cu": (3.00, 5.00),
        "Nb": (0.15, 0.45),
        "Fe": (70.00, 80.00)
    },

    "Duplex Stainless Steel 2205": {
        "C": (0.00, 0.030),
        "Cr": (21.00, 23.00),
        "Ni": (4.50, 6.50),
        "Mo": (2.50, 3.50),
        "N": (0.08, 0.20),
        "Mn": (0.00, 2.00),
        "Si": (0.00, 1.00),
        "Fe": (65.00, 75.00)
    }
}


# ============================================================
# COPPER
# ============================================================

COPPER = {

    "Copper C10100 OFE": {
        "Cu": (99.990, 100.000),
        "Pb": (0.000, 0.0005),
        "Zn": (0.000, 0.0001),
        "Fe": (0.000, 0.0010),
        "P": (0.000, 0.0003),
        "Ag": (0.000, 0.0025),
        "O": (0.000, 0.0005)
    },

    "Copper C10200 OF": {
        "Cu": (99.950, 100.000),
        "O": (0.000, 0.0010)
    },

    "Copper C11000 ETP": {
        "Cu": (99.900, 100.000),
        "O": (0.000, 0.040)
    },

    "Copper C12200 DHP": {
        "Cu": (99.900, 100.000),
        "P": (0.015, 0.040)
    }
}


# ============================================================
# BRASS
# ============================================================

BRASS = {

    "Brass C26000 Cartridge Brass": {
        "Cu": (68.50, 71.50),
        "Zn": (28.50, 31.50),
        "Pb": (0.00, 0.07),
        "Fe": (0.00, 0.10)
    },

    "Brass C27000": {
        "Cu": (63.00, 68.50),
        "Zn": (31.50, 37.00),
        "Pb": (0.00, 0.07),
        "Fe": (0.00, 0.10)
    },

    "Brass C36000 Free-Cutting": {
        "Cu": (60.00, 63.00),
        "Zn": (34.00, 38.00),
        "Pb": (2.50, 3.70),
        "Fe": (0.00, 0.35)
    },

    "Brass C46400 Naval Brass": {
        "Cu": (59.00, 62.00),
        "Zn": (36.00, 40.00),
        "Sn": (0.50, 1.00),
        "Pb": (0.00, 0.50),
        "Fe": (0.00, 0.10)
    },

    "Brass C68700 Aluminium Brass": {
        "Cu": (76.00, 80.00),
        "Al": (1.80, 2.50),
        "Fe": (0.50, 1.50),
        "Zn": (16.00, 22.00)
    }
}


# ============================================================
# BRONZE
# ============================================================

BRONZE = {

    "Phosphor Bronze C51000": {
        "Cu": (94.00, 96.00),
        "Sn": (4.00, 6.00),
        "P": (0.03, 0.35)
    },

    "Phosphor Bronze C52100": {
        "Cu": (91.00, 93.00),
        "Sn": (7.00, 9.00),
        "P": (0.03, 0.35)
    },

    "Aluminium Bronze C95400": {
        "Cu": (83.00, 89.00),
        "Al": (10.00, 11.50),
        "Fe": (2.00, 4.00),
        "Mn": (0.00, 1.50),
        "Ni": (0.00, 1.50)
    },

    "Silicon Bronze C65500": {
        "Cu": (95.00, 98.00),
        "Si": (2.80, 4.00),
        "Mn": (0.00, 1.50),
        "Zn": (0.00, 1.50)
    },

    "Beryllium Copper C17200": {
        "Cu": (96.80, 98.20),
        "Be": (1.80, 2.00),
        "Co": (0.20, 0.60)
    }
}


# ============================================================
# TITANIUM
# ============================================================

TITANIUM = {

    "Titanium Grade 1": {
        "Ti": (99.40, 100.00),
        "Fe": (0.00, 0.20),
        "O": (0.00, 0.18),
        "N": (0.00, 0.03),
        "C": (0.00, 0.08)
    },

    "Titanium Grade 2": {
        "Ti": (99.00, 100.00),
        "Fe": (0.00, 0.30),
        "O": (0.00, 0.25),
        "N": (0.00, 0.03),
        "C": (0.00, 0.10)
    },

    "Titanium Grade 4": {
        "Ti": (98.00, 100.00),
        "Fe": (0.00, 0.50),
        "O": (0.00, 0.40),
        "N": (0.00, 0.05),
        "C": (0.00, 0.10)
    },

    "Titanium Grade 5 Ti-6Al-4V": {
        "Ti": (88.00, 91.00),
        "Al": (5.50, 6.75),
        "V": (3.50, 4.50),
        "Fe": (0.00, 0.40),
        "O": (0.00, 0.20),
        "C": (0.00, 0.10),
        "N": (0.00, 0.05)
    },

    "Titanium Grade 23 Ti-6Al-4V ELI": {
        "Ti": (88.50, 91.00),
        "Al": (5.50, 6.50),
        "V": (3.50, 4.50),
        "Fe": (0.00, 0.25),
        "O": (0.00, 0.13),
        "C": (0.00, 0.08),
        "N": (0.00, 0.05)
    }
}


# ============================================================
# MAGNESIUM
# ============================================================

MAGNESIUM = {

    "Magnesium AZ31B": {
        "Mg": (94.00, 96.50),
        "Al": (2.50, 3.50),
        "Zn": (0.60, 1.40),
        "Mn": (0.15, 0.50)
    },

    "Magnesium AZ61A": {
        "Mg": (90.00, 93.50),
        "Al": (5.80, 7.20),
        "Zn": (0.40, 1.50),
        "Mn": (0.15, 0.50)
    },

    "Magnesium AZ80A": {
        "Mg": (89.00, 92.00),
        "Al": (7.80, 9.20),
        "Zn": (0.20, 0.80),
        "Mn": (0.12, 0.50)
    },

    "Magnesium ZK60A": {
        "Mg": (92.00, 98.00),
        "Zn": (4.80, 6.20),
        "Zr": (0.40, 0.90)
    }
}


# ============================================================
# NICKEL ALLOYS
# ============================================================

NICKEL = {

    "Nickel 200": {
        "Ni": (99.00, 100.00),
        "C": (0.00, 0.15),
        "Fe": (0.00, 0.40),
        "Mn": (0.00, 0.35),
        "Si": (0.00, 0.35)
    },

    "Nickel 201": {
        "Ni": (99.00, 100.00),
        "C": (0.00, 0.02),
        "Fe": (0.00, 0.40),
        "Mn": (0.00, 0.35),
        "Si": (0.00, 0.35)
    },

    "Nickel Alloy 400 / Monel 400": {
        "Ni": (63.00, 70.00),
        "Cu": (28.00, 34.00),
        "Fe": (0.00, 2.50),
        "Mn": (0.00, 2.00),
        "C": (0.00, 0.30),
        "Si": (0.00, 0.50)
    },

    "Nickel Alloy 600": {
        "Ni": (72.00, 78.00),
        "Cr": (14.00, 17.00),
        "Fe": (6.00, 10.00),
        "C": (0.00, 0.15)
    },

    "Nickel Alloy 625": {
        "Ni": (58.00, 64.00),
        "Cr": (20.00, 23.00),
        "Mo": (8.00, 10.00),
        "Fe": (0.00, 5.00),
        "Nb": (3.15, 4.15)
    },

    "Nickel Alloy 718": {
        "Ni": (50.00, 55.00),
        "Cr": (17.00, 21.00),
        "Fe": (17.00, 21.00),
        "Mo": (2.80, 3.30),
        "Nb": (4.75, 5.50),
        "Ti": (0.65, 1.15),
        "Al": (0.30, 0.80)
    },

    "Nickel Alloy 825": {
        "Ni": (38.00, 46.00),
        "Cr": (19.50, 23.50),
        "Mo": (2.50, 3.50),
        "Cu": (1.50, 3.50),
        "Fe": (20.00, 30.00)
    },

    "Nickel Alloy C-276": {
        "Ni": (50.00, 70.00),
        "Cr": (14.50, 16.50),
        "Mo": (15.00, 17.00),
        "Fe": (4.00, 7.00),
        "W": (3.00, 5.00)
    }
}


# ============================================================
# ZINC ALLOYS
# ============================================================

ZINC = {

    "Zamak 2": {
        "Zn": (92.00, 96.00),
        "Al": (3.50, 4.30),
        "Cu": (2.60, 3.30),
        "Mg": (0.02, 0.06),
        "Fe": (0.00, 0.10)
    },

    "Zamak 3": {
        "Zn": (95.00, 97.00),
        "Al": (3.50, 4.30),
        "Cu": (0.20, 0.30),
        "Mg": (0.02, 0.06),
        "Fe": (0.00, 0.10)
    },

    "Zamak 5": {
        "Zn": (94.00, 97.00),
        "Al": (3.50, 4.30),
        "Cu": (0.75, 1.25),
        "Mg": (0.03, 0.08),
        "Fe": (0.00, 0.10)
    },

    "Zamak 7": {
        "Zn": (95.00, 97.00),
        "Al": (3.50, 4.30),
        "Cu": (0.20, 0.30),
        "Mg": (0.005, 0.020),
        "Fe": (0.00, 0.075)
    },

    "ZA-8": {
        "Zn": (89.00, 91.00),
        "Al": (8.00, 8.80),
        "Cu": (0.80, 1.30),
        "Mg": (0.015, 0.030),
        "Fe": (0.00, 0.075)
    },

    "ZA-12": {
        "Zn": (86.00, 89.00),
        "Al": (10.50, 11.50),
        "Cu": (0.50, 1.25),
        "Mg": (0.015, 0.030),
        "Fe": (0.00, 0.075)
    },

    "ZA-27": {
        "Zn": (68.00, 73.00),
        "Al": (25.00, 28.00),
        "Cu": (2.00, 2.50),
        "Mg": (0.010, 0.020),
        "Fe": (0.00, 0.075)
    }
}


# ============================================================
# CAST IRON
# ============================================================

CAST_IRON = {

    "Gray Cast Iron": {
        "C": (2.50, 4.00),
        "Si": (1.50, 3.00),
        "Mn": (0.20, 1.00),
        "P": (0.00, 0.30),
        "S": (0.00, 0.15),
        "Fe": (90.00, 96.00)
    },

    "Ductile Cast Iron": {
        "C": (3.00, 4.00),
        "Si": (1.80, 3.00),
        "Mn": (0.10, 0.50),
        "P": (0.00, 0.10),
        "S": (0.00, 0.03),
        "Mg": (0.03, 0.07),
        "Fe": (90.00, 96.00)
    },

    "Compacted Graphite Iron": {
        "C": (3.00, 4.00),
        "Si": (1.80, 3.00),
        "Mn": (0.20, 0.80),
        "P": (0.00, 0.10),
        "S": (0.005, 0.03),
        "Mg": (0.01, 0.03),
        "Fe": (90.00, 96.00)
    },

    "White Cast Iron": {
        "C": (2.00, 3.60),
        "Si": (0.50, 1.50),
        "Mn": (0.20, 1.00),
        "P": (0.00, 0.30),
        "S": (0.00, 0.15),
        "Fe": (93.00, 97.00)
    }
}


# ============================================================
# MASTER MATERIAL DATABASE
# ============================================================

MATERIALS = {
    "Aluminium": ALUMINIUM,
    "Steel": STEEL,
    "Copper": COPPER,
    "Brass": BRASS,
    "Bronze": BRONZE,
    "Titanium": TITANIUM,
    "Magnesium": MAGNESIUM,
    "Nickel": NICKEL,
    "Zinc": ZINC,
    "Cast Iron": CAST_IRON
}


# ============================================================
# MATERIAL SELECTION
# ============================================================

st.subheader("1️⃣ Select Material Family")

material_type = st.selectbox(
    "Material",
    list(MATERIALS.keys())
)

grades = MATERIALS[material_type]

st.success(
    f"{len(grades)} industrial grades/families available."
)


# ============================================================
# COMPOSITION INPUT
# ============================================================

st.subheader("2️⃣ Enter Chemical Composition")

elements = sorted(
    set(
        element
        for grade in grades.values()
        for element in grade
    )
)

composition = {}

columns = st.columns(3)

for index, element in enumerate(elements):

    with columns[index % 3]:

        composition[element] = st.number_input(
            f"{element} (wt. %)",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.4f"
        )

st.caption(
    "Enter the elements measured by XRF, OES or chemical analysis. "
    "Leave elements that were not measured at 0."
)


# ============================================================
# SCORING FUNCTION
# ============================================================

def calculate_score(sample, grade):

    checked = 0
    inside = 0
    total_score = 0.0

    for element, value in sample.items():

        if value <= 0:
            continue

        checked += 1

        if element not in grade:

            # The sample contains an element that this grade
            # does not specify in our screening database.
            total_score += 0.0
            continue

        low, high = grade[element]

        # ----------------------------------------------------
        # Value is inside the expected range
        # ----------------------------------------------------

        if low <= value <= high:

            inside += 1
            total_score += 100.0

        # ----------------------------------------------------
        # Value is outside the expected range
        # ----------------------------------------------------

        else:

            if value < low:
                distance = low - value
            else:
                distance = value - high

            range_width = max(high - low, 0.001)

            penalty = (
                distance / range_width
            ) * 100.0

            penalty = min(penalty, 100.0)

            element_score = 100.0 - penalty

            total_score += max(
                element_score,
                0.0
            )

    if checked == 0:
        return 0.0, 0.0

    similarity = total_score / checked

    range_match = (
        inside / checked
    ) * 100.0

    return similarity, range_match


# ============================================================
# ANALYSIS BUTTON
# ============================================================

if st.button(
    "🔍 Analyze Alloy",
    type="primary",
    use_container_width=True
):

    entered_elements = {
        element: value
        for element, value in composition.items()
        if value > 0
    }

    # --------------------------------------------------------
    # No input
    # --------------------------------------------------------

    if not entered_elements:

        st.error(
            "Please enter at least one chemical composition value."
        )

    else:

        results = []

        # ----------------------------------------------------
        # Compare sample with every grade
        # ----------------------------------------------------

        for grade_name, grade_data in grades.items():

            similarity, range_match = calculate_score(
                composition,
                grade_data
            )

            results.append({
                "grade": grade_name,
                "similarity": similarity,
                "range_match": range_match
            })

        # Highest similarity first
        results.sort(
            key=lambda item: item["similarity"],
            reverse=True
        )

        best = results[0]

        # ====================================================
        # BEST MATCH
        # ====================================================

        st.subheader("3️⃣ Best Matching Grade")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Best Match",
                best["grade"]
            )

        with col2:

            st.metric(
                "Similarity",
                f"{best['similarity']:.1f}%"
            )

        with col3:

            st.metric(
                "Elements Within Range",
                f"{best['range_match']:.1f}%"
            )

        # ----------------------------------------------------
        # Result interpretation
        # ----------------------------------------------------

        if best["range_match"] >= 80:

            st.success(
                f"✅ Strong composition match: {best['grade']}"
            )

        elif best["range_match"] >= 50:

            st.warning(
                f"⚠️ Possible composition match: {best['grade']}"
            )

        else:

            st.error(
                "❌ No strong composition match found."
            )


        # ====================================================
        # TOP 5 RESULTS
        # ====================================================

        st.subheader("📊 Top Matching Grades")

        for rank, result in enumerate(results[:5], start=1):

            st.write(
                f"**{rank}. {result['grade']}**  \n"
                f"Similarity: **{result['similarity']:.1f}%**  |  "
                f"Elements in range: **{result['range_match']:.1f}%**"
            )

            progress_value = int(
                min(
                    max(result["similarity"], 0),
                    100
                )
            )

            st.progress(progress_value)


        # ====================================================
        # ELEMENT-BY-ELEMENT VERIFICATION
        # ====================================================

        st.subheader(
            f"🔬 Composition Check — {best['grade']}"
        )

        best_grade = grades[best["grade"]]

        for element, value in entered_elements.items():

            # ------------------------------------------------
            # Element not listed in database
            # ------------------------------------------------

            if element not in best_grade:

                st.error(
                    f"❌ {element}: {value:.4f}% "
                    f"— element not specified for this screening grade"
                )

                continue

            low, high = best_grade[element]

            # ------------------------------------------------
            # Inside range
            # ------------------------------------------------

            if low <= value <= high:

                st.success(
                    f"✅ {element}: {value:.4f}%  "
                    f"| Expected: {low:.4f}–{high:.4f}%"
                )

            # ------------------------------------------------
            # Outside range
            # ------------------------------------------------

            else:

                st.error(
                    f"❌ {element}: {value:.4f}%  "
                    f"| Expected: {low:.4f}–{high:.4f}%"
                )


        # ====================================================
        # IMPORTANT NOTICE
        # ====================================================

        st.markdown("---")

        st.warning(
            "Important: A composition match is not equivalent to "
            "material certification. Product form, heat treatment, "
            "mechanical properties, microstructure and the applicable "
            "material standard may also be required for final identification."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "⚙️ Alloy Composition Analyzer | "
    "Metallurgical & Materials Engineering | "
    "Preliminary Industrial Screening Tool"
)
