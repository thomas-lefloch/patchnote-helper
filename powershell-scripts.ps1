
New-Item -Path $PROFILE -ItemType "File" -Force
echo "Set-Alias venv ./venv/Scripts/Activate.ps1" >> $profile