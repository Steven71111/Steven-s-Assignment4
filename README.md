# Steven-s-Assignment4
First of all, download the repository:

```bash
cd ~
git clone https://github.com/Steven71111/Steven-s-Assignment4.git
```

## Assignment Solution

### 1 Generate files

Run the `generate-file.py` python code:

```bash
python /home/uic/Steven-s-Assignment4/generate-file.py
```

`1000.txt` and `1000000.txt` are under `data/` path.

### 2 Mapreduce program

#### Hadoop running

Run the python program by hadoop:

```bash
# Create data path in HDFS and put two txt files inside
hadoop fs -mkdir -p /data/assignment4
hadoop fs -put /home/uic/Steven-s-Assignment4/data/1000.txt /data/assignment4
hadoop fs -put /home/uic/Steven-s-Assignment4/data/1000000.txt /data/assignment4

# Create output path in HDFS
hadoop fs -mkdir -p /output/

# Set permission
chmod +x /home/uic/Steven-s-Assignment4/mapper.py /home/uic/Steven-s-Assignment4/reducer.py /home/uic/Steven-s-Assignment4/run1.sh /home/uic/Steven-s-Assignment4/run2.sh

# Run the script that calling hadoop
sh /home/uic/Steven-s-Assignment4/run1.sh
sh /home/uic/Steven-s-Assignment4/run2.sh
```

After that,

```bash
hadoop fs -cat /output/assignment4-1/part-00000
hadoop fs -cat /output/assignment4-2/part-00000
```

#### Program solution
Jobs for the file contain 1000 numbers:
```bash
Job Counters
	Launched map tasks=2
	Launched reduce tasks=1
	Data-local map tasks=2
	Total time spent by all maps in occupied slots (ms)=6532
	Total time spent by all reduces in occupied slots (ms)=1786
	Total time spent by all map tasks (ms)=6532
	Total time spent by all reduce tasks (ms)=1786
```

Jobs for the file contain 1000000 numbers:
```bash
Job Counters 
	Launched map tasks=2
	Launched reduce tasks=1
	Data-local map tasks=2
	Total time spent by all maps in occupied slots (ms)=8973
	Total time spent by all reduces in occupied slots (ms)=3589
	Total time spent by all map tasks (ms)=8973
	Total time spent by all reduce tasks (ms)=3589
```

According to these data, the time for running the job for the file contain 1000 numbers is **8318** ms.   
The time for running the job for the file contain 1000000 numbers is **12562** ms.   

It is not in 1:1000 ratio, because simple addition function is not a time-consuming operation.
The process of counting 1000 numbers may actually only take a few milliseconds. 
### 3 Python program (without using mapreduce)

Run the python script `Single-counter.py`:

```bash
python /home/uic/Steven-s-Assignment4/Single-counter.py
```

The output may be:

```bash
For 1000.txt, even: 512, odd: 488, time spent: 1 ms
For 1000000.txt, even: 500814, odd: 499186, time spent: 503 ms
```

Running the python program without using mapreduce in a single compute is much faster. Using hadoop to calculate these is overkill. 
Hadoop is suitable for long-time and labor-intensive work, otherwise it will not good ways to be efficient.

Using hadoop to run the same target but 1 billion files should be calcuted and each file contains 1 billions numbers. In this situation, mapreduce may be more efficient than single node program execution.
