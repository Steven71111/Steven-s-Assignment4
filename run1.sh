hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/Steven-s-Assignment4/mapper.py -mapper /home/uic/Steven-s-Assignment4/mapper.py \
-file /home/uic/Steven-s-Assignment4/reducer.py -reducer /home/uic/Steven-s-Assignment4/reducer.py \
-input /data/assignment4/1000.txt -output /output/assignment4-1/