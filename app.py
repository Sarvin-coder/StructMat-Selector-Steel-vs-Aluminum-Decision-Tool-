import streamlit as st
import io
from contextlib import redirect_stdout
import builtins  # ✅ FIX: use builtins instead of __builtins__

# ---------------------------------------------------------
# Steel vs Aluminum Structural Material Selection Tool
# Streamlit Wrapper (No function changes)
# ---------------------------------------------------------

steel = {
    "name": "Steel",
    "tensile_strength": 400,
    "yield_strength": 250,
    "density": 7850,
    "cost": 3.0,
    "corrosion_rating": 2
}

aluminum = {
    "name": "Aluminum",
    "tensile_strength": 310,
    "yield_strength": 275,
    "density": 2700,
    "cost": 12.0,
    "corrosion_rating": 5
}

# ---------------------------------------------------------
# YOUR ORIGINAL FUNCTIONS (UNCHANGED)
# ---------------------------------------------------------

def strength_selection():
    print("\n--- Application 1: Strength-Based Selection ---")
    print("This application compares materials based on tensile and yield strength.\n")

    print(f"{steel['name']} Tensile Strength: {steel['tensile_strength']} MPa")
    print(f"{aluminum['name']} Tensile Strength: {aluminum['tensile_strength']} MPa\n")

    print(f"{steel['name']} Yield Strength: {steel['yield_strength']} MPa")
    print(f"{aluminum['name']} Yield Strength: {aluminum['yield_strength']} MPa\n")

    steel_score = steel["tensile_strength"] + steel["yield_strength"]
    aluminum_score = aluminum["tensile_strength"] + aluminum["yield_strength"]

    if steel_score > aluminum_score:
        print("✅ Recommendation: Steel is stronger overall for structural use.")
    else:
        print("✅ Recommendation: Aluminum is stronger overall for structural use.")


def weight_selection():
    print("\n--- Application 2: Weight-Based Selection ---")
    print("This application compares materials based on density (lighter material is preferred).\n")

    print(f"{steel['name']} Density: {steel['density']} kg/m^3")
    print(f"{aluminum['name']} Density: {aluminum['density']} kg/m^3\n")

    if aluminum["density"] < steel["density"]:
        print("✅ Recommendation: Aluminum is lighter and more suitable when weight reduction is needed.")
    else:
        print("✅ Recommendation: Steel is lighter (unlikely case).")


def cost_selection():
    print("\n--- Application 3: Cost-Based Selection ---")
    print("This application compares materials based on cost per kilogram.\n")

    print(f"{steel['name']} Cost: RM {steel['cost']} per kg")
    print(f"{aluminum['name']} Cost: RM {aluminum['cost']} per kg\n")

    if steel["cost"] < aluminum["cost"]:
        print("✅ Recommendation: Steel is more cost-effective for structural projects.")
    else:
        print("✅ Recommendation: Aluminum is more cost-effective (unlikely case).")


def corrosion_selection():
    print("\n--- Application 4: Corrosion Resistance Selection ---")
    print("This application compares materials based on corrosion resistance rating.\n")

    print(f"{steel['name']} Corrosion Rating: {steel['corrosion_rating']} / 5")
    print(f"{aluminum['name']} Corrosion Rating: {aluminum['corrosion_rating']} / 5\n")

    if aluminum["corrosion_rating"] > steel["corrosion_rating"]:
        print("✅ Recommendation: Aluminum is better for outdoor or corrosive environments.")
    else:
        print("✅ Recommendation: Steel is better (unlikely case).")


def structural_element_recommendation():
    print("\n--- Application 5: Structural Element Recommendation ---")
    print("This application recommends materials based on the structural element type.\n")

    print("Choose a structural element:")
    print("1. Beam")
    print("2. Column")
    print("3. Slab")
    print("4. Truss")
    print("5. Frame")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nBeams usually require high strength and stiffness.")
        print("✅ Recommendation: Steel is preferred for beam applications due to higher strength.")
    elif choice == "2":
        print("\nColumns require strength and stability under compression.")
        print("✅ Recommendation: Steel is preferred because it can support higher compressive loads.")
    elif choice == "3":
        print("\nSlabs require cost-effectiveness and durability.")
        print("✅ Recommendation: Steel is preferred due to lower cost and strong structural performance.")
    elif choice == "4":
        print("\nTrusses benefit from lightweight materials, especially for long spans.")
        print("✅ Recommendation: Aluminum is preferred due to lower density and easier handling.")
    elif choice == "5":
        print("\nFrames require balanced performance and corrosion consideration.")
        print("✅ Recommendation: Steel is preferred for strength, but Aluminum can be chosen for corrosion resistance.")
    else:
        print("\n❌ Invalid input. Please select from 1 to 5.")


# ---------------------------------------------------------
# Helper: Capture printed output from your functions
# ---------------------------------------------------------
def run_and_capture(func, input_value=None):
    buffer = io.StringIO()

    original_input = builtins.input  # ✅ FIXED

    def fake_input(prompt=""):
        return str(input_value)

    try:
        # Patch input() only when needed (Application 5)
        if input_value is not None:
            builtins.input = fake_input

        with redirect_stdout(buffer):
            func()

    finally:
        # Always restore input()
        builtins.input = original_input

    return buffer.getvalue()


# ---------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------
st.set_page_config(page_title="Steel vs Aluminum Tool", page_icon="⚙️", layout="centered")

st.title("⚙️ Steel vs Aluminum Structural Material Selection Tool")
st.write("This web application compares steel and aluminum based on strength, weight, cost, and corrosion resistance.")
st.write("Choose an application module below to generate results.")

app_choice = st.selectbox(
    "Select an Application Module:",
    [
        "Application 1: Strength-Based Selection",
        "Application 2: Weight-Based Selection",
        "Application 3: Cost-Based Selection",
        "Application 4: Corrosion Resistance Selection",
        "Application 5: Structural Element Recommendation"
    ]
)

# For Application 5: we need user input from dropdown instead of console input
element_choice = None
if app_choice == "Application 5: Structural Element Recommendation":
    element_choice = st.selectbox(
        "Select Structural Element:",
        ["Beam", "Column", "Slab", "Truss", "Frame"]
    )

# Run button
if st.button("Run Application ✅"):
    if app_choice == "Application 1: Strength-Based Selection":
        output = run_and_capture(strength_selection)

    elif app_choice == "Application 2: Weight-Based Selection":
        output = run_and_capture(weight_selection)

    elif app_choice == "Application 3: Cost-Based Selection":
        output = run_and_capture(cost_selection)

    elif app_choice == "Application 4: Corrosion Resistance Selection":
        output = run_and_capture(corrosion_selection)

    elif app_choice == "Application 5: Structural Element Recommendation":
        mapping = {"Beam": 1, "Column": 2, "Slab": 3, "Truss": 4, "Frame": 5}
        output = run_and_capture(structural_element_recommendation, input_value=mapping[element_choice])

    st.subheader("📌 Output")
    st.code(output, language="text")

st.markdown("---")
st.caption("Developed for KKCE1112 Project (IR 4.0 Material Selection Tool)")
