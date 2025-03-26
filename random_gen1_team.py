import random
import requests
import streamlit as st
import json

fully_evolved_pokemon_list = ["Venusaur", "Charizard", "Blastoise", "Butterfree", "Beedrill", "Pidgeot", "Raticate", "Fearow", "Arbok", "Raichu", "Sandslash", "Nidoqueen", "Nidoking", "Clefable", "Ninetales", "Wigglytuff", "Vileplume", "Parasect", "Venomoth", "Dugtrio", "Persian", "Golduck", "Primeape", "Arcanine", "Poliwrath", "Alakazam", "Machamp", "Victreebel", "Tentacruel", "Golem", "Rapidash", "Slowbro", "Farfetch'd", "Dodrio", "Dewgong", "Muk", "Cloyster", "Gengar", "Hypno", "Kingler", "Electrode", "Exeggutor", "Marowak", "Hitmonlee", "Hitmonchan", "Weezing", "Kangaskhan", "Seaking", "Starmie", "Mr. Mime", "Jynx", "Pinsir", "Tauros", "Gyarados", "Lapras", "Ditto", "Vaporeon", "Jolteon", "Flareon", "Omastar", "Kabutops", "Aerodactyl", "Snorlax", "Dragonite"]

def get_pokemon_data(pokemon):
    pokemon = pokemon.lower().replace(" ", "-").replace(".", "").replace("'", "")
    with open(f'./pokemon_json_files/{pokemon}.json', 'r') as json_file:
        pokemon_json = json.load(json_file)
    return pokemon_json

def get_pokemon_sprite(pokemon):
    pokemon_data = get_pokemon_data(pokemon)
    sprite_url = pokemon_data['sprites']["versions"]["generation-iii"]["emerald"]["front_default"]
    return sprite_url

def get_pokemon_types(pokemon):
    pokemon_data = get_pokemon_data(pokemon)
    type_data = [pokemon_data['types'][t]["type"]["name"] for t in range(len(pokemon_data['types']))]
    return type_data

st.header('Random Pokémon Team Generator')

st.subheader('Generate a random team based on all fully evolved Pokémon from Red/Blue/Yellow (excluding Legendaries and Mythicals).')

st.markdown("---")

with st.sidebar.expander("How many Pokémon are featured? 🤔", expanded=False):

    st.markdown(
    """
    You have a choice of 64 Pokémon, from Venusaur to Dragonite.
    """)

with st.sidebar.expander("Where is the data from? 🤖", expanded=False):

    st.markdown(
        """
        All the Pokémon data has been scraped from [PokéAPI](https://pokeapi.co/). Initially, the script pulled data directly from the API but to save on bandwidth and improve speed, I scraped data for all 64 Pokémon.
        """
    )

with st.sidebar.expander("To do list 📝", expanded=False):

    st.markdown(
        """
        - Add more data (if the public demand it!)
        """
    )

st.sidebar.markdown('Made with love and [Streamlit](https://streamlit.io/) by [@LukeDavisSEO](https://twitter.com/LukeDavisSEO)')

st.sidebar.markdown('<a href="https://ko-fi.com/A6102C2T"><img src="https://cdn.ko-fi.com/cdn/kofi2.png" alt="Buy Me a Coffee at ko-fi.com" height="36"></a>', unsafe_allow_html=True)

st.markdown("---")

st.info("Click 'Generate Team' to generate your random team of 6")

generate_team = st.button('Generate team')

st.markdown("---")

if generate_team:

    pokemon_team = random.sample(fully_evolved_pokemon_list,6)
    st.subheader('Your Pokémon team is...')

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    columns_list = [col1, col2, col3, col4, col5, col6]

    for i in columns_list:
        pkmn_id = pokemon_team[columns_list.index(i)]
        get_pokemon_data(pkmn_id)
        i.image(get_pokemon_sprite(pkmn_id))
        i.write(pkmn_id)
        types = get_pokemon_types(pkmn_id)
        if len(types) > 1:
            i.write(f'{types[0].capitalize()}/{types[1].capitalize()}')
        else:
            i.write(types[0].capitalize())
