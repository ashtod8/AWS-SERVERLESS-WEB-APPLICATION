# AWS-SERVERLESS-WEB-APPLICATION
AWS Serverless Web Application built using Amazon S3, AWS Lambda (Python), and Amazon API Gateway. Demonstrates static website hosting, serverless backend execution, and HTTP request handling using AWS cloud services.

# AWS Serverless Web Application

## 1. Project Overview

This project demonstrates the development and deployment of a basic **Serverless Web Application using Amazon Web Services (AWS)**.

The application uses Amazon S3 for static website hosting, AWS Lambda for serverless backend execution, and Amazon API Gateway to expose the Lambda function through an HTTP endpoint.

The frontend is developed using HTML and JavaScript. When a user clicks the **Description** button, an HTTP GET request is sent to the API Gateway endpoint. API Gateway invokes the Lambda function, which executes the Python backend code and returns a response to the frontend.

This project demonstrates how multiple AWS managed services can work together to build a simple cloud-based application without provisioning or maintaining traditional servers.

## 2. Project Objectives

- Understand the fundamentals of serverless computing.
- Deploy a static website using Amazon S3.
- Create and configure an AWS Lambda function using Python.
- Integrate Lambda with Amazon API Gateway.
- Handle HTTP GET requests through an API endpoint.
- Connect a frontend application with a serverless backend.
- Understand how different AWS services communicate with each other.

## 3. AWS Services and Technologies Used

| Service / Technology | Purpose |
|---|---|
| Amazon S3 | Static website hosting |
| AWS Lambda | Serverless backend execution |
| Amazon API Gateway | HTTP request handling and API integration |
| Python | Backend programming language |
| HTML | Frontend structure |
| JavaScript | HTTP request handling and frontend interaction |

## 4. Architecture

The application follows a simple serverless architecture.

### Architecture Workflow

1. The user accesses the static website hosted on Amazon S3.
2. The website displays a heading and a Description button.
3. When the user clicks the button, JavaScript sends an HTTP GET request to the API Gateway endpoint.
4. API Gateway receives the request and invokes the associated AWS Lambda function.
5. AWS Lambda executes the Python backend code.
6. Lambda returns the execution result to API Gateway.
7. API Gateway sends the HTTP response back to the frontend.
8. JavaScript displays the returned response on the website.

### AWS Architecture Components

- **Amazon S3:** Hosts the frontend HTML file and serves the static website.
- **Amazon API Gateway:** Acts as the HTTP entry point for backend requests.
- **AWS Lambda:** Executes backend logic without requiring server management.

## 5. Implementation Steps

### Step 1: Create an AWS Lambda Function

1. Open the AWS Management Console.
2. Navigate to AWS Lambda.
3. Select **Create function**.
5. Enter the function name.
6. Select Python as the runtime.
7. Configure the execution role.
8. Select **Create function**.

### Step 2: Configure Python Backend Code

1. Open the newly created Lambda function.
2. Navigate to the Code section.
3. Replace the default code with the required Python code.
4. Select **Deploy** to save the changes.

### Step 3: Create and Configure API Gateway

1. Open the Lambda function.
2. Navigate to the Function overview section.
3. Select **Add trigger**.
4. Choose **API Gateway**.
5. Select HTTP API as the API type.
6. Configure the security settings.
7. Add the API Gateway trigger.
8. AWS automatically creates the API Gateway integration with the Lambda function.
9. Copy the generated API endpoint.

API Gateway acts as the HTTP interface between the frontend and the Lambda backend.

### Step 4: Create an Amazon S3 Bucket

1. Navigate to Amazon S3.
2. Select **Create bucket**.
3. Enter a globally unique bucket name.
4. Select the AWS Region.
5. Configure the bucket settings.
6. Create the bucket.

### Step 5: Upload the Frontend Website

1. Open the newly created S3 bucket.
2. Navigate to the Objects section.
3. Select **Upload**.
4. Upload the `index.html` file.
5. Complete the upload.

The HTML file contains the frontend structure and JavaScript function that communicates with API Gateway.

### Step 6: Connect the Frontend to API Gateway

Open the `index.html` file and configure the JavaScript function to use the API Gateway endpoint.

Replace the placeholder with your generated API Gateway invoke URL:

```javascript
xhttp.open(
    "GET",
    "YOUR_API_GATEWAY_INVOKE_URL",
    true
);
```

Ensure that API Gateway CORS settings allow requests from your S3 website origin.

### Step 7: Enable S3 Static Website Hosting

1. Open the S3 bucket.
2. Navigate to the Properties tab.
3. Locate **Static website hosting**.
4. Select **Edit**.
5. Enable static website hosting.
6. Choose **Host a static website**.
7. Set the index document to `index.html`.
8. Save the configuration.

Copy the generated S3 website endpoint.

Configure the required bucket permissions if the website needs to be publicly accessible.


### Step 8: Test the Serverless Web Application

1. Open the S3 static website endpoint in a browser.
2. Verify that the webpage loads successfully.
3. Click the **Description** button.
4. JavaScript sends an HTTP GET request to API Gateway.
5. API Gateway invokes the Lambda function.
6. Lambda executes the Python backend code.
7. The response is returned to the frontend.
8. Verify that the response is displayed on the webpage.

If the request fails, check API Gateway integration, Lambda permissions, CORS configuration, and CloudWatch logs.

## 6. Project Structure

```text
aws-serverless-web-application/
│
├── README.md
│
├── lambda_function.py
│
├── index.html
│
└── screenshots/
    ├── 01_lambda_configuration.png
    ├── 02_api_gateway.png
    ├── 03_s3_bucket_objects.png
    ├── 04_s3_static_website_hosting.png
    ├── 05_website_initial_output.png
    └── 06_website_description_response.png
```

## 7. Expected Output

The deployed application displays a simple webpage titled:

**Serverless Web-Application**

When the user clicks the Description button, the application sends an HTTP request to API Gateway, which invokes the Lambda function and returns the backend response.

## 8. Key Concepts Learned

Through this project, the following AWS and cloud computing concepts are demonstrated:

- Amazon S3 static website hosting.
- Serverless application architecture.
- AWS Lambda function creation and deployment.
- Python-based backend execution.
- API Gateway and Lambda integration.
- HTTP GET request handling.
- Frontend and backend communication.
- CORS configuration.
- AWS resource configuration and deployment.
- Basic troubleshooting using CloudWatch logs.

## 9. Security Considerations

- Avoid uploading AWS access keys, secret keys, or credentials to GitHub.
- Use placeholder values for API endpoints in publicly shared source code.
- Configure S3 bucket permissions carefully.
- Restrict CORS to trusted origins in production.
- Monitor Lambda execution and API requests.
- Apply the principle of least privilege to IAM permissions.

**Important:** API Gateway invoke URLs are not secret credentials. A placeholder is used in this repository so that other users can configure their own endpoint when reproducing the project.

## 10. Future Improvements

The project can be extended with additional AWS services and features:

- Amazon DynamoDB for persistent data storage.
- AWS IAM policies for more granular access control.
- Amazon CloudWatch for monitoring and logging.
- AWS WAF for additional web application protection.
- Amazon CloudFront for HTTPS delivery and content distribution.
- Infrastructure as Code using AWS CloudFormation or Terraform.

These are potential future enhancements and are not part of the current implementation.

## 11. Conclusion

This project demonstrates how Amazon S3, AWS Lambda, and Amazon API Gateway can be integrated to develop and deploy a basic serverless web application.

By separating frontend hosting from backend execution, the application uses managed AWS services without requiring a dedicated server.

The project provides practical exposure to AWS cloud services, serverless architecture, API integration, and frontend-backend communication.

---

