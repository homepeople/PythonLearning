# -*- coding: utf-8 -*-

'''
This module will catch at least one Bible verse from the different Bible version of Jw.org and 
Compare different version of Bible by each verse,and print the same number of
each verse together,also print the version of the verse after it. 
If the verse content are exactly same then the verse just print once and plus their
version info together and print those after the verse.

比较不同圣经版本的经文，保留所有常规标点符号，生成多语言支持的HTML文件
不同章保存到不同文件
"""

import re
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import urllib.request

# 全局配置
BOOK = '66'          # 书籍编号（如创世记）
CHAPTERS = ['1','2']    # 章节列表
VERSIONS = [
    {
        'name': '新世界译本2013',  # 中文版本名称
        'url': 'https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/nwt/{book}/{chapter}#study=discover',
        'language': 'zh-CN'
    },
    {
        'name': '新世界译本1983',
        'url': 'https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/bi12/{book}/{chapter}#study=discover',
        'language': 'zh-CN'
    },
    {
        'name': '和合本',
        'url': 'https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/sbi1/{book}/{chapter}#study=discover',
        'language': 'zh-CN'
    },
    {
        'name': 'New World Translation',  # 英文版本名称
        'url': 'https://wol.jw.org/en/wol/b/r1/lp-e/nwt/{book}/{chapter}#study=discover',
        'language': 'en'
    }
]


# 书籍编号到英文名称的映射（完整66卷）
BOOK_NAMES = {
    '1': 'Genesis',             # 创世记
    '2': 'Exodus',              # 出埃及记
    '3': 'Leviticus',           # 利未记
    '4': 'Numbers',             # 民数记
    '5': 'Deuteronomy',         # 申命记
    '6': 'Joshua',              # 约书亚记
    '7': 'Judges',              # 士师记
    '8': 'Ruth',                # 路得记
    '9': '1_Samuel',            # 撒母耳记上
    '10': '2_Samuel',           # 撒母耳记下
    '11': '1_Kings',            # 列王纪上
    '12': '2_Kings',            # 列王纪下
    '13': '1_Chronicles',       # 历代志上
    '14': '2_Chronicles',       # 历代志下
    '15': 'Ezra',               # 以斯拉记
    '16': 'Nehemiah',           # 尼希米记
    '17': 'Esther',             # 以斯帖记
    '18': 'Job',                # 约伯记
    '19': 'Psalms',             # 诗篇
    '20': 'Proverbs',           # 箴言
    '21': 'Ecclesiastes',       # 传道书
    '22': 'Song_of_Solomon',    # 雅歌
    '23': 'Isaiah',             # 以赛亚书
    '24': 'Jeremiah',           # 耶利米书
    '25': 'Lamentations',       # 耶利米哀歌
    '26': 'Ezekiel',            # 以西结书
    '27': 'Daniel',             # 但以理书
    '28': 'Hosea',              # 何西阿书
    '29': 'Joel',               # 约珥书
    '30': 'Amos',               # 阿摩司书
    '31': 'Obadiah',            # 俄巴底亚书
    '32': 'Jonah',              # 约拿书
    '33': 'Micah',              # 米该亚书
    '34': 'Nahum',              # 那鸿书
    '35': 'Habakkuk',           # 哈巴谷书
    '36': 'Zephaniah',          # 西番雅书
    '37': 'Haggai',             # 哈该书
    '38': 'Zechariah',          # 撒迦利亚书
    '39': 'Malachi',            # 玛拉基书

    '40': 'Matthew',            # 马太福音
    '41': 'Mark',               # 马可福音
    '42': 'Luke',               # 路加福音
    '43': 'John',               # 约翰福音
    '44': 'Acts',               # 使徒行传
    '45': 'Romans',             # 罗马书
    '46': '1_Corinthians',      # 哥林多前书
    '47': '2_Corinthians',      # 哥林多后书
    '48': 'Galatians',          # 加拉太书
    '49': 'Ephesians',          # 以弗所书
    '50': 'Philippians',        # 腓立比书
    '51': 'Colossians',         # 歌罗西书
    '52': '1_Thessalonians',    # 帖撒罗尼迦前书
    '53': '2_Thessalonians',    # 帖撒罗尼迦后书
    '54': '1_Timothy',          # 提摩太前书
    '55': '2_Timothy',          # 提摩太后书
    '56': 'Titus',              # 提多书
    '57': 'Philemon',           # 腓利门书
    '58': 'Hebrews',            # 希伯来书
    '59': 'James',              # 雅各书
    '60': '1_Peter',            # 彼得前书
    '61': '2_Peter',            # 彼得后书
    '62': '1_John',             # 约翰一书
    '63': '2_John',             # 约翰二书
    '64': '3_John',             # 约翰三书
    '65': 'Jude',               # 犹大书
    '66': 'Revelation'          # 启示录
}

# 版本名称到缩写的映射
VERSION_ABBREVIATIONS = {
    '新世界译本2013': 'NWT2013',
    '新世界译本1983': 'NWT1983',
    '和合本': 'CUV',
    'New World Translation': 'NWT',
}

def fetch_html(url):
    """获取网页内容"""
    try:
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None

def extract_chapter_text(html):
    """提取章节文本内容"""
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find('article', id='article')
    return article.get_text(separator='\n') if article else ''

def clean_text(text):
    """保留所有正常标点符号，仅去除特殊符号"""
    cleaned = re.sub(
        r'[^\u4e00-\u9fa5'  # 汉字
        r'\u3001-\u3002'    # ，。 
        r'\uff01-\uff1f'    # ！？ 
        r'\uff1a-\uff1b'    # ：；
        r'\u201c-\u201d'    # “”
        r'\u2018-\u2019'    # ‘’
        r'\u300c-\u300d'    # 「」
        r'\u3014-\u3015'    # 『』
        r'\uff08-\uff09'    # （）
        r'\u2013-\u2014'    # –—
        r'\w\s\.\,\!\?\;\:\'\"\(\)\[\]\{\}\«\»\-\—\–]',  # 英文标点
        '', text
    )
    return re.sub(r'\s+', ' ', cleaned).strip()

def split_verses(text):
    """根据章节号分割经文（保留必要空格和标点）"""
    verses = []
    current_verse = ''
    lines = text.split('\n')
    for line in lines:
        if line.strip().startswith(tuple('0123456789')):
            if current_verse:
                verses.append(current_verse.strip())
            current_verse = line
        else:
            current_verse += line
    if current_verse:
        verses.append(current_verse.strip())
    return verses

def merge_verses(verses_list, versions):
    """合并相同内容的经文"""
    merged = {}
    for verse_group in zip(*verses_list):
        for j, verse in enumerate(verse_group):
            cleaned_verse = clean_text(verse)
            if not cleaned_verse.strip():
                continue
            if cleaned_verse not in merged:
                merged[cleaned_verse] = []
            merged[cleaned_verse].append(versions[j]['name'])
    return merged

def format_output(merged, book_english, chapter):
    """生成多语言支持的HTML内容"""
    html = []
    html.append('<!DOCTYPE html>')
    html.append('<html>')
    html.append('<head>')
    html.append('<meta charset="UTF-8">')
    html.append('<title>Bible Comparison</title>')
    html.append('<style>')
    html.append('body { font-family: Arial, "Microsoft YaHei", sans-serif; }')
    html.append('table { width: 100%; border-collapse: collapse; margin: 20px 0; }')
    html.append('th, td { border: 1px solid #ddd; padding: 8px; }')
    html.append('</style>')
    html.append('</head>')
    html.append('<body>')
    
    # 英文标题
    html.append(f'<h1>{book_english} Chapter {chapter}</h1>')
    html.append('<table>')
    html.append('<tr><th>Verse</th><th>Versions</th></tr>')

    for verse, versions in merged.items():
        formatted_versions = ' | '.join(f"({v})" for v in versions)
        html.append(f'<td>{verse}</td>')
        html.append(f'<td>{formatted_versions}</td>')
        html.append('</tr>')
      
    html.append('</table>')
    html.append('</body>')
    html.append('</html>')
    return '\n'.join(html)

def main():
    for chapter in CHAPTERS:
        book_english = BOOK_NAMES.get(BOOK, f"Book_{BOOK}")
        
        # 生成文件名
        versions_abbr = [VERSION_ABBREVIATIONS[v['name']] for v in VERSIONS]
        filename = f"{book_english}_{chapter}_" + "_".join(versions_abbr) + ".html"
        
        urls = [v['url'].format(book=BOOK, chapter=chapter) for v in VERSIONS]
        
        with ThreadPoolExecutor() as executor:
            htmls = list(executor.map(fetch_html, urls))
        
        verses_list = []
        for html in htmls:
            if html:
                text = extract_chapter_text(html)
                verses = split_verses(text)
                cleaned_verses = [clean_text(v) for v in verses]
                verses_list.append(cleaned_verses)
            else:
                verses_list.append([])
           
        merged = merge_verses(verses_list, VERSIONS)
        
        # 生成HTML内容
        html_content = format_output(merged, book_english, chapter)
        
        # 保存文件
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"对比结果已保存到 {filename}")

        
if __name__ == '__main__':
    main()
