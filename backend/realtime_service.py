from azure.messaging.webpubsubservice import WebPubSubServiceClient
import os
import json

def send_order_update(order_id: int, status: str):
    conn_str = os.getenv("WEBPUBSUB_CONNECTION_STRING")
    if not conn_str:
        return

    client = WebPubSubServiceClient.from_connection_string(
        conn_str,
        hub="orderhub"
    )

    client.send_to_all(
        json.dumps({
            "order_id": order_id,
            "status": status
        }),
        content_type="application/json"
    )