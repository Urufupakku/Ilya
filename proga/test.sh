readarray -t timer < domain.txt
for ip in ${!timer[*]}
do
echo ${timer[$ip]}
echo "<================>"
soa=$(host -C ${timer[$ip]} 8.8.8.8) 
echo $soa | sed s/^.*"record"/\\t/g | sed s/^.*":"//g
echo "<================>"
done>test.csv