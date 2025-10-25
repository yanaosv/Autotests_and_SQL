import configuration
import requests

def post_courier(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER,
                         json=body)

def post_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_ORDERS,
                        params={"t": track_number})