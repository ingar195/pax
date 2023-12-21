from pycalima.Calima import Calima
import logging


def read_config(file="config.json"):
    import json
    with open(file, "r") as f:
        config = json.load(f)
    return config


def get_state(fan):
    state = fan.getState()
    humidity = state[0]
    light = state[1]
    temp = state[2]
    rpm = state[3]
    mode = state[4]

    state = {
        "humidity": humidity,
        "light": light,
        "temp": temp,
        "rpm": rpm,
        "mode": mode
    }
    logging.info(f"humidity: {humidity}")
    logging.info(f"light: {light}")
    logging.info(f"temp: {temp}")
    logging.info(f"rpm: {rpm}")
    logging.info(f"mode: {mode}")

    return state

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%d-%m-%Y:%H:%M:%S',
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler("log.log"),
            logging.StreamHandler()
        ])

    config = read_config()
    fan = Calima(config["mac"], config["pin"])
    state = get_state(fan)

    fan.disconnect()
