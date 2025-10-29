
-----

# 🚲 Bike Sharing Demand Prediction API

This project provides a machine learning model to predict the hourly demand for bike rentals. It includes a Python script (`model.py`) to train a Random Forest Regressor model and a Flask web application (`app.py`) that serves this model via an API.

The entire application is containerized using Docker for easy setup, deployment, and scalability.

## 🌟 Features

  * **ML Model:** Predicts hourly bike rental counts using a Random Forest Regressor.
  * **Web API:** A Flask server to handle prediction requests from a web interface.
  * **Data Preprocessing:** Includes robust preprocessing (outlier removal, one-hot encoding, feature scaling) that is saved and applied consistently during training and inference.
  * **Containerized:** Comes with a `Dockerfile` for building and running the application in an isolated environment.

## 🛠️ Technologies Used

  * **Backend:** Flask
  * **ML / Data Science:** Scikit-learn, Pandas, NumPy
  * **Containerization:** Docker
  * **Base Image:** `python:3.10-slim`

## 📁 Project Structure

```
.
├── app.py             # Main Flask application logic
├── model.py           # Model training script
├── Dockerfile         # Docker configuration
├── requirements.txt   # Python dependencies
├── model.pkl          # Serialized (pre-trained) ML model
├── scaling.pkl        # Serialized (pre-fitted) StandardScaler
│
├── image_06ec1c.png   # Screenshot 1: Web UI
├── image_3d6d66.png   # Screenshot 2: Terminal/Docker logs
│
├── hour.csv           # (Required for training - NOT INCLUDED)
└── templates/
    └── index.html     # Web interface for the API
```


1.  **`hour.csv`**: This dataset is required to run `model.py`. You can download it from the [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset).

-----

## 🚀 Running the Application

There are two ways to run this project: using Docker (recommended) or setting it up locally.

### 1\. Running with Docker (Recommended)

1.  **Build the Docker image:**
    Open your terminal in the project's root directory and run:

    ```sh
    docker build -t bike-predictor .
    ```

2.  **Run the Docker container:**
    This command maps port 5000 on your local machine to port 5000 inside the container.

    ```sh
    docker run -p 5000:5000 bike-predictor
    ```

3.  **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

### 2\. Running Locally (Without Docker)

1.  **Clone the repository:**

    ```sh
    git clone <your-repo-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    The `requirements.txt` file lists all necessary packages.

    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    The `app.py` file is configured to run in debug mode.

    ```sh
    python app.py
    ```

5.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000`.

-----

## 📸 Application in Action

<img width="698" height="708" alt="Screenshot 2025-10-29 133050" src="https://github.com/user-attachments/assets/2eff201a-de2b-4222-9b00-6c079de99601" />

Here is a look at the running application.

### Web Interface & Prediction

This screenshot shows the web form and the output after a successful prediction.

### Terminal Output

This screenshot shows the Docker build and run commands, as well as the server logs confirming that the application is running and handling `GET` and `POST` requests.

-----

## 🧠 Retraining the Model

If you want to retrain the model (e.g., with new data or different parameters), follow these steps:

1.  **Add the data:**
    Make sure you have downloaded the `hour.csv` file and placed it in the root directory.

2.  **Install dependencies:**
    If you haven't already, install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the training script:**

    ```sh
    python model.py
    ```

This script will perform all preprocessing, train a new `RandomForestRegressor`, and overwrite the existing `model.pkl` and `scaling.pkl` files with the new versions.

## 📋 API Endpoint

  * **Endpoint:** `/`

      * **Method:** `GET`
      * **Description:** Renders the main `index.html` page for user input.

  * **Endpoint:** `/predict`

      * **Method:** `POST`
      * **Description:** Receives user input from the web form, preprocesses it, and returns the prediction.
      * **Form Data:**
          * `atemp`: (float) "Feels like" temperature
          * `hum`: (float) Humidity
          * `windspeed`: (float) Wind speed
          * `holiday`: (int) 0 (No) or 1 (Yes)
          * `workingday`: (int) 0 (No) or 1 (Yes)
          * `season`: (int) 1 (Spring), 2 (Summer), 3 (Fall), 4 (Winter)
          * `yr`: (int) 0 (Year 1) or 1 (Year 2)
          * `mnth`: (int) 1 (Jan) to 12 (Dec)
          * `hr`: (int) 0 to 23
          * `weekday`: (int) 0 (Sun) to 6 (Sat)
          * `weathersit`: (int) 1 (Clear) to 4 (Heavy Rain/Snow)
      * **Response:**
        Renders the `index.html` template again, this time displaying the prediction (e.g., `Predicted Hourly Rentals: 135`).
