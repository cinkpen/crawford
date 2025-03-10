import pynmea2

# Example NMEA sentence with a potential checksum error
nmea_sentence = "$GPGSVTG,46.59,T,,M,0.28,N,0.52,K,N*1F"

def parse_nmea_sentence(sentence):
    try:
        msg = pynmea2.parse(sentence)
        print(f"Parsed message: {msg}")
        print(f"Latitude: {msg.latitude}")
        print(f"Longitude: {msg.longitude}")
    except pynmea2.ChecksumError as e:
        print(f"Checksum error: {e}")
    except pynmea2.ParseError as e:
        print(f"Parse error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Simulate receiving NMEA sentences from the PA1010D GPS module
nmea_sentences = [
    "$GPGSA,A,1,,,,,,,000,,,,,0,0,,,M,,M,,*5",
    "$GPGSVTG,46.59,T,,M,0.28,N,0.52,K,N*1F",
    "$GPGGA,181908.00,3404.7041778,N,07044.3966270,W,4,13,1.00,495.144,M,29.200,M,0.10,0000*40"
    # Add more NMEA sentences here for testing
]

for sentence in nmea_sentences:
    print(f"Raw NMEA sentence: {sentence}")
    parse_nmea_sentence(sentence)