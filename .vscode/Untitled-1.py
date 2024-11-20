
import requests # type: ignore

def fetch_trending_repositories(language):
    url = f"https://gh-trending-api.herokuapp.com/repositories?language={language}&since=daily"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            print(f"Repository Name: {repo['repositoryName']}")
            print(f"Username: {repo['username']}")
            print(f"URL: {repo['url']}")
            print(f"Description: {repo['description']}")
            print(f"Language: {repo['language']}")
            print(f"Total Stars: {repo['totalStars']}")
            print(f"Forks: {repo['forks']}")
            print(f"Stars Since: {repo['StarsSince']}")
            print(f"Built By: {[dev['username'] for dev in repo['builtBy']]}")
            print("-" * 40)
    else:
        print(f"Failed to fetch trending repositories. Status code: {response.status_code}")

# Example usage
fetch_trending_repositories("Python")
