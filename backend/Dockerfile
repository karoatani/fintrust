# start from a base image
FROM python:3.10.0-alpine

EXPOSE 8000

# Create new user with home directory and group
RUN addgroup app && adduser -S -G app app

# Set the user app to be the current user 
USER app



WORKDIR /app/backend

# COPY FILE FROM CURRENT DIRECTORY TO CONTAINER DIRECTORY
COPY . .



# INSTALL APPLICATION DEPENDENCIES
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir


# START APPLICATION
ENTRYPOINT ["/app/backend/run.sh"]