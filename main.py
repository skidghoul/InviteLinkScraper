import requests, time, random, json, threading, art, gratient
import os

inviteScrapeJson = 'scrape/input/config.json'
inviteScrapeData =  json.load(open(inviteScrapeJson, 'r'))
invitesScraped   =  []

class DiscordServers:
      def __init__(self) -> None:
          pass

      def searchKeyword(self, keyWord, minimumSize = 30):
          return requests.get(
                              'https://search.discordservers.com/?term={}&size={}&from=0'.format(
                                       keyWord,
                                       minimumSize
                              ), headers = {
                                         'Host'     : 'search.discordservers.com',
                                         'Origin'   : 'https://discordservers.com',
                                         'Referer'  : 'https://discordservers.com/',
                              }
          ).json()

print(art.text2art('InviteScraper'))
while True:
      for keyWord in inviteScrapeData['scraperKeywords']:
          for guildData in DiscordServers().searchKeyword(keyWord, minimumSize = 150)['results']:
              if guildData['customInvite'] != None and guildData['customInvite'] not in invitesScraped:
                 if True:
                    print('[>] Scraped Invite Code: %s | Member Count: %s | Keyword: %s' % (gratient.red(str(guildData['customInvite'])).strip(), gratient.red(str(guildData['members'])).strip(), gratient.red(keyWord).strip()))
                          
                 open(inviteScrapeData['scraperPaths']['inviteCodes'], 'a+').write(f'{guildData["customInvite"]}\n')
                 open(inviteScrapeData['scraperPaths']['extraInfo'], 'a+').write(f'{guildData["customInvite"]}|{guildData["members"]}|{guildData["name"]}\n')
                 open(inviteScrapeData['scraperPaths']['inviteLinks'], 'a+').write(f'https://discord.gg/{guildData["customInvite"]}\n')
                 invitesScraped += [guildData['customInvite']]
              time.sleep(.35)
      time.sleep(5)
