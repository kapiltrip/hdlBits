param(
    [string]$Iverilog = "C:\iverilog\bin\iverilog.exe"
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$stubs = Join-Path $PSScriptRoot "hdlbits_stubs.sv"

if (-not (Test-Path -LiteralPath $Iverilog)) {
    $command = Get-Command iverilog -ErrorAction SilentlyContinue
    if (-not $command) { throw "Icarus Verilog was not found." }
    $Iverilog = $command.Source
}

$files = Get-ChildItem (Join-Path $root "solutions") -Recurse -Filter *.sv | Sort-Object FullName
$failures = @()
$warnings = @()

foreach ($file in $files) {
    $messages = & $Iverilog -g2012 -Wall -t null -s top_module $stubs $file.FullName 2>&1
    if ($LASTEXITCODE -ne 0) {
        $failures += [pscustomobject]@{ file = $file.FullName.Substring($root.Length + 1); messages = @($messages) }
    }
    elseif ($messages) {
        $warnings += [pscustomobject]@{ file = $file.FullName.Substring($root.Length + 1); messages = @($messages) }
    }
}

$result = [ordered]@{
    checked = $files.Count
    passed = $files.Count - $failures.Count
    failed = $failures.Count
    warnings = $warnings.Count
    failures = $failures
    warningDetails = $warnings
}

$result | ConvertTo-Json -Depth 6
if ($failures.Count -gt 0 -or $warnings.Count -gt 0) { exit 1 }
