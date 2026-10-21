# 界面素材师 · A 版 WorkBuddy × 钉钉提醒教程 s0–s6 · 1080x1920 示意界面（底部 300px 留字幕）
import pathlib
R = pathlib.Path(__file__).parent
CSS = """
@font-face{font-family:"N";src:url("../assets/fonts/NotoSansSC.ttf");font-weight:100 900}
:root{--bg:#F4F6FA;--ink:#1D2742;--sub:#5B6680;--line:#DCE1EA;--blue:#2F6BFF;--bs:#DDE7FF;--mint:#17B890;--ms:#D6F5EC;--red:#EF4757;--rs:#FDE0E3;--amber:#FF9F1C;--dt:#1677FF;--wb:#6C4BFF}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;background:var(--bg);color:var(--ink);font-family:"N",sans-serif;overflow:hidden;position:relative}
.top{position:absolute;left:72px;right:72px;top:110px}
.no{font-size:30px;font-weight:700;color:var(--blue);letter-spacing:2px}
.h1{font-size:74px;font-weight:800;margin-top:12px}
.lead{font-size:36px;color:var(--sub);margin-top:14px}
.demo{position:absolute;right:72px;top:116px;font-size:26px;color:#8A93A8;background:#E7EAF0;border-radius:12px;padding:6px 18px}
.stage{position:absolute;left:60px;right:60px;top:430px;bottom:340px}
.win{background:#fff;border:2px solid var(--line);border-radius:28px;box-shadow:0 24px 60px rgba(29,39,66,.10);overflow:hidden;position:relative}
.tb{height:64px;display:flex;align-items:center;gap:12px;padding:0 24px;border-bottom:2px solid var(--line);font-size:26px;font-weight:700;color:var(--sub)}
.dot{width:16px;height:16px;border-radius:50%;background:#E3E6EC}
.mk{outline:6px solid var(--red);outline-offset:8px;box-shadow:0 0 0 22px rgba(239,71,87,.13)}
.it{display:inline-block;background:var(--red);color:#fff;font-size:24px;font-weight:700;border-radius:10px;padding:2px 12px;margin-left:16px;vertical-align:middle}
.hl{position:absolute;border:6px solid var(--red);border-radius:18px;box-shadow:0 0 0 10px rgba(239,71,87,.15)}
.tag{position:absolute;background:var(--red);color:#fff;font-size:28px;font-weight:700;border-radius:14px;padding:6px 18px}
.btn{display:inline-block;background:var(--blue);color:#fff;font-weight:700;border-radius:14px;padding:12px 30px;font-size:30px}
.ghost{display:inline-block;border:2px solid var(--line);border-radius:14px;padding:10px 26px;font-size:28px;color:var(--sub)}
.badge{display:inline-flex;align-items:center;justify-content:center;border-radius:28px;color:#fff;font-weight:800}
.lbl{font-size:26px;color:var(--sub)}
.arrow{text-align:center;font-size:44px;color:#A9B2C4;line-height:1}
.sub{position:absolute;left:0;right:0;bottom:0;height:300px}
"""
def page(n, no, title, lead, body):
    (R/'src'/f'{n}.html').write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="top"><div class="no">{no}</div><div class="h1">{title}</div><div class="lead">{lead}</div></div><div class="demo">示意</div><div class="stage">{body}</div><div class="sub"></div></body></html>')
def win(title, inner, h, extra=''):
    return f'<div class="win" style="height:{h}px;{extra}"><div class="tb"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span style="margin-left:12px">{title}</span></div>{inner}</div>'
WB = '<span class="badge" style="width:{s}px;height:{s}px;background:var(--wb);font-size:{f}px">WB</span>'
DT = '<span class="badge" style="width:{s}px;height:{s}px;background:var(--dt);font-size:{f}px">钉</span>'

# s0
page('s0','s0 · 开场','到点提醒你打卡','WorkBuddy × 钉钉',f'''
<div style="position:absolute;left:170px;top:0;width:620px;height:900px;background:#fff;border:3px solid var(--line);border-radius:60px;box-shadow:0 24px 60px rgba(29,39,66,.12);overflow:hidden">
 <div style="text-align:center;font-size:96px;font-weight:300;margin-top:70px">09:12</div>
 <div style="text-align:center;font-size:28px;color:var(--sub)">10月21日 星期三</div>
 <div class="mk" style="margin:60px 30px 0;background:var(--rs);border-radius:28px;padding:30px;position:relative">
  <div style="display:flex;align-items:center;gap:16px">{DT.format(s=56,f=28)}<span style="font-size:26px;color:var(--sub)">考勤打卡 · 刚刚</span></div>
  <div style="font-size:46px;font-weight:800;color:var(--red);margin-top:18px">上班缺卡</div>
  <div style="font-size:28px;color:var(--sub);margin-top:8px">今日上班未打卡，请及时处理</div></div>
 
</div>
<div style="position:absolute;left:0;right:0;top:960px;display:flex;justify-content:center;align-items:center;gap:30px">
 {WB.format(s=120,f=44)}<span style="font-size:60px;color:#A9B2C4">×</span>{DT.format(s=120,f=56)}</div>
<div style="position:absolute;left:0;right:0;top:1110px;text-align:center"><span style="background:var(--ms);color:#0E8A6B;font-size:34px;font-weight:700;border-radius:999px;padding:12px 36px">它不替你打卡，只提醒</span></div>
''')

# s1
page('s1','s1 · ① 下载安装','安装并登录','官网下载 · Windows / Mac · 微信扫码',f'''
{win('WorkBuddy 官网', f"""<div style="padding:30px 40px;display:flex;align-items:center;gap:26px">{WB.format(s=80,f=30)}<div><div style="font-size:38px;font-weight:800">WorkBuddy</div><div class="lbl">你的办公 AI 助理</div></div></div>
<div style="padding:0 40px;display:flex;gap:20px"><span class="btn mk">下载 Windows 版</span><span class="btn mk" style="background:#1D2742">下载 Mac 版</span></div>""",300)}

<div class="arrow" style="margin:14px 0">↓</div>
{win('安装向导', """<div style="padding:30px 40px;display:flex;align-items:center;justify-content:space-between"><div><div style="font-size:36px;font-weight:800">安装完成 ✓</div><div class="lbl" style="margin-top:6px">WorkBuddy 已安装到本机</div></div><span class="btn">立即启动</span></div>""",190)}
<div class="arrow" style="margin:14px 0">↓</div>
{win('登录', f"""<div style="display:flex;align-items:center;gap:40px;padding:30px 40px"><svg width="210" height="210" viewBox="0 0 21 21"><rect width="21" height="21" fill="#fff"/><g fill="#1D2742"><rect x="0" y="0" width="7" height="7"/><rect x="14" y="0" width="7" height="7"/><rect x="0" y="14" width="7" height="7"/></g><g fill="#fff"><rect x="1" y="1" width="5" height="5"/><rect x="15" y="1" width="5" height="5"/><rect x="1" y="15" width="5" height="5"/></g><g fill="#1D2742"><rect x="2" y="2" width="3" height="3"/><rect x="16" y="2" width="3" height="3"/><rect x="2" y="16" width="3" height="3"/><rect x="9" y="2" width="2" height="2"/><rect x="8" y="8" width="3" height="2"/><rect x="12" y="9" width="2" height="3"/><rect x="9" y="12" width="2" height="2"/><rect x="15" y="12" width="3" height="2"/><rect x="12" y="15" width="2" height="3"/><rect x="16" y="17" width="3" height="2"/><rect x="9" y="17" width="2" height="2"/></g></svg>
<div><div style="font-size:38px;font-weight:800">微信扫码登录</div><div class="lbl" style="margin-top:10px">打开微信 → 扫一扫</div><div style="margin-top:20px;font-size:26px;color:#0E8A6B;font-weight:700">● 等待扫码</div></div></div>""",340)}
''')

# s2
page('s2','s2 · ② 钉钉建机器人','群里加个自定义机器人','机器人 → 自定义 → 关键词「打卡」',f'''
{win('钉钉 · 打卡提醒测试群 · 群设置', """<div style="display:flex;height:956px">
<div style="width:200px;flex-shrink:0;border-right:2px solid var(--line);padding:24px 0;font-size:28px;color:var(--sub)">
<div style="padding:18px 30px">群公告</div><div style="padding:18px 30px">群管理</div><div style="padding:18px 30px;background:var(--bs);color:var(--blue);font-weight:700">机器人</div><div style="padding:18px 30px">群文件</div></div>
<div style="flex:1;min-width:0;padding:30px 44px 30px 34px">
<div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:34px;font-weight:800">添加机器人 · 自定义</div><span class="ghost" style="font-size:24px">Webhook 接入</span></div>
<div class="lbl" style="margin-top:34px">机器人名字</div><div style="border:2px solid var(--line);border-radius:12px;padding:14px 18px;font-size:30px;margin-top:10px">打卡提醒</div>
<div style="font-size:30px;font-weight:700;margin-top:40px">安全设置</div>
<div class="mk" style="margin-top:18px;font-size:30px;display:flex;align-items:center;gap:14px;border-radius:8px"><span style="width:38px;height:38px;border-radius:8px;background:var(--blue);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-size:26px">✓</span>自定义关键词<span class="it">勾选 · 填「打卡」</span></div>
<div style="margin-top:14px;margin-left:52px;display:inline-block;background:var(--bs);color:var(--blue);font-size:32px;font-weight:800;border-radius:12px;padding:8px 24px">打卡</div>
<div style="margin-top:22px;font-size:30px;color:#A9B2C4;display:flex;align-items:center;gap:14px"><span style="width:38px;height:38px;border-radius:8px;border:2px solid var(--line);display:inline-block"></span>加签</div>
<div style="margin-top:12px;font-size:30px;color:#A9B2C4;display:flex;align-items:center;gap:14px"><span style="width:38px;height:38px;border-radius:8px;border:2px solid var(--line);display:inline-block"></span>IP 地址（段）</div>
<div style="font-size:30px;font-weight:700;margin-top:44px">Webhook<span class="it">复制，打码保存</span></div>
<div class="mk" style="margin-top:20px;display:flex;gap:14px;align-items:center;border-radius:12px"><div style="flex:1;border:2px solid var(--line);border-radius:12px;padding:14px 16px;font-size:22px;color:var(--sub);background:#F7F8FB;white-space:nowrap;overflow:hidden;min-width:0">oapi.dingtalk.com/robot/send?access_token=••••</div><span class="btn" style="font-size:28px;padding:12px 22px">复制</span></div>
<div class="lbl" style="margin-top:16px">Webhook 等同密码，不要发到群外</div>
</div></div>""",1020)}


''')

# shared WorkBuddy window
def wbwin(main, h=1020, active='定时任务', mark=False):
    items=['新对话','任务','定时任务','技能','设置']
    side=''.join(f'<div style="padding:18px 26px;{"background:var(--bs);color:var(--blue);font-weight:700;border-radius:12px;margin:0 10px" if i==active else "margin:0 10px"}" class="{"mk" if (mark and i==active) else ""}">{i}{"<div style=&quot;font-size:22px&quot;></div>" if 0 else ""}</div>' for i in items)
    return win('WorkBuddy', f'<div style="display:flex;height:{h-64}px"><div style="width:220px;border-right:2px solid var(--line);padding:24px 0;font-size:28px;color:var(--sub)"><div style="padding:0 26px 22px">{WB.format(s=56,f=22)}</div>{side}</div><div style="flex:1;position:relative;padding:30px 34px">{main}</div></div>', h)

# s3
page('s3','s3 · ③ 定时任务','新建定时任务','定时任务 → 新建 ▾ → 从任务新建', wbwin('''
<div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:36px;font-weight:800">定时任务<span class="it">① 左侧进入</span></div><span><span class="it" style="margin-right:20px">②</span><span class="btn mk">新建 ▾</span></span></div>
<div style="position:absolute;right:34px;top:130px;width:330px;background:#fff;border:2px solid var(--line);border-radius:18px;box-shadow:0 16px 40px rgba(29,39,66,.14);font-size:28px;overflow:hidden">
<div style="padding:22px 26px;color:var(--sub)">空白新建</div><div class="mk" style="padding:22px 26px;background:var(--bs);color:var(--blue);font-weight:700;outline-offset:-6px;box-shadow:none">从任务新建<span class="it">③</span></div><div style="padding:22px 26px;color:var(--sub)">从模板新建</div></div>
<div style="position:absolute;left:34px;right:34px;top:400px;text-align:center;color:#A9B2C4;font-size:30px">还没有定时任务</div>
<div style="position:absolute;left:34px;right:34px;bottom:34px;border:2px solid var(--blue);border-radius:20px;padding:24px;min-height:200px;font-size:32px">帮我创建一个定时任务：<span style="color:var(--blue)">|</span><div style="text-align:right;margin-top:60px"><span class="btn" style="background:#C9D6FF">发送</span></div></div>
''',mark=True)+'''

''')

# s4
page('s4','s4 · 说一句话','用一句话描述任务','工作日 8:50 / 18:00 · curl → Webhook', wbwin('''
<div style="font-size:36px;font-weight:800">新建定时任务</div>
<div style="position:absolute;left:34px;right:34px;top:130px;border:3px solid var(--blue);border-radius:22px;padding:30px;font-size:36px;line-height:1.6;background:#fff">帮我创建一个定时任务：<br><b>每个工作日 8:50 和 18:00，用 curl 往钉钉 Webhook 发打卡提醒</b>，消息内容「该打卡了」。<br><span style="font-size:26px;color:var(--sub)">Webhook：https://oapi.dingtalk.com/robot/send?access_token=••••</span>
<div style="text-align:right;margin-top:40px"><span class="btn mk" style="font-size:34px;padding:14px 40px">发送 ➤</span></div></div>
<div style="position:absolute;left:34px;right:34px;top:760px;font-size:26px;color:var(--sub);line-height:1.6">提示：消息里要带关键词「打卡」，否则钉钉会拦截</div>
'''))
# highlight for s4 send
#p=R/'src'/'s4.html'; p.write_text(p.read_text().replace('<div class="sub">','<div class="sub">'))

# s5
page('s5','s5 · ④ 确认配置','确认配置','周一至周五 · 完全访问 · 常关机选云端', wbwin('''
<div style="background:var(--ms);border-radius:18px;padding:22px 26px;font-size:28px"><b style="color:#0E8A6B">✓ 已创建定时任务</b><div style="color:var(--sub);margin-top:6px">打卡提醒 · 工作日 08:50 / 18:00</div><div style="text-align:right;margin-top:-40px"><span class="ghost" style="background:#fff">编辑</span></div></div>
<div style="margin-top:28px;border:2px solid var(--line);border-radius:20px;padding:28px 30px;font-size:30px">
<div style="font-size:34px;font-weight:800;margin-bottom:20px">编辑定时任务</div>
<div class="lbl">任务名称</div><div style="margin:8px 0 22px">打卡提醒</div>
<div class="lbl">重复</div><div class="mk" style="margin:8px 0 26px;display:inline-flex;gap:10px;border-radius:30px">''' + ''.join(f'<span style="width:58px;height:58px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:26px;{"background:var(--blue);color:#fff" if d in "一二三四五" else "background:#EEF0F4;color:#A9B2C4"}">{d}</span>' for d in '一二三四五六日') + '''</div>
<div class="lbl">时间</div><div class="mk" style="margin:8px 0 26px;display:inline-flex;gap:14px;border-radius:14px"><span class="ghost" style="color:var(--ink);font-weight:700">08:50</span><span class="ghost" style="color:var(--ink);font-weight:700">18:00</span></div>
<div class="lbl">权限</div><div style="margin:8px 0 26px"><span class="mk" style="font-weight:700;color:var(--blue);border-radius:8px">● 完全访问权限 ▾</span></div>
<div class="lbl">运行位置</div><div style="margin:8px 0 6px;display:flex;gap:14px"><span class="ghost">本机</span><span class="ghost" style="border-color:var(--amber);color:#B86A00">云端任务（常关机选这个）</span></div>
</div>''')+'''

''')

# s6
page('s6','s6 · ⑤ 立即运行','立即运行验证','立即运行 → 钉钉收到 → 运行成功',f'''
{win('WorkBuddy · 定时任务', """<div style="padding:26px 34px;display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:34px;font-weight:800">打卡提醒</div><div class="lbl">工作日 08:50 / 18:00</div></div><span class="btn mk">▶ 立即运行</span></div>""",210)}

<div class="arrow" style="margin:14px 0">↓</div>
{win('钉钉 · 打卡提醒测试群', f"""<div style="padding:26px 34px;display:flex;gap:20px;align-items:flex-start"><span class="badge" style="width:70px;height:70px;background:#8A93A8;font-size:26px;border-radius:50%">机</span><div><div class="lbl">打卡提醒 · 机器人 · 刚刚</div><div style="margin-top:10px;background:var(--bs);border-radius:0 22px 22px 22px;padding:20px 28px;font-size:40px;font-weight:800"><svg width="40" height="40" viewBox="0 0 24 24" style="vertical-align:-6px"><circle cx="12" cy="13" r="9" fill="#FF9F1C"/><circle cx="12" cy="13" r="6.5" fill="#fff"/><path d="M12 9v4l3 2" stroke="#1D2742" stroke-width="2" fill="none" stroke-linecap="round"/></svg> 该打卡了</div></div></div>""",230)}
<div class="arrow" style="margin:14px 0">↓</div>
{win('WorkBuddy · 运行记录', """<div style="padding:10px 34px;font-size:28px">
<div style="display:flex;padding:16px 0;color:var(--sub);border-bottom:2px solid var(--line)"><span style="flex:2">时间</span><span style="flex:1">方式</span><span style="flex:1;text-align:right">状态</span></div>
<div style="display:flex;padding:20px 0;border-bottom:2px solid var(--line);font-weight:700"><span style="flex:2">10-21 15:40</span><span style="flex:1">手动</span><span style="flex:1;text-align:right"><span class="mk" style="color:#0E8A6B;border-radius:8px;padding:0 8px">● 成功</span></span></div>
<div style="display:flex;padding:20px 0;color:#A9B2C4"><span style="flex:2">下次 10-22 08:50</span><span style="flex:1">定时</span><span style="flex:1;text-align:right">待运行</span></div></div>""",330)}
''')

# s7 合规提醒
def warn(n, t, d, extra=''):
    return f'<div style="background:#FFF6E0;border:3px solid #FFC94D;border-radius:28px;padding:30px 34px;display:flex;gap:28px;align-items:center;margin-bottom:28px"><span class="badge" style="width:84px;height:84px;background:var(--amber);font-size:44px;border-radius:50%;flex-shrink:0">{n}</span><div style="flex:1"><div style="font-size:40px;font-weight:800">{t}</div><div style="font-size:28px;color:var(--sub);margin-top:6px">{d}</div></div>{extra}</div>'
PIN = '<svg width="110" height="110" viewBox="0 0 48 48" style="flex-shrink:0"><path d="M24 6c-7 0-12 5-12 12 0 9 12 22 12 22s12-13 12-22c0-7-5-12-12-12z" fill="#C9D3E3"/><circle cx="24" cy="18" r="5" fill="#fff"/><path d="M8 8L40 40M40 8L8 40" stroke="#EF4757" stroke-width="5" stroke-linecap="round"/></svg>'
page('s7','s7 · 注意三点','注意三点','不代打卡 · 不虚拟定位 · 不外传', '<div style="padding-top:20px">' +
 warn('1','不代打卡，不改定位','AI 只提醒；虚拟定位违规，钉钉会判异常', PIN) +
 warn('2','Webhook 别外传','它等同密码，截图、发群都要打码') +
 warn('3','本地任务电脑要开机','客户端别退出；常关机就用云端任务') + '</div>')

# s8 结尾
page('s8','s8 · 结尾','你只管伸手打卡','收藏 · 转给总忘打卡的同事', f'''
<div style="position:absolute;left:170px;top:0;width:620px;height:820px;background:#fff;border:3px solid var(--line);border-radius:60px;box-shadow:0 24px 60px rgba(29,39,66,.12);overflow:hidden">
 <div style="height:110px;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:700;border-bottom:2px solid var(--line)">考勤打卡</div>
 <div style="margin:70px auto 0;width:300px;height:300px;border-radius:50%;background:var(--mint);display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 26px var(--ms)"><svg width="150" height="150" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
 <div style="text-align:center;font-size:52px;font-weight:800;color:#0E8A6B;margin-top:60px">打卡正常</div>
 <div style="text-align:center;font-size:30px;color:var(--sub);margin-top:10px">上班 08:53 · 已提醒 08:50</div>
</div>
<div style="position:absolute;left:0;right:0;top:880px;display:flex;justify-content:center;align-items:center;gap:30px">{WB.format(s=120,f=44)}<span style="font-size:60px;color:#A9B2C4">×</span>{DT.format(s=120,f=56)}</div>
<div style="position:absolute;left:0;right:0;top:1030px;text-align:center"><span style="background:var(--bs);color:var(--blue);font-size:34px;font-weight:700;border-radius:999px;padding:12px 36px">到点就提醒 · 收藏转给爱忘打卡的同事</span></div>
''')
