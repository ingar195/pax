
from pycalima.Calima import Calima
import logging
import json


def get_state(fan):
    state = fan.getState()
    return state


def read_config(file="config.json"):
    import json
    with open(file, "r") as f:
        config = json.load(f)
    return config


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

    logging.debug(f"State: {state}")
    logging.debug(f"type: {type(state)}")

    humidity = state[0]
    light = state[1]
    temp = state[2]
    rpm = state[3]
    mode = state[4]

    logging.debug(f"Humidity: {humidity}")
    logging.debug(f"Light: {light}")
    logging.debug(f"Temp: {temp}")
    logging.debug(f"RPM: {rpm}")
    logging.debug(f"Mode: {mode}")

    fan.disconnect()
