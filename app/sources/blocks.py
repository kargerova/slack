ticket_input_block = [
    # Header
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "New ticket", "emoji": True},
    },
    # Ticket type select
    {
        "type": "input",
        "block_id": "ticket_type",
        "element": {
            "type": "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Select ticket type",
                "emoji": True,
            },
            "options": [
                {
                    "text": {"type": "plain_text", "text": "Problem", "emoji": True},
                    "value": "problem",
                },
                {
                    "text": {"type": "plain_text", "text": "Change", "emoji": True},
                    "value": "change",
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "Service request",
                        "emoji": True,
                    },
                    "value": "service-request",
                },
            ],
            "action_id": "static_select-action-ticket_type",
        },
        "label": {"type": "plain_text", "text": "Type", "emoji": True},
    },
    # Ticket subject
    {
        "dispatch_action": True,
        "type": "input",
        "block_id": "ticket_subject",
        "element": {
            "type": "plain_text_input",
            "action_id": "plain_text_input-action-ticket_subject",
        },
        "label": {"type": "plain_text", "text": "Ticket subject", "emoji": True},
    },
    # Ticket_text
    {
        "type": "input",
        "block_id": "ticket_text",
        "element": {
            "type": "plain_text_input",
            "multiline": True,
            "action_id": "plain_text_input-action-ticket_text",
        },
        "label": {"type": "plain_text", "text": "Ticket text", "emoji": True},
    },
    # Submit button
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Submit", "emoji": True},
                "value": "btn-ticket_submit",
                "action_id": "actionId-ticket_submit",
            }
        ],
    },
]