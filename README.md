pip3 install elasticsearch

bin/logstash -f /etc/logstash.conf

telnet localhost 2064

http://localhost:2070  --> post

http://localhost:7096  --> post  give json data



D:\xxxxxxx\logstash-6.6.2\bin>logstash -f ..\..\data_upload\console.conf



step 1: D:\xxxxx\logstash-6.6.2\bin>logstash -f ..\..\data_upload\access_log_logstash.conf

step 2: D:\xxxxxx\data_upload>echo " " >> apache_logs

tcp

step 1: D:\xxxxx\logstash-6.6.2\bin>logstash -f ..\..\data_upload\tcp.conf

step 2: D:\xxxxxxx\data_upload>telnet localhost 2064

