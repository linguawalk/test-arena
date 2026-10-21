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
}
SCI_CHAPTERS = {
    "s1": {
        "phy-kin": ["차원 분석과 어림", "미분으로 보는 운동", "적분으로 보는 운동", "벡터와 포물선 운동"],
        "phy-dyn": ["뉴턴 법칙과 자유물체도", "일과 에너지", "운동량과 충돌", "원운동과 만유인력"],
        "phy-em": ["전기력과 전기장", "가우스 법칙과 전위", "축전기와 직류 회로", "자기장과 전자기 유도"],
    },
    "s2": {
        "phy-rigid": ["강체의 회전", "단진동", "감쇠·강제 진동"],
        "phy-thermo": ["기체 분자 운동론", "열역학 법칙", "열기관과 엔트로피"],
        "phy-optics": ["기하 광학", "파동 광학"],
        "phy-exp": ["측정과 오차 전파", "그래프 분석과 선형화"],
    },
    "s3": {
        "phy-modern": ["특수 상대론", "양자 기초"],
        "phy-lab": ["실험 문제 접근법", "모의 실험 과제"],
    },
}
SCI_ORDER = ["phy-kin", "phy-dyn", "phy-em", "phy-rigid", "phy-thermo", "phy-optics", "phy-exp", "phy-modern", "phy-lab"]

# 과목별 묶음. levels는 단계별 수준 문구, competition은 레슨 JSON의 대회 태그,
# work는 서술형 문항 이름(math: 증명, sci: 풀이).
CURRICULUM = {
    "math": {"tracks": TRACKS, "chapters": CHAPTERS, "order": TRACK_ORDER, "competition": "KMO", "work": "증명",
             "levels": {"s3": "IMO 수준"}},
    "sci": {"tracks": SCI_TRACKS, "chapters": SCI_CHAPTERS, "order": SCI_ORDER, "competition": "KPhO", "work": "풀이",
            "levels": {"s3": "IPhO 등 국제 대회 수준"}},
}
