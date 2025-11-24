<h1>Project Scenario – CareMap: 치료 단계 기반 의료 행정·지원 네비게이션 앱 (반복 이용 구조 강조 포함)</h1>

<table>
  <tr>
    <th>항목</th>
    <th>내용</th>
  </tr>
  <tr>
    <td><strong>프로젝트명</strong></td>
    <td>CareMap – 치료 단계 기반 의료 행정·지원 안내 플랫폼</td>
  </tr>
  <tr>
    <td><strong>프로젝트 키워드</strong></td>
    <td>Healthcare · Caregiver · Support Program · Sanjeongteukrye · Insurance Hint</td>
  </tr>
  <tr>
    <td><strong>트랙</strong></td>
    <td>헬스케어 · 공공정보 · AI 요약</td>
  </tr>
  <tr>
    <td><strong>프로젝트 멤버</strong></td>
    <td>정아윤, (팀원), (팀원)</td>
  </tr>
  <tr>
    <td><strong>지도 교수</strong></td>
    <td>운영정 교수님</td>
  </tr>
  <tr>
    <td><strong>무엇을 만들고자 하는가</strong></td>
    <td>
      보호자는 치료 자체보다 정보를 몰라 생기는 행정·재정 부담에 큰 스트레스를 받는다.  
      특히 산정특례, 지원제도, 급여 기준, 보험 청구 가능성은 치료 단계가 바뀔 때마다 계속 변화한다.  
      CareMap은 <strong>초진 → 수술 → 항암 → 만성 관리 등 치료 여정 전체를 따라가며, 단계 변경 시마다 필요한 정보를 반복 제공하는 서비스</strong>이다.  
      한 번만 입력해도 단계가 바뀔 때마다 필요한 정보를 자동 안내해주며, 보호자의 행정 부담을 줄여준다.
    </td>
  </tr>
  <tr>
    <td><strong>고객(페르소나)</strong></td>
    <td>
      ① <strong>신부전/루푸스 환자 보호자</strong> – 산정특례·지원제도·약값 기준을 반복 확인해야 함  
      ② <strong>희귀암 환자의 자녀</strong> – 항암제 변경·재발 여부 등 치료 단계 변화 시 계속 정보가 새로 필요함  
      ③ <strong>만성질환 부모 돌보는 직장인</strong> – 주기적 검사·치료 변화에 따라 행정 절차를 반복적으로 확인해야 함  
    </td>
  </tr>
  <tr>
    <td><strong>Pain Point</strong></td>
    <td>
      1) 질병별 제도 혜택을 스스로 찾기 어려움<br>
      2) 제도별 조건·서류·소득 기준이 달라 비교가 어려움<br>
      3) 보험 청구 가능 항목을 약관에서 직접 찾기 어려움<br>
      4) <strong>단계가 바뀔 때마다 필요한 행정 절차가 달라져 보호자가 반복적으로 다시 찾아봐야 하나 이를 관리해주는 시스템이 없음</strong>
    </td>
  </tr>
 <tr>
  <td><strong>핵심 기능 (상세 예시 포함)</strong></td>
  <td>

  <strong>① 질병 카테고리 기반 제도 추천</strong><br>
  - 희귀암, 신부전, 자가면역질환 버튼 선택 → 산정특례 가능성, 본인부담률, 서류 요약 제공<br>
  예시: <em>C49 희귀암 → 산정특례 등록 가능 / 본인부담률 95%→5% / 필요한 서류 요약</em><br><br>

  <strong>② 치료 단계 기반 "액션 플랜"</strong><br>
  - 초진/수술/항암 시작/재발 단계 선택 → “지금 해야 할 일 3가지” 자동 생성<br>
  - 단계가 바뀔 때마다 행동 리스트 자동 갱신 → 반복 이용 구조<br>
  예시: <em>항암 시작 전: 산정특례 확인 / 항암제 급여 기준 확인 / 입원 영수증 준비</em><br><br>

  <strong>③ 최소 입력 보험 체크</strong><br>
  - 보장 유형 체크만으로 청구 후보 제공 (진단비·고액암·입원일당 등)<br>
  - 금액 계산 X / 약관에서 찾아야 할 키워드 안내<br>
  예시: <em>암 진단비 선택 → “최초 진단일 청구 가능 / 약관의 ‘고액암’ 키워드 확인”</em><br><br>

  <strong>④ 일정·만료 알림 기능</strong><br>
  - 진료·검사 일정 등록<br>
  - 산정특례 만료 3개월/1개월 전 알림<br>
  - 지자체 지원사업 공고 알림<br><br>

  <strong>⑤ 제도 설명 AI 요약</strong><br>
  - 긴 정책 문서를 보호자 친화적 문장으로 2~3줄 요약 제공
    </td>
  </tr>
  <tr>
    <td><strong>사용할 스택</strong></td>
    <td>React Native/Flutter, Firebase(Firestore), Node.js(FaaS), 간단한 AI 요약 모델</td>
  </tr>
  <tr>
    <td><strong>데이터</strong></td>
    <td>
      - 산정특례 질환 리스트<br>
      - 재난적의료비·지자체 지원 프로그램 DB<br>
      - 보험 보장 유형 DB (진단비/고액암/입원/수술 등)<br>
      - 사용자가 선택한 질병·치료 단계·보장 유형
    </td>
  </tr>
  <tr>
    <td><strong>깃허브 URL</strong></td>
    <td>(추가 예정)</td>
  </tr>
  <tr>
    <td><strong>최종 수정일</strong></td>
    <td>2025-11-24</td>
  </tr>
</table>
