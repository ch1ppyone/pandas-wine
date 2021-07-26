import pandas as pd
import argparse
import os.path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='?', type=str, default="wine2.xlsx" )
args = parser.parse_args()

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

excel_data_df = pd.read_excel(args.filename,  header=None, skiprows=1,  names=None,   na_values=[
                              'N/A', 'NA'], keep_default_na=False)

rendered_page = template.render(
    data=excel_data_df
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
