docker run -d --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto:latest
source venv/bin/activate
docker build -t litter -t cinkpen/litter:latest .

docker run --rm -it --device /dev/i2c-1:/dev/i2c-1 cinkpen/litter:latest