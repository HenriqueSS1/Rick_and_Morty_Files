import requests
import pandas as pd

def fetch_characters():
    base_url = "https://rickandmortyapi.com/api/character"
    characters = []

    current_page = 1
    while len(characters) < 50:
        response = requests.get(f"{base_url}?page={current_page}")
        if response.status_code != 200:
            print(f"Erro ao buscar dados: {response.status_code}")
            break

        data = response.json()
        results = data.get("results", [])

        for char in results:
            if len(characters) < 50:
                characters.append({
                    "id": char["id"],
                    "name": char["name"],
                    "status": char["status"],
                    "species": char["species"],
                    "type": char["type"],
                    "gender": char["gender"]
                })
            else:
                break

        current_page += 1

    return characters

def save_to_csv(characters, filename="rick_and_morty_50_personagens.csv"):
    df = pd.DataFrame(characters)
    df.to_csv(filename, sep=";", index=False)
    print(f"Arquivo salvo como {filename}")

if __name__ == "__main__":
    print("Buscando informações dos personagens...")
    characters = fetch_characters()
    print(f"Total de personagens buscados: {len(characters)}")
    save_to_csv(characters)
    print("Processo concluído!")