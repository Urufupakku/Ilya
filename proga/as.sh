for as in $(cat as.txt):
do echo $as;
fields=$(whois -h whois.radb.net -i origin $as| egrep 'route:|route6:|descr:')
echo $fields | sed s/'route:'/\\r/g | sed s/'route6:'/\\n/g | sed s/'descr:'/\\t/g
done>as.csv

for as in $(cat as.txt)
do
echo $as>as2.txt
#curl GET https://api.bgpview.io/asn/$as | jq '.' >as2.txt
curl GET https://api.bgpview.io/asn/$as/prefixes | jq '.' >as2.txt
#curl GET https://api.bgpview.io/asn/$as/peers| jq '.' >as2.txt
done