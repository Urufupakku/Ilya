readarray -t timer < domain.txt
for ip in ${!timer[*]}
do
if (($ip%2!=0))
then
echo ${timer[$ip]}
echo "<================>"
a=$(curl --request GET \
   --url 'https://www.virustotal.com/vtapi/v2/url/report?apikey=c87205136d3d1e987c85d0cca44810c373c2589dd029db1328b8b45f4a74773b&resource='${timer[$ip]})
echo $a | jq

else
echo "2 element"
sleep 10
echo ${timer[$ip]}
echo "<================>"

a=$(curl --request GET \
   --url 'https://www.virustotal.com/vtapi/v2/url/report?apikey=c87205136d3d1e987c85d0cca44810c373c2589dd029db1328b8b45f4a74773b&resource='${timer[$ip]})
echo $a | jq
fi
done>vs.txt
