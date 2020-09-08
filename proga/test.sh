for i in $(cat domain.txt)
do
a=$(curl --request GET \
   --url 'https://www.virustotal.com/vtapi/v2/url/report?apikey=c87205136d3d1e987c85d0cca44810c373c2589dd029db1328b8b45f4a74773b&resource='$i)
   echo $a
done | jq>oufile.txt
echo "Hello World"
   
