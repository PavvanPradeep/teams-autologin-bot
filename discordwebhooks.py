from discord_webhooks import DiscordWebhooks

webhook_url = 'place your discord webhook link here'


def send_msg(status, start_time, end_time):
    webhook = DiscordWebhooks(webhook_url)

    webhook.set_footer(text='-- Add your Name here')

    if status == "joined":

        webhook.set_content(title='Class Joined Successfully',
                            description="Report")

        # webhook.add_field(name='Class', value=class_name)
        webhook.add_field(name='Status', value=status)
        webhook.add_field(name='Joined at', value=start_time)
        webhook.add_field(name='Leaving at', value=end_time)

    elif status == "left":
        webhook.set_content(title='Class left Successfully',
                            description="Here's your report:")

        # webhook.add_field(name='Class', value=class_name)
        webhook.add_field(name='Status', value=status)
        webhook.add_field(name='Joined at', value=start_time)
        webhook.add_field(name='Left at', value=end_time)


    elif status == "no class":
        webhook.set_content(title='Seems like no class today',
                            description="No join button found no class.")

        # webhook.add_field(name='Class', value=class_name)
        webhook.add_field(name='Status', value=status)
        webhook.add_field(name='Expected Join time', value=status)
        webhook.add_field(name='Expected Leave time', value=end_time)

    webhook.send()

    print("Sent message to discord")
