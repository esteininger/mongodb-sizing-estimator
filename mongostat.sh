host=""
username=""
password=""

mongostat --host $host --ssl --username $username --password $password --authenticationDatabase admin | tee output.txt
