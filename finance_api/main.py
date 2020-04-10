from fastapi import FastAPI

from .gateways import paypal


def get_application():
    application = FastAPI()

    application.include_router(paypal.router)

    return application


app = get_application()