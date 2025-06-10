import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Maintenance Engineering Guide", layout="centered")

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007acc;
        color: white;
        font-size: 1.1em;
        font-weight: bold;
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 8px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    div.stButton > button:first-child:hover {
        background-color: #005a99;
        transition: 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ Maintenance Strategy Advisor")
st.markdown("""
Welcome to the **Maintenance Strategy Advisor** — an educational and interactive tool designed for engineering students, professionals,
and maintenance planners. This application will walk you through the types of maintenance, strategic decision-making, and Maintenance KPI's.

**Use the sidebar to explore topics:**
""")

st.sidebar.title("🔧 Topics")
selection = st.sidebar.radio("Go to:", [
    "Overview of Maintenance Types",
    "Strategy Recommendation Tool",
    "Condition Monitoring Techniques",
    "D-I-P-F Curve",
    "Bathtub Curve",
    "Maintenance KPIs Calculator",
    "Maintenance Quiz",  # ✅ Add this line
    "About"])

if selection == "Overview of Maintenance Types":
    st.header("📘 Types of Maintenance")
    st.markdown("""
    ### 🧠 Introduction
    Maintenance strategies are essential for ensuring the reliability, safety, and cost-effectiveness of equipment and systems across various industries.     These strategies define how maintenance activities are planned and executed to prevent failures, extend asset life, and optimize operational performance. The main types of maintenance strategies include **Corrective Maintenance (Run to Failure)**, **Preventive Maintenance (Time-Based)**, **Predictive Maintenance (Condition-Based)**, **Proactive Maintenance**, **Prescriptive Maintenace**, and **Reliability-Centered Maintenance (RCM)**. Each approach differs in terms of complexity, cost, required resources, and effectiveness in minimizing downtime. Understanding these strategies is crucial for selecting the most appropriate method based on equipment criticality, failure consequences, and operational context. 
    **Below are the most widely used strategies in engineering industries:**

    ### 1. 🛑 Corrective Maintenance (CM) — Also called Breakdown or Run-to-Failure
    - **Definition**: Maintenance performed only after equipment fails.
    - **Goal**: Restore functionality post-failure.
    - **Advantages**: No planning cost, simple.
    - **Disadvantages**: High risk, unplanned downtime, costly in critical systems.
    - **Best for**: Low-value, non-critical assets.
    - **Examples**: Light bulbs, decorative motors.

    ### 2. 🔁 Preventive Maintenance (PM)
    - **Definition**: Periodic maintenance at fixed time or usage intervals regardless of asset condition.
    - **Goal**: Prevent unexpected failures.
    - **Advantages**: Reduces failure risk, easy to plan.
    - **Disadvantages**: May result in unnecessary maintenance and costs.
    - **Best for**: Assets with predictable wear.
    - **Examples**: Replacing filters, monthly cleaning, oil changes.

    ### 3. 📊 Predictive Maintenance (PdM or CBM)
    - **Definition**: Uses real-time condition monitoring (vibration, temperature, oil analysis) to decide when to maintain.
    - **Goal**: Optimize timing of interventions.
    - **Advantages**: Prevents both under- and over-maintenance.
    - **Disadvantages**: Requires sensors and diagnostics.
    - **Best for**: High-value, rotating, or critical machines.
    - **Examples**: Vibration analysis for motors, DGA for transformers.

    ### 4. 🧠 Proactive Maintenance
    - **Definition**: Focuses on root cause elimination — redesigns, training, better lubrication, etc.
    - **Goal**: Stop failure before it begins.
    - **Advantages**: Long-term reliability improvement.
    - **Disadvantages**: Requires deep failure analysis.
    - **Best for**: Plants with high reliability goals.

    ### 5. 🔄 Reliability-Centered Maintenance (RCM)
    - **Definition**: Structured analysis method to select the best maintenance approach for each failure mode.
    - **Goal**: Balance safety, availability, and cost.
    - **Advantages**: Risk-based, asset-specific.
    - **Disadvantages**: Time-consuming and analytical.
    - **Best for**: Critical industries (power, aviation, oil & gas).

    ### 6. 🤖 Prescriptive Maintenance (AI-driven)
    - **Definition**: Uses machine learning to recommend what action to take based on data.
    - **Goal**: Automate decisions using historical and real-time data.
    - **Advantages**: High efficiency, ideal for digital plants.
    - **Disadvantages**: Requires data integration, algorithm training.
    - **Best for**: Industry 4.0, digital twins.

    ---
    **Choosing the right strategy** depends on asset criticality, failure behavior, cost, and available technology. Use the selector in this app to help guide your decision.
    """)

    # --- Add comparison table ---
    st.markdown("### 🧾 Comparative Table of Maintenance Strategies")

    comparison_data = {
        "Strategy": ["Corrective", "Preventive", "Predictive", "Proactive", "Prescriptive", "RCM"],
        "Definition": [
            "Performed after failure occurs",
            "Scheduled at regular intervals",
            "Based on actual condition data",
            "Eliminates root causes before failure",
            "Uses AI to predict & prescribe actions",
            "Selects best strategy by criticality"
        ],
        "Trigger": [
            "Failure happens",
            "Time or usage interval",
            "Condition thresholds",
            "Root cause identification",
            "Data-driven prediction",
            "Function/failure analysis"
        ],
        "Tools/Techniques": [
            "Manual repair, fault diagnosis",
            "Calendar-based schedules",
            "Sensors, condition monitoring",
            "RCA, FMEA, tribology",
            "Machine learning, digital twins",
            "FMEA, reliability modeling"
        ],
        "Advantages": [
            "Simple, no upfront cost",
            "Reduces surprise failures",
            "Targets real issues, efficient",
            "Improves long-term reliability",
            "Optimizes decisions automatically",
            "Balances risk, cost, and performance"
        ],
        "Disadvantages": [
            "High downtime, costly failures",
            "Can cause over-maintenance",
            "Requires instrumentation, analysis",
            "Needs deep technical insights",
            "Complex implementation, data needs",
            "Time-consuming analysis"
        ],
        "Best Use Case": [
            "Low-value, non-critical assets",
            "Equipment with predictable aging",
            "Rotating/high-value machinery",
            "Recurring or systemic issues",
            "Smart/digitalized operations",
            "Critical assets with high consequences"
        ]
    }

    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)


    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Strategy Recommendation Tool":
    st.header("🧩 Maintenance Strategy Selector")
    st.markdown("""
    Answer the following questions to get a strategy recommendation based on asset criticality, cost, and environment.
    """)

    criticality = st.selectbox("1️⃣ Asset Criticality", ["High", "Medium", "Low"],
        help="**Definition**: Importance of the asset to safety, production, or legal compliance.\n- High: Generator, main transformer, turbine\n- Medium: HVAC motor, feedwater pump, coolling fan\n- Low: Lights, admin printers")

    environment = st.selectbox("2️⃣ Operating Environment", ["Harsh", "Normal", "Clean"],
        help="**Definition**: Physical conditions around the asset.\n- Harsh: Heat, vibration, dust, chemicals\n- Clean: Lab or server room\n- Normal: Typical plant conditions")

    failure_history = st.selectbox("3️⃣ Failure History", ["Frequent", "Occasional", "Rare"],
        help="**Definition**: How often this asset fails.\nUse historical CMMS data if available.")

    maintenance_cost = st.selectbox("4️⃣ Maintenance Cost", ["High", "Medium", "Low"],
        help="**Definition**: Cost to repair, including labor, tools, spares, downtime.")

    downtime_cost = st.selectbox("5️⃣ Downtime Cost", ["High", "Medium", "Low"],
        help="**Definition**: Cost of system unavailability in terms of production, safety, or compliance.")

    recommendation = ""
    reason = ""
    examples = ""

    if criticality == "Low" and failure_history == "Rare":
        recommendation = "Run-to-Failure (RTF)"
        reason = "Non-critical asset with rare failures. Let it run until it fails."
        examples = "Small lights, backup indicators."
    elif criticality == "High" and environment == "Harsh" and failure_history != "Rare":
        recommendation = "Condition-Based Maintenance (CBM)"
        reason = "Critical asset in harsh conditions benefits from monitoring sensors."
        examples = "Pumps with vibration sensors, motors with IR thermography."
    elif criticality == "Medium" and failure_history == "Frequent":
        recommendation = "Time-Based Maintenance (TBM)"
        reason = "Frequent failures warrant a routine schedule."
        examples = "Monthly maintenance of air filters."
    elif criticality == "High" and downtime_cost == "High" and maintenance_cost == "High":
        recommendation = "Reliability-Centered Maintenance (RCM)"
        reason = "Critical and costly failures justify detailed RCM analysis."
        examples = "Turbine system, excitation panel."
    else:
        recommendation = "Preventive Maintenance (PM)"
        reason = "Standard scheduled checks fit this scenario."
        examples = "Lubrication plans, visual inspections."

    st.success(f"Recommended Strategy: **{recommendation}**")
    st.markdown(f"**Why:** {reason}")
    st.markdown(f"**Examples:** {examples}")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)


elif selection == "Condition Monitoring Techniques":
    st.header("📊 Condition Monitoring Techniques")
    st.markdown("""
    Condition monitoring is a key component of modern maintenance strategies, enabling the early detection of faults and degradation in assets before failures occur. It involves the continuous or periodic measurement and analysis of specific parameters that reflect the health and performance of equipment. By monitoring variables such as vibration, temperature, oil quality, acoustic emissions, and electrical signals, condition monitoring techniques help identify abnormal conditions, wear, or potential failures in advance. 

    **This proactive approach helps to:**
    - Support predictive maintenance
    - Reduce unplanned downtime
    - Enhances safety
    - Extends asset life
    - Detect developing faults
    - Prevent catastrophic failures

    ### Techniques & Tools:

    #### 1. **Vibration Analysis**
    - Detects: Imbalance, misalignment, bearing failure
    - Used with FFT to view frequency spectrum
    - Tools: Accelerometers, online monitoring systems
    - Applications: Generators, Turbines, Motors, Pumps 

    #### 2. **Infrared Thermography**
    - Detects: Overheating, phase imbalance, loose connections
    - Tools: Thermal cameras
    - Applications: Transformers, Switchgears, Motors

    #### 3. **Oil Analysis (including DGA)**
    - Detects: Vescosity, density, flash point, moisture, oxidation, breakdown voltage, gas generation,... etc
    - Tools: Lab. instruments
    - Applications: Transformers, turbines, engines, gearboxes,... etc

    #### 4. **Ultrasound Monitoring**
    - Detects: Air/gas leaks, bearing wear, arcing
    - Tools: Ultrasonic detectors
    - Applications: Pneumatic circuits, electrical cabinets

    #### 5. **Electrical Signature Analysis (ESA)**
    - Detects: Rotor bar faults, stator issues
    - Applications: Motors, generators

    ✅ Best Practice:
    - Combine techniques for reliability
    - Train technicians and analyze trends over time
    """)

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "D-I-P-F Curve":
    st.header("📉 D-I-P-F Curve: Detection, Indication, Prediction, and Failure")
    
    st.markdown("""
    ### 🧠 Introduction
    The **D-I-P-F curve** represents a modern approach to asset failure progression, commonly used in condition-based and predictive maintenance frameworks. It breaks down the failure process into four key stages:
    
    - **D (Detection)**: Early changes or weak signals are detected—often invisible to operators. Detected by advanced condition monitoring or machine learning.
    - **I (Indication)**: Observable symptoms begin to appear, such as noise, heat, or vibration. Alerts may be triggered.
    - **P (Prediction)**: Sufficient data is available to estimate remaining useful life (RUL) or time to failure with predictive models.
    - **F (Failure)**: The asset fails or reaches a critical point where performance is lost or unsafe.

    This curve emphasizes the **window of opportunity** between detection and failure, during which maintenance can be performed proactively to avoid unplanned downtime.
    """)

    st.image("dipf_curve_example.png", caption="Illustrative DIPF Curve", use_container_width=True)

    st.markdown("""
    ### 📌 Key Insights
    - 📍 The earlier the detection, the wider the window for predictive maintenance.
    - 🔍 Predictive models and condition monitoring can significantly shift interventions earlier in the curve.
    - 🧠 Understanding DIPF improves decision-making in AI-based maintenance strategies.

    ### 🔧 Applications
    - Rotating equipment health monitoring
    - Transformer DGA interpretation
    - Predictive maintenance using IoT/ML
    - Failure mode tracking in RCM

    """)

    st.success("DIPF is foundational to building effective predictive maintenance systems.")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Bathtub Curve":
    st.header("🛁 Bathtub Curve")
    st.markdown("""
    The **Bathtub curve** is a visual representation of the failure rate of a product or group of products over time and guides maintenance strategy.
    By plotting the occurrences of failure over time, a bathtub curve maps out three phases that an asset experiences within its lifetime: Infant mortality phase, Useful life pase, and Wear-out phase.

    ### Lifecycle Phases:

    1. **Infant Mortality** (High failure rate)
       - Causes: Design or Manufacturing flaws, installation defects, improper commissioning.
       - Overcome by: Early inspections/testing, burn-in


    2. **Useful Life** (Constant, low rate)
       - Causes: Random, external events, process upsets, improper maintenance/operation, random failures, human errors.
       - Action: Condition monitoring, scheduled PM, proper operation, training.


    3. **Wear-Out Phase** (Increasing failures)
       - Causes: Fatigue, aging, erosion, corrosion.
       - Overcome by: Overhaul, replacement, RCM.

    ✅ Use this curve to match strategy with lifecycle stage.
    """)
    st.image("bathtub_curve_example.png", caption="Bathtub Curve with Maintenance Zones")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Maintenance KPIs Calculator":
    st.header("📈 Maintenance KPIs Calculator — Interactive Dashboard")
    st.markdown("""
    KPIs provide a measurable way to assess and improve your maintenance program.
    Enter data below to calculate:
    """)

    st.subheader("1. 🔁 MTBF (Mean Time Between Failures)")
    st.markdown(r"""
    **Formula:**
    $$\text{MTBF} = \frac{\text{Total Uptime}}{\text{Number of Failures}}$$
    """)
    uptime = st.number_input("Total Uptime (hours)", value=1000)
    failures = st.number_input("Number of Failures", value=5)
    if failures > 0:
        st.success(f"MTBF = {uptime / failures:.2f} hours")

    st.subheader("2. 🔧 MTTR (Mean Time to Repair)")
    st.markdown(r"""
    **Formula:**
    $$\text{MTTR} = \frac{\text{Total Downtime}}{\text{Number of Repairs}}$$
    """)
    downtime = st.number_input("Total Downtime (hours)", value=50)
    repairs = st.number_input("Number of Repairs", value=5)
    if repairs > 0:
        st.success(f"MTTR = {downtime / repairs:.2f} hours")

    st.subheader("3. ⚙️ Availability")
    st.markdown(r"""
    **Formula:**
    $$\text{Availability} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
    or equivalently:
    $$\text{Availability} = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}}$$
    """)
    if (uptime + downtime) > 0:
        availability = uptime / (uptime + downtime)
        st.success(f"Availability = {availability:.2%}")

    st.subheader("4. 📦 Maintenance Cost per Unit Output")
    st.markdown(r"""
    **Formula:**
    $$\text{Cost per Unit} = \frac{\text{Total Maintenance Cost}}{\text{Total Output}}$$
    """)
    cost = st.number_input("Total Maintenance Cost ($)", value=15000)
    output = st.number_input("Total Output (e.g., MWh, Tons)", value=1000)
    if output > 0:
        st.success(f"Cost per unit = ${cost/output:.2f}")

    st.subheader("5. 📅 Schedule Compliance (%)")
    st.markdown(r"""
    **Formula:**
    $$\text{Schedule Compliance} = \frac{\text{Completed On Time}}{\text{Scheduled Jobs}} \times 100$$
    """)
    scheduled = st.number_input("Scheduled Jobs", value=120)
    completed = st.number_input("Completed On Time", value=108)
    if scheduled > 0:
        st.success(f"Schedule Compliance = {completed/scheduled*100:.2f}%")

    st.subheader("6. 💰 Maintenance Budget Adherence")
    st.markdown(r"""
    **Formula:**
    $$\text{Budget Variance} = \frac{\text{Actual Spend} - \text{Planned Budget}}{\text{Planned Budget}} \times 100$$
    """)
    budget = st.number_input("Planned Budget ($)", value=20000)
    actual = st.number_input("Actual Spend ($)", value=18500)
    if budget > 0:
        variance = (actual - budget) / budget * 100
        st.success(f"Budget Variance = {variance:.2f}%")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Maintenance Quiz":
    st.header("🧠 Maintenance Knowledge Quiz")
    st.markdown("""
    Test your knowledge on maintenance strategies, reliability metrics, and condition monitoring. Select the best answer for each question. Click the button below to evaluate all answers at once.
    """)

    quiz_questions = [
        ("Which maintenance strategy involves fixing equipment only after a breakdown?", ["Preventive", "Corrective", "Predictive", "Proactive"], 1, "Corrective maintenance is performed only after a failure occurs."),
        ("MTBF stands for:", ["Mean Time Before Failure", "Maximum Test Base Factor", "Mean Time Between Failures", "Machine Tolerance Based Function"], 2, "MTBF is the average time between failures, used as a reliability indicator."),
        ("What does infrared thermography detect in electrical systems?", ["Current leakage", "Oil level", "Overheating or hotspots", "Gas buildup"], 2, "IR thermography identifies heat anomalies that indicate potential failure points."),
        ("Which method detects bearing wear through sound?", ["Thermal imaging", "Ultrasound monitoring", "Infrared scanning", "Oil sampling"], 1, "Ultrasound detects high-frequency sounds from worn bearings and leaks."),
        ("CBM stands for:", ["Corrective Based Monitoring", "Condition Based Maintenance", "Continuous Battery Maintenance", "Certified Breakdown Model"], 1, "CBM relies on actual equipment condition to determine maintenance needs."),
        ("What is the purpose of proactive maintenance?", ["Replace all components regularly", "React after failure", "Eliminate root causes of failure", "Ignore minor defects"], 2, "Proactive maintenance eliminates root causes before failure occurs."),
        ("A bathtub curve shows:", ["Temperature rise", "Maintenance cost trend", "Failure rate over time", "Lubricant viscosity"], 2, "It represents failure rate across asset lifecycle: early, steady, and wear-out."),
        ("DGA in transformer oil analysis stands for:", ["Dynamic Gas Analysis", "Dissolved Gas Analysis", "Delayed Gasket Actuation", "Divergent Ground Alignment"], 1, "DGA analyzes gases dissolved in oil to detect incipient transformer faults."),
        ("The wear-out period of an asset is characterized by:", ["Low failure rate", "Sudden voltage spikes", "High and increasing failure rate", "Noisy operations"], 2, "Failures increase due to age-related wear and fatigue."),
        ("Which KPI shows how much of the scheduled work was done?", ["MTTR", "MTBF", "Schedule Compliance", "Availability"], 2, "Schedule Compliance measures % of jobs completed on time."),
        ("RCM aims to:", ["Reduce staffing levels", "Select optimal strategy per failure mode", "Use one strategy for all equipment", "Eliminate the need for monitoring"], 1, "RCM chooses maintenance strategy based on risk and function."),
        ("Electrical Signature Analysis is mainly used for:", ["Pipe thickness", "Bearing vibration", "Motor diagnostics", "Gas insulation"], 2, "ESA identifies motor faults via voltage/current waveform analysis."),
        ("Which maintenance type uses AI to decide timing/actions?", ["Prescriptive", "Preventive", "Proactive", "Corrective"], 0, "Prescriptive maintenance uses AI models to recommend actions."),
        ("Which of the following is NOT a condition monitoring technique?", ["Vibration analysis", "Infrared scan", "Painting", "Oil analysis"], 2, "Painting is not a diagnostic method."),
        ("Which KPI combines MTTR and MTBF?", ["Efficiency", "Cost ratio", "Availability", "Utilization"], 2, "Availability = MTBF / (MTBF + MTTR), a core reliability metric."),
        ("Why is MTTR important?", ["It shows productivity", "It tracks job frequency", "It measures repair efficiency", "It increases OEE"], 2, "MTTR indicates how quickly a system is restored after failure."),
        ("Which curve phase is best for predictive maintenance?", ["Wear-out", "Useful life", "Infant mortality", "Shutdown"], 1, "During useful life, predictive monitoring is most valuable."),
        ("Which is a disadvantage of PM?", ["Reduces risk", "May cause over-maintenance", "Requires sensors", "Needs trained experts"], 1, "PM may be done too often, wasting resources."),
        ("In CBM, what triggers action?", ["Calendar date", "Runtime hours", "Sensor-based data", "Weather forecast"], 2, "CBM relies on actual asset condition from sensors."),
        ("Best maintenance for LED light in office:", ["RCM", "CBM", "RTF", "PdM"], 2, "Low-cost non-critical items are ideal for Run-to-Failure."),
        ("OEE includes:", ["Availability, performance, quality", "Load, fuel, temperature", "Speed, torque, voltage", "Time, cost, effort"], 0, "OEE is a productivity metric: A × P × Q."),
        ("A CMMS is used for:", ["Cooling motors", "Measuring voltage", "Managing maintenance tasks", "Oil filtration"], 2, "CMMS software schedules, tracks, and documents maintenance."),
        ("Which asset benefits most from RCM?", ["Office printer", "Emergency diesel generator", "Desk lamp", "UPS outlet"], 1, "Critical systems with safety/operational impact need RCM."),
        ("A low MTBF indicates:", ["Good reliability", "Frequent failures", "High maintenance budget", "Efficient planning"], 1, "Lower MTBF means failures are occurring often."),
        ("What type of maintenance is usually lowest cost upfront?", ["RCM", "Preventive", "Corrective", "Predictive"], 2, "Corrective has no planning cost—only when failure happens.")
      ]

    user_answers = {}
    submitted = st.button("📊 Submit All Answers")

    score = 0
    for i, (question, options, correct_idx, explanation) in enumerate(quiz_questions):
        st.subheader(f"Q{i+1}: {question}")
        user_choice = st.radio("Select one:", options, key=f"quiz_{i}")
        user_answers[i] = user_choice

        if submitted:
            correct_answer = options[correct_idx]
            if user_choice == correct_answer:
                st.success(f"✅ Correct — {explanation}")
                score += 1
            else:
                st.error(f"❌ Incorrect. Correct answer: {correct_answer} — {explanation}")

    if submitted:
        st.info(f"🏁 Final Score: {score} out of {len(quiz_questions)}")


    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "About":
    st.header("ℹ️ About This App")
    st.markdown("""
    This educational application was built to help engineers understand maintenance types, select appropriate strategies,
    and visualize key reliability concepts.

    👤 Developed by **Eng. Mohammed Assaf – CMRP, CEPSS**  
    ⚡ **Power Plant Electrical Maintenance Engineer**  
    🏭 **Attarat Operation and Maintenance Company (OMCO), Jordan**

    📧 Email: [Mo7ammed.assaf1@gmail.com](mailto:Mo7ammed.assaf1@gmail.com)  
    🔗 LinkedIn: [linkedin.com/in/mohammed-assaf](https://linkedin.com/in/mohammed-assaf)
    """)

