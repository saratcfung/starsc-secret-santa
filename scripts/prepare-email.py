"""Build individual unsent invitations locally. Never send mail or print private links."""
from pathlib import Path
import json, html
from email.message import EmailMessage
from email.policy import SMTP
from email.parser import BytesParser
invites=json.loads(Path('.private/invitations.json').read_text())
assert len(invites)==6 and len({i['email'] for i in invites if i.get('email')})==6, 'Six distinct email addresses are required.'
template=Path('email-template.html').read_text()
art='https://saratcfung.github.io/starsc-secret-santa/assets/christmas-chibi.png'
for invite in invites:
    name=invite['name']
    body=template.replace('{{NAME}}',html.escape(name)).replace('{{LINK}}',html.escape(invite['url'],quote=True)).replace('{{ART_URL}}',art)
    assert '{{' not in body
    stem=Path('.private')/(name.lower()+'-invitation')
    stem.with_suffix('.html').write_text(body)
    msg=EmailMessage(policy=SMTP)
    msg['To']=invite['email']
    msg['Subject']=f'🎀 {name}, a little STARSC Christmas magic awaits!'
    msg.set_content(f'Merry Christmas, {name}!\n\nYour STARSC Secret Santa mission awaits. Open your private invitation:\n'+invite['url']+'\n\nPlease keep your link private. Anyone with it can see your fixed recipient. Keep this email to revisit your result.\n\nWith Christmas love, STARSC')
    msg.add_alternative(body,subtype='html')
    stem.with_suffix('.eml').write_bytes(msg.as_bytes())
    for suffix in ('.html','.eml'): stem.with_suffix(suffix).chmod(0o600)
    parsed=BytesParser(policy=SMTP).parsebytes(stem.with_suffix('.eml').read_bytes())
    assert parsed['To']==invite['email'] and not parsed['Cc'] and not parsed['Bcc']
    assert invite['url'] in parsed.get_body(preferencelist=('plain',)).get_content()
    for other in invites:
        if other['name']!=name: assert other['url'] not in body
print('Prepared and verified six separate illustrated emails. Nothing sent; no private links printed.')
