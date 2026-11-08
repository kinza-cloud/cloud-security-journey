# AWS Route 53 – Routing Policies

## What are Routing Policies?

Routing policies in Route 53 determine how AWS responds to DNS queries. It decides which server the user will be sent to.

## 3 Main Types of Routing Policies:

1. **Simple Routing:** 
   - Used when you have only one server. 
   - All traffic goes to that single server.

2. **Weighted Routing:** 
   - Used when you have multiple servers.
   - You can split traffic by weight. Example: Send 80% of traffic to Server A, and 20% to Server B.

3. **Latency Routing:** 
   - Used for global applications.
   - Route 53 sends the user to the server that provides the fastest response time (lowest latency) based on their location.

## One Sentence to Remember

> Route 53 Routing Policies decide which server receives the user's traffic based on rules like simple, weight, or latency.
