# k6 (Grafana_Labs)

**Step:1**
choco install k6 -y

**Step:2**
k6 version

**Step:3**
command to run the script
k6 run your-script.js

-----------------------------
# Locust 

**Step1** Install Locust
pip install locust -y

**Step2**
locust --version

**Step3**

locust -f locustfile.py --headless -u 1000 -r 100 --run-time 30s --host http://172.17.26.241:30146

