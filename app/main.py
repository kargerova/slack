## Slack bot - creating ticket
## Author: Lenka Kargerova

import requests
from configuration import setting, logger
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from sources.blocks import ticket_input_block



# Initializing app
app = App(
    token=setting.SLACK_BOT_TOKEN,
    signing_secret=setting.SLACK_SIGNING_SECRET,
    logger= logger,
    name="k8s slackbot sister",
)


# Adding functionality
# @app.event("app_home_opened") etc
@app.command("/ticket")
def send_ticket_blocks(ack, say, logger):
    logger.info('ticket command called')
    ack("Let's create a shiny new ticket!")
    say(text="Add some info!", blocks=ticket_input_block)


@app.action("static_select-action-ticket_type")
def handle_some_action(ack, body, logger):
    ack()
    logger.info(body)


@app.action("actionId-ticket_submit")
def obtain_ticket_blocks(ack, say, body, logger):
    ack("Received ticket entry... ")
    try:
        user_name=body["user"]['username']
        ticket_type = body["state"]["values"]["ticket_type"][
            "static_select-action-ticket_type"
        ]["selected_option"]["value"]
        ticket_subject = body["state"]["values"]["ticket_subject"][
            "plain_text_input-action-ticket_subject"
        ]["value"]
        ticket_text = body["state"]["values"]["ticket_text"][
            "plain_text_input-action-ticket_text"
        ]["value"]

        logger.info(user_name, ticket_type, ticket_subject, ticket_text)
        say(text=':ticket: OK')
    except Exception as e:
        logger.error(e)
        say(text='Some error occured while processing :scream:')

    # Delete blocks from chat
    response=requests.post(
        url=body['response_url'],
        json={
            "replace_original": "true",
            "text": f"Thanks for your ticket request, <@{user_name}> we'll process it and get back to you."})
    logger.info(response)
    
        


# App start
def main():
    handler = SocketModeHandler(app, app_token=setting.SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
