from serpapi import GoogleSearch

params = {
  "q": "Coffee",
  "location": "Kochi, Kerala, India",
  "hl": "en",
  "gl": "en",
  "google_domain": "google.co.in/",
  "api_key": "a2c05cf3986b23c9078d8b57d283bd138460fa15b1f54c9f66aee3d8f4310240"
  "tbm": "nws"
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)
