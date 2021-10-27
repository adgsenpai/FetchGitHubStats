# FetchGitHubStats

## Returns Your GitHub Repos to a Pandas Dataframe

### Interactive Demo
<a href="https://colab.research.google.com/github/ADGVLOGS/FetchGitHubStats/blob/main/GitHub_API_to_DataFrame.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Usage 

in bash

'''
pip install FetchGitHubStats
'''

#### Coding usage

'''
from FetchGitHubStats import dataframe

# Make sure to use your GitHub API URL
dataframe.ReturnDataFrame('https://api.github.com/users/ADGVLOGS/repos')
'''
