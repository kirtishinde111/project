## Overview

This Django project provides a web interface for uploading, processing, and visualizing CSV files. Users can upload CSV files, process them to view basic statistics, and visualize data through histograms.

## Prerequisites

1- Python 3.x
- Django 4.x
- Other Python libraries (listed in `requirements.txt`)

## Setup Instructions

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

3. Install Dependencies/
Install the required Python packages:
pip install -r requirements.txt

4. Run migrations to set up the database:
python manage.py migrate

5. Create a superuser to access the Django admin site:
python manage.py createsuperuser

6. Start the Django development server:
python manage.py runserver

7. Access the Application.
Open your web browser and navigate to:
http://127.0.0.1:8000/
You should see the home page of your Django application.

# Explanation :
The Data Analysis Web Application is a Django-based tool designed for handling and visualizing CSV files. The application provides a user-friendly interface for managing data analysis tasks through a web browser.

Key Features:
File Uploading: Users can upload CSV files to the application. The system supports various CSV formats and ensures that files are securely saved for further processing.

File Processing: Once a file is uploaded, users can process it to extract useful information:

Summary Statistics: Displays statistical summaries such as mean, median, standard deviation, and other descriptive statistics.
First Rows: Shows the first few rows of the dataset to give users a preview of the data.
Missing Values: Lists columns with missing values along with the count of missing entries.
Data Visualization: Users can generate histograms for numerical columns in the dataset. This feature helps in understanding the distribution of data and identifying patterns or outliers.

File Management: Users can view a list of uploaded files with options to process, visualize, or delete them. This allows for easy management of multiple files and data sets.


