# 🐻 Bearth Discord Bot

Bearth 資訊導覽 Discord 機器人，使用 Python + discord.py 建立。

## 📁 檔案結構

```
bearth_bot/
├── bearth_bot.py      # 主程式
├── keep_alive.py      # HTTP 服務 (免費方案用)
├── requirements.txt   # Python 依賴
├── render.yaml        # Render 部署配置
└── README.md          # 說明文件
```

## 🚀 部署到 Render（免費方案）

### 步驟 1：推送到 GitHub

```bash
cd bearth_bot
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/你的帳號/bearth-discord-bot.git
git push -u origin main
```

### 步驟 2：在 Render 建立服務

1. 登入 [Render Dashboard](https://dashboard.render.com/)
2. 點擊 **New +** → **Web Service**
3. 連接你的 GitHub Repository
4. 設定：
   - **Name**: `bearth-discord-bot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bearth_bot.py`
   - **Instance Type**: `Free`

### 步驟 3：設定環境變數

在 Render Dashboard → **Environment** 加入：
- **Key**: `DISCORD_TOKEN`
- **Value**: `你的 Discord Bot Token`

### 步驟 4：設定 UptimeRobot 防止休眠

Render 免費方案會在 15 分鐘無活動後休眠，需要外部監控：

1. 註冊 [UptimeRobot](https://uptimerobot.com/)（免費）
2. 新增 Monitor：
   - **Type**: HTTP(s)
   - **URL**: `https://你的服務名.onrender.com/health`
   - **Interval**: 5 分鐘
3. 這樣 UptimeRobot 會每 5 分鐘 ping 你的服務，保持活躍

## 🖥️ 本地測試

```bash
# 安裝依賴
pip install -r requirements.txt

# 設定環境變數 (Windows PowerShell)
$env:DISCORD_TOKEN="你的Token"

# 執行機器人
python bearth_bot.py
```

## 📝 功能說明

- `/mindmap` - 開啟 Bearth 資訊導覽選單
- 點擊按鈕會更新同一個訊息（不會彈出新對話框）

## 🔧 取得 Discord Bot Token

1. 前往 [Discord Developer Portal](https://discord.com/developers/applications)
2. 建立新的 Application
3. 到 **Bot** 頁面，點擊 **Reset Token** 取得 Token

## 📋 邀請機器人到伺服器

1. 到 **OAuth2** → **URL Generator**
2. 勾選 Scopes: `bot`, `applications.commands`
3. 勾選 Bot Permissions: `Send Messages`, `Use Slash Commands`, `Embed Links`
4. 複製產生的 URL 並在瀏覽器開啟
