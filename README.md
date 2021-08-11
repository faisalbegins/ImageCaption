### Build recommender api server
docker build . --tag faisalbegins/imagecaption-api:latest

### Run recommender api server
docker run -it  -v /Users/Faisal/Laboratory/imagecaption-data:/mnt --env DATA_ROOT_DIR='/mnt' -p 5000:5000 faisalbegins/imagecaption-api:latest
