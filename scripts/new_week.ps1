<#
.SYNOPSIS
    Quickly scaffold a new weekly report folder from the base template.
.DESCRIPTION
    Automatically copies the template directory to reports/week-XX and updates the week number.
.EXAMPLE
    .\scripts\new_week.ps1 2
#>

param (
    [Parameter(Mandatory=$true, Position=0)]
    [int]$WeekNumber
)

$weekStr = $WeekNumber.ToString("D2")
$targetDir = Join-Path $PSScriptRoot "..\reports\week-$weekStr"
$templateDir = Join-Path $PSScriptRoot "..\template"

if (Test-Path $targetDir) {
    Write-Warning "Directory $targetDir already exists!"
    exit 1
}

Write-Host "Scaffolding weekly report for Week $WeekNumber at $targetDir..." -ForegroundColor Cyan

# Create directory and copy template files
New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
Copy-Item -Path "$templateDir\*" -Destination $targetDir -Recurse -Exclude "*.aux","*.log","*.pdf","*.out","*.synctex.gz","*.fdb_latexmk","*.fls","weekly_report_template.*"

# Create week-specific figures directory
New-Item -ItemType Directory -Path "$targetDir\figures" -Force | Out-Null

# Update relative style paths in main.tex (going up 2 directories)
$mainTex = Join-Path $targetDir "main.tex"
if (Test-Path $mainTex) {
    $content = [System.IO.File]::ReadAllText($mainTex, [System.Text.Encoding]::UTF8)
    $content = $content.Replace('\usepackage{../style/weeklyreport}', '\usepackage{../../style/weeklyreport}')
    $content = $content.Replace('\input{../style/macros.tex}', '\input{../../style/macros.tex}')
    [System.IO.File]::WriteAllText($mainTex, $content, [System.Text.Encoding]::UTF8)
}

# Update week number in config.tex
$configTex = Join-Path $targetDir "config.tex"
if (Test-Path $configTex) {
    $configContent = [System.IO.File]::ReadAllText($configTex, [System.Text.Encoding]::UTF8)
    $configContent = [System.Text.RegularExpressions.Regex]::Replace($configContent, '\\newcommand\{\\WeekNo\}\{\d+\}', "\newcommand{\WeekNo}{$WeekNumber}")
    [System.IO.File]::WriteAllText($configTex, $configContent, [System.Text.Encoding]::UTF8)
}

Write-Host "Successfully created reports/week-$weekStr!" -ForegroundColor Green
Write-Host "Open $targetDir\config.tex and files in sections/ to start writing." -ForegroundColor Yellow
