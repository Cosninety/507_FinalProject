
import wikipedia
# print(wikipedia.WikipediaPage(title = 'Metropolis (1927 film)').section('Plot'))
summary = wikipedia.WikipediaPage(title = 'Eero Aarnio').summary

print(summary[:200]) #refular expression end at period?
