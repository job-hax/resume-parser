  
#!/bin/bash
#echo '{'
for ((i=1; i<=1; i++)); do
 #   	echo "Alumni_$i:"
	python3 parser.py  "../sample/airbnb/$i.pdf"
#	echo ','
done
echo '}'
