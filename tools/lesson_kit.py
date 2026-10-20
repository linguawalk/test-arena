"""레슨 작성 도우미. 각 함수는 math-arena 레슨 스키마 v1.0의 화면 하나를 만든다.

test-arena 전용 추가 형식
- proof: 자가 채점 증명 문항
  prompt, model_answer(모범 증명 단계 배열), criteria([{text, points}]), hint, explanation(선택)
"""


def X(title, body, stage="discover", figure=None):
    s = {"type": "explain", "stage": stage, "title": title, "body": body}
    if figure:
        s["figure"] = figure
    return s


def E(problem, steps, answer, stage="discover", title="예제"):
    return {"type": "example", "stage": stage, "title": title, "problem": problem, "steps": steps, "answer": answer}


def N(prompt, answer, hint, expl, stage="discover", fmt="integer"):
    return {"type": "question", "stage": stage, "qtype": "numeric", "prompt": prompt, "answer": str(answer),
            "answer_format": fmt, "tolerance": 0, "hint": hint, "explanation": expl}


def F(prompt, blanks, hint, expl, stage="discover", unordered=None):
    s = {"type": "question", "stage": stage, "qtype": "fill_blank", "prompt": prompt,
         "blanks": [{"answers": a} for a in blanks], "hint": hint, "explanation": expl}
    if unordered:
        s["unordered_groups"] = unordered
    return s


def O(prompt, steps, shown, hint, expl, stage="discover"):
    """steps: 올바른 순서의 문장들, shown: 화면에 보여 줄 순서(steps의 0부터 시작하는 번호 목록)."""
    items = [{"id": f"o{k + 1}", "text": t} for k, t in enumerate(steps)]
    return {"type": "question", "stage": stage, "qtype": "ordering", "prompt": prompt,
            "items": [items[k] for k in shown], "answer_order": [it["id"] for it in items],
            "hint": hint, "explanation": expl}


def PR(prompt, model, criteria, hint, stage="apply", expl=None):
    s = {"type": "question", "stage": stage, "qtype": "proof", "prompt": prompt, "model_answer": model,
         "criteria": [{"text": t, "points": p} for t, p in criteria], "hint": hint}
    if expl:
        s["explanation"] = expl
    return s
