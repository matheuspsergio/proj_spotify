import json
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Lê o arquivo .env e injeta as variáveis no ambiente do sistema
load_dotenv()

# Busca os valores usando o módulo 'os'
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

output_dir = Path("data/raw")

def extract_recent_tracks(limit: int = 50) -> str:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-read-recently-played",
        cache_path='.spotify_cache'
    ))

    # 1. Busca o payload bruto completo na API
    recent_tracks = sp.current_user_recently_played(limit=limit)

    # 2. Gera um nome único com timestamp (ex: recent_tracks_20261117_215300.json)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"recent_tracks_{timestamp}.json"

    # 3. Salva o JSON bruto preservando acentos (ensure_ascii=False)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(recent_tracks, f, ensure_ascii=False, indent=4)

    print(f"Extração concluída: {file_path}")
    return str(file_path)

if __name__ == "__main__":
    extract_recent_tracks()