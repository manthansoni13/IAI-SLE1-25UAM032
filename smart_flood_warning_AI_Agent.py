class SmartFloodWarningAgent:
    """
    PEAS Agent for Real-Time Hydrologic Sensing, Risk Modeling,
    and Multi-Channel Emergency Dispatch.
    """
    def __init__(self):
        self.history = []

    def verify_and_clean_data(self, water_level, rainfall):
        """Noise reduction filter to avoid false triggers."""
        cleaned_level = max(0.0, water_level)
        cleaned_rain = max(0.0, rainfall)
        return cleaned_level, cleaned_rain

    def calculate_flood_probability(self, water_level, rainfall, dam_release):
        """Predictive risk modeling engine."""
        risk_score = (water_level * 12) + (rainfall * 0.5)
        if dam_release:
            risk_score += 20
        
        probability = min(100, max(0, risk_score))
        return round(probability, 1)

    def select_actuation_protocol(self, probability):
        """Actuation Protocol Matrix mapping risk levels to actions."""
        if probability <= 30.0:
            risk_level = "Low / Advisory"
            actuators = "Dashboard & Web Portal"
            action = "Log data; increment sensor polling frequency."
        elif 30.0 < probability <= 60.0:
            risk_level = "Moderate Alert"
            actuators = "Mobile App Notifications"
            action = "Notify local authorities & emergency teams."
        elif 60.0 < probability <= 85.0:
            risk_level = "High Warning"
            actuators = "SMS Alerts + Mobile App"
            action = "Send targeted evacuation advisories to citizens."
        else:  # > 85%
            risk_level = "Critical Emergency"
            actuators = "Sirens + SMS + Broadcast"
            action = "Sound physical sirens; initiate automated evacuation."

        return risk_level, actuators, action

    def step(self, raw_water_level, raw_rainfall, dam_release):
        # 1. Perception & Data Filtering
        water_level, rainfall = self.verify_and_clean_data(raw_water_level, raw_rainfall)
        
        # 2. Inference
        prob = self.calculate_flood_probability(water_level, rainfall, dam_release)
        
        # 3. Actuation Selection
        risk, actuators, action = self.select_actuation_protocol(prob)

        return {
            "Water Level (m)": water_level,
            "Rainfall (mm/h)": rainfall,
            "Dam Release": dam_release,
            "Flood Probability": f"{prob}%",
            "Risk Level": risk,
            "Target Actuators": actuators,
            "Action Executed": action
        }


def get_user_inputs():
    """Prompts the user for manual telemetry values with error validation."""
    print("\n--- Enter Telemetry Percepts ---")
    
    # Input for Water Level
    while True:
        try:
            water_level = float(input("Enter River Water Level (in meters, e.g., 4.2): "))
            break
        except ValueError:
            print("Invalid input! Please enter a numerical value for water level.")

    # Input for Rainfall Intensity
    while True:
        try:
            rainfall = float(input("Enter Rainfall Rate (in mm/hour, e.g., 15.0): "))
            break
        except ValueError:
            print("Invalid input! Please enter a numerical value for rainfall.")

    # Input for Dam Release Status
    while True:
        dam_input = input("Is upstream dam releasing water? (yes/no): ").strip().lower()
        if dam_input in ['yes', 'y', 'true', '1']:
            dam_release = True
            break
        elif dam_input in ['no', 'n', 'false', '0']:
            dam_release = False
            break
        else:
            print("Invalid response! Please enter 'yes' or 'no'.")

    return water_level, rainfall, dam_release


if __name__ == "__main__":
    agent = SmartFloodWarningAgent()
    print("=== SMART FLOOD WARNING AGENT (MANUAL INPUT MODE) ===")

    while True:
        # Collect telemetry parameters from user
        water_level, rainfall, dam_release = get_user_inputs()
        
        # Process step through agent logic
        result = agent.step(water_level, rainfall, dam_release)
        
        # Output evaluation details
        print("\n" + "=" * 45)
        print(" AGENT ACTUATION RESULT")
        print("=" * 45)
        for key, val in result.items():
            print(f"  {key:<20}: {val}")
        print("=" * 45)
        
        # Option to continue or exit loop
        again = input("\nWould you like to test another scenario? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Exiting agent simulation program.")
            break
