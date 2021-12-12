import pandas as pd
import re

with open('input.html', 'r') as f:
    html_content = f.read()

result = pd.read_html(html_content)[2]
places = result.Weiterbildungsstätten

trimmed_places_list = []

for p in places:
    # regex remove tilde distance
    address = re.search(r'(.*)\s~.*', p)[1]
    trimmed_places_list.append(address)

with open('out.csv', 'w') as f:
    f.write('Weiterbildungsstätten\n')
    for place in trimmed_places_list:
        f.write('"{}"\n'.format(place))
