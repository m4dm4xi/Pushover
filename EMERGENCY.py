from chump import Application
app = Application('a9acbhw54uvnfxr7k7s91duexphdfs')
app.is_authenticated
user = app.get_user('ujm7395t6eg57jwrcyjycm4vzr1i1a')
user.is_authenticated, user.devices
message = user.create_message(
    title="What's up, dog?",
    message="hello",
    html=True,
    sound='intermission',
    priority=2
    )
message.is_sent, message.id
message.send()
message.is_sent, message.id, str(message.sent_at)
