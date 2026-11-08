# Route 53 Latency Routing Simulator

print("--- Route 53 Latency Routing ---")
user_location = input("Where is the user located? (e.g., Pakistan, USA): ")

print("\nFinding the server with the lowest latency...")

if user_location == "Pakistan":
    print("Routing user to the Server in Karachi (Latency: 10ms)")
elif user_location == "USA":
    print("Routing user to the Server in New York (Latency: 15ms)")
elif user_location == "UK":
    print("Routing user to the Server in London (Latency: 12ms)")
else:
    print("Routing user to the Default Server (Latency: 100ms)")

print("Routing Complete.")
