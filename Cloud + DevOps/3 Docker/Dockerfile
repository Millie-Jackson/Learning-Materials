# Specify image:tag
FROM python:latest

# Run a bash command
RUN mkdir /mydirectory

# Set the current working directory
WORKDIR /mydirectory

# Copy data from docker context
COPY main.py .

# When we run the container this will be the command
ENTRYPOINT ["python3", "main.py"]