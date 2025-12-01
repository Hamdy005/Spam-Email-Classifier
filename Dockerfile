# 1. Use official Python image
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy project files
COPY . /app

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Download NLTK Data
RUN python -m nltk.downloader wordnet stopwords

# 7. Expose Streamlit Port
EXPOSE 8501

# 8. Run the Streamlit App
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
