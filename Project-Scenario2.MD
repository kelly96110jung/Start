# Project Scenario – 자유여행자를 위한 숙소·테마 기반 AI 여행 일정 플래너

| 항목 | 내용 |
|------|------|
| **프로젝트명** | 자유여행자를 위한 숙소·테마 기반 AI 여행 일정 플래너 |
| **프로젝트 키워드** | Travel · AI · Open Data · Personalization · Itinerary |
| **트랙** | 스마트라이프 · 여행 · 공공데이터 활용 |
| **프로젝트 멤버** | 정아윤, 이다은, 임하령 |
| **팀 지도 교수** | 윤명국 교수님 |
| **무엇을 만들고자 하는가** | 사용자가 **도시, 숙소 위치(1개 이상), 여행 기간, 테마, 필수 방문지, 제약 조건(예: 도보 한도)** 등을 입력하면, 공공데이터 기반으로 **개인화된 일정 후보(플랜 A/B)**를 자동 생성·비교할 수 있는 앱. 숙소가 여러 곳일 경우, 각 숙소를 기준으로 일정을 분할하고 **숙소 이동일도 자동 반영**한다. 실제 길안내는 외부 지도 앱을 연동하고, 본 앱은 **테마·제약 반영, 필수 방문지 포함, 대안 플랜 생성**에 초점을 둔다. |
| **고객 (페르소나)** | - **김지현 (25세, 대학생 – 단기 여행자)**: 시험 끝나고 3박4일 도쿄 여행. “문화 중심/맛집 중심” 두 플랜을 비교해 선택.<br><br>- **박수연 (34세, 직장인 – 커플 여행자)**: 2박3일 파리. 준비 시간 부족 → 앱이 제공하는 **유적지+맛집 일정**으로 빠르게 계획을 완성.<br><br>- **이도훈 (40세, 가족 여행자)**: 4박5일 미국 여행. 뉴욕(2박) + 보스턴(2박)으로 숙소를 옮기는 일정이라 복잡했는데, 앱이 **숙소 A/B 기준으로 분할 일정**을 자동 생성해 계획 수립이 훨씬 수월해짐. 또, “꼭 방문하고 싶은 장소(자유의 여신상)”을 폼에서 입력해 일정에 반영. |
| **Pain Point** | - 여행지는 많지만 **방문 순서**를 만드는 게 가장 번거롭다.<br>- 운영시간·휴무일 확인을 누락해 허탕치는 경우 발생.<br>- 패키지는 획일적이고, 자유여행은 직접 설계 부담이 크다.<br>- 기존 서비스는 장소 리스트 추천 위주이며, **대안 일정·숙소 이동 반영·필수 방문지 반영**이 부족하다. |
| **핵심 기능 (AI 적용)** | 1) **자동 일정 생성·비교**: 도시/숙소/기간/테마/제약 입력 → **플랜 A/B** 생성<br>2) **필수 방문지 반영**: 사용자가 지정한 장소는 반드시 일정에 포함<br>3) **다중 숙소 반영**: 숙소가 여러 곳일 경우, 숙소별 분할 일정 + 이동일 자동 생성<br>4) **테마·제약 반영**: 문화/맛집/유적지 가중치, 도보 한도(슬라이더), 필수 방문지 포함 규칙<br>5) **운영정보 필터링**: 휴무일·운영시간 충돌 장소 자동 제외<br>6) **지도 연동**: 각 장소에 구글 지도 버튼 제공 |
| **사용할 소프트웨어** | - **앱 제작:** Glide, FlutterFlow (노코드/로우코드)<br>- **데이터 저장:** Airtable, Google Sheets<br>- **지도 연동:** Google Maps 딥링크<br>- **데이터 소스:** 공공데이터 (예: 한국=TourAPI, 일본=Tokyo Open Data, 미국=NPS API, 대만=TDX API, 싱가포르=data.gov.sg) + Wikidata/Wikipedia, OpenStreetMap(보완용) |
| **사용할 소프트웨어 패키지의 명칭과 URL** | - Glide: https://glideapps.com/<br>- FlutterFlow: https://flutterflow.io/<br>- Airtable: https://airtable.com/<br>- Google Sheets: https://workspace.google.com/<br>- Google Maps: https://maps.google.com/<br>- TourAPI(한국): https://www.data.go.kr/<br>- Tokyo Open Data: https://catalog.data.metro.tokyo.lg.jp/<br>- NPS API(미국): https://www.nps.gov/subjects/developer/api-documentation.htm<br>- TDX API(대만): https://tdx.transportdata.tw/<br>- data.gov.sg(싱가포르): https://data.gov.sg/ |
| **데이터** | - 공공 관광 데이터 API(국가/도시 포털)에서 장소명·좌표·태그·운영시간·휴무일·이미지 수집<br>- 내부 테이블에 테마 태그/권역/평점/운영정보 캐시 |
| **팀그라운드룰 URL** | https://github.com/kelly96110jung/Start/blob/main/GroundRule.md |
| **최종 수정일** | 2025-09-21 |
