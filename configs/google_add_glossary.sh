curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @google_add_glossary.json \
https://translation.googleapis.com/v3/projects/415574831314/locations/us-central1/glossaries
