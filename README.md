# IAI-SLE1-25UAM032

# Theoretical Framework: Smart Flood Warning Agent

## 1. System Overview & Problem Statement
The Smart Flood Warning Agent is an autonomous, real-time decision-support system designed to mitigate disaster risks in vulnerable hydrologic regions. By continuously processing telemetry from river networks, rainfall gauges, and dam infrastructures, the system evaluates disaster probability and triggers automated, multi-tiered emergency dispatch protocols without manual intervention delay.

---

## 2. PEAS Framework Specification

* **Performance Measure:**
  * Maximizing prediction accuracy of flood conditions.
  * Achieving zero false-negative triggers during critical emergencies.
  * Minimizing false-positive alarms to preserve public trust.
  * Maintaining ultra-low latency in multi-channel notification dispatch.

* **Environment:**
  * River basins, floodplains, and drainage channels.
  * Distributed IoT sensor networks (telemetry nodes).
  * Upstream dam spillway control systems.
  * External meteorological and weather forecasting feeds.
  * Emergency response communication networks.

* **Actuators:**
  * **Web Dashboard:** Centralized monitoring portal for logging and analytics.
  * **Mobile Push Notification System:** Direct alerts sent to registered mobile applications.
  * **Emergency SMS Gateway:** Targeted text broadcasts to citizens in affected geofences.
  * **Physical Acoustic Sirens:** High-decibel local alarm systems deployed at hazardous zones.

* **Sensors:**
  * **Ultrasonic River Level Sensors:** Measures water depth (in meters).
  * **Digital Rainfall Gauges:** Measures precipitation intensity (in mm/hour).
  * **Dam Spillway Status Feed:** Binary/numeric state indicators of upstream dam water release.

---

## 3. Agent Architecture & Decision Logic

The agent relies on a **Utility-Based / Model-Based Reflex Agent** structure:

1. **Perception & Filtering Phase:** The agent receives raw telemetry input and runs noise-reduction filters to strip negative anomalies or invalid sensor spikes.
2. **Inference & Risk Scoring Engine:** Sensor readings are combined into a dynamic risk probability score $P_{\text{risk}} \in [0, 100\%]$ using a weighted model:
   $$P_{\text{risk}} = \min\Big(100, \max\Big(0, (H_{\text{water}} \times 12) + (R_{\text{rain}} \times 0.5) + S_{\text{dam}}\Big)\Big)$$
   *Where $H_{\text{water}}$ is water height (m), $R_{\text{rain}}$ is rainfall rate (mm/h), and $S_{\text{dam}}$ is dam release status ($+20$ if active).*

3. **Actuation Protocol Selection:** The calculated risk probability maps directly to a 4-tier emergency escalation matrix:

| Threshold | Alert Level | Active Actuators | System Action Executed |
| :--- | :--- | :--- | :--- |
| **0% – 30%** | Low / Advisory | Web Dashboard | Log telemetry; maintain default sensor polling rate. |
| **31% – 60%** | Moderate Alert | Mobile App | Alert local authorities and field emergency units. |
| **61% – 85%** | High Warning | Mobile App + SMS | Issue targeted evacuation warnings to residents. |
| **> 85%** | Critical Emergency | Sirens + SMS + Broadcast | Trigger acoustic sirens; launch automated community evacuation. |
