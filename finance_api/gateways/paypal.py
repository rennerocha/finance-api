import logging

import requests
from dynaconf import settings
from fastapi import APIRouter, Request, Response, HTTPException, status


router = APIRouter()

logger = logging.getLogger(__name__)



def store_notification(ipn_message):
    ...


def paypal_handshake(ipn_message):
    logger.info("Notification received. Initiating IPN verification.")

    ipn_message["cmd"] = "_notify-validate"
    response = requests.post(settings.PAYPAL_VERIFY_IPN_URL, data=ipn_message)

    if response.text == "VERIFIED":
        store_notification(ipn_message)
    elif response.text == "INVALID":
        logger.error("Invalid message sent to Paypal.")



@router.post("/gateway/paypal")
async def paypal(request: Request):
    user_agent = request.headers.get("user-agent")
    if user_agent != settings.PAYPAL_REQUEST_USER_AGENT:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    form = await request.form()
    receiver_email = form.get("receiver_email")
    if receiver_email != settings.PAYPAL_ACCOUNT:
        logger.error("Received notification from invalid PayPal account.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    paypal_handshake(dict(form))

    return Response()
