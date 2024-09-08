
# Dockerized Weather App with Cloud Run and CI/CD

This project is a weather application built with Flask that provides real-time weather updates. It is containerized using Docker and deployed on Google Cloud Run for scalable and efficient cloud-based execution. The application also features an automated CI/CD pipeline through Google Cloud Build, ensuring seamless integration and deployment.




## Technologies Used

This project utilizes the following technologies and tools:

1. Flask: A lightweight Python web framework used to build the weather application.
2. Docker: Containerization platform used to create and manage the application's Docker images.
3. Google Artifact Registry: Managed Docker container registry for storing and managing Docker images.
4. Google Cloud Run: Serverless platform for deploying and scaling containerized applications.
5. Google Cloud Build: Continuous Integration/Continuous Deployment (CI/CD) service for automating the build and deployment processes.
6. GitHub: Version control system for source code management and integration with Google Cloud Build.
## Workflow Diagram



![Untitled](https://github.com/user-attachments/assets/2ac2b4fd-3749-4dfc-a8c6-77ac55b027b7)

## GitHub:

Role: Source code repository.

Function: Hosts the Flask weather app's source code. Any changes or updates to the code are pushed here.

## Google Cloud Build:
Role: CI/CD service.

Function: Monitors the GitHub repository for changes. When code changes are detected, Cloud Build automatically triggers a build process.

## Docker:

Role: Containerization platform.

Function: Cloud Build uses Docker to build a container image of the Flask app based on the Dockerfile. This image encapsulates the app and its dependencies.

## Google Artifact Registry:

Role: Container registry.

Function: Stores the Docker image built by Cloud Build. This registry manages and provides access to the Docker images.

## Google Cloud Run:

Role: Serverless compute platform.

Function: Deploys and runs the Docker container image from Artifact Registry. Cloud Run handles scaling and managing the application based on incoming traffic.
## How it works

1. Development: You develop and test your Flask app locally.
2. Dockerization: You create a Docker image of your app to ensure consistent environments.
3. Push to Artifact Registry: You upload the Docker image to Google Artifact Registry.
4. Deploy to Cloud Run: The Docker image is deployed to Google Cloud Run, where it runs in a serverless environment.
5. Automate CI/CD with Cloud Build: Any changes in your GitHub repository trigger Cloud Build to rebuild and redeploy your app automatically.
6. Update in Cloud Run: Cloud Run receives the updated Docker image and redeploys it, ensuring your app is always up-to-date with the latest code changes.
## Continuous Integration and Deployment (CI/CD)

This project uses Google Cloud Build for CI/CD automation. Whenever changes are pushed to the GitHub repository, Cloud Build automatically triggers a pipeline to:

1. Build a Docker image of the Flask weather app.
2. Push the Docker image to Google Artifact Registry.
3. Deploy the updated image to Google Cloud Run.
## Conclusion

This Flask-based weather application, containerized with Docker and deployed on Google Cloud Run, provides a scalable and efficient solution for real-time weather updates. The automated CI/CD pipeline using Google Cloud Build simplifies the process of integrating and deploying code changes.
