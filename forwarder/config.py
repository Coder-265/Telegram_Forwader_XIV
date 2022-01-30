from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5293939339:AAE-CDplj_SQiipe1AUQnE7bCA6GKIeloME"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001767529378,-1001713522142,-1001715704828,-1001796119329,-1001612158871]# List of chat id's to forward messages from.
    TO_CHATS = [-1001766663366]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 32
   
    
