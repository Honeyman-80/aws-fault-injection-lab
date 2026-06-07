# Troubleshooting Scenarios

## HTTP 403 Forbidden

Possible Causes:

* Missing API key
* API key not associated with Usage Plan
* Invalid API key
* Route protection enabled

Investigation Steps:

1. Verify API Key Required setting.
2. Verify API key exists.
3. Verify API key is associated with a Usage Plan.
4. Verify Usage Plan is associated with the correct API stage.

---

## HTTP 429 Too Many Requests

Possible Causes:

* API Gateway throttling
* Usage Plan rate limits exceeded

Investigation Steps:

1. Review Usage Plan throttling settings.
2. Identify affected API key.
3. Determine whether traffic is expected or abnormal.
4. Review CloudWatch API Gateway metrics.

---

## HTTP 502 Internal Server Error

Possible Causes:

* Lambda exception
* IAM permission failure
* Environment variable misconfiguration
* Downstream service failure

Investigation Steps:

1. Open Lambda CloudWatch logs.
2. Read the complete error message.
3. Identify:

   * Principal
   * Action
   * Resource
4. Confirm environment variables and service configuration.

---

## Missing Authentication Token

Possible Causes:

* Wrong route
* Wrong HTTP method
* Wrong stage
* Deployment mismatch

Investigation Steps:

1. Verify API Gateway resources.
2. Verify route exists.
3. Verify correct HTTP method.
4. Verify correct stage URL.

---

## AccessDenied Investigation Checklist

When encountering AccessDenied:

1. Who was denied?
2. What action was attempted?
3. Which resource was targeted?
4. Is the targeted resource the expected resource?

Do not assume every AccessDenied error is caused by missing permissions. Incorrect configuration can produce similar symptoms.

# Troubleshooting Playbook

## 403 Forbidden
Likely before Lambda. Check API Gateway method settings, API key requirement, usage plan, and stage association.

## 429 Too Many Requests
Likely API Gateway throttling. Check usage plan rate/burst limits.

## 502 Internal Server Error
Likely backend failure. Check Lambda CloudWatch logs.

## Missing Authentication Token
Usually route, method, or stage mismatch. Compare client URL/method to API Gateway resources.

## AccessDeniedException
Do not assume “just add permissions.” Check:
- Who was denied
- What action was attempted
- Which resource was targeted
- Whether that resource is expected

## HandlerNotFound
Check Lambda runtime handler setting and function name in code.

## KeyError
Check request body field names against what the Lambda code expects.

## CloudTrail
Use CloudTrail to answer:
- Who changed something?
- What action was taken?
- When did it happen?
- What resource was changed?
