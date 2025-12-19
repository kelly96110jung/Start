import os
import json
from google import genai
from typing import Optional, Dict, Any

# Gemini 클라이언트 초기화 (API 키를 환경 변수에서 자동 로드)
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_KEY:
    print("오류: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다. 터미널을 확인하세요.")
    exit()

client = genai.Client(api_key=GEMINI_KEY)
def summarize_medical_text(medical_text: str) -> Optional[Dict[str, Any]]:
    """
    주어진 진료 텍스트를 LLM(Gemini)을 사용하여 요약하고 쉬운 말로 변환
    결과는 JSON 형식으로 요청하여 파싱
    """
    # LLM에 전달할 Prompt(프롬프트)
    # 결과의 신뢰도를 높이기 위해 JSON 출력을 강제하고 필요한 필드를 지정합니다.
    prompt = f"""
    당신은 환자의 이해도를 높이는 의료 보조 AI입니다.
    아래 진료 텍스트를 분석하여 일반인이 이해하기 쉽도록 정리해 주세요.
    
    출력은 반드시 다음 세 가지 키를 가진 **JSON 형식**으로만 반환해야 합니다:
    1. "key_summary": 진료의 핵심 내용을 3가지 항목으로 요약한 리스트 (List of strings).
    2. "easy_explanation": 전문 용어를 쉬운 말로 풀이한 일반인 대상의 설명 (String).
    3. "next_steps": 처방, 다음 예약, 주의사항 등 환자가 해야 할 다음 조치 (String).

    진료 텍스트: "{medical_text}"
    """

    try:
        # Gemini API 호출 (LLM 모델 실행)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                {"role": "user", "parts": [{"text": prompt}]}
            ],
            config=genai.types.GenerateContentConfig(
                # JSON 출력 요청
                response_mime_type="application/json",
            )
        )
        
        # JSON 응답 파싱
        # Gemini 응답 텍스트(string)를 Python 딕셔너리로 변환
        json_output = json.loads(response.text)
        return json_output

    except Exception as e:
        print(f"API 호출 중 오류가 발생했습니다: {e}")
        return None

def print_formatted_summary(summary_data: Dict[str, Any]):
    """
    콘솔에 요약 결과 출력
    """
    print("\n" + "═"*60)
    print("진료 설명 자동 요약 결과")
    print("═"*60)

    # 1. 쉬운 말 변환 출력
    print("\n## 일반인 대상 쉬운 말 설명:")
    print(summary_data.get("easy_explanation", "정보 없음"))

    # 2. 핵심 요약 출력
    print("\n## 진료 핵심 요약:")
    for i, item in enumerate(summary_data.get("key_summary", [])):
        # 리스트 형태의 요약 출력
        print(f"  - {item}")
        
    # 3. 다음 조치 출력
    print("\n## 다음 조치 및 주의사항:")
    print(summary_data.get("next_steps", "정보 없음"))
    
    print("═"*60 + "\n")

# =========================================================
# 메인 실행 블록: 사용자가 임의의 텍스트를 입력하고 처리하는 부분
# =========================================================
if __name__ == "__main__":
    # 5. 임의의 진료 텍스트 정의 (나중에 앱의 STT 결과가 들어갈 부분)
    input_text = """
    환자분은 고혈압과 당뇨가 만성적으로 있으시니, 이번에 처방한 메트포르민(Metformin)은 식후 30분에 꼭 복용해 주시고요.
    혈압약인 암로디핀(Amlodipine)은 아침에 한 번 드시면 됩니다.
    그리고 다음 주 화요일 오전 10시에 혈당 검사를 위해 재방문해 주세요.
    특히 짠 음식은 심장에 부담을 줄 수 있으니 저염식으로 식단을 조절하셔야 합니다.
    """
    
    print("--- 입력된 진료 텍스트 (STT 결과) ---")
    print(input_text.strip())
    print("--------------------------------------\n")

    # 요약 함수 호출
    summary = summarize_medical_text(input_text)

    if summary:
        # 결과 출력
        print_formatted_summary(summary)
    else:
        print("요약 생성에 실패했습니다. API 키 또는 네트워크 연결을 확인하세요.")
