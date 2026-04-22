from gtts import gTTS
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def text_to_audio(text, filename):
    if not filename.endswith(".mp3"):
        filename += ".mp3"

    tts = gTTS(text=text)
    tts.save(filename)

    return True, filename


def text_to_pdf(title, text, filename):
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

   
    content.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    content.append(Spacer(1, 20))

    
    content.append(Paragraph(text, styles['Normal']))

    doc.build(content)

    return True, filename