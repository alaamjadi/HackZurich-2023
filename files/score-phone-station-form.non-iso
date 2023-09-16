<#
.SYNOPSIS
	Writes the moon phase
.DESCRIPTION
	This PowerShell script writes the current moon phase to the console.
.EXAMPLE
	PS> ./write-moon.ps1
.LINK
	https://github.com/fleschutz/PowerShell
.NOTES

try {
	(Invoke-WebRequest http://wttr.in/Moon -userAgent "curl" -useBasicParsing).Content
	exit 0 # success
} catch {
	"âš ï¸ Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}#Client number: JB-4957-1840-BANK
#Client: Yvette Löwer
#IBAN: GB18UIGI55591207180587
