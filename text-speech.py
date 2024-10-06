from gtts import gTTS

text="vanakkam da mapla...,   thenila irunthu"

language='en'

obj=gTTS(text=text,lang=language,slow=False)

obj.save('sample.mp3')