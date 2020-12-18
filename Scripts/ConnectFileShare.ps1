[CmdletBinding()]
param
(
    [string] $saname,
    [string] $fsname
)

if (-not($saname)) {
    $saname = Read-Host -Prompt "Enter the name of the storage account where the file share is found" 
}
if (-not($fsname)) {
    $fsname = Read-Host -Prompt "Enter the name of the file share"
}


$ModuleName = "Az"
$module = Get-Module $ModuleName -ListAvailable -ErrorAction SilentlyContinue
$module
if (!$module) {
    Write-Host "Installing module $ModuleName ..."
    #Install-Module -Name $ModuleName -Force -Scope CurrentUser
    Write-Host "Module installed"
}

#connect to Azure
if ($null -eq $login) {
    $login = Connect-AzAccount
}

Select-AzSubscription vdl

$rgname = Get-AzStorageAccount | Where-Object {$_.StorageAccountName -eq $saname} | Select-Object -ExpandProperty ResourceGroupName
$keys = Get-AzStorageAccountKey -ResourceGroupName $rgname -AccountName $saname
$key = $keys[0].value

$connectTestResult = Test-NetConnection -ComputerName "$saname.file.core.windows.net" -Port 445
if ($connectTestResult.TcpTestSucceeded) {
    # Save the password so the drive will persist on reboot
    cmd.exe /C "cmdkey /add:`"$saname.file.core.windows.net`" /user:`"Azure\$saname`" /pass:`"$key`""
    # Mount the drive
    New-PSDrive -Name "S" -PSProvider FileSystem -Root "\\$saname.file.core.windows.net\$fsname" -Persist
} else {
    Write-Error -Message "Unable to reach the Azure storage account via port 445. Check to make sure your organization or ISP is not blocking port 445, or use Azure P2S VPN, Azure S2S VPN, or Express Route to tunnel SMB traffic over a different port."
}