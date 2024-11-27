#!/bin/bash
BACKUP_FOLDER=$(jq --raw-output '.backup_folder' /data/options.json)
FILES_TO_WATCH=$(jq --raw-output '.files_to_watch[]' /data/options.json)

mkdir -p "$BACKUP_FOLDER"

for FILE in $FILES_TO_WATCH; do
  inotifywait -m -e modify "$FILE" | while read -r; do
    TIMESTAMP=$(date +"%Y%m%d%H%M%S")
    cp "$FILE" "$BACKUP_FOLDER/$(basename "$FILE")_$TIMESTAMP"
  done
done