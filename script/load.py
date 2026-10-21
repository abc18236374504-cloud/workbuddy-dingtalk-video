"""Normalize script/script.json (编剧 9 镜格式 shots[].narration/onscreen/est_sec) + script/view.json (画面标题/提示条/徽章) -> [{id:sN, step, title, screen, vo, est_sec, badge?}]"""
import json, os
def load(root):
    d = json.load(open(os.path.join(root, "script", "script.json")))
    view = json.load(open(os.path.join(root, "script", "view.json")))
    out = []
    for s in d["shots"]:
        sid = f"s{s['id']-1}"
        v = view.get(sid, {})
        out.append({"id": sid, "step": v.get("step", 0), "title": v.get("title", s["title"]),
                    "screen": v.get("screen", s["onscreen"]), "vo": s["narration"], "est_sec": s["est_sec"],
                    **({"badge": v["badge"]} if "badge" in v else {})})
    return out
