from os import getenv
import requests
import json

rapidapi_key = getenv("X-RAPIDAPI-KEY")

def shorten_json(json_data):
    # Check if the JSON data has the expected structure
    if 'titles' in json_data and isinstance(json_data['titles'], list):
        # Iterate through each title and keep only the desired fields
        shortened_titles = []
        for title_obj in json_data['titles']:
            if 'jawSummary' in title_obj:
                jaw_summary = title_obj['jawSummary']
                shortened_title = {
                    'id': jaw_summary.get('id'),
                    'title': jaw_summary.get('title'),
                    'releaseYear': jaw_summary.get('releaseYear'),
                    'synopsis': jaw_summary.get('synopsis'),
                    'seasonCount': jaw_summary.get('seasonCount'),
                    'Episodes': jaw_summary.get('Episodes')
                }
                # Add the 'link' field based on 'id'
                if 'id' in shortened_title:
                    shortened_title['link'] = f"https://www.netflix.com/title/{shortened_title['id']}"
                shortened_titles.append(shortened_title)

        # Replace the 'titles' field with the shortened titles
        json_data['titles'] = shortened_titles

    if 'suggestions' in json_data and isinstance(json_data['suggestions'], list):
         # Iterate through each title and keep only the desired fields
        shortened_suggestions = []
        for suggestion_obj in json_data['suggestions']:
            if 'summary' in suggestion_obj and isinstance(suggestion_obj['summary'], dict):
                summary = suggestion_obj['summary']
                shortened_suggestion = {}
                
                # Check if 'name' is not null or missing
                if 'name' in summary and summary['name']:
                    shortened_suggestion['name'] = summary['name']
                
                # Check if 'id' is not null or missing
                if 'id' in summary and summary['id']:
                    shortened_suggestion['id'] = summary['id']
                    
                    # Add the 'link' field based on 'id'
                    shortened_suggestion['link'] = f"https://www.netflix.com/title/{summary['id']}"
                
                shortened_suggestions.append(shortened_suggestion)

        # Replace the 'suggestions' field with the shortened suggestions
        json_data['suggestions'] = shortened_suggestions
    else:
        # Botflix will reply on it's own
        return None 
    return json_data

def fetch_netflix_datas(query, offset="0", limit_titles="5", lang="en"):
    url = "https://netflix54.p.rapidapi.com/search/"
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "netflix54.p.rapidapi.com"
    }
    querystring = {
        "query": query,
        "offset": offset,
        "limit_titles": limit_titles,
        "lang": lang
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        expected_response = response.json()
        return shorten_json(expected_response)
    else:
        # Handle the case when the API request fails or returns an error
        # Botflix will reply on it's own
        return None

