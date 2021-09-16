# Pyaudio Docker
To test pyaudio on AWS

## To test locally 
```
git clone https://github.com/rajashekar/pyaudio_docker.git
cd pyaudio_docker
docker build -t pyaudio_test .
docker run --publish 5000:5000 pyaudio_test
```
Verify by going to http://localhost:5000/ 

## To deploy in AWS Elastic Bean
First initialize app
```
eb init -p docker pyaudio_test --region us-west-2
```
Next create app & deploy
```
eb create pyaudio-test --instance_type t2.large --max-instances 1
```