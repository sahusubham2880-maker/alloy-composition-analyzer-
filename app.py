import streamlit as st

st.set_page_config(
    page_title="Alloy Composition Analyzer",
    page_icon="⚙️"
)

st.title("⚙️ Alloy Composition Analyzer")
st.write("Enter the chemical composition of the selected alloy.")

# Alloy selection
alloy = st.selectbox(
    "Select Alloy Grade",
    ["Stainless Steel 304"]
)

st.info(f"Selected Grade: {alloy}")

# Composition input
st.subheader("Enter Chemical Composition (%)")

C = st.number_input("C (%)", min_value=0.0, value=0.04, step=0.01)
Cr = st.number_input("Cr (%)", min_value=0.0, value=18.1, step=0.1)
Ni = st.number_input("Ni (%)", min_value=0.0, value=8.1, step=0.1)
Mn = st.number_input("Mn (%)", min_value=0.0, value=1.0, step=0.1)
Si = st.number_input("Si (%)", min_value=0.0, value=0.5, step=0.1)

if st.button("🔍 Analyze Composition"):

    limits = {
        "C": (0, 0.08),
        "Cr": (18, 20),
        "Ni": (8, 10.5),
        "Mn": (0, 2),
        "Si": (0, 1)
    }

    values = {
        "C": C,
        "Cr": Cr,
        "Ni": Ni,
        "Mn": Mn,
        "Si": Si
    }

    passed = True

    st.subheader("Analysis Result")

    for element in limits:
        minimum, maximum = limits[element]
        value = values[element]

        if minimum <= value <= maximum:
            st.success(
                f"✅ {element}: {value}% — Within range "
                f"({minimum}–{maximum}%)"
            )
        else:
            st.error(
                f"❌ {element}: {value}% — Outside range "
                f"({minimum}–{maximum}%)"
            )
            passed = False

    st.subheader("Final Result")

    if passed:
        st.success("✅ Composition matches Stainless Steel 304")
    else:
        st.warning("⚠️ Composition does not fully match Stainless Steel 304")

st.caption(
    "Screening tool only. Exact composition limits depend on the applicable "
    "material standard and product specification."
)
