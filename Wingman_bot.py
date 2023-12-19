import discord
import random
from discord.ext import commands


pick_up_lines = [
    "When I send your pic to my group chat, which one would you like me to use?",
    "When your parents made you, they were really just showing off.",
    "I know your name is [insert their name], but can I call you mine?",
    "Do you believe in love at first sight, or do you need to look at my profile again?",
    "Aside from being this good-looking, what else do you do in your free time?",
    "I don’t believe in love at first sight, but you have me considering love at first swipe.",
    "I’d say bless you, but it looks like you already have been.",
    "Do you have a map? I just got lost in your eyes.",
    "My mom told me not to talk to strangers online, but I’ll make an exception for you",
    "Something’s wrong with my eyes because I can’t take them off of you.",
    "Well, here I am! What are your other two wishes?",
    "They say dating is a numbers game, so can I get yours?",
    "Are you a magician? ‘Cuz when I look at you, everyone else disappears.",
    "Do you know what the Little Mermaid and I have in common? We both want to be a part of your world.",
    "I’d like to take you to the movies, but they don’t let you bring in your own snacks.",
    "Titanic? That’s my icebreaker. What’s up?",
    "I hope you know CPR ‘cuz you just took my breath away!",
    "I’m going to complain to Spotify about you not being in this week’s hottest singles.",
    "I am not a photographer, but I can easily picture us together.",
    "Kiss me if I’m wrong, but dinosaurs still exist, right?",
    "Hey, you’re pretty and I’m cute. Together we’d be pretty cute.",
    "I would flirt with you, but I’d rather seduce you with my awkwardness.",
    "I usually go for 8s but I guess I’ll settle for a 10.",
    "Are you https? ‘Cuz without you I’m just ://",
    "Do you like Mexican food? ‘Cuz I want to wrap you up and make you my Bae-ritto.",
    "Truth or date?",
    "Hi, I’m Mrs. Right. Someone said you were looking for me?",
    "You don’t know how many times I’ve had to swipe left to find you.",
    "When our friends ask us how we met, what are we going to tell them? Funny answers only.",
    "If you could be anywhere in the world, doing anything you wanted, where would we be?",
    "I don’t know how this works. Are we married now?",
    "Hey, I’m writing an article on the finer things in life and was hoping I could interview you.",
    "Not to be cheesy, but oh my god you’re gorgeous!",
    "My sweet tooth has been driving me crazy since the second I saw your profile!",
    "I had this awesome pickup line, but I forgot it the moment I laid eyes on you.",
    "I tripped while looking at you. I guess you owe me a new pair of shoes.",
    "I had the best pickup line on the way, but I saw you and now I'm speechless.",
    "If you were a fruit, you’d be a fineapple. Ba dum tss.",
    "I assumed happiness started with an ‘H’ but I believe it actually starts with ‘U.’",
    "Are you my appendix? ‘Cuz this feeling in my stomach makes me want to take you out.",
    "On a scale of 1 to 10, you’re a 9, and I’m the 1 you need.",
    "Are you a fruit ‘cuz we could make a great pear.",
    "Are you a time traveler? ‘Cuz I see you in my future.",
    "Do you like bagels? Because you’re bae goals.",
    "Roses are red, violets are blue, how did I get so lucky to match with you?",
    "Do you watch Star Wars? Because Yoda only one for me.",
    "Hi, my name is [insert your name], but you can call me tonight or tomorrow.",
    "I’m no organ donor but I’d be happy to give you my heart.",
    "Are you a bank loan? ‘Cuz you have my interest.",
    "Life without you is like a broken pencil… pointless.",
    "Are you religious? ‘Cuz you’re the answer to all of my prayers.",
    "I must be in a museum because you truly are a work of art.",
    "Let’s commit the perfect crime. I’ll steal your heart, you steal mine.",
    "Even if there was no gravity on Earth, I’d still fall for you.",
    "They say nothing lasts forever, so will you be my nothing?",
    "Well, you’re the sweetest thing I’ve seen in a while on this app. Hello there!",
    "Are you an archaeologist ‘cuz you dug up a hole in my heart.",
    "Coffee, tea, or sushi?",
    "You have one of the most beautiful faces I’ve seen in a long, long time.",
    "Do you know how to train butterflies? The ones in my stomach right now are quite untamed.",
    "Swiped for the dog, stayed for the human.",
    "I’m trying to think of something to say, but all I can think about is how cute you are.",
    "I’d give up my morning cereal to spoon you instead.",
    "It looks like I’ve lost my phone number. Could I get yours instead?",
    "You swiped right, I swiped right, should we establish we’re not serial killers first or can we proceed to date right away?",
    "No pen, no paper… but you still ‘draw’ my attention.",
    "I’m researching important dates in history. Would you like to be mine?",
    "Damn, you have a dog! Does that mean I’ll never win the ‘best cuddler ever’ title?",
    "I’m not an electrician, but I can light up your day.",
    "I know we’re not socks, but I’m sure we’d make a great pair.",
    "I think someone must have stolen the stars and put them in your eyes.",
    "Are you good at algebra? ‘Cuz I’d like you to replace my X without asking Y.",
    "Oh, by the way, I’m wearing that smile you gave me.",
    "Do you have a pencil? ‘Cuz I want to erase your past and write our future.",
    "You know those gaps between your fingers? I think they were made for mine.",
    "Mind if I tie your shoes? I’d hate to see you falling for anyone else.",
    "You make my Spidey Sense tingle.",
    "Saw you’re a foodie, I know a few things you could taste.",
    "Are you as good at cuddling as you are good-looking? If so, when can I get a cuddle?",
    "Want to help me get on Santa’s naughty list this year?",
    "You look like you know how to have a good time! I like it.",
    "Your lips look lonely. Would they like to meet mine?",
    "I know you’re busy, but please add me to your list of things to do.",
    "I’ve heard it said that kissing is the ‘language of love.’ Would you care to have a conversation with me about it sometime?",
    "If you let me borrow a kiss, I promise I’ll give it right back.",
    "When I make you breakfast in the morning, what would you like?",
    "I just bought kiss-proof lipstick, and I need a lab partner to test its claims. Are you in?",
    "If I told you that you had a great body, would you hold it against me?",
    "I love my bed, but I’d rather be in yours.",
    "They say the human body is 70 percent water… I’m feeling pretty thirsty.",
    "Dinner first, or can we go straight for dessert?",
    "Damn, if being sexy was a crime, you’d be guilty as charged!",
    "My name isn’t Elmo, but you can tickle me any time you want.",
    "That shirt looks great on you… as a matter of fact, so would I.",
    "If you look that good in clothes, you must look even better out of them.",
    "Complete this sentence: “You, me, and ____.”",
    "I’ve been wondering, do your lips taste as good as they look?",
    "I’m not feeling myself today. Can I feel you instead?",
    "Do you like sleeping? Me too. We should do it together some time.",
    "Choose: Your place or mine?"
]

active_conversations = {}

intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True  
intents.guilds = True  
intents.members = True 

client = commands.Bot(command_prefix='!', intents=intents)
TOKEN = ''  #ADD TOKEN

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(name='pickupline', help='Get a pick-up line!')
async def pickupline(ctx, target: discord.Member):
    response = f'{target.mention}, {random.choice(pick_up_lines)}'
    await ctx.send(response)

@client.command(name='sendpickup', help='Send an anonymous pick-up line!')
async def sendpickup(ctx, target: discord.Member):
    
    conversation_id = f'{ctx.author.id}-{target.id}'

    
    response = f'{target.mention}, {random.choice(pick_up_lines)}'
    await target.send(response)

    
    active_conversations[conversation_id] = ctx.author.id

    await ctx.send(f"Conversation started with {target.mention}. You can now send and receive messages with them.")

@client.event
async def on_message(message):
   
    if message.author.id != client.user.id and message.content.startswith('!') and str(message.author.id) in active_conversations.values():
       
        conversation_id = [key for key, value in active_conversations.items() if str(value) == str(message.author.id)][0]

       
        target_user_id = conversation_id.split('-')[1]

  
        target_user = await client.fetch_user(target_user_id)


        await target_user.send(f"Message from {message.author.mention}: {message.content}")

    await client.process_commands(message)

@client.command(name='stop', help='End the current conversation session.')
async def stop(ctx):

    conversation_id = [key for key, value in active_conversations.items() if str(value) == str(ctx.author.id)][0]


    target_user_id = conversation_id.split('-')[1]


    target_user = await client.fetch_user(target_user_id)


    await target_user.send(f"Conversation ended. Last message: {ctx.message.content}")


    del active_conversations[conversation_id]

    await ctx.send("Conversation ended. You can start a new conversation with !sendpickup.")

client.run(TOKEN)
