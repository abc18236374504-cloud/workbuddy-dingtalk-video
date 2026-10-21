#!/usr/bin/env bash
# python3 tts.py (optional, needs TTS_KEY) -> python3 build.py -> lint -> render/final.mp4
set -e; cd "$(dirname "$0")"
[ -f ~/hfenv.sh ] && . ~/hfenv.sh
python3 build.py
cd project && npx -y hyperframes@0.8.184 lint && npx -y hyperframes@0.8.184 render -o ../render/final.mp4 -f 30 -q standard --quiet
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate:format=duration -of compact ../render/final.mp4
