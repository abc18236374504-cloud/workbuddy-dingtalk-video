#!/usr/bin/env python3
"""script/script.json -> audio/sN.wav + audio/voice.wav + script/durations.json
Key: export TTS_KEY=...  (or put TTS_KEY=... in .env, which is gitignored). Never commit the key.
"""
import json, os, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__))
key = os.environ.get("TTS_KEY")
if not key and os.path.exists(os.path.join(ROOT, ".env")):
    for l in open(os.path.join(ROOT, ".env")):
        if l.startswith("TTS_KEY="): key = l.split("=", 1)[1].strip()
SPEED = float(os.environ.get("TTS_SPEED", "1.3")); GAP = 0.45; LEAD = 0.3
segs = json.load(open(os.path.join(ROOT, "script", "script.json")))
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]))
out = []; t = LEAD
for s in segs:
    wav = os.path.join(ROOT, "audio", f"{s['id']}.wav")
    if key:
        body = json.dumps({"model":"tts-1","input":s["vo"],"voice":"alloy","speed":SPEED,"response_format":"wav"}, ensure_ascii=False)
        subprocess.run(["curl","-sf","-X","POST","https://tts.apivip.qzz.io/v1/audio/speech","-H",f"Authorization: Bearer {key}","-H","Content-Type: application/json","--data-binary",body,"-o",wav], check=True)
    d = dur(wav); out.append({"id":s["id"],"step":s["step"],"vo_start":round(t,3),"vo_duration":round(d,3)}); t += d + GAP
for i,o in enumerate(out): o["start"] = 0 if i == 0 else round(o["vo_start"]-0.15,3)
for i,o in enumerate(out):
    end = out[i+1]["start"] if i+1 < len(out) else round(t+0.6,3); o["duration"] = round(end-o["start"],3)
total = round(out[-1]["start"]+out[-1]["duration"],3)
json.dump({"fps":30,"width":1080,"height":1920,"total":total,"segments":out}, open(os.path.join(ROOT,"script","durations.json"),"w"), ensure_ascii=False, indent=1)
cmd = ["ffmpeg","-y","-v","error"]; flt = ""
for i,o in enumerate(out):
    cmd += ["-i", os.path.join(ROOT,"audio",f"{o['id']}.wav")]
    flt += f"[{i}:a]aresample=48000,adelay={int(o['vo_start']*1000)}:all=1[a{i}];"
flt += "".join(f"[a{i}]" for i in range(len(out))) + f"amix=inputs={len(out)}:normalize=0,apad,atrim=0:{total},loudnorm=I=-16:TP=-1.5[out]"
subprocess.run(cmd+["-filter_complex",flt,"-map","[out]","-ac","2","-ar","48000",os.path.join(ROOT,"audio","voice.wav")], check=True)
print("total", total)
