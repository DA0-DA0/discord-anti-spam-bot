# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot files
COPY bot.py .
COPY config.py .

# Create a non-root user for security
RUN adduser --disabled-password --gecos "" bot
RUN chown -R bot:bot /app
USER bot

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "bot.py"]