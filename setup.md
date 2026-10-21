# HyperFrames 部署与合成说明（HyperFrames 工程师）

## 1. 安装
```bash
git clone --depth 1 https://github.com/heygen-com/hyperframes.git   # 源码/文档参考
node -v                     # 需 >= 22
npx -y hyperframes@0.8.184 --version
npx hyperframes doctor      # 需 ffmpeg/ffprobe + Chrome
npx hyperframes browser ensure   # x86_64 自动装 Chrome Headless Shell
```
### Linux ARM64 / 无 root（本次环境）
官方 headless shell 无 arm64 包，apt 无权限，改用 Playwright 的 arm64 headless shell + 手动补库：
```bash
npx -y playwright install chromium-headless-shell
# 缺 libatk / libatspi / libXcomposite / libXdamage：从 deb.debian.org pool 下 arm64 .deb，dpkg-deb -x 到 ~/libs/root
export LD_LIBRARY_PATH=~/libs/root/usr/lib/aarch64-linux-gnu
export HYPERFRAMES_BROWSER_PATH=~/.cache/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-linux-arm64/chrome-headless-shell
export HYPERFRAMES_SKIP_SKILLS=1
```

## 2. 测试片（5 秒 1080×1920）
```bash
npx hyperframes init test --example blank --resolution portrait --non-interactive
# index.html 里 data-duration 改 5
cd test && npx hyperframes render -o test.mp4 -f 30 -q draft
ffprobe test.mp4   # 1080x1920, 30/1, 5.000000s   渲染耗时约 9s
```

## 3. 配音（TTS，语速 1.3）
```bash
curl -X POST "https://tts.apivip.qzz.io/v1/audio/speech" \
  -H "Authorization: Bearer $TTS_KEY" -H "Content-Type: application/json" \
  -d '{"model":"tts-1","input":"<每段口播>","voice":"alloy","speed":1.3,"response_format":"wav"}' -o audio/s0.wav
```
- 注意：用 curl 调；Python urllib 默认 UA 会被 403。
- 每段时长 ffprobe 量出，写入 durations.json（start / vo_start / vo_duration / duration，段间留 0.45s）。
- 各段按 vo_start 用 ffmpeg adelay+amix 拼成 voice.wav，loudnorm -16 LUFS。

## 4. 合成模板写法（build.py 读 script/ audio/ assets/，生成 project/index.html）
```html
<div id="root" data-composition-id="main" data-start="0" data-duration="53.412" data-width="1080" data-height="1920">
  <section class="clip scene" id="s1" data-start="7.374" data-duration="5.312" data-track-index="1">
    <div class="head"><div class="badge">STEP 1</div><h2>标题</h2></div>   <!-- 步骤编号 -->
    <div class="stage"><div class="cam" id="s1-cam">素材/UI</div></div>     <!-- 推拉 -->
    <div class="chip">屏幕字</div>
    <div class="sub"><p><span class="ch" id="s1-c0">第</span>…<span class="caret"></span></p></div> <!-- 打字机 -->
  </section>
  <div class="hud"><div class="dots">1…6</div><div class="track"><div id="pbar"></div></div></div> <!-- 进度条 -->
  <audio class="clip" src="assets/voice.wav" data-start="0" data-duration="53.412" data-track-index="5"></audio>
</div>
<script src="assets/gsap.min.js"></script>
<script>
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
tl.fromTo("#s1-cam",{scale:1.12},{scale:1,duration:5.312,ease:"sine.inOut"},7.374);   // 推/拉交替
tl.set("#s1-c0",{display:"inline"},7.524);                                            // 打字机：按配音时长逐字
tl.fromTo("#pbar",{scaleX:0},{scaleX:1,duration:53.412,ease:"none"},0);               // 进度条
window.__timelines["main"] = tl;
</script>
```
规则：只用确定性逻辑（无 Date.now/Math.random/网络），GSAP 和字体放本地 assets（CDN 在渲染机可能 407）；中文字体用 NotoSansSC 子集 + @font-face，否则 lint 报 font_family_without_font_face。

## 5. 替换真实素材
其他成员交来 assets/sN.png|mp4 后，先把文件放进 assets/，再把 build.py 里 MOCK["sN"] 换成
`<img src="assets/sN.png" style="width:900px">` 或 `<video src="assets/sN.mp4" muted class="clip" data-start=.. data-duration=..>`，改 script.json 屏幕字/口播后：
```bash
python3 tts.py   # 读 TTS_KEY 环境变量或 .env → audio/*.wav、script/durations.json、audio/voice.wav
pyftsubset NotoSansSC[wght].ttf --text-file=chars.txt --output-file=project/assets/NotoSansSC-subset.ttf
./render.sh      # build.py → lint → render/final.mp4
```
