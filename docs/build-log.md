## 2026-06-03 – API Security, Monitoring, and Troubleshooting

### API Key Security

Configured API Gateway to require an API key for the POST /messages endpoint.

Implemented:

* API Key
* Usage Plan
* API Stage association
* Request throttling

Testing:

* Request without API key returned HTTP 403 Forbidden.
* Request with valid API key returned HTTP 200 OK.

### API Throttling

Configured throttling through API Gateway Usage Plans.

Tested by sending multiple requests rapidly.

Observed:

* Initial requests succeeded with HTTP 200.
* Excess requests were rejected with HTTP 429 Too Many Requests.

Learned that API Gateway can protect backend services by rejecting excessive requests before Lambda executes.

### Troubleshooting Exercise – API Key Association

Removed API key association from the Usage Plan.

Observed:

* API returned HTTP 403 Forbidden.
* Lambda was never invoked.

Investigation:

* Verified API Key Required setting.
* Checked API Key associations.
* Determined API key was no longer attached to the Usage Plan.

Resolution:

* Re-associated API key with Usage Plan.
* API returned HTTP 200 OK.

### Troubleshooting Exercise – IAM Permissions

Removed DynamoDB permissions from the Lambda execution role.

Observed:

* API returned HTTP 502 Internal Server Error.

Investigation:

* Reviewed Lambda CloudWatch logs.
* Identified AccessDeniedException for dynamodb:PutItem.

Resolution:

* Restored DynamoDB PutItem permission.
* API returned HTTP 200 OK.

### Troubleshooting Exercise – Environment Variables

Modified Lambda environment variable TABLE_NAME to an invalid table name.

Observed:

* API returned HTTP 502 Internal Server Error.

Investigation:

* Reviewed Lambda CloudWatch logs.
* Noted AccessDeniedException on resource table/wrong-table-name.
* Determined root cause was incorrect configuration rather than missing permissions.

Resolution:

* Corrected TABLE_NAME environment variable.
* API returned HTTP 200 OK.

### Monitoring

Created CloudWatch alarm for API Gateway 4XX errors.

Configuration:

* Metric: 4XXError
* Threshold: Greater than 0
* Evaluation: 1 out of 1 datapoints
* Missing Data: Not Breaching

Testing:

* Generated HTTP 403 responses.
* Verified alarm transitioned from OK to ALARM.

### Key Lessons Learned

* 403 errors generally indicate API Gateway security or access issues.
* 429 errors indicate throttling and request limits.
* 502 errors typically indicate backend or Lambda failures.
* "Missing Authentication Token" usually indicates a route, method, or stage issue.
* AccessDenied errors should be analyzed by identifying:

  * Who was denied
  * What action was attempted
  * Which resource was targeted
  * Whether the resource is expected
* Absence of Lambda logs can indicate the request never reached Lambda.
