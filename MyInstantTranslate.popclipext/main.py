# coding=utf-8
import os, urllib2

LANG_CODES = {
    "Arabic": "ar",
    "Bosnian (Latin)": "bs-Latn",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese Simplified": "zh-CHS",
    "Chinese Traditional": "zh-CHT",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Haitian Creole": "ht",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hmong Daw": "mww",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Klingon": "tlh",
    "Klingon (pIqaD)": "tlh-Qaak",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Maltese": "mt",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Querétaro Otomi": "otq",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian (Cyrillic)": "sr-Cyrl",
    "Serbian (Latin)": "sr-Latn",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swedish": "sv",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Yucatec Maya": "yua"
}

def translate(to_translate, to_langage="auto", langage="auto"):
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",'accept-language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','upgrade-insecure-requests':'1'}
	before_trans = 'class="t0">'
	link = "https://translate.google.cn/m?hl=en&sl=en&tl=zh-CN&ie=UTF-8&prev=_m&q=%s" % (to_translate.strip().replace("#","").replace("\n"," ").replace("\r"," ").replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

result = translate(os.environ['POPCLIP_TEXT'], LANG_CODES[os.environ['POPCLIP_OPTION_DESTLANG']], "auto");

print result
