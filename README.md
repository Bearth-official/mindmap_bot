# 🐻 Bearth Discord Bot

Bearth 資訊導覽 Discord 機器人，使用 Python + discord.py 建立。

## 📁 檔案結構

```
bearth_bot/
├── bearth_bot.py      # 主程式
├── requirements.txt   # Python 依賴
├── render.yaml        # Render 部署配置
└── README.md          # 說明文件
```

## 🚀 部署到 Render

### 步驟 1：推送到 GitHub

1. 建立一個新的 GitHub Repository
2. 將 `bearth_bot` 資料夾的內容推送上去：

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
2. 點擊 **New +** → **Background Worker**
3. 連接你的 GitHub Repository
4. 設定：
   - **Name**: `bearth-discord-bot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bearth_bot.py`

### 步驟 3：設定環境變數

1. 在 Render Dashboard 的服務頁面，點擊 **Environment**
2. 加入環境變數：
   - **Key**: `DISCORD_TOKEN`
   - **Value**: `你的 Discord Bot Token`

> ⚠️ **重要**：不要把 Token 直接寫在程式碼裡！

### 步驟 4：部署

1. 點擊 **Manual Deploy** → **Deploy latest commit**
2. 等待部署完成
3. 檢查 Logs 確認機器人已上線

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
- 按鈕選項：
  - ✨ Vision & Value
  - 🤝 Community
  - 📈 Expansion
  - 💻 Digital
  - 🧸 Physical
  - 🔗 Hybrid

## 🔧 取得 Discord Bot Token

1. 前往 [Discord Developer Portal](https://discord.com/developers/applications)
2. 建立新的 Application
3. 到 **Bot** 頁面，點擊 **Reset Token** 取得 Token
4. 開啟以下 Privileged Gateway Intents（如果需要）：
   - Presence Intent
   - Server Members Intent
   - Message Content Intent

## 📋 邀請機器人到伺服器

在 Discord Developer Portal：
1. 到 **OAuth2** → **URL Generator**
2. 勾選 Scopes: `bot`, `applications.commands`
3. 勾選 Bot Permissions: `Send Messages`, `Use Slash Commands`, `Embed Links`
4. 複製產生的 URL 並在瀏覽器開啟
