import tweepy
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

auth = tweepy.OAuthHandler('1PLmPG8s1d8jScK2DyRqv0sgx', 
                    'QicuSp6rhAYXzjaFiPSA3aOCywNqLyZoU9le7uqKi7VE5CAktX')

auth.set_access_token('312459843-1ZtMFPm9P3AbhiTjAqKuFKf4dCZEOqW7xO7IST12',
                    'p5mcfeNuXZ8wSzknNbezGBAqHnIQHJyZgBdw9BcaOB68o')

api = tweepy.API(auth)

link = input("Enter the tweet link: ")
tweet_id = int(link.split('/')[-1])
tweet = api.get_status(tweet_id, tweet_mode="extended")

variants = tweet._json['extended_entities']['media'][0]['video_info']['variants']

table = Table(show_header=True,header_style="bold magenta",show_lines=True)
table.add_column("URL",style="dim")
table.add_column("Bitrate")
table.add_column("Dimensions",justify='right')

for variant in variants:
    try:
        bitrate = variant['bitrate']
        url = variant['url']
        dimensions = url.split('/')[-2]
    except KeyError:
        continue
    table.add_row(f"{url}", f"{bitrate}", f"{dimensions}")

console.print(table)