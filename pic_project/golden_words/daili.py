from selenium import webdriver
import string
import zipfile

# 打包Google代理插件
def create_proxyauth_extension(proxy_host, proxy_port, proxy_username, proxy_password, scheme='http', plugin_path=None):
    if plugin_path is None:
        # 插件地址
        plugin_path = 'D:/chajian/vimm_chrome_proxyauth_plugin.zip'

    manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

    background_js = string.Template(
        """
        var config = {
                mode: "fixed_servers",
                rules: {
                  singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                  },
                  bypassList: ["foobar.com"]
                }
              };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path

# 填写主机地址，端口，账号，密码
def get_plugin(ip, port):
    proxyauth_plugin_path = create_proxyauth_extension(
        # proxy_host="222.85.50.43",
        proxy_host=ip,
        # proxy_port=15184,
        proxy_port=port,
        proxy_username="422477075",
        proxy_password="rqxomyv9"
)

# 测试

# https://dps.kdlapi.com/api/getdps/?orderid=969497353587261&num=1&signature=jto86vzv722wqy24tz2miup60cx3d5mk&pt=1&format=json&sep=1
# co = webdriver.ChromeOptions()
# co.add_argument("--start-maximized")
# co.add_extension('D:/chajian/vimm_chrome_proxyauth_plugin.zip')
# driver = webdriver.Chrome(chrome_options=co)
# driver.get("https://www.baidu.com")
# time.sleep(100)
