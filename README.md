# workbuddy-dingtalk-video

HyperFrames 竖屏教程：用 WorkBuddy 两分钟设好钉钉打卡提醒。1080×1920，30fps，约 53 秒。

| 目录 | 内容 |
|---|---|
| script/ | script.json（分镜、屏幕字、口播），durations.json（按配音算出的时间），style.css |
| audio/ | sN.wav 分段配音（tts-1 alloy，speed 1.3），voice.wav 混好的整轨 |
| assets/ | 字体子集、gsap.min.js；素材组的 sN.png/mp4 也放这里 |
| project/ | HyperFrames 工程（build.py 生成 index.html） |
| render/ | test.mp4（5 秒测试片）、final.mp4 |
| shots/ | 关键帧截图 |

```bash
export TTS_KEY=...        # 只在改口播时需要；也可以写进 .env（已 gitignore）
python3 tts.py            # 生成 audio/ + script/durations.json
./render.sh               # build.py → lint → render/final.mp4
```
安装和 ARM64 环境说明见 setup.md。
