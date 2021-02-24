import praw
import keyboard

reddit = praw.Reddit(
    client_id="id_goes_here",
    client_secret="secret_goes_here",
    user_agent="Make_here", #Format in {Botname (creator name)} - example; 'HelloBot (by u/fakeaccount)'
    username="Bot_account_name", #The bot's account, not yours
    password="Bot_account_password" #The bot's password, not yours
)

try:
    print(f'Authenticated as {reddit.user.me()}!')
except:
    print('Something went wrong :(')

trigger = ['hello', 'hi'] #add trigger (keywords) here. Seperate with comma 
subreddits = 'anime + cats + askreddit' #Seperate communities with a plus sign. Don't add r/ in front of community name.
max_character = 50 #Max character limit (Optional). Usefult to avoid disrupting discussions.
cooldown = 18000 #A cooldown town between responses (Optional, but recommended). Useful to not make the bot seem spammy. Value is in seconds.

reply = '''

Custom response goes here.

^This ^comment ^was ^made ^by ^a ^bot. 

'''

for comment in reddit.subreddit(subreddits).stream.comments(skip_existing = True):
    if any(keyword in comment.body for keyword in trigger):
        if len(comment.body) <= max_character:
            print(comment.body)
            comment.reply(reply)
            time.sleep(cooldown)
