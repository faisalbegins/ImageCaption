# base image
FROM python:3.8.2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# create working directory
WORKDIR /app

# copy all the source files from current directory to docker
COPY . .

# expose port
EXPOSE 5000

# start the application
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

