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

c.content.headers.custom = {}

for url in [
    'https://wx.qq.com/*',
    'https://web.weixin.qq.com/*',
    'https://web.wechat.com/*',
    'https://web1.wechat.com/*',
    'https://web2.wechat.com/*',
    'https://wx2.qq.com/*',
    'https://wx8.qq.com/*',
]:
    config.set('content.headers.custom', {
        "extspam": "Go8FCIkFEokFCggwMDAwMDAwMRAGGvAESySibk50w5Wb3uTl2c2h64jVVrV7gNs06GFlWplHQbY/5FfiO++1yH4ykCyNPWKXmco+wfQzK5R98D3so7rJ5LmGFvBLjGceleySrc3SOf2Pc1gVehzJgODeS0lDL3/I/0S2SSE98YgKleq6Uqx6ndTy9yaL9qFxJL7eiA/R3SEfTaW1SBoSITIu+EEkXff+Pv8NHOk7N57rcGk1w0ZzRrQDkXTOXFN2iHYIzAAZPIOY45Lsh+A4slpgnDiaOvRtlQYCt97nmPLuTipOJ8Qc5pM7ZsOsAPPrCQL7nK0I7aPrFDF0q4ziUUKettzW8MrAaiVfmbD1/VkmLNVqqZVvBCtRblXb5FHmtS8FxnqCzYP4WFvz3T0TcrOqwLX1M/DQvcHaGGw0B0y4bZMs7lVScGBFxMj3vbFi2SRKbKhaitxHfYHAOAa0X7/MSS0RNAjdwoyGHeOepXOKY+h3iHeqCvgOH6LOifdHf/1aaZNwSkGotYnYScW8Yx63LnSwba7+hESrtPa/huRmB9KWvMCKbDThL/nne14hnL277EDCSocPu3rOSYjuB9gKSOdVmWsj9Dxb/iZIe+S6AiG29Esm+/eUacSba0k8wn5HhHg9d4tIcixrxveflc8vi2/wNQGVFNsGO6tB5WF0xf/plngOvQ1/ivGV/C1Qpdhzznh0ExAVJ6dwzNg7qIEBaw+BzTJTUuRcPk92Sn6QDn2Pu3mpONaEumacjW4w6ipPnPw+g2TfywJjeEcpSZaP4Q3YV5HG8D6UjWA4GSkBKculWpdCMadx0usMomsSS/74QgpYqcPkmamB4nVv1JxczYITIqItIKjD35IGKAUwAA==",
        "client-version": "2.0.0",
    }, url)
