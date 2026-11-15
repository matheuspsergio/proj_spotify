import spotipy
from spotipy.oauth2 import SpotifyOAuth


import os
from dotenv import load_dotenv

# Lê o arquivo .env e injeta as variáveis no ambiente do sistema
load_dotenv()

# Busca os valores usando o módulo 'os'
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

# Teste rápido para validar (apague o print depois)
print("ID carregado com sucesso:", client_id is not None)

# Define as permissões para ler artistas principais, faixas e histórico
SCOPE = 'user-top-read user-read-recently-played'

# Inicia a autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=SCOPE,
    cache_path='.spotify_cache'
))

'''# Extrai os 10 artistas mais ouvidos (médio prazo - últimos 6 meses)
print("--- Seus Top 10 Artistas ---")
top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')
for i, artist in enumerate(top_artists['items']):
    print(f"{i + 1}. {artist['name']}")

# Extrai as 10 faixas mais ouvidas (médio prazo - últimos 6 meses)
print("\n--- Suas Top 10 Faixas ---")
top_tracks = sp.current_user_top_tracks(limit=10, time_range='medium_term')
for i, track in enumerate(top_tracks['items']):
    print(f"{i + 1}. {track['name']} - {track['artists'][0]['name']}")'''

# Extrai as últimas 5 músicas reproduzidas
print("\n--- Tocadas Recentemente ---")
recent = sp.current_user_recently_played(limit=10)

for i, item in enumerate(recent['items']):
    track = item['track']
    print(f"{i + 1}. {track['name']} - {track['artists'][0]['name']}")