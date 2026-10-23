param(
    [string]$TaskName = "AwesomeVLADaily",
    [string]$StartTime = "09:30"
)

$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Python = (Get-Command python).Source
$RuntimeDir = Join-Path $Root ".runtime"
New-Item -ItemType Directory -Force -Path $RuntimeDir | Out-Null

$At = [datetime]::ParseExact($StartTime, "HH:mm", $null)
$Action = New-ScheduledTaskAction `
    -Execute $Python `
    -Argument "scripts\run_daily_job.py" `
    -WorkingDirectory $Root
$Trigger = New-ScheduledTaskTrigger `
    -Weekly `
    -WeeksInterval 1 `
    -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday `
    -At $At
$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 15) `
    -ExecutionTimeLimit (New-TimeSpan -Hours 3)

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Description "Rank, publish, and email the Awesome VLA daily digest." `
    -Force | Out-Null

Write-Host "Installed $TaskName for Monday-Friday at $StartTime."
Write-Host "SMTP_AUTH_CODE must be configured in the task user's environment."

