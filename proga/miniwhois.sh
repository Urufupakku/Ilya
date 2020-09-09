for i in $(cat ip.txt)
do
echo $i
a=$(whois $i )
echo "<=========>"
echo "$a" | sed -e s/'%.*$'//g
echo "<=========>" 
done>mimi2.csv


