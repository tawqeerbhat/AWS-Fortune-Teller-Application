# <h1 style="font-size: 36px;">AWS Fortune Teller Application</h1>

### <h3 style="font-size: 24px;">Overview</h3>
This project creates a simple "Fortune Teller" application using **AWS Lambda** and **API Gateway**. The application responds to user questions with one of three random answers: **"yes," "no," or "maybe."**

---

## <h2 style="font-size: 30px;">Steps to Create the Fortune Teller Application</h2>

---

### <h3 style="font-size: 24px;">Step 1: Set Up an AWS Lambda Function</h3>
1. Open the **AWS Management Console** and navigate to the **Lambda service**.
2. Click on **Create function**.
3. Select **Author from scratch**.
4. **Function Name**: Enter a name for your function (e.g., `FortuneTeller`).
5. **Runtime**: Select Python 3.8 (or any other supported version).
6. Click on **Create function**.

---

### <h3 style="font-size: 24px;">Step 2: Write the Fortune-Telling Code</h3>
1. In the **Function code** section, you'll see an editor. Replace any existing code with the following:

```python
import json
import random

def lambda_handler(event, context):
    responses = ["yes", "no", "maybe"]
    answer = random.choice(responses)
    return {
        'statusCode': 200,
        'body': answer
    }

Click on Deploy to save the changes.
<h3 style="font-size: 24px;">Step 3: Set Up an API Gateway</h3>
Navigate to the API Gateway service in the AWS console.
Click on Create API.
Choose HTTP API.
Click Build.
API name: Enter FortuneTeller.
Click on Next.
<h3 style="font-size: 24px;">Step 4: Define the Integration</h3>
Choose Add integration.
Select Lambda and choose the Lambda function you created (e.g., FortuneTeller).
Click on Next.
<h3 style="font-size: 24px;">Step 5: Create the Route</h3>
For the resource path, enter /FortuneTeller.
For Method, select GET.
Click on Next.
<h3 style="font-size: 24px;">Step 6: Define Stages</h3>
Stage name: You can keep the default stage $default.
Enable Auto-deploy.
Click on Next.
<h3 style="font-size: 24px;">Step 7: Review and Create the API</h3>
Review the configurations you have made.
Click Create to finalize the API.
<h3 style="font-size: 24px;">Step 8: Test Your API</h3>
After deployment, copy the Invoke URL provided (it should look something like https://<your-api-id>.execute-api.us-east-1.amazonaws.com).
In your web browser or Postman, append /FortuneTeller to the Invoke URL:
https://<your-api-id>.execute-api.us-east-1.amazonaws.com/FortuneTeller
Press Enter to send the request. You should receive a response with "yes," "no," or "maybe."
<h3 style="font-size: 24px; text-align: center;">And that's it! 🎉 You've successfully built your Fortune Teller application!</h3> ```
