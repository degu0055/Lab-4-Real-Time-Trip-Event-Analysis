<!-- 

Repo link:
https://github.com/degu0055/Lab-4-Real-Time-Trip-Event-Analysis


ChatGPT:
https://chatgpt.com/c/68883c5e-6850-8001-b904-fad3c71dec17

JSON:
https://chatgpt.com/c/68886f49-c814-8001-9bc2-56a55b39a774

Sample Data:
https://chatgpt.com/c/688ae0ff-59b4-8001-87d2-886d536754cc


Parse JSON step:
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "vendorID": {
        "type": "string"
      },
      "tripDistance": {
        "type": "number"
      },
      "passengerCount": {
        "type": "integer"
      },
      "paymentType": {
        "type": "string"
      },
      "insights": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "isInteresting": {
        "type": "boolean"
      },
      "summary": {
        "type": "string"
      }
    },
    "required": [
      "isInteresting"
    ]
  }
}

If else JSON card:
{
  "type": "AdaptiveCard",
  "body": [
    {
      "type": "TextBlock",
      "text": "@{if(contains(items('For_each')?['insights'], 'SuspiciousVendorActivity'), '⚠️ Suspicious Vendor Activity Detected', '🚨 Interesting Trip Detected')}",
      "weight": "Bolder",
      "size": "Large",
      "color": "Attention"
    },
    {
      "type": "FactSet",
      "facts": [
        { "title": "Vendor", "value": "@{items('For_each')?['vendorID']}" },
        { "title": "Distance (mi)", "value": "@{items('For_each')?['tripDistance']}" },
        { "title": "Passengers", "value": "@{items('For_each')?['passengerCount']}" },
        { "title": "Payment", "value": "@{items('For_each')?['paymentType']}" },
        { "title": "Insights", "value": "@{join(items('For_each')?['insights'], ', ')}" }
      ]
    }
  ],
  "actions": [],
  "version": "1.2"
}

 -->

 # CST8917 – Lab 4: Real-Time Trip Event Analysis

This lab demonstrates a real-time trip data analysis pipeline using Azure Event Hub, Azure Logic Apps, and Adaptive Cards integration with Microsoft Teams.

## 📌 Overview

Trip data is streamed to Azure Event Hub, analyzed using an Azure Function (optional), and evaluated by a Logic App that posts insights to Microsoft Teams based on conditions.

## ⚙️ Logic App Workflow

Logic App: `TripEventAnalysisLogicApp`

### Workflow Steps:
1. **Trigger** – `When events are available in Event Hub`
2. **HTTP Action** – (Optional) Sends incoming data to a custom Azure Function endpoint for processing
3. **Parse JSON** – Parses event body to extract `vendorID`, `tripDistance`, `passengerCount`, `paymentType`, `insights`, `isInteresting`, and `summary`
4. **For Each** – Iterates through each event in the batch
5. **Condition** – Checks if `isInteresting` is true  
   - `@{items('For_each')?['isInteresting']} equals true`

### If True:
- Check if `"SuspiciousVendorActivity"` is in `insights`:
  - Post **⚠️ Suspicious Vendor Activity Detected** Adaptive Card to Teams  
- Else:
  - Post **🚨 Interesting Trip Detected** Adaptive Card to Teams

### If False:
- Post **✅ Trip Analyzed - No Issues** Adaptive Card to Teams

## 🧠 Optional: Azure Function Code

You may include a Python function like `send_event.py` to test sending JSON events to Event Hub for simulation.

## 🗂️ Repo Structure

```
├── logic-app-definition.json      # Exported Logic App (from Azure Portal)
├── send_event.py                 # (Optional) Python script to send test events to Event Hub
├── adaptive-cards/
│   ├── interesting-trip.json
│   ├── suspicious-vendor.json
│   └── not-interesting.json
├── .http                         # HTTP test file to send requests
└── README.md                     # This file
```

## 🎥 Demo Video

[Click here to watch the demo video](https://drive.google.com/file/d/1G3u5Q_dQBcJ8-IjJlraqmEPmrl2vgBvZ/view?usp=sharing)


---

## ✅ Submission Notes

- This repository is public and well-structured as per assignment guidelines.
- Logic App definition and Adaptive Card JSONs are included.
- Demo video link is provided above (if available).