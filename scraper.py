import twitter
api = twitter.Api(consumer_key='6GhjLPbZahCKk4gpLtFCa0XSh',
                      consumer_secret='Q1rPti2CMnEH555ZSUjTymg5KP1RAzi0PpKjjp0tXYNS27IP2K',
                      access_token_key='1259788333-dmMU7hlLFvT8z1dQDKKbjUHn3x4EQMo5QkY4tEY',
                      access_token_secret='uV4qboOa6QWcZbiojRIMaSrAJ5bowVOEnUiqpO2zeZWAJ',
                      cache=None)

print api.VerifyCredentials()