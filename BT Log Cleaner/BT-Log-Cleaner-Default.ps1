$files = Get-ChildItem "[Log File Path]" -Recurse -Include *.txt

foreach ($f in $files){

    $outfile = "[Destination Path]\[Log]-Dump.txt"
    
    Get-Content $f.FullName | Select-String -Pattern '[Search items separated by | ]' -AllMatches| Select-Object -ExpandProperty Line |Add-Content $outfile
    
    }

Read-Host -Prompt "Press Enter to exit"

if ($Error)
{
    Pause
}