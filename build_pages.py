# Builds the three app detail pages from one template so they stay consistent.
import os
ROOT = os.path.dirname(os.path.abspath(__file__)).replace(os.sep, '/') + '/'
CAP = {'class': 'Original Oni Class interface · fictional demonstration data · Korean UI',
       'record': 'Oni Record as it runs · student names are pseudonyms · Korean UI',
       'proctor': 'Oni Proctor running its built-in sample exam · fictional names · Korean UI'}

def shot(src, w, h, alt, label, cap=None, pins=None, lazy=True, style=''):
    pins_html = ''.join(f'<span class="pin" style="left:{x}%;top:{y}%">{n}</span>' for n, x, y in (pins or []))
    lz = ' loading="lazy"' if lazy else ''
    return (f'<figure{style}><button class="screen" data-image="{src}" aria-label="Enlarge {label}">'
            f'<img src="{src}" alt="{alt}"{lz} width="{w}" height="{h}">{pins_html}'
            f'<span class="zoom">↗ View full screen</span></button>'
            + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>')

def notes(items, cls=''):
    out = f'<div class="notes{cls}">'
    for i, it in enumerate(items, 1):
        if isinstance(it, tuple):
            out += f'<div><span class="number">{i}</span><p><b>{it[0]}</b>{it[1]}</p></div>'
        else:
            out += f'<div><span class="number">{i}</span><p>{it}</p></div>'
    return out + '</div>'

def steps(items, cls=''):
    return f'<div class="steps{cls}">' + ''.join(f'<div><b>{n:02d} <span>{t}</span></b><p>{d}</p></div>' for n, (t, d) in enumerate(items, 1)) + '</div>'

def chapter(cid, eyebrow, h2, p, body, tinted=False):
    return (f'<section class="chapter{" tinted" if tinted else ""}" id="{cid}"><div class="wrap">'
            f'<div class="chapter-heading"><div><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div><p>{p}</p></div>{body}</div></section>')

def tip(b, text):
    return f'<aside class="tip"><b>{b}</b><span>{text}</span></aside>'

def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'

def page(key, name, title, desc, og, body, others):
    foot = ' · '.join(f'<a href="../{k}/">{n}</a>' for k, n in others)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://onischool.net/oni-{key}/">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://onischool.net/oni-{key}/">
<meta property="og:image" content="https://onischool.net/{og}">
<link rel="stylesheet" href="../assets/app.css">
</head>
<body class="app-{key}">
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
<a class="brand" href="#"><span class="mark" aria-hidden="true"></span>{name}</a>
<nav aria-label="Page navigation">
<a href="../">Oni School</a>
<a href="#tour">Product tour</a>
<a href="#storage">Your data</a>
<a href="#start">Get started <span>↗</span></a>
</nav>
</header>
<main id="main">
{body}
</main>
<footer class="wrap footer">
<a class="brand" href="#">{name}</a>
<span>By <a href="../">Oni School</a> · <a href="mailto:oniaby@onischool.net">oniaby@onischool.net</a></span>
<span>{foot}</span>
</footer>
<dialog id="viewer"><div class="viewer-head"><span>{name} · Example screen</span><button id="close" aria-label="Close enlarged screen">Close ✕</button></div><img alt=""></dialog>
<script src="../assets/app.js"></script>
</body>
</html>
'''

def hero(eyebrow, h1, lead, actions, micro, fig, step_items):
    return (f'<section class="hero wrap"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p>'
            f'<div class="actions">{actions}</div><p class="micro">{micro}</p>{fig}{steps(step_items)}</section>')

def intro(eyebrow, h2, p):
    return f'<section class="intro wrap" id="tour"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2><p>{p}</p></section>'

def card(label, h3, body, cls='', blue=False):
    return f'<article{cls}><span class="data-label{" blue" if blue else ""}">{label}</span><h3>{h3}</h3>{body}</article>'

def write(key, html):
    os.makedirs(ROOT + f'oni-{key}', exist_ok=True)
    open(ROOT + f'oni-{key}/index.html', 'w', encoding='utf-8', newline='\n').write(html)
    print(key, len(html))

# ───────────────────────── Oni Class (content from the standalone branch) ─────────────────────────
A = '../assets/class/'
c = CAP['class']
def cshot(f, alt, label, lazy=True):
    return shot(A + f, 1440, 960, alt, label, c, lazy=lazy)
body = hero('Made for the everyday work of teaching', 'A busy classroom.<br><em>A calmer school day.</em>',
    'Class records, attendance, submissions and lesson progress. <br>One familiar workspace for the details that fill your day.',
    '<a class="button primary" href="#tour">Explore the app <span>↓</span></a><a class="button" href="#start">Windows beta <span>↗</span></a>',
    'Windows desktop app · Korean interface · English product guide',
    cshot('calendar.png', 'Oni Class calendar and daily details in the actual application interface', 'calendar screen', lazy=False),
    [('Plan', 'Start with the calendar.'), ('Record', 'Keep the context close.'), ('Follow up', 'See what still needs attention.'), ('Stay in view', 'Bring useful details to the desktop.')])
body += intro('A closer look', 'Less searching.<br>More of your day in one place.', 'Follow the real interface through six parts of a teacher’s workflow. Click any screen to inspect it at full size.')
body += chapter('calendar', '01 / Daily overview', 'Start with the whole day.', 'Your calendar, to-dos and attendance share one workspace. Select a date to see its details without losing the month around it.',
    cshot('calendar.png', 'Calendar workspace showing example October events and the selected day', 'calendar screen') +
    notes(['See school events and personal reminders together.', 'Keep a checklist next to the day it belongs to.', 'Open attendance from the selected day.']))
body += chapter('students', '02 / Class records', 'Know the student behind the row.', 'Move from your class roster to an individual profile. Keep observations and counseling follow-ups close to the student they concern.',
    cshot('students.png', 'Class roster and individual student profile using fictional students', 'students screen') +
    notes(['View student details in a structured profile.', 'Record counseling notes and follow-up actions.', 'Use the seating view to arrange your classroom.']), True)
body += chapter('attendance', '03 / Attendance', 'From one day to the month.', 'Record an absence, late arrival, early departure or missed class. Review monthly totals and open the underlying record when you need the detail.',
    cshot('attendance.png', 'Monthly attendance summary for fictional students', 'attendance screen') +
    notes(['Keep attendance categories and supporting-document status together.', 'Expand a student row to inspect dated records.', 'Review absence statements in the dedicated tab.']))
body += chapter('submissions', '04 / Submissions &amp; lists', 'See exactly what is still missing.', 'Create a collection with more than one document. Check each item per student, then switch to the outstanding list before your next reminder.',
    cshot('submissions.png', 'Document submission tracker with individual checkboxes and completion totals', 'submissions screen') +
    notes(['Track forms separately, even within the same collection.', 'Filter completed and pending students.', 'Copy the pending list or export the collection to Excel.']) +
    tip('A practical routine', 'Create the collection → check each document → filter pending students → send your reminder through your usual channel.'), True)
body += chapter('progress', '05 / Lesson progress', 'One plan. Each class at its own pace.', 'Define the units once, then track how far each class has reached. Compare classes without keeping a separate spreadsheet for every group.',
    cshot('progress.png', 'Lesson progress plan comparing four classes', 'progress screen') +
    notes(['Organize a plan by grade and subject.', 'Keep the ordered lesson units together.', 'Adjust progress independently for each class.']))
body += chapter('widgets', '06 / Desktop widgets', 'Keep the useful part in view.', 'Choose compact views for today, the timetable, lesson progress, notes and the calendar. The Windows app can place them on your desktop.',
    cshot('widgets.png', 'Actual widget gallery with example data', 'widgets screen') +
    notes(['Choose a widget size to suit your workspace.', 'Keep quick notes within reach.', 'Use desktop placement and window pinning in the installed app.']) +
    '<p class="micro">The gallery is shown here. Desktop positioning and pinning require the installed Windows app.</p>', True)
body += ('<section class="storage wrap" id="storage"><p class="eyebrow">Your data, explained</p><h2>Detailed records stay on your PC.<br><em>Selected records can travel with you.</em></h2>'
    '<p class="section-lead">Oni Class uses local storage and a limited mobile sync scope. “Stored locally” does not mean that every feature works without an account or cloud services.</p><div class="data-grid">'
    + card('On this Windows PC', 'The fuller student picture', '<p>Detailed student profiles, enrollment history, counseling and observation notes, seating layouts, memos, lesson progress and import history remain in the local record store.</p><p class="small">The Windows app stores records in SQLite and protects record payloads with Windows account-based encryption (DPAPI).</p>')
    + card('Mobile sync scope', 'What you need on the move', '<p>Calendar entries and to-dos, attendance, submission lists, timetable information and a minimal class roster are included in the mobile sync scope.</p><p class="small">The minimal roster includes student ID, name, class number and class placement. Timetable and roster data are supplied by the PC.</p>', blue=True)
    + '</div><p class="storage-note">Account and service checks use online services. Make backups through the app; a database file alone should not be treated as a portable, readable backup. NEIS transfer is a separate, teacher-initiated workflow.</p></section>')
body += ('<section class="tinted"><div class="wrap setup" id="start"><p class="eyebrow">Before your first class</p><h2>A clear place to begin.</h2><div class="setup-grid">'
    '<article><b>1</b><h3>Install the Windows beta</h3><p>Open the release page, review the release notes and select the Windows installer.</p></article>'
    '<article><b>2</b><h3>Set up your class</h3><p>Sign in, enter your school and class details, then add or import your roster.</p></article>'
    '<article><b>3</b><h3>Start with one routine</h3><p>Add a reminder, record attendance or create a document checklist. Build from there.</p></article></div>'
    + faq([('Is this the app’s actual visual design?', 'Yes. Screens are rendered from Oni Class’s original React components and stylesheet files, with fictional classroom data in an isolated preview. Native Windows operations and live cloud sync were not exercised for these images.'),
           ('Is Oni Class available in English?', 'This product guide is in English. The application interface shown here is Korean.'),
           ('Do I need my own AI API key?', 'No personal AI API key is required for the class-management workflows shown here. Oni Class and Oni Record are different applications with different storage and service requirements.'),
           ('What should I know about NEIS?', 'NEIS integration requires a separate browser extension and a supported school environment. Availability depends on the target NEIS screen and version. Review transferred records in NEIS. This tour does not demonstrate or verify a live NEIS transfer.')])
    + '</div></section>')
body += ('<section class="cta wrap"><span class="mark" aria-hidden="true"></span><h2>Give your everyday work<br>a place to belong.</h2><p>Oni Class · A workspace for teachers</p>'
    '<div class="actions"><a class="button primary" href="https://github.com/yang102948549/oni-class/releases" target="_blank" rel="noopener">View Windows releases ↗</a><a class="button" href="mailto:oniaby@onischool.net">Contact Oni School</a></div></section>')
write('class', page('class', 'Oni Class', 'Oni Class — A calmer school day',
    'Explore Oni Class: a Windows workspace for class records, attendance, submissions, calendars and lesson progress.',
    'assets/class/calendar.png', body, [('oni-record', 'Oni Record'), ('oni-proctor', 'Oni Proctor')]))

# ───────────────────────── Oni Record ─────────────────────────
A = '../assets/record/'
c = CAP['record']
body = hero('Made for the end-of-term record season', 'Student records, written and checked.<br><em>In one table, with AI.</em>',
    'Type as you would in Google Sheets, pick your material from keyword chips, let AI write the draft, check it against the official writing guidelines, then apply it to NEIS.',
    '<a class="button primary" href="#tour">Explore the app <span>↓</span></a><a class="button" href="#start">Windows beta <span>↗</span></a>',
    'Windows desktop app · Korean interface · Beta v0.1.1-beta.9 · AI features need your own Gemini API key',
    shot(A + 'hero.webp', 1250, 750, 'Oni Record window: a table of students with keyword columns, the finished record in the last column, and the Write sidebar on the right', 'main screen', c, lazy=False),
    [('Write', 'AI drafts for subject comments, behavior notes and activities.'), ('Assist', 'Keyword chips supply the material for each sentence.'), ('Check', 'Before and after, against the writing guidelines.'), ('Apply', 'Batch entry into NEIS.')])
body += intro('A closer look', 'From a blank cell to NEIS.<br>One table the whole way.', 'Follow the real interface through five parts of the job. Click any screen to inspect it at full size. NEIS is Korea’s national school information system.')
body += chapter('screen', '01 / The screen', 'Five areas, one window.', 'Sheets run along the top, students run down the table, and the right panel changes with the task. Nothing moves to a separate window while you work.',
    shot(A + 'screen.webp', 1250, 755, 'Oni Record window with five numbered markers: sheet tabs, toolbar, editing table, the Write, Check and Assist panel, and the generate button', 'annotated screen', 'A moral education subject-comment sheet for class 1-3 · ' + c) +
    notes([('Sheet tabs', 'One tab per class and subject.'), ('Toolbar', 'Undo, row and column editing, find, import and export, text size and zoom.'), ('Editing table', 'Arrow-key movement, copy and paste, and a NEIS byte count in each cell.'),
           ('Write · Check · Assist', 'Choose <span class="ko">세특</span>, <span class="ko">행특</span>, <span class="ko">자율</span> or <span class="ko">기타</span> (club and career).'), ('Start generating', 'Select students and draft them in one run. The NEIS apply button sits just below.')]) +
    tip('Byte counting', 'NEIS limits records by bytes, not characters. A Korean character counts as 3 bytes and a line break as 2, so every long-text cell shows its count as you type.'))
types = ('<div class="data-grid three">'
    + card('세특 · 교과 세부능력 및 특기사항', 'Subject comments',
        shot(A + 'write-course.webp', 352, 1060, 'Write panel for subject comments: four lesson activities, a character count of 150, a student list and the generate button', 'subject comment panel')
        + '<ol><li><b>Add lesson activities.</b> Each activity name becomes a column in the table.</li><li><b>Enter notes for each student.</b> The draft uses only what the student actually did.</li><li><b>Set the length, select students, start.</b> Written to the character count you set, spaces included.</li></ol>'
          '<p class="small"><b>AI writing rules.</b> The subject teacher’s point of view, in one connected paragraph. Wording that implies one lesson continued from another is avoided, and an empty activity is never invented.</p>')
    + card('행특 · 행동특성 및 종합의견', 'Behavior notes',
        shot(A + 'write-behavior.webp', 352, 1066, 'Write panel for behavior notes: evaluation items for personality, peer relations and attitude, a character count of 200, and seven students selected', 'behavior note panel')
        + '<ol><li><b>Set the evaluation items.</b> For example personality, peer relations and attitude to school life.</li><li><b>Enter keywords for each item.</b> Pick them from Assist chips or type them yourself.</li><li><b>Set the length, select students, start.</b> The keywords are worked into the sentences.</li></ol>'
          '<p class="small"><b>AI writing rules.</b> The homeroom teacher’s point of view, centered on current positive change. A weakness is written with the effort to improve, and the note closes with one sentence on the student’s potential.</p>')
    + card('자율활동 · 자율활동 특기사항', 'Autonomous activities',
        '<ol><li><b>Save each activity’s date and name.</b> Saved activities appear as a pick list in the table’s activity cells.</li><li><b>Set the number of activity slots</b> and enter each student’s notes. Add as many slots as you need.</li><li><b>Set the length, select students, start.</b> The date follows each activity name in <code>(YYYY.MM.DD.)</code> form.</li></ol>'
        '<p class="small"><b>AI writing rules.</b> One paragraph that connects what the activity meant with how the student grew. Activity names are written without quotation marks, and opening phrases are varied from student to student.</p>')
    + '</div>')
body += chapter('write', '02 / Write', 'Choose the record type.<br>The panel follows.', 'Pick what you are writing and the input panel and the AI’s writing rules change to fit it. The steps stay the same: enter material, set a length, select students.',
    types + '<p class="micro">Club and career activity sheets have their own writing and checking rules, under <span class="ko">기타</span>. They cannot be applied to NEIS yet, so the generated text is copied by hand.</p>', True)
body += chapter('assist', '03 / Assist', 'Press chips instead of typing.', 'There is no need to start each sentence from a blank cell. Keyword chips organized by subject and item go into the selected cell, and the AI writes from those keywords.',
    shot(A + 'assist.webp', 1250, 750, 'A behavior-note sheet with the Assist panel open. The selected cell holds two keywords, and the same two chips are highlighted in the panel', 'assist screen', 'Select a cell and press chips. They are entered joined by commas, as in “활발한, 적극적인” · ' + c) +
    notes([('The chips change with the area', 'Subject comments are grouped by subject. Behavior notes are grouped by personality, peer relations, class attitude, school life and self-management.'),
           ('Open a chip to go deeper', 'Opening a group such as “active and sociable” shows more specific keywords like “lively” and “outgoing”. Either level can be chosen.'),
           ('Straight into the cell', 'Chosen keywords are listed under “keywords in this cell”. Remove one with ×, or edit the cell by hand. The same keyword is entered only once.'),
           ('Search, collapse, cautions', 'Keyword search, collapse all, and a list of writing cautions for each area come with the panel.')], ' two') +
    tip('Ten subject groups', 'Korean · Mathematics · English, foreign languages and classical Chinese · Social studies, history and ethics · Science · Physical education · Arts · Technology, home economics and informatics · Career and liberal arts · Other. Behavior notes, autonomous activities, clubs and career have their own chips.') +
    '<p class="micro">The keywords you choose are what the AI uses to interpret and write each sentence. The keyword lists are a first draft and have not yet been reviewed in schools.</p>')
body += chapter('check', '04 / Check', 'A separate sheet shows what changed, and why.', 'The original is left as it is. Oni Record makes a check sheet with the text before, the text after and the reason, so nothing is overwritten until you decide.',
    steps([('Make a check sheet', 'Columns for original, before, after and reason are created.'), ('Select students and check', 'Each student is marked fixed or unchanged.'), ('Apply to the original', 'Only fixed items are written back to the original cell.')], ' three') +
    shot(A + 'check.webp', 1250, 750, 'A check sheet with original, before, after and reason columns for each student, and the Check panel listing each student’s status', 'check screen', 'Changed parts are marked red before and green after, with the reason beside them · ' + c, style=' style="margin-top:30px"') +
    '<div class="pair">' + shot(A + 'check-done.webp', 448, 242, 'Dialog: check complete. 8 students checked, 4 fixed, 4 unchanged', 'check complete dialog', 'When checking ends, the app reports how many were fixed and how many were unchanged.') +
    notes(['Review the reason for each student and choose what to apply to the original.', 'If nothing needs fixing, the original is kept and marked <span class="ko">수정사항 없음</span> (no changes).', 'A result that was shortened too much keeps the original and raises a warning.', 'Write your own criteria under “additional check items” and they are checked as well.']) + '</div>' +
    '<h3 class="sub">What is checked, following the 2026 writing guidelines</h3><ul class="criteria">'
    '<li><b>Sentence endings</b>Noun-form endings, with varied endings</li><li><b>Particles and subject</b>No “~에서는”, required particles in place</li>'
    '<li><b>Quotation marks</b>Single quotes only for book and project titles</li><li><b>Dates</b>One format: (YYYY.MM.DD.)</li>'
    '<li><b>Symbols and layout</b>Decorative symbols, bullet lists and double spaces cleaned up</li><li><b>Not to be recorded</b>University and institution names, overseas results, competition content</li>'
    '<li><b>Vocabulary</b>Colloquial and abbreviated words made standard</li><li><b>Content kept</b>The student’s own content is neither deleted nor invented</li></ul>'
    '<p class="micro">The teacher makes the final decision on anything the AI checks. Read the reasons before applying.</p>', True)
body += chapter('neis', '05 / Apply to NEIS', 'A whole class in one go.', 'No copying and pasting student by student. The app matches its text to NEIS by class, number and name and enters it in a batch through the browser extension.',
    steps([('Connect', 'Link the Chrome extension to the open NEIS tab.'), ('Set the target', 'School year, grade and class, and the type of record.'), ('Match and enter', 'Class, number and name, entered in one batch.'), ('Save and confirm', 'After saving, the result is compared with the app’s text.')]) +
    notes(['Subject comments, autonomous activities and behavior notes are supported. Club and career records are not yet.', 'An existing record that differs from the selected text is replaced. An empty text is not entered.', 'The student roster can also be read from NEIS into a new sheet.']) +
    '<p class="micro">If NEIS screens change, some steps may behave differently. Always check the result before and after applying. The extension currently supports <code>cbe.neis.go.kr</code>, with more regions to follow after verification.</p>')
body += ('<section class="tinted"><div class="wrap storage" id="key"><p class="eyebrow">Before you start</p><h2>AI features need<br><em>a Gemini API key.</em></h2>'
    '<p class="section-lead">Writing and checking call the AI once per student, so running a whole class sends the calls one after another. On the free tier, request limits can make a batch stop or slow down partway through.</p><div class="data-grid">'
    + card('Without an API key', 'The table still works', '<p>Editing the table, entering Assist chips, and importing or exporting CSV and Excel all work. AI writing and checking do not.</p>')
    + card('Paid-tier API key · recommended', 'A whole class at once', '<p>With a key that has billing connected, a whole class can be written and checked without interruption. Usage is billed to the teacher’s own Google account.</p>', ' class="pick"', True)
    + '</div><p class="storage-note">The key is issued in Google AI Studio and entered in the app’s settings. Pricing and limits follow Google’s policy and can change, so check them when you get the key.</p></div></section>')
body += ('<section class="storage wrap" id="storage"><p class="eyebrow">Your data, explained</p><h2>Your work stays on your PC.<br><em>AI requests go to Google.</em></h2>'
    '<p class="section-lead">Student records are sensitive, so the app is explicit about where they go. Reviewed against the app source on 9 October 2026.</p><div class="data-grid">'
    + card('On this Windows PC', 'Sheets and settings', '<p>Writing sheets, student cell contents, generated text, preferences and prompt templates are saved in store.json in the Windows user profile. The separate check window uses store-check.json.</p><p class="small">The reviewed source does not sync these sheets to an Oni account cloud. These work files are not encrypted by the app.</p>')
    + card('Sent to the AI', 'Only what you run', '<p>Generation and checking send task prompts and the selected work content to Google Gemini, directly from the desktop app, using the teacher’s own API key.</p><p class="small">Local file storage does not mean that AI processing stays offline. Handle personal information such as real names following your school’s guidance.</p>', blue=True)
    + card('The API key', 'Kept on the PC', '<p>The app encrypts the saved key with Electron safeStorage (Windows DPAPI) when it is available.</p><p class="small">The current implementation falls back to plaintext key storage when OS encryption is unavailable.</p>')
    + card('NEIS', 'Only on request', '<p>Nothing is entered in NEIS until the teacher opens the apply dialog and confirms.</p><p class="small">The extension works only on the NEIS tab already open in the browser.</p>', blue=True)
    + '</div></section>')
body += ('<section class="tinted"><div class="wrap setup" id="start"><p class="eyebrow">Before your first class</p><h2>A clear place to begin.</h2><div class="setup-grid">'
    '<article><b>1</b><h3>Install the Windows beta</h3><p>Open the release page and run the installer. New versions arrive through the built-in updater.</p></article>'
    '<article><b>2</b><h3>Enter your Gemini API key</h3><p>Issue a key in Google AI Studio and paste it into the app’s settings. A paid-tier key is recommended.</p></article>'
    '<article><b>3</b><h3>Start with one class</h3><p>Bring in a roster from CSV, Excel, Google Sheets or NEIS, write a few students, check them, then apply.</p></article></div>'
    + faq([('Are these the app’s real screens?', 'Yes. They are screenshots of the app as it runs. Student names are pseudonyms.'),
           ('Is the AI’s text final?', 'No. Text written or corrected by AI must be reviewed and edited by the teacher before it is used.'),
           ('Which records can be applied to NEIS?', 'Subject comments, autonomous activities and behavior notes. Applying needs the Chrome extension installed and connected. Club and career records are written and checked in the app but not yet applied.'),
           ('Can I bring in existing work?', 'Yes. CSV, Excel and Google Sheets content can be imported, and check results can be exported to Excel.'),
           ('Is Oni Record available in English?', 'This product guide is in English. The application interface is Korean.')])
    + '</div></section>')
body += ('<section class="cta wrap"><span class="mark" aria-hidden="true"></span><h2>This term, spend less time<br>on student records.</h2><p>Oni Record · Windows desktop app · Beta v0.1.1-beta.9</p>'
    '<div class="actions"><a class="button primary" href="https://github.com/yang102948549/oni-record/releases" target="_blank" rel="noopener">View Windows releases ↗</a><a class="button" href="mailto:oniaby@onischool.net">Contact Oni School</a></div></section>')
write('record', page('record', 'Oni Record', 'Oni Record — Student records, written and checked in one table',
    'Oni Record is a Windows desktop app for Korean teachers. Type like a spreadsheet, pick keyword chips, draft with AI, check against the writing guidelines and apply to NEIS.',
    'assets/record/hero.webp', body, [('oni-class', 'Oni Class'), ('oni-proctor', 'Oni Proctor')]))

# ───────────────────────── Oni Proctor ─────────────────────────
A = '../assets/proctor/'
c = CAP['proctor']
def pshot(f, h, alt, label, cap=None, **kw):
    return shot(A + f, 1800, h, alt, label, (cap + ' · ' + c) if cap else c, **kw)
body = hero('Made for the exams office', 'A full exam roster.<br><em>Fair, and checked.</em>',
    'Enter the exam schedule, the rooms and each teacher’s conditions. Oni Proctor assigns every seat without breaking a rule, evens out the load between teachers, lets you swap by hand, and exports the roster to Excel.',
    '<a class="button primary" href="#tour">Explore the app <span>↓</span></a><a class="button" href="#start">Release status <span>↗</span></a>',
    'Windows desktop app · Korean interface · Works offline · In development',
    pshot('assign.webp', 1125, 'Oni Proctor assignment table: teachers in rows, exam days and periods in columns, each cell showing the room a teacher proctors, with a score for every teacher', 'assignment table', lazy=False),
    [('Set up', 'Exam days, periods, subjects and rooms.'), ('Teachers', 'Subjects, homerooms and the periods each teacher can cover.'), ('Assign', 'Every rule kept, the load balanced.'), ('Adjust and export', 'Swap by hand, then save as Excel.')])
body += intro('A closer look', 'Less balancing by hand.<br>More certainty before you print.', 'Follow the real interface through eight parts of the job, in the order the left menu lays them out. Click any screen to inspect it at full size.')
body += chapter('screen', '01 / The screen', 'The menu follows the job.', 'Exam setup, teachers, the assignment table, then records. Each menu splits into two or three tabs, and everything is edited in place.',
    pshot('screen.webp', 1125, 'Oni Proctor exam setup screen with five numbered markers: new exam button, workspace menu, page tabs, top bar, and the work area with rooms by grade', 'annotated screen', 'Exam setup with the sample exam loaded',
          pins=[(1, 17.5, 10.3), (2, 12, 16.4), (3, 40, 17.5), (4, 83, 3), (5, 52, 62)]) +
    notes([('New exam', 'Start a blank exam, or open the sample to look around.'), ('Workspace menu', '<span class="ko">시험 설정</span>, <span class="ko">교사 설정</span>, <span class="ko">배정표</span> and <span class="ko">기록</span>, in working order. The sidebar can be collapsed.'),
           ('Page tabs', 'Such as schedule and rooms, then mode and scoring.'), ('Top bar', 'Current exam, undo and redo, license status, import and export of exam files.'), ('Work area', 'Cards and tables you edit in place. Chips open a picker.')]) +
    tip('Saving', 'Input is saved automatically a moment after you type, and Ctrl+S saves at once. Each exam is kept as its own record, so last term’s exam can be reopened.'))
body += chapter('setup', '02 / Schedule and rooms', 'The schedule decides which seats exist.', 'A seat is a place a proctor is needed: a room in a period, or a corridor zone. Register the rooms, add exam days, then type the subject for each period and grade.',
    pshot('schedule.webp', 1125, 'Rooms listed by grade, corridor zones, and three exam days shown as cards with a period by grade table of subjects', 'schedule screen', 'Rooms by grade and three exam days') +
    '<div class="pair">' + shot(A + 'room-picker.webp', 1000, 930, 'Dialog for a period: the subject English applied to rooms 1-1 and 1-2, with a second subject row ready to be added', 'subject and room picker', 'The subject and room picker for one period and grade.') +
    notes([('Register rooms by grade', 'Add classes one at a time or several at once, then corridor zones and special rooms.'), ('Add exam days and periods', 'Each day is a card with its own number of periods.'),
           ('Type the subject into each cell', 'Arrow keys move between cells and Enter moves down, like a spreadsheet.'), ('Split a cell when classes differ', 'Add a second subject and choose which rooms each one applies to. Nothing changes until you confirm.')]) + '</div>' +
    tip('How seats are made', 'A corridor seat is created only in periods that have an exam. If every subject in a period is self-study, no corridor seat is made.'), True)
body += chapter('mode', '03 / Mode and scoring', 'Decide what counts as a fair share.', 'Choose how rooms are staffed and how much each kind of duty weighs. The engine balances teachers on the score these weights produce.',
    pshot('settings.webp', 640, 'Settings: a switch for chief and assistant proctor mode, weights of 2 for classroom and 1 for corridor duty, and reference counts', 'mode and scoring screen', 'Mode, weights and reference counts') +
    notes([('Choose the proctoring mode', 'Regular mode places one proctor per room plus corridor duty. <span class="ko">정/부감독</span> mode places a chief and an assistant, with rooms you mark as single-proctor.'),
           ('Set the weights', 'By default a classroom duty counts 2 points and a corridor duty 1. Any value of zero or more, including decimals, can be used.'),
           ('Set reference counts', 'Limits such as classroom duties over the whole exam or corridor duties in a day raise a warning when exceeded.')]) +
    tip('Good to know', 'Reference counts are warnings, not limits: they never block an assignment. In chief and assistant mode every duty counts as 1 point.'))
body += chapter('teachers', '04 / Teacher list', 'Conditions come from one table.', 'Bring in the list, then set each teacher’s subjects, homeroom and blocked classes with a click. A preview shows how columns were matched and which rows have problems.',
    pshot('teachers.webp', 1125, 'Teacher table with columns for name, subject, homeroom, blocked classes and role. Two teachers have special roles', 'teacher list screen', 'The teacher list with two special roles set') +
    notes([('Bring in the list', 'Type it, paste a table, open an Excel, CSV or TSV file, use a Google Sheets link, or search a school in Comcigan’s public data.'),
           ('Click a chip to set conditions', 'Subjects (more than one allowed), one homeroom class, and any classes the teacher must not proctor.'),
           ('Set the role', 'Most are regular teachers. Roles such as roaming or corridor-only change where that teacher may be placed.')]) +
    tip('Why it matters', 'A teacher is never placed in their own homeroom, in a blocked class, or in a period when their own subject is being examined. Those rules come from this table.'), True)
body += chapter('times', '05 / Who can cover when', 'Tick the exceptions, not the whole grid.', 'Regular teachers are available in every period unless you say otherwise. Special teachers work the other way round: they are placed only in the periods you tick.',
    pshot('special.webp', 1000, 'A grid of exam days and periods with checkboxes for two special teachers, and a seat preference for each', 'special teacher screen', 'Special teachers: periods they proctor and where they sit') +
    pshot('blocked.webp', 1125, 'A grid of regular teachers by exam period with checkboxes for periods they cannot proctor, and a reason field', 'unavailable periods screen', 'Regular teachers: only the periods they cannot cover') +
    notes([('Special teachers', 'Part-time lecturers, non-subject, roaming and corridor-only teachers are placed in the periods you tick, and are used in those periods whenever possible.'),
           ('Seat preference', 'Classroom and corridor, or corridor only. A “corridor first” teacher can still cover a classroom when proctors run short.'),
           ('Unavailable periods', 'For regular teachers, tick only what is not possible, such as a business trip or childcare hours, with the reason beside it.')]))
body += chapter('assign', '06 / Automatic assignment', 'Rules first, then fairness.', 'One button works out the whole roster. Hard rules are never relaxed to fill a seat or to improve a score, and the same rules apply when you edit by hand.',
    pshot('assign.webp', 1125, 'Assignment result by teacher, with a summary of seats filled, unassigned seats, count warnings and unmet designated placements', 'assignment result screen', 'Gray cells show why a teacher is not free in that period, such as their own subject’s exam') +
    '<div class="data-grid">'
    + card('Hard rules', 'Rules that never bend', '<ul><li>No excluded teachers and no unavailable periods</li><li>No own homeroom and no blocked class</li><li>No period in which the teacher’s own subject is examined</li><li>One seat per teacher in a period, one teacher per seat</li></ul>')
    + card('Priorities', 'Then, in this order', '<ol><li>Place special teachers in the periods set for them</li><li>Fill as many seats as possible</li><li>Respect seat preferences</li><li>Narrow the gap between the highest and lowest score</li><li>Bring everyone closer to the average</li></ol>', blue=True)
    + card('Time', 'About ten seconds', '<p>The solver works for roughly ten seconds and returns the best roster it found. It states whether that roster was proven optimal or not. You can cancel, and the previous result is kept.</p>')
    + card('Validation', 'Checked a second time', '<p>A separate checker validates every result. The summary shows seats filled, unassigned seats, count warnings and unmet placements.</p>', blue=True)
    + '</div><p class="micro">A teacher’s score in regular mode is classroom duties × the classroom weight plus corridor duties × the corridor weight. “Optimal” refers to the conditions you entered: it does not mean that a condition missing from the input was taken into account.</p>', True)
body += chapter('adjust', '07 / Review and adjust', 'Swap by hand. The rules still hold.', 'Real schools have exceptions. Manual changes are held as a draft until you apply them, and every move is checked against the same rules.',
    steps([('Review', 'Scores, empty seats and warnings, by teacher or by room.'), ('Swap or move', 'Click two cells in the same period, or pick a teacher for a seat.'), ('Apply changes', 'Validated and saved. Until then you can undo or cancel.')], ' three') +
    pshot('swap.webp', 1125, 'Teacher view with one cell selected. Cells in the same period that can be swapped with it are highlighted', 'swap screen', 'Teacher view: select a cell and the cells it can be exchanged with light up', style=' style="margin-top:30px"') +
    pshot('rooms.webp', 700, 'Room view: rooms in rows, exam periods in columns, each cell naming the assigned proctor', 'room view screen', 'Room view: click a seat to see who can take it and why others cannot') +
    '<div class="pair">' + shot(A + 'verify.webp', 800, 335, 'Validation dialog listing one warning: a teacher has two corridor duties on one day against a reference of one', 'validation dialog', 'The validation list names the teacher, the day and the count behind each warning.') +
    notes(['A swap or assignment that would break a rule is refused, and the reason is shown.', 'Changes stay in a draft state across pages until you apply them. Undo and cancel work on the draft.', 'Empty teacher cells can receive a duty, so a seat can be moved as well as swapped.', 'After a manual change, the earlier “proven optimal” label is no longer shown.']) + '</div>')
body += chapter('export', '08 / Export', 'Print-ready Excel, and files you can move.', 'When the roster is settled, save it as a workbook laid out for printing, and keep the whole exam as a file you can back up.',
    '<div class="pair">' + shot(A + 'export.webp', 800, 735, 'Export dialog: pick exam days, choose a layout by teacher, by room or both, and include the full assignment table', 'export dialog', 'Excel export options.') +
    notes([('A4 landscape', 'Daily rosters are laid out to print on A4 landscape. Pick which exam days to include.'), ('By teacher, by room, or both', 'Both can sit side by side on one sheet.'),
           ('Full table', 'A full table can be added, with each teacher’s total duties and score.'), ('Exam file', 'The whole exam exports as a JSON file. An imported exam is added as a new record and never overwrites an existing one.')]) + '</div>', True)
body += ('<section class="storage wrap" id="offline"><p class="eyebrow">Before you start</p><h2>It runs on one PC,<br><em>without the internet.</em></h2>'
    '<p class="section-lead">The assignment engine is built into the app. Setting up, assigning, adjusting, saving and exporting all work offline, and nothing else needs to be installed.</p><div class="data-grid">'
    + card('What you prepare', 'The facts of the exam', '<p>Exam dates and periods, the subjects for each grade, the rooms, and the teacher list with subjects and homerooms.</p>')
    + card('What the app does not guess', 'Missing conditions', '<p>A homeroom, role or blocked class that is missing from your source is not filled in for you. The result is only as complete as the conditions you enter.</p>', ' class="pick"', True)
    + '</div><p class="storage-note">The internet is used only when you choose to import a teacher list or timetable from a Google Sheets link or from Comcigan’s public timetable data.</p></section>')
body += ('<section class="tinted"><div class="wrap storage" id="storage"><p class="eyebrow">Your data, explained</p><h2>Everything stays on your PC.<br><em>Imports are the only exception.</em></h2>'
    '<p class="section-lead">Based on the app’s documentation and source as of October 2026.</p><div class="data-grid">'
    + card('On this Windows PC', 'Exams and teachers', '<p>Each exam is saved as a file in the Windows user profile, separate from the program folder, together with the last good copy.</p><p class="small">A damaged file is reopened from that copy and the app says so.</p>')
    + card('No account', 'No cloud sync', '<p>The app does not upload teacher or exam data. Syncing to a cloud is outside its scope.</p><p class="small">To move an exam to another PC, export it as a JSON file.</p>', blue=True)
    + card('Online imports', 'Only when you ask', '<p>Fetching a Google Sheets link or Comcigan’s public timetable data is a request you start.</p><p class="small">It does not sign in to an account or keep syncing afterwards.</p>')
    + card('The engine', 'Calculated on the PC', '<p>The assignment engine runs inside the app. The roster is not sent to a server to be solved.</p><p class="small">Automatic saving protects against a crash, not against a lost PC. Keep a JSON export as a backup.</p>', blue=True)
    + '</div></div></section>')
body += ('<section><div class="wrap setup" id="start"><p class="eyebrow">Release status</p><h2>In development.<br><em>Not yet released.</em></h2><div class="setup-grid">'
    '<article><b>1</b><h3>Open the sample exam</h3><p>The app ships with a fictional exam so you can look around every screen before entering anything.</p></article>'
    '<article><b>2</b><h3>Set up your own exam</h3><p>Rooms, exam days and subjects first, then the teacher list and each teacher’s conditions.</p></article>'
    '<article><b>3</b><h3>Assign, adjust, export</h3><p>Run the assignment, read the warnings, swap where needed, then save the Excel roster.</p></article></div>'
    + faq([('Can I download it now?', 'Not yet. There is no public download. Release and licensing details will be published on this page when it is ready.'),
           ('Does it need the internet?', 'No, for the core work. Assignment, adjustment, saving and export run offline. Importing from Google Sheets or Comcigan needs a connection.'),
           ('What does “optimal” mean here?', 'It means no better roster exists for the conditions you entered. It does not check whether a real-world condition was left out of the input.'),
           ('Can a seat stay empty after a run?', 'Yes. If no teacher is allowed to take a seat, it stays empty and is reported. The rules are not relaxed to fill it.'),
           ('Are these the app’s real screens?', 'Yes. They were captured from the app’s own interface running its built-in sample exam. All names are fictional.'),
           ('Is Oni Proctor available in English?', 'This product guide is in English. The application interface is Korean.')])
    + '</div></section>')
body += ('<section class="cta wrap"><span class="mark" aria-hidden="true"></span><h2>Spend exam week<br>on the exam.</h2><p>Oni Proctor · Windows desktop app · In development</p>'
    '<div class="actions"><a class="button primary" href="mailto:oniaby@onischool.net">Ask about release</a><a class="button" href="../">All Oni apps</a></div></section>')
write('proctor', page('proctor', 'Oni Proctor', 'Oni Proctor — A full exam roster, fair and checked',
    'Oni Proctor is a Windows desktop app for Korean schools. Enter the exam schedule, rooms and teacher conditions, assign proctors automatically, adjust by hand and export the roster to Excel.',
    'assets/proctor/assign.webp', body, [('oni-class', 'Oni Class'), ('oni-record', 'Oni Record')]))

# ───────────────────────── Home (ecosystem hub) ─────────────────────────
APPS = [
 ('class', 'Oni Class', '#007aff', 'Beta', 'beta', 'assets/class/calendar.png', 'Oni Class calendar and daily details',
  'A homeroom teacher’s workspace for calendars, timetables, student rosters, attendance and submissions. Built around the Windows desktop, with selected records available on mobile.',
  [('oni-class/', 'Full tour →'), ('https://github.com/yang102948549/oni-class/releases', 'Windows beta ↗')]),
 ('record', 'Oni Record', '#e05252', 'Beta', 'beta', 'assets/record/hero.webp', 'Oni Record table of students with the Write panel',
  'Draft student records from observation notes and keyword chips, check the wording against the writing guidelines, and apply teacher-approved text to NEIS.',
  [('oni-record/', 'Full tour →'), ('https://github.com/yang102948549/oni-record/releases', 'Windows beta ↗')]),
 ('proctor', 'Oni Proctor', '#149c95', 'In development', 'dev', 'assets/proctor/assign.webp', 'Oni Proctor assignment table by teacher',
  'Assigns exam proctors across rooms and periods from the schedule and each teacher’s conditions, keeps the load even, and exports the roster to Excel. Not yet released.',
  [('oni-proctor/', 'Full tour →')]),
]
PLANNED = [
 ('Oni Time', '#8b65d8', 'Planned', 'The next Oni tool, for school timetable work. Features and supported platforms will be announced during development.'),
 ('Oni Enrollment', '#e58a32', 'Planned', 'A planned tool for elective course registration and seat management.'),
]
strip = ''.join(f'<a href="oni-{k}/"><span class="mark" style="--mark:{col}" aria-hidden="true"></span><b>{n}</b><span class="st">{st}</span></a>' for k, n, col, st, *_ in APPS)
strip += ''.join(f'<a href="#apps"><span class="mark" style="--mark:{col}" aria-hidden="true"></span><b>{n}</b><span class="st">{st}</span></a>' for n, col, st, _ in PLANNED)
cards = ''
for k, n, col, st, stc, img, alt, desc, links in APPS:
    ln = ''.join(f'<a href="{h}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') + f'>{t}</a>' for h, t in links)
    cards += (f'<article class="app-card" style="--mark:{col}"><a class="thumb" href="oni-{k}/" aria-label="{n} tour"><img src="{img}" alt="{alt}" loading="lazy" width="1440" height="900"></a>'
              f'<div class="body"><div class="head"><span class="mark" aria-hidden="true"></span><h3>{n}</h3><span class="status {stc}">{st}</span></div><p>{desc}</p>'
              f'<p class="micro">Windows desktop · Korean interface</p><div class="links">{ln}</div></div></article>')
planned = ''.join(f'<article class="app-card" style="--mark:{col}"><div class="body"><div class="head"><span class="mark" aria-hidden="true"></span><h3>{n}</h3><span class="status">{st}</span></div><p>{d}</p></div></article>' for n, col, st, d in PLANNED)
home = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Oni School — Tools for Korean school teachers</title>
<meta name="description" content="Oni School is a family of desktop tools for Korean school teachers. Browse every app, its status, and a tour of how each one works.">
<link rel="canonical" href="https://onischool.net/">
<meta property="og:title" content="Oni School — Tools for Korean school teachers">
<meta property="og:description" content="Oni School is a family of desktop tools for Korean school teachers. Browse every app, its status, and a tour of how each one works.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://onischool.net/">
<meta property="og:image" content="https://onischool.net/assets/class/calendar.png">
<link rel="stylesheet" href="assets/app.css">
</head>
<body class="app-home">
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
<a class="brand" href="#"><span class="mark" aria-hidden="true"></span>Oni School</a>
<nav aria-label="Page navigation">
<a href="#apps">Apps</a>
<a href="#platform">Platform</a>
<a href="#contact">Contact <span>↗</span></a>
</nav>
</header>
<main id="main">
<section class="hero wrap">
<p class="eyebrow">Tools for teachers · Made in Korea</p>
<h1>Less paperwork.<br><em>More time for teaching.</em></h1>
<p class="lead">Oni School is a family of desktop tools for Korean school teachers. Each app takes on one part of school work, and each has its own page with a tour of the interface, its data handling and its release status.</p>
<div class="actions"><a class="button primary" href="#apps">See the apps <span>↓</span></a><a class="button" href="#contact">About Oni School</a></div>
<p class="micro">Two apps in beta · One in development · Two planned</p>
<div class="steps five">{strip}</div>
</section>
<section class="chapter" id="apps"><div class="wrap">
<div class="chapter-heading"><div><p class="eyebrow">The apps</p><h2>A focused tool for each part of the job.</h2></div><p>Open an app’s tour to see its screens, workflow and data handling. Each app is a separate download with its own release status.</p></div>
<div class="apps">{cards}</div>
<div class="apps two">{planned}</div>
</div></section>
<section class="tinted"><div class="wrap setup" id="platform">
<p class="eyebrow">The platform</p><h2>Different jobs, one way of working.</h2>
<div class="setup-grid">
<article><b>1</b><h3>One look across every app</h3><p>A color-coded switch icon for each app, and the same calm layout, type and controls inside.</p></article>
<article><b>2</b><h3>Built around Korean school work</h3><p>Korean interfaces that follow real school routines, including the steps that end in NEIS, the national school information system.</p></article>
<article><b>3</b><h3>Data handling stated per app</h3><p>Storage differs from app to app, so each tour says what stays on the PC and what leaves it.</p></article>
</div></div></section>
<section class="storage wrap" id="contact">
<p class="eyebrow">About Oni School</p><h2>Built from the everyday work of a school.</h2>
<div class="data-grid">
<article><span class="data-label">Who makes it</span><h3>A teacher, building for teachers</h3><p>Oni School is an education software project developed and operated by Oniaby, a Korean teacher building tools to reduce repetitive school administration.</p><p class="small">We distinguish available features from work that is still in development.</p></article>
<article><span class="data-label">Contact</span><h3>Questions and feedback</h3><p class="contact-mail"><a href="mailto:oniaby@onischool.net">oniaby@onischool.net</a></p><button type="button" class="copy" data-copy-email>Copy email address</button><span id="copy-status" role="status" aria-live="polite"></span><p class="small">We welcome messages in Korean or English.</p></article>
</div>
</section>
</main>
<footer class="wrap footer">
<a class="brand" href="#">Oni School</a>
<span>© 2026 Oni School · Oniaby</span>
<span><a href="oni-class/">Oni Class</a> · <a href="oni-record/">Oni Record</a> · <a href="oni-proctor/">Oni Proctor</a></span>
</footer>
<script src="assets/app.js"></script>
</body>
</html>
'''
open(ROOT + 'index.html', 'w', encoding='utf-8', newline='\n').write(home)
print('home', len(home))
