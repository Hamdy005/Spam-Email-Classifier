Spam Email Classifier

A machine learning application built with Python and Streamlit to detect and classify emails as either "Spam" or "Ham" (Not Spam).

📋 Table of Contents

About

Prerequisites

Installation

Usage

Technologies Used

ℹ️ About

This project uses Natural Language Processing (NLP) techniques to analyze the content of emails. Users can input email text directly into the web interface, and the model will predict whether the message is legitimate or spam based on trained patterns.

🛠️ Prerequisites

Python 3.8 or higher

pip (Python package installer)

🚀 Installation

Follow these steps to set up the project locally:

Clone the repository (if applicable) or navigate to your project folder:

cd path/to/spam-email-classifier


Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

Windows:

python -m venv venv


macOS / Linux:

python3 -m venv venv


Activate the Virtual Environment

Windows:

.\venv\Scripts\activate


macOS / Linux:

source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


💻 Usage

Once the installation is complete and your virtual environment is active, you can launch the application.

Run the Streamlit App:

streamlit run app.py


Access the Interface:
The application will automatically open in your default web browser. If it doesn't, navigate to the URL provided in the terminal (usually http://localhost:8501).

🧰 Technologies Used

Python: Core programming language.

Streamlit: For the web application interface.

Scikit-learn: For the machine learning model.

Pandas: For data manipulation.

NLTK/re: For text processing (if applicable).