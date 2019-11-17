  
#!/bin/bash
for ((i=1; i<=20; i++)); do
    echo "Contact $i"
    python3 parser.py  "sample/google/$i.pdf"
done

