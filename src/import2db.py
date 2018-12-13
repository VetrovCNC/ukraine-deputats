from deputats.parsing import parser
index_filename = '/home/alex/_DJANGO_/freelance/ukraine-deputats/src/deputats/parsing/downloads/index.html'
deputats = parser.parse_index_page(index_filename)
parser.create_deputats(deputats)
