<#
.SYNOPSIS
	Opens the user's downloads folder
.DESCRIPTION
	This PowerShell script launches the File Explorer showing the user's downloads folder.
.EXAMPLE
	PS> ./open-downloads-folder
.LINK
	https://github.com/fleschutz/PowerShell
.NOTES

try {
	if ($IsLinux) {
		$Path = Resolve-Path "$HOME/Downloads"
	} else {
		$Path = (New-Object -ComObject Shell.Application).NameSpace('shell:Downloads').Self.Path
	}
	if (-not(Test-Path "$Path" -pathType container)) {
		throw "Downloads folder at 📂$Path doesn't exist (yet)"
	}
	& "$PSScriptRoot/open-file-explorer.ps1" $Path
	exit 0 # success
} catch {
	"⚠� Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
#ZRNR: JB-4573-3166-BANK
#Account number: DE81698883022213004043
#Client: Bryan James
