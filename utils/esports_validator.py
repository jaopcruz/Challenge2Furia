# simulacao de validacao de perfis de esports
def validate_esports_profile(profile_url, user_email):
    # em uma implementação real, isso verificaria o perfil em plataformas específicas
    # como no exemplo: FaceIT
    
    return {
        'valid': True,
        'platform': 'FURIA' if 'furia' in profile_url.lower() else 'Other',
        'account_age': '2 years',  # Simulação
        'activity': 'active',      # Simulação
        'matches_identity': True   # Simulação
    }