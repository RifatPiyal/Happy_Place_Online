from calendar_api.calendar_api import google_calendar_api
from sphinx.addnodes import desc

m = google_calendar_api()
m.create_event(calendar_id='<566217121295-h1gg708rsfs4tk7cct21lejmehc7ari2.apps.googleusercontent.com>', start='2017-12-5T15:00:00.603111+00:00',
               end='2017-12-5T15:00:00.603111+00:00', desc  = 'foo')


