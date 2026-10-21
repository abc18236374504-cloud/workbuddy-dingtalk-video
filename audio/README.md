# audio（配音师）

依据 script/script.json（9 镜 s0–s8）。tts-1，alloy，speed 1.25，每镜单独 loudnorm 到 -16 LUFS，48 kHz 单声道 16-bit wav。

| 镜 | 秒 |
|---|---|
| s0 | 13.001 |
| s1 | 5.833 |
| s2 | 11.275 |
| s3 | 7.337 |
| s4 | 9.325 |
| s5 | 12.155 |
| s6 | 7.723 |
| s7 | 12.548 |
| s8 | 7.055 |

合计 86.252 s（不含镜间停顿）。时间线以 durations.json 为准。

重新生成：在 audio/ 下运行 TTS_KEY=… python3 tts_gen.py（密钥只走环境变量）。
