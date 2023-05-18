import subprocess

# Update system
subprocess.run(['sudo', 'pacman', '-Syu'])

# Install packages
subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'libreoffice-fresh', 'oh-my-zsh', 'yay', 'pamac'])
subprocess.run(['sudo', 'yay', '-S', '--noconfirm','pamac-all'])


# Replace KDE application launcher widget with application menu
subprocess.run(['kwriteconfig5', '--file', '~/.config/plasma-org.kde.plasma.desktop-appletsrc', '--group', 'Containments', '--key', 'org.kde.plasma.desktop.defaultPanel', '--type', 'string', 'com.canonical.menu.kicker'])

# Restart KDE Plasma
subprocess.run(['killall', 'plasmashell'])
subprocess.run(['kstart5', 'plasmashell'])
