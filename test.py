


import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)

text1 = """김기현 의원은 "자신들의 거짓과 위선이 드러나기 시작하자 반성하기는커녕 느닷없이 현직 대통령 탄핵을 운운하고 있으니 그 처지가 애잔하다"며 "민주당은 신성한 촛불을 모욕하는 헛된 짓을 집어 치우고 권력형 부정부패의 몸통인 이재명 대표에 대한 탄핵이나 제대로 하길 충언한다"고 했다."""

translator = Translator()

print(translator.detect(text1))
trans1 = translator.translate(text1, src='ko', dest='en')
print("English to Japanese: ", trans1.text)


from gtts import gTTS
tts = gTTS(trans1.text, lang="zh-cn")
tts.save('media/hello.mp3')
