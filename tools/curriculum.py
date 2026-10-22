"""test-arena 커리큘럼 정의.

단계: s1 예선(국내 1차) / s2 본선(국내 2차·최종 선발) / s3 국제(목차·학습 가이드 중심)
과목마다 TRACKS·CHAPTERS·TRACK_ORDER를 둔다 (아래 CURRICULUM).
- math: proof 증명의 기초 · alg 대수 · nt 정수론 · comb 조합 · geo 기하
- sci: 물리(phy-*)부터. 트랙의 group은 탐색 화면에서 과목 묶음 제목으로 쓴다.
레슨이 정의된 챕터만 available = True 가 된다 (build.py가 lessons/ 폴더를 보고 판단).
과목의 available은 열린 챕터가 하나라도 있으면 True로 빌드 때 정해진다.
"""

SUBJECTS = [
    {"id": "math", "title": "수학 올림피아드", "path": "KMO → IMO",
     "description": "대수·정수론·조합·기하와 증명 쓰기", "available": True},
    {"id": "sci", "title": "과학 올림피아드", "path": "KPhO·KChO·KBO·KESO·천문 → 국제",
     "description": "물리·화학·생물·지구과학·천문", "available": False},
    {"id": "info", "title": "정보 올림피아드", "path": "KOI → IOI",
     "description": "자료구조·알고리즘 설계·그래프", "available": False},
    {"id": "hum", "title": "인문·사회 경시", "path": "IPO·IOL·iGeo·IEO·역사",
     "description": "철학·언어학·지리·경제·역사 (개인 시험 부분)", "available": False},
]

STAGES = [
    {"no": 1, "id": "s1", "title": "S1 예선", "level": "국내 1차 시험 수준",
     "description": "교과를 넘어서는 경시 기초 도구와 증명 쓰기. 설명과 문제가 번갈아 나오는 레슨으로 배웁니다."},
    {"no": 2, "id": "s2", "title": "S2 본선", "level": "국내 2차·최종 선발 수준",
     "description": "서술형 증명 중심. 모범 증명과 채점 기준으로 스스로 채점합니다."},
    {"no": 3, "id": "s3", "title": "S3 국제", "level": "IMO 수준",
     "description": "목차와 학습 가이드 중심으로 독학합니다."},
]

TRACKS = {
    "proof": {"title": "증명의 기초", "description": "명제와 증명, 수학적 귀납법, 답안 쓰기"},
    "alg": {"title": "대수", "description": "부등식, 다항식, 수열, 함수방정식"},
    "nt": {"title": "정수론", "description": "약수·배수, 합동식, 소수, 디오판토스 방정식"},
    "comb": {"title": "조합", "description": "세기, 비둘기집 원리, 포함-배제, 그래프"},
    "geo": {"title": "기하", "description": "닮음, 원의 성질, 삼각형의 오심, 기하 변환"},
}

# 단계별 트랙과 챕터 제목. 커리큘럼(v1) 문서의 1장 표를 레슨 단위로 나눈 것.
CHAPTERS = {
    "s1": {
        "proof": ["명제와 증명", "수학적 귀납법", "답안 쓰기"],
        "alg": ["산술·기하 평균 부등식", "코시-슈바르츠 부등식", "다항식", "수열과 점화식"],
        "nt": ["약수·배수와 최대공약수", "합동식", "페르마 소정리", "소수와 소인수분해"],
        "comb": ["세기의 원리 심화", "비둘기집 원리", "포함-배제 원리", "점화식으로 세기"],
        "geo": ["닮음과 비", "원의 성질", "삼각형의 오심", "넓이와 삼각비"],
    },
    "s2": {
        "proof": ["귀납법·귀류법 심화", "답안 작성법"],
        "alg": ["함수방정식", "재배열·젠센 부등식", "SOS와 부등식 전략"],
        "nt": ["위수와 원시근", "디오판토스 방정식", "이차잉여"],
        "comb": ["그래프 이론", "불변량과 단조변량", "극단 원리"],
        "geo": ["체바·메넬라오스 정리", "근축과 방멱", "반전 기초"],
    },
    "s3": {
        "proof": ["출제 경향 분석", "모의고사"],
        "alg": ["다항식 고급", "복합 함수방정식"],
        "nt": ["LTE 보조정리", "p진 평가", "고급 디오판토스"],
        "comb": ["조합 기하", "확률적 방법", "게임"],
        "geo": ["사영기하", "복소수·좌표 기법", "고급 반전"],
    },
}

TRACK_ORDER = ["proof", "alg", "nt", "comb", "geo"]

# ---------------------------------------------------------------- 과학 올림피아드
# 물리 (KPhO → IPhO). 커리큘럼(v1) 문서 2장 표: S1 미적분 기반 역학·전자기 기초 /
# S2 강체·진동, 열역학, 광학, 오차 분석 / S3 상대론·양자 기초, 실험 문제
SCI_TRACKS = {
    "phy-kin": {"group": "물리", "title": "운동과 물리 수학", "description": "차원 분석, 미분·적분으로 보는 운동, 벡터와 포물선 운동"},
    "phy-dyn": {"group": "물리", "title": "역학", "description": "뉴턴 법칙, 에너지, 운동량, 원운동과 중력"},
    "phy-em": {"group": "물리", "title": "전자기 기초", "description": "전기장, 가우스 법칙과 전위, 회로, 자기장과 유도"},
    "phy-rigid": {"group": "물리", "title": "강체와 진동", "description": "강체의 회전, 단진동, 감쇠·강제 진동"},
    "phy-thermo": {"group": "물리", "title": "열역학", "description": "기체 분자 운동론, 열역학 법칙, 열기관"},
    "phy-optics": {"group": "물리", "title": "광학", "description": "기하 광학, 파동 광학"},
    "phy-exp": {"group": "물리", "title": "실험과 오차", "description": "측정과 오차 전파, 그래프 분석"},
    "phy-modern": {"group": "물리", "title": "현대 물리", "description": "특수 상대론, 양자 기초"},
    "phy-lab": {"group": "물리", "title": "실험 문제", "description": "실험 문제 접근법, 모의 실험 과제"},
    # 화학 (KChO → IChO). 문서 2장 표: S1 화학양론·평형·산염기 / S2 열역학·반응속도론, 유기 반응 메커니즘 /
    # S3 분광 분석, 배위화학, 실험 설계
    "chem-stoich": {"group": "화학", "competition": "KChO", "title": "화학양론", "description": "몰과 화학식, 반응의 양적 관계, 용액의 농도, 기체"},
    "chem-eq": {"group": "화학", "competition": "KChO", "title": "화학 평형", "description": "평형 상수, 르샤틀리에 원리, 용해 평형"},
    "chem-acid": {"group": "화학", "competition": "KChO", "title": "산과 염기", "description": "pH, 약산·약염기, 완충 용액, 적정"},
    "chem-thermo": {"group": "화학", "competition": "KChO", "title": "열역학과 반응 속도", "description": "엔탈피·엔트로피·자유 에너지, 속도 법칙"},
    "chem-org": {"group": "화학", "competition": "KChO", "title": "유기 반응", "description": "작용기, 치환·제거·첨가 반응과 메커니즘"},
    "chem-spec": {"group": "화학", "competition": "KChO", "title": "분광 분석", "description": "IR·NMR·질량 분석으로 구조 결정"},
    "chem-coord": {"group": "화학", "competition": "KChO", "title": "배위화학", "description": "착화합물의 구조, 결정장 이론"},
    "chem-lab": {"group": "화학", "competition": "KChO", "title": "실험 설계", "description": "정량 분석, 실험 설계와 오차"},
    # 생물 (KBO → IBO). 문서 2장 표: S1 세포·유전 심화 / S2 분자생물학, 생리학, 생태·진화 / S3 생물정보·통계, 실험 해석
    "bio-cell": {"group": "생물", "competition": "KBO", "title": "세포", "description": "세포 구조, 생체막과 수송, 효소, 세포 호흡과 광합성"},
    "bio-gen": {"group": "생물", "competition": "KBO", "title": "유전", "description": "세포 분열, 멘델 유전과 확장, 연관과 지도, 집단 유전"},
    "bio-mol": {"group": "생물", "competition": "KBO", "title": "분자생물학", "description": "DNA 복제, 전사·번역, 유전자 발현 조절, 생명공학 기법"},
    "bio-phys": {"group": "생물", "competition": "KBO", "title": "생리학", "description": "신경과 근육, 순환·호흡, 항상성, 식물 생리"},
    "bio-eco": {"group": "생물", "competition": "KBO", "title": "생태와 진화", "description": "개체군과 군집, 생태계, 자연 선택과 계통"},
    "bio-info": {"group": "생물", "competition": "KBO", "title": "생물정보와 통계", "description": "서열 분석, 계통수 작성, 생물 통계"},
    "bio-lab": {"group": "생물", "competition": "KBO", "title": "실험 해석", "description": "실험 설계와 대조군, 자료 해석"},
    # 지구과학 (KESO → IESO). 문서 2장 표: S1 지질·대기·해양 기초 / S2 지구계 상호작용, 자료 해석 /
    # S3 야외조사형·팀 과제는 결정 사항(온라인 구현 범위)에 따라 제외
    "earth-geo": {"group": "지구과학", "competition": "KESO", "title": "지질", "description": "광물과 암석, 지구 내부, 판 구조론, 지질 시대"},
    "earth-atmo": {"group": "지구과학", "competition": "KESO", "title": "대기", "description": "대기 구조와 복사, 안정도와 구름, 대기 순환, 날씨"},
    "earth-ocean": {"group": "지구과학", "competition": "KESO", "title": "해양", "description": "해수의 성질, 해류, 파도와 조석, 해양과 기후"},
    "earth-system": {"group": "지구과학", "competition": "KESO", "title": "지구계 상호작용", "description": "물질 순환, 에너지 수지, 기후 변화"},
    "earth-data": {"group": "지구과학", "competition": "KESO", "title": "자료 해석", "description": "지질·기상·해양 자료 읽기와 해석"},
}
SCI_CHAPTERS = {
    "s1": {
        "phy-kin": ["차원 분석과 어림", "미분으로 보는 운동", "적분으로 보는 운동", "벡터와 포물선 운동"],
        "phy-dyn": ["뉴턴 법칙과 자유물체도", "일과 에너지", "운동량과 충돌", "원운동과 만유인력"],
        "phy-em": ["전기력과 전기장", "가우스 법칙과 전위", "축전기와 직류 회로", "자기장과 전자기 유도"],
        "chem-stoich": ["몰과 화학식", "화학 반응식과 양적 관계", "용액의 농도", "기체"],
        "chem-eq": ["평형 상수", "르샤틀리에 원리", "기체 평형", "용해 평형"],
        "chem-acid": ["산과 염기의 정의", "pH와 약산·약염기", "완충 용액", "중화 적정"],
        "bio-cell": ["세포의 구조", "생체막과 물질 수송", "효소", "세포 호흡과 광합성"],
        "bio-gen": ["세포 분열과 염색체", "멘델 유전과 확장", "연관과 유전자 지도", "집단 유전"],
        "earth-geo": ["광물과 암석", "지구 내부와 지진파", "판 구조론", "지질 시대와 연대 측정"],
        "earth-atmo": ["대기의 구조와 복사", "대기 안정도와 구름", "대기 대순환과 바람", "기단과 날씨"],
        "earth-ocean": ["해수의 성질", "해류와 해양 순환", "파도와 조석", "해양과 기후"],
    },
    "s2": {
        "phy-rigid": ["강체의 회전", "단진동", "감쇠·강제 진동"],
        "phy-thermo": ["기체 분자 운동론", "열역학 법칙", "열기관과 엔트로피"],
        "phy-optics": ["기하 광학", "파동 광학"],
        "phy-exp": ["측정과 오차 전파", "그래프 분석과 선형화"],
        "chem-thermo": ["엔탈피와 헤스 법칙", "엔트로피와 자유 에너지", "반응 속도식", "활성화 에너지와 반응 메커니즘"],
        "chem-org": ["작용기와 명명", "치환과 제거 반응", "첨가 반응", "반응 메커니즘 쓰기"],
        "bio-mol": ["DNA 복제", "전사와 번역", "유전자 발현 조절", "생명공학 기법"],
        "bio-phys": ["신경과 근육", "순환과 호흡", "항상성과 내분비", "식물 생리"],
        "bio-eco": ["개체군과 군집", "생태계", "자연 선택과 진화", "계통과 분류"],
        "earth-system": ["물질 순환", "지구 에너지 수지", "엘니뇨와 기후 변화"],
        "earth-data": ["지질 자료 해석", "기상·해양 자료 해석"],
    },
    "s3": {
        "phy-modern": ["특수 상대론", "양자 기초"],
        "phy-lab": ["실험 문제 접근법", "모의 실험 과제"],
        "chem-spec": ["적외선 분광법", "핵자기 공명", "질량 분석"],
        "chem-coord": ["착화합물의 구조와 이성질체", "결정장 이론"],
        "chem-lab": ["정량 분석", "실험 설계와 오차"],
        "bio-info": ["서열 분석", "계통수 작성", "생물 통계"],
        "bio-lab": ["실험 설계와 대조군", "자료 해석"],
    },
}
SCI_ORDER = ["phy-kin", "phy-dyn", "phy-em", "phy-rigid", "phy-thermo", "phy-optics", "phy-exp", "phy-modern", "phy-lab",
             "chem-stoich", "chem-eq", "chem-acid", "chem-thermo", "chem-org", "chem-spec", "chem-coord", "chem-lab",
             "bio-cell", "bio-gen", "bio-mol", "bio-phys", "bio-eco", "bio-info", "bio-lab",
             "earth-geo", "earth-atmo", "earth-ocean", "earth-system", "earth-data"]

# 과목별 묶음. levels는 단계별 수준 문구, competition은 레슨 JSON의 대회 태그,
# work는 서술형 문항 이름(math: 증명, sci: 풀이).
CURRICULUM = {
    "math": {"tracks": TRACKS, "chapters": CHAPTERS, "order": TRACK_ORDER, "competition": "KMO", "work": "증명",
             "levels": {"s3": "IMO 수준"}},
    "sci": {"tracks": SCI_TRACKS, "chapters": SCI_CHAPTERS, "order": SCI_ORDER, "competition": "KPhO", "work": "풀이",
            "levels": {"s3": "IPhO 등 국제 대회 수준"}},
}
