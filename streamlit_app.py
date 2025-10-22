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
    "Capillary Rheometer": ["Chanhassen, MN", "Bridgewater, NJ"],  # Updated
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
st.image("Henkel Logo.png",
         caption="Company Logo", width = 200, use_container_width=False, channels="RBG")
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

if main_choice == "Chemical Composition":
    chem_choice = st.selectbox("What do you need to analyze?", [
        "Select...", "Identify chemical elements", "Identify functional groups",
        "Separate and identify organic compounds", "Quantify moisture or organics"
    ])
    if chem_choice == "Identify chemical elements":
        trace = st.radio("Do you need trace-level detection?", ["Yes", "No"])
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

elif main_choice == "Physical / Mechanical Properties":
    mech = st.selectbox("Which property?", ["Hardness", "Tensile strength", "Viscosity / Flow"])
    if mech == "Hardness":
        suggest_method("Durometer")
    elif mech == "Tensile strength":
        suggest_method("Tensometer")
    elif mech == "Viscosity / Flow":
        flow = st.radio("Flow condition?", ["Low shear", "Light-sensitive", "Melt/high shear"])
        method = {
            "Low shear": "Brookfield Viscometer",
            "Light-sensitive": "Photorheometer",
            "Melt/high shear": "Capillary Rheometer"
        }[flow]
        suggest_method(method)

elif main_choice == "Thermal Analysis":
    thermal = st.selectbox("Which thermal property?", [
        "Thermal transitions", "Thermal degradation", "Dimensional change with temp",
        "Viscoelastic response", "TIM performance"
    ])
    method_map = {
        "Thermal transitions": "DSC",
        "Thermal degradation": "TGA",
        "Viscoelastic response": "DMA",
        "TIM performance": "TIM Tester"
    }
    if thermal in method_map:
        suggest_method(method_map[thermal])
    elif thermal == "Dimensional change with temp":
        option = st.radio("Choose method:", ["TMA", "Dilatometer"])
        suggest_method(option)

elif main_choice == "Surface & Barrier Properties":
    sbp = st.selectbox("Property?", ["Surface energy / wettability", "Barrier properties"])
    if sbp == "Surface energy / wettability":
        surface = st.radio("Measurement type:", ["Contact angle", "Surface tension"])
        suggest_method("Goniometer" if surface == "Contact angle" else "Sessile Drop Surface Tension Analyzer")
    elif sbp == "Barrier properties":
        suggest_method("WVTR")

elif main_choice == "Electrical Properties":
    elec = st.radio("Measurement:", ["Volume Resistivity", "Surface Resistance"])
    if elec == "Volume Resistivity":
        suggest_method("Volume Resistivity Analyzer")
    else:
        st.warning("⚠️ Surface Resistance not yet mapped.")

elif main_choice == "Microscopy & Imaging":
    micro = st.selectbox("Technique:", [
        "Confocal (optical)", "AFM (surface topology)", "SEM", "FIB/SEM", "EDS", "Ion Milling", "XRD", "XPS", "XRF"
    ])
    suggest_method(micro)



