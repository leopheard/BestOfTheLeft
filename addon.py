from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

URL1 = "https://hippiesympathizer.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://spotlight.radiopublic.com/images/thumbnail?url=http%3A%2F%2Fstatic.libsyn.com%2Fp%2Fassets%2Fa%2F7%2Fa%2Fa%2Fa7aad30e2da4890d%2FBotL_Scaled_up_Portrait_Logo.jpg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://spotlight.radiopublic.com/images/thumbnail?url=http%3A%2F%2Fstatic.libsyn.com%2Fp%2Fassets%2Fa%2F7%2Fa%2Fa%2Fa7aad30e2da4890d%2FBotL_Scaled_up_Portrait_Logo.jpg"},
    ]

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast = mainaddon.get_playable_podcast(soup)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items


if __name__ == '__main__':
    plugin.run()
