from serpapi import GoogleSearch
# import secrets
import json
from pprint import pprint

def suggest_location(search_location):
  params = {
    "engine": "google",
    "q": search_location + " attractions",
    "location": "Singapore",
    "tbm": "shop",
    "api_key": "8df6d8e4b1cfc7ffb2352495bc8d85280b63a56ed9bd6d5fad8acdb6b6433de0"
  }

  search = GoogleSearch(params)
  results = search.get_dict()

  pprint(results)
  json.dumps(results, indent=4, sort_keys=True)
  results_string = ""

# print(json.dumps(parsed, indent=4, sort_keys=True))
  if "top_sights" in results:
    top_sights = results['top_sights']['sights']

    # print(top_sights)
    json.dumps(top_sights, indent=4, sort_keys=True)
    sights_suggested = "Suggested places to visit:\n"
    for i in top_sights:
      sights_suggested += i['title'] + '\n'

    print(sights_suggested)
    results_string = sights_suggested
  elif "popular_destinations" in results:
    destinations = results["popular_destinations"]["destinations"]
    destinations_string = "Suggested places to visit:"
    for i in destinations:
      destinations_string += i['title'] + "\n"

    # print(destinations_string)
    json.dumps(destinations_string, indent=4, sort_keys=True)
    results_string = destinations_string
  else:
    results_string = "No suggestions found."

  if not results_string.strip():
    results_string = "No suggestions found."
  print("here")
  return results_string

results = suggest_location("Louis vtiton bag")
print(results)