$ErrorActionPreference = "Stop"

Write-Output "Loading VS2026 MSVC environment..."

$vsPath = "C:\Program Files\Microsoft Visual Studio\18\Enterprise"
$msvcVer = "14.51.36231"
$sdkVer = "10.0.26100.0"

$msvcBin = "$vsPath\VC\Tools\MSVC\$msvcVer\bin\Hostx64\x64"
$msvcInclude = "$vsPath\VC\Tools\MSVC\$msvcVer\include"
$msvcLib = "$vsPath\VC\Tools\MSVC\$msvcVer\lib\x64"

$sdkPath = "C:\Program Files (x86)\Windows Kits\10"
$sdkBin = "$sdkPath\bin\$sdkVer\x64"
$sdkInclude = "$sdkPath\Include\$sdkVer"
$sdkLib = "$sdkPath\Lib\$sdkVer"

$env:PATH = "$msvcBin;$sdkBin;$sdkPath\bin\x64;$vsPath\Common7\IDE;$vsPath\Common7\Tools;$env:PATH"
$env:INCLUDE = "$msvcInclude;$sdkInclude\ucrt;$sdkInclude\um;$sdkInclude\shared;$sdkInclude\winrt;$sdkInclude\cppwinrt"
$env:LIB = "$msvcLib;$sdkLib\ucrt\x64;$sdkLib\um\x64"
$env:LIBPATH = "$msvcLib"

Write-Output "Configuring CMake..."
cmake --preset local-msvc-debug -S "$PSScriptRoot"

Write-Output ""
Write-Output "Building..."
cmake --build --preset local-msvc-debug --parallel