from azure.eventhub import EventHubProducerClient, EventData
import json

# Replace with your actual connection string
connection_str = "Endpoint=sb://cst8917evhubns5873.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=rK9/rSJAbN1OC3vG8fWezriYSVOKMo3hV+AEhAKwupI="
eventhub_name = "gagokaba"

# Load the sample trip event
with open("trip_event.json", "r") as file:
    trip_data = json.load(file)

producer = EventHubProducerClient.from_connection_string(
    conn_str=connection_str,
    eventhub_name=eventhub_name
)

event_data_batch = producer.create_batch()
event_data_batch.add(EventData(json.dumps(trip_data)))

producer.send_batch(event_data_batch)
print("Trip event sent.")
