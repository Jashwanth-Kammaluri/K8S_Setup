 ##Install Helm via Chocolatey
**Step 1:**
Open PowerShell as Administrator and run:  choco install kubernetes-helm -y

**Step2:**  Verify the Installation
helm version

**Step3:**  Add Your Chart Repository
helm repo add my-charts https://your.chart.repo/
helm repo update
