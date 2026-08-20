# Web Server – Security Guard Analogy

A web server is like a **security guard** at the door of a building.

- Someone (client) comes with a message (request)
- The guard (web server) takes the message
- The guard goes inside and gives it to the owner (backend/dashboard)
- The owner reads it and gives a reply
- The guard brings the reply back to the person (response)

## Security Layers (Like Checkpoints):

| Checkpoint | What It Does |
|------------|--------------|
| Security Group | Tells guard: "Only allow port 80 and 443" |
| Private Subnet | Owner lives in a hidden room — no direct outside access |
| Bastion Host | ID check — only verified people can enter |
| WAF | Scans messages for dangerous content (SQL injection) |
| SSL/TLS | Secret code — only guard and owner can read it |

## Why Keep Backend Private?

- The dashboard/database performs important tasks
- If someone sends a bad request, it could destroy data
- Personal data (like pics, videos, info) must stay safe
