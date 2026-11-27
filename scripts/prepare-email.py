"""Build Sara's unsent invitation locally. Does not send mail or print its link."""
from pathlib import Path
import json, html
from email.message import EmailMessage
from email.policy import SMTP
invite=next(i for i in json.loads(Path('.private/invitations.json').read_text()) if i['name']=='Sara')
if not invite['email']: raise SystemExit('Add the recipient email to the private invitation file first.')
template=Path('email-template.html').read_text()
art='https://saratcfung.github.io/starsc-secret-santa/assets/christmas-friends.png'
body=template.replace('{{NAME}}',html.escape(invite['name'])).replace('{{LINK}}',html.escape(invite['url'],quote=True)).replace('{{ART_URL}}',art)
Path('.private/sara-invitation.html').write_text(body)
msg=EmailMessage(policy=SMTP);msg['To']=invite['email'];msg['Subject']='🎀 Sara, a little STARSC Christmas magic awaits!'
msg.set_content('Merry Christmas, Sara!\n\nYour STARSC Secret Santa mission awaits. Open your private invitation:\n'+invite['url']+'\n\nPlease keep your link private. Anyone with it can see your fixed recipient. Keep this email to revisit your result.\n\nWith Christmas love, STARSC')
msg.add_alternative(body,subtype='html')
Path('.private/sara-invitation.eml').write_bytes(msg.as_bytes())
print('Prepared the illustrated HTML and multipart email locally. Not sent.')
