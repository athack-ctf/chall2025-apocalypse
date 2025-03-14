# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /chall

COPY ./src /chall

# Installing Flask
RUN pip install Flask


# Set environment vars
ENV FLASK_APP=flag.py
ENV FLASK_RUN_PORT=80

# Expose the port that the chall will run on
EXPOSE 80

# Run the chall
CMD ["flask", "run", "--host=0.0.0.0"]
