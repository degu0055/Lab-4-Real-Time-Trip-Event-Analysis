import logging
import azure.functions as func
import json

# Set the default HTTP auth level to ANONYMOUS to allow public access
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="HttpTripProcessor")
@app.route(route="trip")  # Endpoint: /api/trip
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        input_data = req.get_json()
        # Support single object or list of trips
        trips = input_data if isinstance(input_data, list) else [input_data]

        results = []

        for record in trips:
            trip = record.get("ContentData", {})

            vendor = trip.get("vendorID")
            distance = float(trip.get("tripDistance", 0))
            passenger_count = int(trip.get("passengerCount", 0))
            payment = str(trip.get("paymentType"))

            insights = []

            if distance > 10:
                insights.append("LongTrip")
            if passenger_count > 4:
                insights.append("GroupRide")
            if payment == "2":
                insights.append("CashPayment")
            if payment == "2" and distance < 1:
                insights.append("SuspiciousVendorActivity")

            results.append({
                "vendorID": vendor,
                "tripDistance": distance,
                "passengerCount": passenger_count,
                "paymentType": payment,
                "insights": insights,
                "isInteresting": bool(insights),
                "summary": f"{len(insights)} flags: {', '.join(insights)}" if insights else "Trip normal"
            })

        return func.HttpResponse(
            body=json.dumps(results, indent=2),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error processing trip data: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)
