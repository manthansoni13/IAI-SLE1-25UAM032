import random
import time

class Environment:
    """
    Simulates the IoT environment consisting of river water levels, 
    rainfall intensity, and upstream weather API feeds.
    """
    def __init__(self):
        self.water_level_m = 3.0  # Base water level in meters
        self.rainfall_mm_hr = 10.0 # Initial rainfall in mm/hour

    def get_sensor_telemetry(self):
        # Simulates real-time IoT telemetry fluctuations
        self.water_level_m += random.uniform(-0.1, 0.4)
        self.rainfall_mm_hr += random.uniform(-2.0, 8.0)
        
        # Sensor readings (Percepts)
        return {
            "water_level": round(max(0, self.water_level_m), 2),
            "rainfall": round(max(0, self.rainfall_mm_hr), 2),
            "upstream_dam_release": random.choice([True, False])
        }

class SmartFloodWarningAgent:
    """
    PEAS Agent for Real-Time Hydrologic Sensing, Risk Modeling,
    and Multi-Channel Emergency Dispatch.
    """
    def __init__(self):
        self.history = []

    def verify_and_clean_data(self, percepts):
        """Noise reduction filter to avoid false triggers."""
        cleaned_level = max(0.0, percepts["water_level"])
        cleaned_rain = max(0.0, percepts["rainfall"])
        return cleaned_level, cleaned_rain

    def calculate_flood_probability(self, water_level, rainfall, dam_release):
        """Predictive risk modeling engine."""
        # Simple weighted model predicting flood risk percentage (0 to 100)
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
        elif 31.0 <= probability <= 60.0:
            risk_level = "Moderate Alert"
            actuators = "Mobile App Notifications"
            action = "Notify local authorities & emergency teams."
        elif 61.0 <= probability <= 85.0:
            risk_level = "High Warning"
            actuators = "SMS Alerts + Mobile App"
            action = "Send targeted evacuation advisories to citizens."
        else: # > 85%
            risk_level = "Critical Emergency"
            actuators = "Sirens + SMS + Broadcast"
            action = "Sound physical sirens; initiate automated evacuation."

        return risk_level, actuators, action

    def step(self, percepts):
        # 1. Perception & Data Filtering
        water_level, rainfall = self.verify_and_clean_data(percepts)
        
        # 2. Inference
        prob = self.calculate_flood_probability(water_level, rainfall, percepts["upstream_dam_release"])
        
        # 3. Actuation Selection
        risk, actuators, action = self.select_actuation_protocol(prob)

        return {
            "Water Level (m)": water_level,
            "Rainfall (mm/h)": rainfall,
            "Dam Release": percepts["upstream_dam_release"],
            "Flood Probability": f"{prob}%",
            "Risk Level": risk,
            "Target Actuators": actuators,
            "Action Executed": action
        }

# Execution loop simulating agent operation
if __name__ == "__main__":
    env = Environment()
    agent = SmartFloodWarningAgent()

    print("--- SMART FLOOD WARNING AGENT SIMULATION ---\n")
    for cycle in range(1, 6):
        sensor_data = env.get_sensor_telemetry()
        result = agent.step(sensor_data)
        
        print(f"[Telemetry Cycle {cycle}]")
        for key, val in result.items():
            print(f"  {key}: {val}")
        print("-" * 50)
        time.sleep(1)
