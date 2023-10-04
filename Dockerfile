FROM python



WORKDIR /code


COPY . .


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN python manage.py makemigrations
RUN python manage.py migrate