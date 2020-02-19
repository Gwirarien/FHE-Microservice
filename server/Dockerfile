# Use an official Python runtime as an image
FROM python:3.7.4-stretch

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Runt the command to start uWSGI
CMD [ "uwsgi", "app.ini" ]

# Run app.py when the container launches
# CMD python app/main.py