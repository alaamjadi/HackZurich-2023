<#
.SYNOPSIS
	Lists motherboard details
.DESCRIPTION
	This PowerShell script lists the motherboard details.
.EXAMPLE
	PS> ./list-motherboard.ps1

	Manufacturer : Gigabyte Technology Co., Ltd.
	...
.LINK
	https://github.com/fleschutz/PowerShell
.NOTES

try {
	Get-WmiObject -Class Win32_BaseBoard
	exit 0 # success
} catch {
	"âš ï¸ Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
#Account number: GB52HLZG07543133308029
#zrnr: JB-6841-0102-BANK
#Name: Balthasar Eberth
