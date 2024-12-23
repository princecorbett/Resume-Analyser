# Job Matching and Candidate Analysis System Expert 
This document provides detailed instructions for setting up and running the Job Matching and Candidate Analysis System Expert application. Follow the steps below to ensure the system operates effectively.

# Table of Contents
Prerequisites
Software Requirements
Hardware Requirements

### Setup Instructions ###
#### Step 1: Clone the Repository
#### Step 2: Create a Virtual Environment
#### Step 3: Install Dependencies
#### Step 4: Configure Environment Variables
#### Step 5: Run the Application


# Dependencies
Troubleshooting
Prerequisites
1. Software Requirements
-- Python: Version 3.10 or above.


## Setup Instructions
# Step 1: Clone the Repository
Open a terminal or command prompt.
Navigate to the directory where you want to clone the project.
Run the following commands:

git clone (https://github.com/princecorbett/Resume-Analyser.git)

cd ats-resume-expert

# Step 2: Create a Virtual Environment
Using a virtual environment is highly recommended to manage dependencies effectively.

## Create a virtual environment:
python -m venv venv

Activate the virtual environment:

Windows:
conda activate ./venv/

Mac/Linux:
source venv/bin/activate

# Step 3: Install Dependencies

Install the required Python libraries listed in the requirements.txt file:
pip install -r requirements.txt

# Step 4: Configure Environment Variables

Create a .env file in the root directory of the project:
touch .env

Add your Google API key to the .env file in the following format:
GOOGLE_API_KEY=your-google-api-key-here

Save the .env file.

# Step 5: Run the Application

Start the Streamlit application by running:
streamlit run app.py

The application will launch in your default web browser.

If it doesn’t open automatically, navigate to the URL displayed in the terminal (e.g., http://localhost:8501).

## Dependencies
The project uses the following Python libraries:

Streamlit 

pdfplumber

Pillow

dotenv

google-generativeai 
