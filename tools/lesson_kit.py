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


# ---------------------------------------------------------------- 도형 그림 (geo 위젯)
def G(alt, *els, maxh=240):
    """도형 그림. 좌표는 수학 좌표(위쪽이 +y)."""
    return {"widget": "geo", "config": {"elements": [e for e in els if e], "alt": alt, "maxh": maxh}, "static": True}


def pt(p, label=None, pos=None, hide=False):
    e = {"t": "pt", "p": [round(p[0], 4), round(p[1], 4)]}
    if label: e["label"] = label
    if pos: e["pos"] = pos
    if hide: e["hide"] = True
    return e


def seg(a, b, dash=False, hl=False):
    e = {"t": "seg", "a": [round(a[0], 4), round(a[1], 4)], "b": [round(b[0], 4), round(b[1], 4)]}
    if dash: e["dash"] = True
    if hl: e["hl"] = True
    return e


def poly(pts, fill=True, hl=False, dash=False):
    e = {"t": "poly", "pts": [[round(x, 4), round(y, 4)] for x, y in pts]}
    if not fill: e["fill"] = False
    if hl: e["hl"] = True
    if dash: e["dash"] = True
    return e


def circ(c, r, dash=False):
    e = {"t": "circle", "c": [round(c[0], 4), round(c[1], 4)], "r": round(r, 4)}
    if dash: e["dash"] = True
    return e


def rt(p, a, b):
    return {"t": "right", "p": list(p), "a": list(a), "b": list(b)}


def ang(p, a, b, label=None, r=22):
    e = {"t": "arc", "p": list(p), "a": list(a), "b": list(b), "r": r}
    if label: e["label"] = label
    return e


def tx(p, s, hl=False):
    e = {"t": "text", "p": [round(p[0], 4), round(p[1], 4)], "s": s}
    if hl: e["hl"] = True
    return e


def with_fig(screen, fig):
    screen["figure"] = fig
    return screen


# 계산 도우미
def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def mid(a, b):
    return lerp(a, b, 0.5)


def on_circle(c, r, deg):
    import math
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))
