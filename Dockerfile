# use Python image
FROM python:3.9-slim

# Set Working directory
WORKDIR /app

# copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# run app
CMD [ "python", "app.py" ]
