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
      <div class="clock" id="s0-clock">08:45</div>
      <div class="hero-sub">工作日 · 自动提醒 · 一键打卡</div></div>''',
    "s1": win("WorkBuddy", f'''<div class="login"><div class="lt">微信扫码登录</div>{qr()}<div class="ok" id="s1-ok">✓ 登录成功</div></div>'''),
    "s2": win("WorkBuddy · 设置", '''<div class="split"><div class="side"><p>账户</p><p class="act" id="s2-conn">连接器</p><p>自动化</p><p>技能</p></div>
      <div class="list"><div class="row"><span class="ic g">微</span>微信<em>未连接</em></div>
      <div class="row"><span class="ic b">企</span>企业微信<em>未连接</em></div>
      <div class="row hl" id="s2-dd"><span class="ic d">钉</span>钉钉<em class="on" id="s2-on">已连接</em></div>
      <div class="row"><span class="ic f">飞</span>飞书<em>未连接</em></div></div></div>'''),
    "s3": win("自动化 · 新建任务", '''<div class="form"><label>任务名称</label><div class="inp">钉钉打卡提醒</div>
      <label>重复</label><div class="chips"><span class="on">工作日</span><span>每天</span><span>每周</span></div>
      <label>触发时间</label><div class="inp big hl" id="s3-time">08:45</div></div>'''),
    "s4": win("自动化 · 任务指令", '''<div class="prompt"><div class="pbox" id="s4-box"><span id="s4-type"></span></div><div class="send" id="s4-send">保存 ▶</div></div>'''),
    "s5": '''<div class="phone"><div class="notch"></div><div class="noti" id="s5-noti"><span class="ic d">钉</span><div><b>WorkBuddy 机器人</b><p>08:45 该上班打卡啦！</p></div></div>
      <div class="punch" id="s5-punch"><div class="pin">上班打卡</div><div class="pt">08:46</div></div><div class="done" id="s5-done">✓ 打卡成功</div></div>''',
    "s6": '''<div class="check"><div class="ci" id="s6-a"><span>✓</span>电脑保持开机</div><div class="ci" id="s6-b"><span>✓</span>WorkBuddy 保持运行</div><div class="ci" id="s6-c"><span>✓</span>每天 08:45 准时提醒</div><div class="follow" id="s6-f">关注我 · 学更多 AI 办公技巧</div></div>''',
}

S4_TEXT = "发钉钉消息提醒我上班打卡；15 分钟后还没打卡，再发邮件提醒我。"

scenes_html = []
js = []
for i, g in enumerate(SEGS):
    s = script[g["id"]]
    st, du, vs, vd = g["start"], g["duration"], g["vo_start"], g["vo_duration"]
    sid = g["id"]
    badge = f'<div class="badge" id="{sid}-badge"><span>STEP</span><b>{s["step"]}</b></div>' if s["step"] else '<div class="badge intro" id="%s-badge"><b>▶</b></div>' % sid
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
    f'tl.from("#s0-clock",{{scale:0.6,opacity:0,duration:0.5,ease:"back.out(2)"}},{at("s0",1.2)});',
    f'tl.to("#s0-clock",{{color:"#ff5a5f",duration:0.2,yoyo:true,repeat:3}},{at("s0",2.2)});',
    f'tl.to("#s1-ok",{{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"}},{at("s1",3.2)});',
    f'tl.to("#s2-conn",{{backgroundColor:"#3b82f6",color:"#fff",duration:0.25}},{at("s2",1.2)});',
    f'tl.to("#s2-dd",{{boxShadow:"0 0 0 6px #3b82f6",duration:0.3}},{at("s2",2.8)});',
    f'tl.to("#s2-on",{{opacity:1,duration:0.3}},{at("s2",5.2)});',
    f'tl.to("#s3-time",{{boxShadow:"0 0 0 6px #22c55e",scale:1.06,duration:0.35}},{at("s3",3.6)});',
    f'tl.to("#s4-send",{{backgroundColor:"#22c55e",scale:1.08,duration:0.3}},{at("s4",7.4)});',
    f'tl.from("#s5-noti",{{y:-220,opacity:0,duration:0.5,ease:"back.out(1.6)"}},{at("s5",1.6)});',
    f'tl.to("#s5-punch",{{scale:0.9,duration:0.15,yoyo:true,repeat:1}},{at("s5",4.6)});',
    f'tl.to("#s5-done",{{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"}},{at("s5",5.0)});',
    f'tl.from("#s6-a",{{x:-80,opacity:0,duration:0.35}},{at("s6",0.4)});',
    f'tl.from("#s6-b",{{x:-80,opacity:0,duration:0.35}},{at("s6",1.6)});',
    f'tl.from("#s6-c",{{x:-80,opacity:0,duration:0.35}},{at("s6",3.0)});',
    f'tl.from("#s6-f",{{scale:0.5,opacity:0,duration:0.45,ease:"back.out(2)"}},{at("s6",4.8)});',
]
# s4 in-UI typewriter of the instruction
for k, c in enumerate(S4_TEXT):
    pass
s4_chars = "".join(f'<span class="ch2" id="s4-t{k}">{html.escape(c)}</span>' for k, c in enumerate(S4_TEXT))
for k in range(len(S4_TEXT)):
    js.append(f'tl.set("#s4-t{k}",{{opacity:1}},{at("s4", 0.9 + 6.0*k/len(S4_TEXT))});')
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
