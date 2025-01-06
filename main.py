##### 기본 정보 입력 ####
# OpenAI API 설정 패키지
from dotenv import load_dotenv
from openai import OpenAI

# 스트림릿 패키지
import streamlit as st

# load_dotenv()
# client = OpenAI()





##### 기능 구현 함수 정리 ####
def askGpt(prompt, apikey):
  client = OpenAI(api_key=apikey)
  response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{'role': 'user', 'content': prompt}]
  )
  gptResponse = response.choices[0].message.content

  return gptResponse





##### 메인 함수 ####
def main():
  st.set_page_config(page_title='요약 프로그램')

  # session_state 초기화
  if 'OPENAI_API' not in st.session_state:
    st.session_state['OPENAI_API'] = ''

  # 사이드바
  with st.sidebar:
    # OpenAI API 키 입력 받기
    openai_apikey = st.text_input(
      label='OPENAI API 키',
      placeholder='Enter Your API Key',
      value='',
      type='password'
    )

    # 세션 스테이트에 저장
    if openai_apikey:
      st.session_state['OPENAI_API'] = openai_apikey
    st.markdown('---')


  # 메인 공간
  st.header('📄요약 프로그램')
  st.markdown('---')

  text = st.text_area('요약할 글을 입력하세요.')
  if st.button('요약'):
    prompt = f'''
      **Instructions** :
      - You are an expert assistant that summarizes text into **Korean language**.
      - Your task is to summarize the **text** sentences in **Korean language**.
      - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
      -text : {text}
    '''
    st.info(askGpt(prompt, st.session_state['OPENAI_API']))

if __name__=='__main__':
  main()