docker run -d --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto:latest
source venv/bin/activate
docker build -t litter-gps-receiver -t cinkpen/litter-gps-receiver:latest .
docker push  cinkpen/litter-gps-receiver:latest

docker run --rm -it --device /dev/i2c-1:/dev/i2c-1 -e MQTT_BROKER=192.168.0.180 cinkpen/litter-gps-receiver:latest