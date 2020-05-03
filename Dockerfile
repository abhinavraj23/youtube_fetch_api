FROM django
ADD . /youtube_fetch_api
WORKDIR /youtube_fetch_api
RUN pip install -r requirements.txt
CMD [ "python", "./manage.py runserver 0.0.0.0:8001" ]