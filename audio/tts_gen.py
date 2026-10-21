# 逐镜合成：密钥只从环境变量 TTS_KEY 读取。用法：TTS_KEY=... python3 tts_gen.py
import json,os,subprocess
S=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','script','script.json'))); C=S['tts']; K=os.environ['TTS_KEY']
SPOKEN=[('WorkBuddy','Work Buddy'),('curl','科尔'),('8 点 50','八点五十'),('6 点','六点'),('「','“'),('」','”')]
out={}
for s in S['shots']:
    t=s['text']
    for a,b in SPOKEN: t=t.replace(a,b)
    json.dump({"model":C['model'],"input":t,"voice":C['voice'],"speed":C['speed'],"response_format":"wav"},open('body.json','w'),ensure_ascii=False)
    for _ in range(3):
        subprocess.run(['curl','-s','-m','90','-X','POST','https://tts.apivip.qzz.io/v1/audio/speech','-H','Authorization: Bearer '+K,'-H','Content-Type: application/json','--data-binary','@body.json','-o','raw.wav'])
        if open('raw.wav','rb').read(4)==b'RIFF': break
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i','raw.wav','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-ar','48000','-ac','1','-c:a','pcm_s16le',f"{s['id']}.wav"])
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f"{s['id']}.wav"],capture_output=True,text=True).stdout)
    out[s['id']]=round(d,3); print(s['id'],d)
os.remove('raw.wav'); os.remove('body.json')
json.dump({"unit":"seconds","voice":C['voice'],"speed":C['speed'],"sample_rate":48000,"shots":out,"total":round(sum(out.values()),3)},open('durations.json','w'),ensure_ascii=False,indent=1)
