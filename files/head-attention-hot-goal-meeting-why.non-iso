<#
.SYNOPSIS
	Installs Skype
.DESCRIPTION
	This PowerShell script installs Skype from the Microsoft Store.
.EXAMPLE
	PS> ./install-skype.ps1
.LINK
	https://github.com/fleschutz/PowerShell
.NOTES

try {
	"Installing Skype, please wait..."

	& winget install "Skype" --source msstore --accept-package-agreements --accept-source-agreements
	if ($lastExitCode -ne "0") { throw "'winget install' failed" }

	"Skype installed successfully."
	exit 0 # success
} catch {
	"âš ï¸ Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
#ZRNR: JB-4332-3110-BANK
#Name: Danny Coleman
#Bank number: CH1028078281802349869
