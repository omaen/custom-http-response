FROM python:3.9-slim
LABEL authors="omaen"

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app/ .
# Set environment variables
ENV TEXT_OUTPUT "Hello, World!"
ENV TEXT_COLOR "black"
ENV BACKGROUND_COLOR "white"

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]