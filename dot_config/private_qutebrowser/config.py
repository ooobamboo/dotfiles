config.load_autoconfig(False)

c.zoom.default = 120

c.url.start_pages = 'file:///dev/null'
c.url.default_page= 'file:///dev/null'

c.tabs.title.format = "{audio}{current_title}"
c.fonts.web.size.default = 20

c.url.searchengines = {
        'DEFAULT': 'https://google.com/search?q={}',
        '!aur': 'https://aur.archlinux.org/packages?O=0&K={}',
        '!ddg': 'https://lite.duckduckgo.com/lite/?q={}',
        '!aw': 'https://wiki.archlinux.org/?search={}',
        '!bing': 'https://cn.bing.com/search?q={}',
        '!apkg': 'https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=',
        '!gh': 'https://github.com/search?o=desc&q={}&s=stars',
        '!cb': 'https://codeberg.org/explore/repos?q={}&only_show_relevant=true&sort=moststars',
        '!yt': 'https://www.youtube.com/results?search_query={}',
        '!wk': 'https://en.wikipedia.org/wiki/{}',
        '!zhwk': 'https://zh.wikipedia.org/wiki/{}',
        '!bl': 'https://search.bilibili.com/all?keyword={}',
        '!fh': 'https://flathub.org/en/apps/search?q={}',
}

c.auto_save.session = False

c.tabs.indicator.width = 0
c.tabs.width = '7%'

# dark mode setup
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'
config.bind('I', 'config-cycle colors.webpage.darkmode.enabled false true')

# fonts
c.fonts.default_family = []
c.fonts.default_size = '12pt'
c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'monospace'

c.downloads.location.directory = "~/dls"
c.downloads.location.prompt = False
c.downloads.remove_finished = 3300

c.content.fullscreen.window = True

# privacy - adjust these settings based on your preference
config.set("completion.cmd_history_max_items", 0)
config.set("content.private_browsing", False)
config.set("content.webgl", False, "*")
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)
config.bind('zc', 'config-cycle content.canvas_reading true false ;; set content.canvas_reading?')
config.bind('zj', 'config-cycle content.javascript.enabled ;; set content.javascript.enabled? ;; reload')
config.bind('<Space>', 'mode=normal')

c.content.blocking.enabled = True
config.bind('za', 'config-cycle content.blocking.enabled')
c.content.blocking.method = 'adblock'
c.content.blocking.adblock.lists = [
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2023.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2024.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-cookies.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-others.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/quick-fixes.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt",
        "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt"
]
