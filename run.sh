#!/bin/bash
for ((i=1; i<=20; i++)); do
    python3 parser.py  "$i.pdf"
done

