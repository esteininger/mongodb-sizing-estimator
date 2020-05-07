host="sa-shared-demo-shard-00-01.lbvlu.mongodb.net:27017"
username="ethan"
password="1RrQIU5UZrp5Gci2"

mongostat --host $host --ssl --username $username --password $password --authenticationDatabase admin | tee output.txt
