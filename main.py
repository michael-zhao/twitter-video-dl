from TwitterAPI import TwitterAPI
import json

api = TwitterAPI('1PLmPG8s1d8jScK2DyRqv0sgx', 'QicuSp6rhAYXzjaFiPSA3aOCywNqLyZoU9le7uqKi7VE5CAktX',
                    '312459843-1ZtMFPm9P3AbhiTjAqKuFKf4dCZEOqW7xO7IST12',
                    'p5mcfeNuXZ8wSzknNbezGBAqHnIQHJyZgBdw9BcaOB68o')

link = input("Enter the tweet link: ")
tweet_id = int(link.split('/')[-1])
tweet = api.request('statuses/show/:%d' % tweet_id)
tweet_dict = json.loads(tweet.text)
print(json.dumps(tweet_dict, indent=4, sort_keys=True))
#print(tweet_dict['extended_entities']['media'][0]['video_info']['variants'])

try:
    for variant in tweet_dict['extended_entities']['media'][0]['video_info']['variants']:
        try:
            bitrate = variant['bitrate']
            url = variant['url']
            dimensions = url.split('/')[-2]
        except KeyError as e:
            continue
        print(f"bitrate: {bitrate}, URL: {url}, dimensions: {dimensions}")
except KeyError as e:
    print("unable to find video address")