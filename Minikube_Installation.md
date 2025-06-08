# Minikube installions:

#step1:
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

#step2:	choco -v

#step:3 choco install minikube -y

#step:4
minikube version
kubectl version --client

#step5: 
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All
Restat_PC
minikube start --driver=hyperv --cpus=4 --memory=8192  --hyperv-virtual-switch="Default Switch"

#step:6
minikube stop
minikube delete
