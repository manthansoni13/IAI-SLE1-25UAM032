# IAI-SLE1-25UAM032

# AI Contribution Log

## Repository Information
- **Repository:** `manthansoni13 / IAI-SLE1-25UAM032`
- **Project Name:** Smart Flood Warning Agent
- **Course / Module:** Introduction to Artificial Intelligence (IAI) - SLE1

---

## 1. Project Overview & AI Assistance
* **Primary AI Tool Used:** Gemini / ChatGPT
* **Objective:** Design, specify, and implement a PEAS-based Smart Flood Warning Agent with real-time sensor processing, predictive risk evaluation, and multi-channel actuation protocol dispatch.

---

## 2. Theoretical Framework & PEAS Formulation

### System Architecture
The agent operates on the classical **PEAS (Performance, Environment, Actuators, Sensors)** model designed for real-time hydrologic sensing and emergency management:

* **Performance Measure:** Maximizing alert accuracy, minimizing false alarm rates, achieving zero false negatives during high-risk events, and ensuring low-latency emergency notification dispatch.
* **Environment:** River basin channels, IoT sensor networks, weather forecasting feeds, and public emergency communication channels.
* **Actuators:** Centralized web dashboard, mobile push notification servers, emergency SMS broadcast gateways, and physical site sirens.
* **Sensors:** Ultrasonic river water level sensors (m), digital tipping-bucket rain gauges (mm/h), and upstream dam spillway status indicators.

---

## 3. Contribution Breakdown

### A. Theoretical Design & PEAS Matrix (Slides & Documentation)
* **AI Contribution:**
  * Proposed the initial PEAS framework layout and multi-tier notification escalation rules.
  * Generated standard risk threshold categories (Low, Moderate, High, Critical).
* **Human Refinement:**
  * Defined precise domain variables relevant to flood monitoring (water level, rainfall, dam release status).
  * Refined risk threshold percentages (30%, 60%, 85%) to align with real-world hydrologic safety standards.

### B. Python Agent Implementation (`smart_flood_warning_AI_Agent.py`)
* **AI Contribution:**
  * Structured the modular Python class `SmartFloodWarningAgent`.
  * Generated the base risk calculation formula and actuation mapping method.
* **Human Refinement:**
  * Converted the script from a passive random simulation to an interactive **User-Defined Input** model (`get_user_inputs()`).
  * Implemented defensive programming (input validation and `try-except` blocks) to handle non-numeric user inputs.
  * Standardized output formatting to display structured telemetry results clearly.

---

## 4. Work Distribution Summary

| Task Component | AI Generated (%) | Human Refined (%) | Key Human Contribution |
| :--- | :--- | :--- | :--- |
| **Theoretical Architecture & PEAS** | 70% | 30% | Defined hydrologic parameters and decision thresholds. |
| **Code Structure & Actuation Logic** | 75% | 25% | Implemented user prompt loop and input error handling. |
| **Documentation & README** | 80% | 20% | Formatted structure to match repository files and assignment goals. |

---

## 5. Verification & Validation
* Validated decision logic across all four risk tiers using manual boundary inputs.
* Ensured data sanitization in `verify_and_clean_data()` prevents negative values from disrupting calculations.
