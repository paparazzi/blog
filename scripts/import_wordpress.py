#!/usr/bin/env python3
"""Rebuild Hugo content from the original WXR export; does not modify the export."""
import collections, html, json, re, tarfile
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
from markdownify import markdownify
ROOT = Path(__file__).resolve().parent.parent
NS = {'wp':'http://wordpress.org/export/1.2/', 'content':'http://purl.org/rss/1.0/modules/content/', 'dc':'http://purl.org/dc/elements/1.1/'}
tree = ET.parse(next(ROOT.glob('*.xml')))
items = tree.findall('./channel/item')
authors = {a.findtext('wp:author_login', '', NS): a.findtext('wp:author_display_name', '', NS) for a in tree.findall('./channel/wp:author', NS)}
def field(item, key): return item.findtext(key, '', NS)
def localize(text):
    return re.sub(r'https?://blog\.paparazziuav\.org(?=[/\s"\'<>]|$)', '', text)
attachments = {field(i, 'wp:post_id'): i for i in items if field(i, 'wp:post_type') == 'attachment'}
media = ROOT / 'static/wp-content'
media.mkdir(parents=True, exist_ok=True)
with tarfile.open(ROOT / 'uploads.tar.gz') as archive:
    archive.extractall(media, filter='data')
report = {'published_posts':0,'published_pages':0,'drafts_excluded':[], 'unhandled_shortcodes':[], 'comments_archived':0}
manifest = []
for item in items:
    kind, status = field(item,'wp:post_type'),field(item,'wp:status')
    if kind not in ('post','page'): continue
    if status != 'publish':
        report['drafts_excluded'].append(field(item,'wp:post_id')); continue
    body = field(item,'content:encoded')
    report['unhandled_shortcodes'] += [{'id':field(item,'wp:post_id'),'code':m} for m in re.findall(r'\[(?:video|audio)\b[^\]]*\](?!\()',body)]
    body = re.sub(r'\[caption\b[^\]]*\](.*?)\[/caption\]', lambda m: '<figure>'+m[1]+'</figure>',body, flags=re.S)
    def gallery(match):
        attrs = dict(re.findall(r'(\w+)=["\']([^"\']*)["\']',match[1]))
        ids = attrs.get('ids', '').split(',') if attrs.get('ids') else [k for k,v in attachments.items() if field(v,'wp:post_parent')==field(item,'wp:post_id')]
        figures=[]
        for aid in ids:
            a=attachments.get(aid)
            if a is None: continue
            url=html.escape(localize(field(a,'wp:attachment_url')),quote=True)
            figures.append(f'<figure><a href="{url}"><img src="{url}" alt="{html.escape(field(a,"title"),quote=True)}" loading="lazy"></a></figure>')
        return '\n\n'+'\n'.join(figures)+'\n\n'
    body = re.sub(r'\[gallery\b([^\]]*)\]',gallery,body)
    body = re.sub(r'\[embed\](.*?)\[/embed\]',r'\1',body, flags=re.S)
    def video(match):
        url=match[1].strip(); parsed=urlsplit(html.unescape(url)); vid=''
        if parsed.hostname in ('www.youtube.com','youtube.com'):
            from urllib.parse import parse_qs
            vid=parse_qs(parsed.query).get('v',[''])[0]
        elif parsed.hostname=='youtu.be': vid=parsed.path.strip('/')
        if re.fullmatch(r'[\w-]{11}',vid):
            return '\n\n<iframe src="https://www.youtube-nocookie.com/embed/'+vid+'" title="YouTube video" loading="lazy" allowfullscreen></iframe>\n\n'
        return match[0]
    body = re.sub(r'(?m)^\s*(https?://(?:www\.)?(?:youtube\.com/watch\?[^\s<]+|youtu\.be/[^\s<]+))\s*$',video,body)
    embeds=[]
    def preserve_embed(match):
        embeds.append(match[0])
        return '\n\nPAPARAZZIEMBEDTOKEN'+str(len(embeds)-1)+'TOKEN\n\n'
    body=re.sub(r'<iframe\b.*?</iframe>',preserve_embed,body,flags=re.S|re.I)
    # WordPress stores paragraph breaks as blank lines, even between inline HTML.
    body = re.sub(r'\n\s*\n', '</p>\n<p>', body)
    body = '<p>'+body+'</p>'
    body = localize(markdownify(body, heading_style='ATX', bullets='-', strip=['script']))
    for index,embed in enumerate(embeds): body=body.replace('PAPARAZZIEMBEDTOKEN'+str(index)+'TOKEN',embed)
    path = urlsplit(field(item,'link')).path
    meta = {'title':html.unescape(field(item,'title')), 'date':(field(item,'wp:post_date_gmt') or field(item,'wp:post_date')).replace(' ','T')+'Z', 'url':path, 'author':authors.get(field(item,'dc:creator'),field(item,'dc:creator')),'wordpress_id':int(field(item,'wp:post_id'))}
    for domain,key in [('category','categories'),('post_tag','tags')]:
        meta[key]=[c.text for c in item.findall('category') if c.get('domain')==domain and c.text]
    comments=[]
    for c in item.findall('wp:comment',NS):
        if field(c,'wp:comment_approved')=='1' and field(c,'wp:comment_type') not in ('pingback','trackback'):
            comments.append({'author':field(c,'wp:comment_author'),'date':field(c,'wp:comment_date'),'text':markdownify(field(c,'wp:comment_content'),strip=['script'])})
    if comments: meta['archived_comments']=comments; report['comments_archived']+=len(comments)
    dest=ROOT/'content'/('posts' if kind=='post' else 'pages')/(field(item,'wp:post_id')+'-'+field(item,'wp:post_name')+'.md')
    dest.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n\n'+body+'\n')
    manifest.append({'url':path,'source':str(dest.relative_to(ROOT))})
    report['published_posts' if kind=='post' else 'published_pages']+=1
(ROOT/'migration-manifest.json').write_text(json.dumps(manifest,indent=2))
(ROOT/'migration-report.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
