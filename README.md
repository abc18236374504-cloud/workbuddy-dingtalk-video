# workbuddy-dingtalk-video

HyperFrames 竖屏教程：用 WorkBuddy 两分钟设好钉钉打卡提醒。1080×1920，30fps，9 镜，约 91 秒。

| 目录 | 内容 |
|---|---|
| script/ | script.json（编剧 9 镜原文）、script.md、view.json（标题/提示条/徽章）、load.py |
| audio/ | sN.wav 分段配音（tts-1 alloy，speed 1.25）+ durations.json |
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

## 成员推送方式

```bash
git clone https://github.com/abc18236374504-cloud/workbuddy-dingtalk-video.git
cd workbuddy-dingtalk-video
# 令牌只放环境变量，不要写进 remote URL、文件或提交
export GH_TOKEN=...      # 需 Contents: Read and write
git pull --rebase origin main
git add <你的路径> && git commit -m "身份：做了什么"
git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)" push origin main
# 被拒（non-fast-forward）就 git pull --rebase 再 push
```

- 配音放 audio/sN.wav 并更新 audio/durations.json；素材放 assets/sN.png|mp4；脚本改 script/script.json。
- 单文件 < 95 MB；成片走 Release，仓库里的 render/final.mp4 只留最新一版。
- .gitignore 已排除 node_modules 和 .env / *token* / *secret* / *key*.txt。
