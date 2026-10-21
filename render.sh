#!/usr/bin/env bash
# python3 tts.py (optional, needs TTS_KEY) -> python3 build.py -> lint -> render/final.mp4
set -e; cd "$(dirname "$0")"
[ -f ~/hfenv.sh ] && . ~/hfenv.sh
python3 build.py
cd project && npx -y hyperframes@0.8.184 lint && npx -y hyperframes@0.8.184 render -o /tmp/hf_final.mp4 -f 30 -q standard --quiet
cp /tmp/hf_final.mp4 ../render/final.mp4   # JuiceFS 等网络盘上 ffmpeg faststart 写 trailer 会 I/O error，先渲到本地盘
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate:format=duration -of compact ../render/final.mp4
