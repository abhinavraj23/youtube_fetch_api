FROM python:3.6

# create root directory for our project in the container
RUN mkdir /youtube_fetch_api

# Set the working directory to /youtube_fetch_api
WORKDIR /youtube_fetch_api

# Copy the current directory contents into the container at /youtube_fetch_api
ADD . /youtube_fetch_api/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt