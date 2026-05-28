# Subnet Notes

A subnet is a small network inside a VPC (Virtual Private Cloud).

Why use subnets?
- Organization: Keep different types of servers separate
- Security: Public servers in one subnet, private databases in another
- Performance: Keep related things close together

Two types of subnets:
- Public Subnet: Can talk directly to the internet (example: web server)
- Private Subnet: Cannot talk directly to the internet (example: database)

Public subnets are for things people need to access. Private subnets are for things that must stay hidden and secure.
