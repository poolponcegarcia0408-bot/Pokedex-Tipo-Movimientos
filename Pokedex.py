import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

print("🐦‍🔥 Bienvenido a la Pokedex del señor Pool 🐦‍🔥")

while True:
    pokemon = input("\nInserte el nombre del Pokémon (o 'salir' para terminar): ").lower()
    
    if pokemon == "salir":
        print("👋 Gracias por usar la Pokedex. ¡Hasta la próxima!")
        break

    print("¿Qué deseas saber?\n1) Movimientos \n2) Tipo")
    actividad = input("Elige opción (1 o 2): ")
    response = requests.get(URL + pokemon)

    if response.status_code == 200:
        data = response.json()

        if actividad == "1":
            print(f"\nMovimientos de {pokemon.capitalize()}:")
            for move in data["moves"]:
                print("-", move["move"]["name"])

        elif actividad == "2":
            print(f"\nTipos de {pokemon.capitalize()}:")
            for tipo in data["types"]:
                print("-", tipo["type"]["name"])

        else:
            print("Opción inválida.")
    else:
        print("Pokémon no encontrado. Verifica el nombre.")