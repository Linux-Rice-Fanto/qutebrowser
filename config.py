# -----------------------------------------------------
#     ____       __      __                             
#    / __ \__ __/ /____ / /  _______ _    _____ ___ ____
#   / /_/ / // / __/ -_) _ \/ __/ _ \ |/|/ (_-</ -_) __/
#   \___\_\_,_/\__/\__/_.__/_/  \___/__,__/___/\__/_/   
# -----------------------------------------------------                                                    

# --------------------
# BASIC CONFIGURATION
# --------------------

config.load_autoconfig(False)
config.set('content.cookies.accept', 'never', 'chrome-devtools://*')
config.set('content.cookies.accept', 'never', 'devtools://*')
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:136.0) Gecko/20100101 Firefox/139.0', 'https://accounts.google.com/*')
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/fanto/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_file_urls', False, 'file:///home/fanto/.local/share/qutebrowser/userscripts/*')

# -------------------
# TABS CONFIGURATION
# -------------------

config.set('tabs.position', 'top')
config.set('tabs.show', 'always')
config.bind('J', 'tab-next')
config.bind('K', 'tab-prev')
config.set('colors.tabs.bar.bg', '#0d1117')
config.set('colors.tabs.even.bg', '#011117')
config.set('colors.tabs.odd.bg', '#0d1117')
config.set('colors.tabs.selected.even.bg', '#0d1117')
config.set('colors.tabs.selected.odd.bg', '#0d1117')
config.set('colors.tabs.even.fg', '#17f501')
config.set('colors.tabs.odd.fg', '#17f501')
config.set('colors.tabs.selected.even.fg', '#ffffff')
config.set('colors.tabs.selected.odd.fg', '#ffffff')
config.bind('xt', 'config-cycle tabs.show always never')


# ------------------------
# STATUS BAR CONFIGURATION
# ------------------------

config.set('colors.statusbar.normal.bg', '#0d1117')
config.set('colors.statusbar.normal.fg', '#ffffff')
config.set('fonts.statusbar', '10pt Jetbrains Mono Nerd Font')
config.bind('xb', 'config-cycle statusbar.show always never')

# --------------------
# HINTS CONFIGURATION
# --------------------

config.set('colors.hints.bg','#0d1117')
config.set('colors.hints.fg','#17f501')
config.set('colors.hints.match.fg','#ffffff')
config.set('fonts.hints', '10pt Jetbrains Mono Nerd Font')

# ------------------------
# COMPLETION CONFIGURATION
# ------------------------

config.set('colors.completion.category.bg','#0d1117')
config.set('colors.completion.category.fg','#17f501')
config.set('colors.completion.even.bg','#0d1117')
config.set('colors.completion.odd.bg','#0d1117')
config.set('colors.completion.fg','#17f501')
config.set('colors.completion.match.fg','#ffffff')
config.set('colors.completion.item.selected.bg', '#999999')
config.set('colors.completion.item.selected.fg', '#000000')
config.set('fonts.completion.entry', '10pt Jetbrains Mono Nerd Font')



