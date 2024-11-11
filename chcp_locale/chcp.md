# Afficher un fichier correctement

## Windows cmd.exe

Pour voir la page de code : `chcp`

Pour mettre la page de code :

- `chcp 1252` pour Windows-1252
- `chcp 65001` pour UTF-8
- `chcp 28591` pour ISO 8859-1
- `chcp 28605` pour ISO-8859-15
- `chcp 437` pour l'encodage DOS par défaut
- `chcp 850` pour l'encodage DOS par défaut en France
- `chcp 10000` pour MacRoman

Clé de registre :

- `HKEY_CURRENT_USER\Software\Microsoft\Command Processor`
- Clé : `Autorun`
- Valeur : `chcp 65001 >NUL`
- PowerShell : `Set-ItemProperty 'HKCU:\Software\Microsoft\Command Processor' AutoRun 'chcp 65001 >NUL'`

Voir aussi `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor`

Source : [Stack Overflow](https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window)

## Powershell

Fichier profile : `notepad $HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`

```pwsh
$utf8 = New-Object System.Text.UTF8Encoding
[console]::OutputEncoding = $utf8
[console]::InputEncoding = $utf8
$OutputEncoding = $utf8
$PSDefaultParameterValues['*:Encoding'] = 'utf8'
```

## Linux

- `locale` pour vérifier la configuration actuelle
- `iconv -f ISO-8859-15 -t utf-8 <fichier>`
- `file -i <fichier>`pour trouver l'encodage d'un fichier
- `chardet <fichier>` si file -i ne renvoie rien (installation : `sudo apt install python3-chardet -y`)

## Ressources

- Source : [Stack Overflow](https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window)
- Clé de registre `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\CodePage` clé `OEMCP`
- [Encodages PowerShell](https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-7.4)
- [System.Text](https://learn.microsoft.com/en-us/dotnet/api/system.text.encoding?view=net-8.0)
