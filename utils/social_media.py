# simulacao
def get_social_media_data(profiles):
    #em uma implementação real, isso usaria APIs oficiais (Twitter API, Facebook Graph API, etc.)
    
    results = {}
    for platform, url in profiles.items():
        if url:
            results[platform] = {
                'url': url,
                'follows_esports': True,  # Simulação
                'activity_level': 'high', # Simulação
                'teams_followed': ['FURIA', 'LOUD'] if platform in ['twitter', 'facebook'] else []
            }
    return results