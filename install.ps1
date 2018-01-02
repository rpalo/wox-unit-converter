$plugin_dir = 'C:\Users\ryan\AppData\Local\Wox\app-1.3.183\Plugins'
$target_name = 'Wox.Plugin.UnitConverter'
$target_path = "$plugin_dir\\$target_name"
Write-Host "Copying to $plugin_dir"
if (Test-Path "$target_path") {
    Remove-Item "$target_path" -Recurse
}
New-Item "$plugin_dir\\$target_name" -ItemType "directory"
Copy-Item ./* "$plugin_dir\\$target_name" -Recurse
Write-Host "Installed."
