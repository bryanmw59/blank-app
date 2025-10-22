import streamlit as st

# === FACILITY AVAILABILITY MAPPING ===
facility_map = {
    "Tensometer": ["Irvine, CA", "Chanhassen, MN", "Madison Heights, MI"],
    "TGA": ["Irvine, CA", "Chanhassen, MN", "Madison Heights, MI", "Bridgewater, NJ"],
    "TMA": ["Irvine, CA", "Chanhassen, MN", "Bridgewater, NJ"],
    "DMA": ["Irvine, CA", "Chanhassen, MN", "Madison Heights, MI", "Bridgewater, NJ"],
    "DSC": ["Irvine, CA", "Chanhassen, MN", "Madison Heights, MI", "Bridgewater, NJ"],
    "GPC": ["Irvine, CA", "Chanhassen, MN", "Bridgewater, NJ"],
    "IC": ["Irvine, CA", "Chanhassen, MN"],
    "FTIR": ["Irvine, CA", "Chanhassen, MN", "Bridgewater, NJ"],
    "NIR": ["Irvine, CA", "Chanhassen, MN", "Bridgewater, NJ"],
    "GC-FID": ["Irvine, CA", "Chanhassen, MN"],
    "TOC": ["Irvine, CA", "Chanhassen, MN"],
    "GC-MS": ["Irvine, CA", "Bridgewater, NJ"],
    "Karl Fischer Titration": ["Irvine, CA", "Bridgewater, NJ"],
    "Soxhlet Extraction": ["Irvine, CA"],
    "WVTR": ["Irvine, CA"],
    "Rotational Rheometer": ["Irvine, CA", "Chanhassen, MN", "Madison Heights, MI", "Bridgewater, NJ"],
    "Durometer": ["Chanhassen, MN", "Madison Heights, MI"],
    "Brookfield Viscometer": ["Madison Heights, MI"],
    "Photorheometer": ["Madison Heights, MI"],
    "Capillary Rheometer": ["Chanhassen, MN", "Bridgewater, NJ"],
    "UV Rheometer": ["Bridgewater, NJ"],
    "Confocal LSM": ["Bridgewater, NJ"],
    "SEM": ["Bridgewater, NJ"],
    "FIB/SEM": ["Bridgewater, NJ"],
    "EDS": ["Bridgewater, NJ"],
    "AFM": ["Bridgewater, NJ"],
    "XRD": ["Bridgewater, NJ"],
    "XPS": ["Bridgewater, NJ"],
    "XRF": ["Bridgewater, NJ"],
    "Ion Milling": ["Bridgewater, NJ"],
    "HPLC": ["Bridgewater, NJ"],
    "Volumetric Titrations": ["Bridgewater, NJ"],
    "Elemental Analysis Spectroscopy": ["Chanhassen, MN", "Bridgewater, NJ"],
    "Gravimetric Moisture Analyzer": ["Madison Heights, MI"],
    "Sessile Drop Surface Tension Analyzer": ["Madison Heights, MI"],
    "Goniometer": ["Madison Heights, MI"],
    "Volume Resistivity Analyzer": ["Madison Heights, MI"],
    "NMR": ["Bridgewater, NJ"],
    "Raman Spectroscopy": ["Bridgewater, NJ"],
    "TIM Tester": ["Chanhassen, MN"],
    "Dilatometer": ["Chanhassen, MN"]
}

# === SUGGEST METHOD + FACILITY OUTPUT ===
def suggest_method(method):
    st.success(f"✅ Recommended: {method}")
    facilities = facility_map.get(method, [])
    if facilities:
        st.write("📍 Available at:")
        for site in facilities:
            st.write(f"- {site}")
    else:
        st.warning("⚠️ No facility location found for this method.")

# === STREAMLIT APP ===
st.image("Henkel Logo.png", caption="Company Logo", width=200, use_container_width=False)
st.title("Henkel NA Analytical Technique Decision Tool")

main_choice = st.selectbox(
    "What type of analysis are you doing?",
    [
        "Select...",
        "Chemical Composition",
        "Physical / Mechanical Properties",
        "Thermal Analysis",
        "Surface & Barrier Properties",
        "Electrical Properties",
        "Microscopy & Imaging"
    ]
)

# === CHEMICAL COMPOSITION ===
if main_choice == "Chemical Composition":
    chem_choice = st.selectbox("What do you need to analyze?", [
        "Select...", "Identify chemical elements", "Identify functional groups",
        "Separate and identify organic compounds", "Quantify moisture or organics"
    ])
    if chem_choice == "Identify chemical elements":
        st.radio("Do you need trace-level detection?", ["Yes", "No"])
        suggest_method("Elemental Analysis Spectroscopy")
    elif chem_choice == "Identify functional groups":
        mat_type = st.radio("Material type:", ["Organic/polymeric", "Solid-state/carbon"])
        suggest_method("FTIR" if mat_type == "Organic/polymeric" else "Raman Spectroscopy")
    elif chem_choice == "Separate and identify organic compounds":
        sample_type = st.radio("Sample type:", ["Volatile organics", "Ions in solution", "Polymer MW"])
        method = {"Volatile organics": "GC-MS", "Ions in solution": "IC", "Polymer MW": "GPC"}[sample_type]
        suggest_method(method)
    elif chem_choice == "Quantify moisture or organics":
        quant = st.radio("Target:", ["Water", "Organic carbon", "Extractables/Volatiles"])
        method = {
            "Water": "Karl Fischer Titration",
            "Organic carbon": "TOC",
            "Extractables/Volatiles": "Soxhlet Extraction"
        }[quant]
        suggest_method(method)

# === PHYSICAL / MECHANICAL ===
elif main_choice == "Physical / Mechanical Properties":
    mech = st.selectbox("Which property?", ["Hardness", "Tensile strength", "Viscosity / Flow"])
    if mech == "Hardness":
        suggest_method("Durometer")
    elif mech == "Tensile strength":
        suggest_method("Tensometer")
    elif mech == "Viscosity / Flow":
        sample_form = st.radio("Sample type:", ["Low-viscosity liquids", "Photosensitive materials", "Molten polymers / high shear"])
        if sample_form == "Low-viscosity liquids":
            suggest_method("Brookfield Viscometer")
        elif sample_form == "Photosensitive materials":
            suggest_method("Photorheometer")
        elif sample_form == "Molten polymers / high shear":
            suggest_method("Capillary Rheometer")

# === THERMAL ANALYSIS ===
elif main_choice == "Thermal Analysis":
    thermal = st.selectbox("Which thermal property?", [
        "Thermal transitions", "Thermal degradation", "Dimensional change with temperature",
        "Viscoelastic response", "TIM performance"
    ])
    
    if thermal == "Thermal transitions":
        metrics = st.multiselect("Which metrics do you need?", ["Glass Transition (Tg)", "Melting Point (Tm)", "Crystallization"])
        st.write("📘 Thermal transitions such as Tg and Tm are typically measured using DSC.")
        suggest_method("DSC")
    elif thermal == "Thermal degradation":
        st.write("📘 Use TGA to assess weight loss and degradation temperatures.")
        suggest_method("TGA")
    elif thermal == "Dimensional change with temperature":
        metric = st.radio("Which metric?", ["CTE (Coefficient of Thermal Expansion)", "Thermal expansion curve"])
        method = "TMA" if metric == "CTE (Coefficient of Thermal Expansion)" else "Dilatometer"
        suggest_method(method)
    elif thermal == "Viscoelastic response":
        st.write("📘 Dynamic mechanical analysis measures storage/loss modulus across temperatures.")
        suggest_method("DMA")
    elif thermal == "TIM performance":
        st.write("📘 Measures thermal impedance/conductivity of TIM materials.")
        suggest_method("TIM Tester")

# === SURFACE & BARRIER ===
elif main_choice == "Surface & Barrier Properties":
    sbp = st.selectbox("Property?", ["Surface energy / wettability", "Water Vapor Transmission Rate (WVTR)"])
    if sbp == "Surface energy / wettability":
        surface = st.radio("Measurement type:", ["Contact angle", "Surface tension"])
        suggest_method("Goniometer" if surface == "Contact angle" else "Sessile Drop Surface Tension Analyzer")
    elif sbp == "Water Vapor Transmission Rate (WVTR)":
        st.write("📘 WVTR directly quantifies the rate of water vapor passage through materials — critical for evaluating moisture barrier properties in films and packaging.")
        suggest_method("WVTR")

# === ELECTRICAL ===
elif main_choice == "Electrical Properties":
    elec = st.radio("Measurement:", ["Volume Resistivity", "Surface Resistance"])
    if elec == "Volume Resistivity":
        suggest_method("Volume Resistivity Analyzer")
    else:
        st.warning("⚠️ Surface Resistance not yet mapped.")

# === MICROSCOPY & IMAGING ===
elif main_choice == "Microscopy & Imaging":
    micro_category = st.selectbox("What are you trying to visualize or measure?", [
        "Surface topography (nanoscale)", 
        "Internal microstructure (submicron-scale)",
        "Surface composition (elemental)",
        "Crystalline structure / phase",
        "Optical sectioning (fluorescence/confocal)"
    ])

    if micro_category == "Surface topography (nanoscale)":
        st.write("📘 Use AFM for high-resolution surface imaging and roughness/topography at the nanoscale.")
        suggest_method("AFM")
    elif micro_category == "Internal microstructure (submicron-scale)":
        st.write("📘 SEM is ideal for detailed imaging of surface fractures, while FIB/SEM can provide cross-sectional views.")
        tool = st.radio("Select method:", ["SEM", "FIB/SEM"])
        suggest_method(tool)
    elif micro_category == "Surface composition (elemental)":
        tool = st.radio("Select method:", ["EDS", "XPS", "XRF"])
        st.write("📘 EDS is SEM-based for spot analysis, XPS is for surface chemistry, and XRF for bulk elemental data.")
        suggest_method(tool)
    elif micro_category == "Crystalline structure / phase":
        st.write("📘 Use XRD to determine crystallinity, d-spacing, and phase composition.")
        suggest_method("XRD")
    elif micro_category == "Optical sectioning (fluorescence/confocal)":
        st.write("📘 Confocal LSM enables optical sectioning of fluorescently labeled materials.")
        suggest_method("Confocal LSM")
