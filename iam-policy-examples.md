# IAM Policy Examples

## What is an IAM Policy?

An IAM Policy is a rule that defines exactly what a user can and cannot do.

It answers three questions:
1. **Who** is this rule for?
2. **What action** can they take? (read, write, delete)
3. **Which resource** does this apply to? (S3 bucket, EC2 server)

## Example 1: Read only

| Question | Answer |
|----------|--------|
| Who | User "Kinza" |
| Action | Read (s3:GetObject) |
| Resource | S3 bucket "my-bucket" |

**Result:** Kinza can **read** files but cannot change or delete them.

## Example 2: Full access

| Question | Answer |
|----------|--------|
| Who | User "Admin" |
| Action | All actions (s3:*) |
| Resource | All S3 buckets |

**Result:** Admin can **read, write, and delete** any file in any S3 bucket.

## Example 3: Deny access

| Question | Answer |
|----------|--------|
| Who | User "Guest" |
| Action | Delete (s3:DeleteObject) |
| Resource | S3 bucket "my-bucket" |

**Result:** Guest cannot delete any file.

## One sentence to remember:

An IAM Policy is a rule that says: "User X can do Action Y on Resource Z."
