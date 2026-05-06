#!/bin/bash
i=1
for FILE in *.{jpg,png,JPG,PNG}; do
  [ -f "$FILE" ] || continue
  ext="${FILE##*.}"
  NEWNAME=$(printf '%04d.%s' $i "$ext")
  mv "$FILE" "$NEWNAME"
  i=$((i+1))
done
