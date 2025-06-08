# Minikube installions: 

**Step 1:**  
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

**Step 2:** 	   
choco -v

**Step 3:**  
choco install minikube -y

**Step 4:** 
minikube version
kubectl version --client

**Step 5:**  
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All
Restat_PC
minikube start --driver=hyperv --cpus=4 --memory=8192  --hyperv-virtual-switch="Default Switch"

**Step 6:** 
minikube stop
minikube delete
