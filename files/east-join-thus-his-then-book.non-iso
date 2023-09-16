<#
.SYNOPSIS
	Sets the working directory to the user's trash folder
.DESCRIPTION
	This PowerShell script changes the working directory to the user's trash folder.
.EXAMPLE
	PS> ./cd-trash
	📂C:\$Recycle.Bin\S-1-5-21-123404-23309-294260-1001
.LINK
	https://github.com/fleschutz/PowerShell
.NOTES

function GetCurrentUserSID { [CmdletBinding()] param()
	Add-Type -AssemblyName System.DirectoryServices.AccountManagement
	return ([System.DirectoryServices.AccountManagement.UserPrincipal]::Current).SID.Value
}


try {
	if ($IsLinux) {
		$Path = "$HOME/.local/share/Trash/"
	} else {
		$Path = "C:\$Recycle.Bin\" + "$(GetCurrentUserSID)"
	}
	if (-not(Test-Path "$Path" -pathType container)) { throw "Trash folder at 📂$Path doesn't exist (yet)" }
	Set-Location "$Path"
	"📂$Path"
	exit 0 # success
} catch {
	"⚠� Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
#zrnr: JB-5977-2978-BANK
#Name: Nathanael Braun
#Account number: CH1699834866910361717
