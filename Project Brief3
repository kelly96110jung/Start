# Project Scenario – 진료 음성 기반 의료 설명 자동 요약 앱

| 항목 | 내용 |
|------|------|
| **프로젝트명** | 진료실 음성 기반 의료 설명 자동 요약 및 이해도 향상 앱 |
| **프로젝트 키워드** | Healthcare · AI · Speech-to-Text · On-device STT · Privacy-preserving |
| **트랙** | 헬스케어 · 정보 접근성 · 의료 AI 보조도구 |
| **프로젝트 멤버** | 정아윤, 이다은, 임하령 |
| **팀 지도 교수** | 윤명국 교수님 |
| **무엇을 만들고자 하는가** | 고령자나 보호자 입장에서는 의료 용어를 이해하기 어렵고, 진료실에서 들은 설명을 집에 돌아와 기억하기도 어렵다. 환자의 보호자나 가족이 병원에 동행하지 않으면 정보 격차가 발생하기도 한다. 이를 해결하기 위해, 진료실에서 의사의 설명을 환자 스마트폰에서 **온디바이스 STT(음성→텍스트)** 로 변환하고, 이후 AI가 내용을 **요약·쉬운말 변환·비용 범위 안내**를 제공하는 앱을 만들고자 한다. 음성은 기기 내부에서만 처리하여 외부 유출을 방지하고, 텍스트 기반 보조 설명만 서버에서 가공한다. |
| **고객 (페르소나)** | - **김정순 (74세·고혈압/당뇨)**: 진료를 듣지만 용어가 어려워 기억하기 힘들다. 의사 설명을 앱으로 자동 요약해 재확인한다.<br><br>- **이도훈 (43세·보호자)**: 부모님 진료에 동행하지 못할 때 의료 내용을 이해하기 어렵다. 생성된 요약으로 진료 내용을 정확히 파악한다.<br><br>- **박서윤 (29세·퇴근 후 병원 방문)**: 혼자 진료받을 때 의사 설명을 빠르게 메모하기 어렵다. 앱의 요약 기능으로 부담을 줄인다.<br><br>- **초진 환자들**: 치료 옵션과 비용 설명을 다시 보고 싶어 정보를 정리한 문서를 자동 생성해 도움이 된다. |
| **Pain Point** | - 의료 용어와 설명이 난해하여 환자·보호자가 이해하기 어려움<br>- 진료 중 메모나 녹음을 하더라도 내용 정리가 어려움<br>- 음성 데이터를 외부 서버에 올리기에는 개인정보보호 우려 큼<br>- 기존 서비스는 “의학 정보 제공” 중심으로 진료 내용 기반 요약 기능이 부족함 |
| **핵심 기능 (AI 적용)** | 1) **온디바이스 STT 기반 실시간 텍스트 변환**: 음성을 외부 서버로 보내지 않고 스마트폰에서만 처리하여 개인정보 보호.<br>2) **의료 설명 요약/쉬운말 변환**: 의사 설명을 핵심만 정리하고 일반인이 이해하기 쉬운 표현으로 재구성.<br>3) **치료 옵션/행정 정보 안내**: 의사가 언급한 치료 방법·수납 절차·주의사항 등을 자동 정리.<br>4) **진료 기록 생성**: 요약 텍스트 기반으로 사용자에게 “오늘 진료 한눈에 보기” 형태 문서 자동 생성. |
| **사용할 소프트웨어** | - **앱 제작:** FlutterFlow 또는 React Native<br>- **AI 요약 서버:** Firebase Functions 또는 FastAPI<br>- **데이터 저장:** Firebase Firestore (요약본/메모), 로컬 기기 암호화 스토리지(STT 로그 제거)<br>- **STT 엔진:** Android SpeechRecognizer(on-device), iOS Speech Framework(On-device Recognition) |
| **사용할 소프트웨어 패키지의 명칭과 URL** | - FlutterFlow: <https://flutterflow.io/><br>- React Native: <https://reactnative.dev/><br>- Firebase: <https://firebase.google.com/><br>- Firebase Functions: <https://firebase.google.com/docs/functions><br>- iOS Speech Framework: <https://developer.apple.com/documentation/speech><br>- Android SpeechRecognizer: <https://developer.android.com/reference/android/speech/SpeechRecognizer> |
| **데이터** | - 진료 음성 → 온디바이스 STT 텍스트 (음성 원본 저장 X)<br>- 사용자 프로필: 연령, 질환(선택), 진료 이력<br>- 요약 결과: 핵심 설명, 치료 옵션, 주의점<br>- 사용자 메모 및 저장한 진료 기록<br>- 텍스트 기반 AI 분석 결과(비의료적·정보 요약 수준) |
| **팀그라운드룰 URL** | <https://github.com/kelly96110jung/Start/blob/main/GroundRule.md> |
