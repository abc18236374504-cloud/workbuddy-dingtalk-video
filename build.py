#!/usr/bin/env python3
"""Generate HyperFrames composition index.html from script.json + durations.json.
Usage: python3 build.py  -> writes project/index.html (copies audio/voice.wav + assets/* into project/assets/)
"""
import json, os, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(ROOT, "project")
os.makedirs(os.path.join(P, "assets"), exist_ok=True)
shutil.copy(os.path.join(ROOT, "audio", "voice.wav"), os.path.join(P, "assets", "voice.wav"))
for f in os.listdir(os.path.join(ROOT, "assets")):
    shutil.copy(os.path.join(ROOT, "assets", f), os.path.join(P, "assets", f))

script = {s["id"]: s for s in json.load(open(os.path.join(ROOT, "script", "script.json")))}
D = json.load(open(os.path.join(ROOT, "script", "durations.json")))
TOTAL = D["total"]
SEGS = D["segments"]
NSTEPS = max(s["step"] for s in SEGS)


def qr(seed=7, n=21):
    # deterministic fake QR pattern
    cells = []
    x = seed
    for r in range(n):
        for c in range(n):
            x = (x * 1103515245 + 12345) & 0x7FFFFFFF
            finder = (r < 7 and c < 7) or (r < 7 and c >= n - 7) or (r >= n - 7 and c < 7)
            if finder:
                rr, cc = r % 14 if r < 7 else r - (n - 7), c if c < 7 else c - (n - 7)
                on = rr in (0, 6) or cc in (0, 6) or (2 <= rr <= 4 and 2 <= cc <= 4)
            else:
                on = (x >> 16) & 1
            cells.append(f'<i class="{"on" if on else ""}"></i>')
    return f'<div class="qr" style="grid-template-columns:repeat({n},1fr)">{"".join(cells)}</div>'


def win(title, body, cls=""):
    return f'''<div class="win {cls}"><div class="bar"><b></b><b></b><b></b><span>{title}</span></div><div class="wbody">{body}</div></div>'''


MOCK = {
    "s0": '''<div class="hero">
      <div class="logo wb">W</div><div class="x">×</div><div class="logo dd">钉</div>
      <div class="clock" id="s0-clock">08:50</div>
      <div class="hero-sub">到点提醒 · 本人打卡</div>
      <div class="warnline" id="s0-no">✕ 不代打卡</div></div>''',
    "s1": win("WorkBuddy", f'''<div class="login"><div class="chips"><span class="on">Windows</span><span class="on">Mac</span></div><div class="lt">微信扫码登录</div>{qr()}<div class="ok" id="s1-ok">✓ 登录成功</div></div>'''),
    "s2": win("钉钉 · 群设置 · 机器人", '''<div class="form"><div class="inp">群：打卡提醒（仅自己）</div>
      <label>机器人</label><div class="inp" id="s2-bot">＋ 添加自定义机器人</div>
      <label>安全设置 · 自定义关键词</label><div class="inp hl" id="s2-kw">打卡</div>
      <label>Webhook</label><div class="inp mono" id="s2-hook">https://oapi.dingtalk.com/robot/send?access_token=••••••••</div>
      <div class="send" id="s2-copy">复制</div></div>'''),
    "s3": win("WorkBuddy", '''<div class="split"><div class="side"><p>对话</p><p class="act" id="s3-sched">定时任务</p><p>技能</p><p>设置</p></div>
      <div class="list"><div class="row"><b class="grow">定时任务</b><span class="nbtn">新建</span><span class="nbtn arr" id="s3-arr">▾</span></div>
      <div class="menu" id="s3-menu"><div class="mi">空白新建</div><div class="mi hl" id="s3-mi">从任务新建</div></div></div></div>'''),
    "s4": win("从任务新建", '''<div class="prompt"><div class="pbox small" id="s4-box"><span id="s4-type"></span></div><div class="send" id="s4-send">发送 ▶</div></div>'''),
    "s5": win("任务配置", '''<div class="form"><label>任务</label><div class="inp">钉钉打卡提醒 · 08:50 / 18:00</div>
      <label>重复</label><div class="chips wk"><span class="on" id="s5-d1">一</span><span class="on" id="s5-d2">二</span><span class="on" id="s5-d3">三</span><span class="on" id="s5-d4">四</span><span class="on" id="s5-d5">五</span><span>六</span><span>日</span></div>
      <label>权限</label><div class="chips"><span>需确认</span><span class="on" id="s5-full">完全访问</span></div>
      <label>运行位置</label><div class="chips"><span>本地</span><span class="on" id="s5-cloud">云端（常关机）</span></div></div>'''),
    "s6": '''<div class="phone"><div class="notch"></div><div class="noti" id="s6-noti"><span class="ic d">钉</span><div><b>打卡提醒机器人</b><p>08:50 该打卡了！</p></div></div>
      <div class="runlog" id="s6-log"><div>立即运行</div><div class="okk">✓ 运行成功</div></div><div class="done" id="s6-done">配好了</div></div>''',
    "s7": '''<div class="check"><div class="ci bad" id="s7-a"><span>✕</span>别让 AI 代打卡、别用虚拟定位</div><div class="ci bad" id="s7-b"><span>✕</span>Webhook 别外传</div><div class="ci" id="s7-c"><span>✓</span>本地任务：电脑开着、客户端别退出</div><div class="note" id="s7-n">以所在公司考勤制度为准</div></div>''',
    "s8": '''<div class="check"><div class="ci" id="s8-a"><span>✓</span>到点提醒</div><div class="ci" id="s8-b"><span>✓</span>你只管伸手打卡</div><div class="follow" id="s8-f">收藏 · 转给总忘打卡的同事</div></div>''',
}

S4_TEXT = "每个工作日早上 8:50 和晚上 18:00，用 curl 往这个钉钉 Webhook 发一条打卡提醒，内容带上「打卡」两个字。"

scenes_html = []
js = []
for i, g in enumerate(SEGS):
    s = script[g["id"]]
    st, du, vs, vd = g["start"], g["duration"], g["vo_start"], g["vo_duration"]
    sid = g["id"]
    badge = f'<div class="badge" id="{sid}-badge"><span>STEP</span><b>{s["step"]}</b></div>' if s["step"] else f'<div class="badge intro {"warn" if s.get("badge")=="!" else ""}" id="{sid}-badge"><b>{html.escape(s.get("badge","▶"))}</b></div>'
    chars = "".join(f'<span class="ch" id="{sid}-c{k}">{html.escape(c)}</span>' for k, c in enumerate(s["vo"]))
    scenes_html.append(f'''
    <section class="clip scene" id="{sid}" data-start="{st}" data-duration="{du}" data-track-index="1">
      <div class="head">{badge}<h2 id="{sid}-title">{html.escape(s["title"])}</h2></div>
      <div class="stage"><div class="cam" id="{sid}-cam">{MOCK[sid]}</div></div>
      <div class="chip" id="{sid}-chip">{html.escape(s["screen"])}</div>
      <div class="sub"><p>{chars}<span class="caret" id="{sid}-caret"></span></p></div>
    </section>''')
    # local times relative to root timeline (absolute)
    zin = i % 2 == 0  # alternate push-in / pull-out
    js.append(f'tl.fromTo("#{sid}-cam",{{scale:{1.0 if zin else 1.12}}},{{scale:{1.12 if zin else 1.0},duration:{du},ease:"sine.inOut"}},{st});')
    js.append(f'tl.from("#{sid}-badge",{{scale:0,rotation:-90,duration:0.45,ease:"back.out(2)"}},{st+0.05});')
    js.append(f'tl.from("#{sid}-title",{{x:-60,opacity:0,duration:0.4,ease:"power3.out"}},{st+0.15});')
    js.append(f'tl.from("#{sid}-cam",{{opacity:0,y:80,duration:0.45,ease:"power2.out"}},{st});')
    js.append(f'tl.from("#{sid}-chip",{{opacity:0,y:30,duration:0.35,ease:"power2.out"}},{st+0.5});')
    # typewriter: reveal chars spread across 92% of vo duration
    n = len(s["vo"])
    for k in range(n):
        js.append(f'tl.set("#{sid}-c{k}",{{display:"inline"}},{round(vs + vd*0.92*k/n,3)});')
    js.append(f'tl.to("#{sid}-caret",{{opacity:0,duration:0.01}},{round(vs+vd,3)});')
    js.append(f'tl.to("#{sid}",{{opacity:0,duration:0.25}},{round(st+du-0.25,3)});')

# per-scene UI actions (cursor-ish highlights)
def at(sid, off):
    g = next(x for x in SEGS if x["id"] == sid)
    return round(g["vo_start"] + off, 3)

js += [
    f'tl.from("#s0-clock",{{scale:0.6,opacity:0,duration:0.5,ease:"back.out(2)"}},{at("s0",1.0)});',
    f'tl.to("#s0-clock",{{color:"#ff5a5f",duration:0.2,yoyo:true,repeat:3}},{at("s0",2.0)});',
    f'tl.from("#s0-no",{{scale:0.4,opacity:0,duration:0.4,ease:"back.out(2)"}},{at("s0",9.5)});',
    f'tl.to("#s1-ok",{{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"}},{at("s1",5.5)});',
    f'tl.to("#s2-bot",{{boxShadow:"0 0 0 6px #3b82f6",duration:0.3}},{at("s2",4.5)});',
    f'tl.to("#s2-kw",{{boxShadow:"0 0 0 6px #22c55e",scale:1.04,duration:0.3}},{at("s2",8.5)});',
    f'tl.to("#s2-copy",{{backgroundColor:"#22c55e",scale:1.08,duration:0.3}},{at("s2",11.2)});',
    f'tl.to("#s3-sched",{{backgroundColor:"#3b82f6",color:"#fff",duration:0.25}},{at("s3",2.2)});',
    f'tl.to("#s3-arr",{{backgroundColor:"#1d4ed8",scale:1.15,duration:0.25}},{at("s3",4.0)});',
    f'tl.to("#s3-menu",{{opacity:1,y:0,duration:0.3}},{at("s3",4.6)});',
    f'tl.to("#s3-mi",{{boxShadow:"0 0 0 5px #3b82f6",duration:0.3}},{at("s3",5.6)});',
    f'tl.to("#s4-send",{{backgroundColor:"#22c55e",scale:1.08,duration:0.3}},{at("s4",10.4)});',
] + [f'tl.from("#s5-d{k}",{{scale:0.4,opacity:0,duration:0.2}},{at("s5",2.0+0.15*k)});' for k in range(1,6)] + [
    f'tl.to("#s5-full",{{boxShadow:"0 0 0 6px #f59e0b",scale:1.08,duration:0.3}},{at("s5",4.6)});',
    f'tl.to("#s5-cloud",{{boxShadow:"0 0 0 6px #3b82f6",scale:1.08,duration:0.3}},{at("s5",9.8)});',
    f'tl.to("#s6-log",{{opacity:1,duration:0.3}},{at("s6",0.6)});',
    f'tl.from("#s6-noti",{{y:-220,opacity:0,duration:0.5,ease:"back.out(1.6)"}},{at("s6",2.2)});',
    f'tl.to("#s6-done",{{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"}},{at("s6",5.6)});',
    f'tl.from("#s7-a",{{x:-80,opacity:0,duration:0.35}},{at("s7",1.2)});',
    f'tl.from("#s7-b",{{x:-80,opacity:0,duration:0.35}},{at("s7",8.0)});',
    f'tl.from("#s7-c",{{x:-80,opacity:0,duration:0.35}},{at("s7",9.6)});',
    f'tl.from("#s7-n",{{opacity:0,duration:0.4}},{at("s7",11.0)});',
    f'tl.from("#s8-a",{{x:-80,opacity:0,duration:0.35}},{at("s8",0.3)});',
    f'tl.from("#s8-b",{{x:-80,opacity:0,duration:0.35}},{at("s8",1.4)});',
    f'tl.from("#s8-f",{{scale:0.5,opacity:0,duration:0.45,ease:"back.out(2)"}},{at("s8",3.4)});',
]
# s4 in-UI typewriter of the instruction
for k, c in enumerate(S4_TEXT):
    pass
s4_chars = "".join(f'<span class="ch2" id="s4-t{k}">{html.escape(c)}</span>' for k, c in enumerate(S4_TEXT))
for k in range(len(S4_TEXT)):
    js.append(f'tl.set("#s4-t{k}",{{opacity:1}},{at("s4", 0.6 + 9.0*k/len(S4_TEXT))});')
MOCK_S4_FILL = s4_chars

# progress bar + step dots
js.append(f'tl.fromTo("#pbar",{{scaleX:0}},{{scaleX:1,duration:{TOTAL},ease:"none"}},0);')
for g in SEGS:
    if g["step"]:
        js.append(f'tl.to("#dot{g["step"]}",{{backgroundColor:"#3b82f6",scale:1.25,duration:0.25}},{g["start"]});')
        js.append(f'tl.to("#dot{g["step"]}",{{scale:1,duration:0.2}},{round(g["start"]+0.25,3)});')
dots = "".join(f'<i id="dot{k}">{k}</i>' for k in range(1, NSTEPS + 1))

body = "\n".join(scenes_html).replace('<span id="s4-type"></span>', MOCK_S4_FILL)

CSS = open(os.path.join(ROOT, "script", "style.css")).read()
out = f'''<!doctype html>
<html lang="zh-CN" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="assets/gsap.min.js"></script>
<style>
{CSS}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
  <div class="bg"></div>
  {body}
  <div class="hud"><div class="dots">{dots}</div><div class="track"><div id="pbar"></div></div></div>
  <audio id="vo" class="clip" src="assets/voice.wav" data-start="0" data-duration="{TOTAL}" data-track-index="5"></audio>
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>
'''
open(os.path.join(P, "index.html"), "w").write(out)
print("ok", TOTAL, len(js), "tweens")
