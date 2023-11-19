# MetricsCentral HitchHiker API

This README outlines the steps to set up and run the Flask application both locally using a Python virtual environment and with Docker using Caddy as a reverse proxy.

## Local Setup with Virtualenv

### Prerequisites

- Python 3.x
- pip
- virtualenv

### Setting Up the Environment

1. **Clone the Repository**

   ```
   git clone <repository-url>
   cd <repository-name>/server
   ```

2. **Create and Activate Virtual Environment**  
   For Windows:

   ```
   virtualenv env
   .\env\Scripts\activate
   ```

   For macOS and Linux:

   ```
   virtualenv env
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```
   python app.py
   ```

5. **Access the Application**  
   Open `http://localhost:5000` in your web browser.

6. **Deactivate the Virtual Environment**  
   When you're done, you can deactivate the virtual environment:

   ```
   deactivate
   ```

## Docker & Caddy Setup

### Prerequisites

- Docker
- Docker Compose

### Running with Docker Compose

1. **Build and Run with Docker Compose**

   Create the Docker network used by the OpenWRT machine and other common containers.

   ```bash
   docker network create hitchnet
   ```

   Build the Docker image and run the container:

   ```bash
   docker-compose up --build
   ```

2. **Access the Application**  
   The Flask application is accessible via `https://localhost`.

### Caddy Configuration

- Caddy is configured to automatically handle HTTPS for local development.
- The configuration can be found and adjusted in the `Caddyfile`.
