#!/bin/bash
for ((i=1; i<=20; i++)); do
    python3 parser.py  "../resumes/itu/google/$i.pdf"
done

