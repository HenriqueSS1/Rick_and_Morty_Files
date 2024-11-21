                ---Rick and Morty API - Script para Buscar Personagens---

-Este script Python interage com a API pública do Rick and Morty para buscar 50 personagens 
e gerar um arquivo CSV contendo 6 dados sobre eles.


---Dependências---
-O script requer as bibliotecas "requests" para realizar as requisições à API e "pandas" para 
manipulação de dados e geração do arquivo CSV.


---Instalar Dependências---
-Antes de executar o script, certifique-se de instalar as bibliotecas necessárias: "pip install requests pandas"


---Como Executar o Script---
1- Clone ou faça o download deste repositório para o seu computador.
2- Abra o terminal ou prompt de comando na pasta do projeto.
3- Execute o script Python com o seguinte comando: "python fetch_rick_and_morty.py"

-O script fará uma requisição para a API do Rick and Morty, buscará informações sobre 50 
personagens e as salvará em um arquivo CSV.


---Formato do CSV Gerado---
-O arquivo CSV gerado será salvo com o nome "rick_and_morty_50_personagens.csv" (você pode 
modificar o nome passando um argumento ao chamar a função save_to_csv). O arquivo CSV estará 
no seguinte formato:
id;name;status;species;type;gender
361;Toxic Rick;Dead;Humanoid;Rick's Toxic Side;Male
25;Armothy;Dead;unknown;Self-aware arm;Male
33;Beebo;Dead;Alien;;Male

-id: Identificador único do personagem.
-name: Nome do personagem.
-status: Status de vida do personagem (Ex.: "Alive", "Dead").
-species: Espécie do personagem (Ex.: "Human", "Alien").
-type: Tipo do personagem (Ex.: "Rick's Toxic Side", "Humanoid").
-gender: Gênero do personagem (Ex.: "Male", "Female").


---Como Funciona o Script---
1-Requisição à API: O script faz uma requisição à API pública do Rick and Morty 
(https://rickandmortyapi.com/api/character) utilizando o método GET.
2-Paginação: A API retorna os dados de personagens em páginas. O script vai iterando sobre as 
páginas até que 50 personagens sejam coletados.
3-Filtragem de Dados: Para cada personagem, ele extrai 6 campos: "id", "name", "status", 
"species", "type" e "gender".
4-Criação do Arquivo CSV: Após obter os dados, o script cria um arquivo CSV contendo todas 
essas informações.


---Exemplo de Saída---
Após a execução do script, você encontrará um arquivo "rick_and_morty_50_personagens.csv" 
contendo as informações dos personagens. Aqui está um exemplo de como os dados podem aparecer
no arquivo:
id;name;status;species;type;gender
361;Toxic Rick;Dead;Humanoid;Rick's Toxic Side;Male
25;Armothy;Dead;unknown;Self-aware arm;Male
33;Beebo;Dead;Alien;;Male