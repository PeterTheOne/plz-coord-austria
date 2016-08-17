import requests
import csv
import time


base_api_url = 'http://nominatim.openstreetmap.org/search?'

url = base_api_url + 'countrycodes=AT&format=jsonv2'

with open('input_data/PLZ_Verzeichnis_AUG16_.csv') as csvfile:
    with open('output_data/PLZ_Verzeichnis_AUG16_.csv', 'w') as output:
        reader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in reader:
            #if i > 10:
            #    break

            if i == 0:
                row.extend([
                    'lat',
                    'lon',
                    'importance',
                ])
            else:
                time.sleep(1)
                r = requests.get(url + '&postalcode=' + row[0], headers={'User-Agent': 'plz-coord-austria'})
                jsondata = r.json()
                if r.status_code == 200 and jsondata:
                    row.extend([
                        jsondata[0]['lat'],
                        jsondata[0]['lon'],
                        str(jsondata[0]['importance']),
                    ])
                else:
                    row.extend(['','',''])
            line = ','.join(row)

            print('{:>4}: {}'.format(i, line))
            output.write('{}\n'.format(line))
            i += 1
