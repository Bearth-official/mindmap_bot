# Bearth Discord Bot - Python Version
# 執行指令： python bearth_bot.py
# 如果出現 ModuleNotFoundError，請先執行： pip install discord.py

import discord
from discord import app_commands
import os

# 1. 建立 Client 實體
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# 按鈕標籤的多語言版本
BUTTON_LABELS = {
    "en": {
        "vision_value": "Vision & Value",
        "community": "Community",
        "expansion": "Expansion",
        "digital": "Digital",
        "physical": "Physical",
        "hybrid": "Hybrid",
        "lang_switch": "中文",
        "lang_emoji": "\U0001F004",  # 🀄 麻將紅中
    },
    "zh": {
        "vision_value": "願景與價值",
        "community": "社群",
        "expansion": "擴展",
        "digital": "數位",
        "physical": "實體",
        "hybrid": "混合",
        "lang_switch": "English",
        "lang_emoji": "\U0001F1FA\U0001F1F8",  # �🇸 美國國旗
    }
}

# 公共訊息 Embed 內容
def get_public_embed(lang: str = "en") -> discord.Embed:
    """根據語言返回公共訊息 Embed"""
    if lang == "en":
        embed = discord.Embed(
            title="\U0001F5FA\uFE0F MINDMAP",
            description="Bearth is an original IP, a universe born from a story of loss and rebirth. We are building a transmedia world that grows and evolves with its community.\n\nThis mindmap is our living blueprint, not a rigid roadmap. It's about creating a home among the stars, one thoughtful step at a time.",
            color=0x5865F2  # Discord 藍色
        )
        embed.add_field(
            name="\U0001F4D6 How to use",
            value="Click the **Read** button below to open your personal navigation panel. Only you can see it!",
            inline=False
        )
    else:
        embed = discord.Embed(
            title="\U0001F5FA\uFE0F 思維導圖",
            description="Bearth 是一個原創 IP，一個從失去與重生的故事中誕生的宇宙。我們正在建立一個與社群共同成長和演化的跨媒體世界。\n\n這個思維導圖是我們的活藍圖，而非僵化的路線圖。這是關於在星空中創造一個家園，一步一個腳印，用心前行。",
            color=0x5865F2
        )
        embed.add_field(
            name="\U0001F4D6 使用說明",
            value="點擊下方的**閱讀**按鈕開啟您的個人導覽面板，只有您自己看得到！",
            inline=False
        )
    return embed

# 多語言內容資料
CONTENT = {
    "en": {
        "header": "🐻 **Bearth Info Center**\nClick the buttons below to explore:",
        "vision_value": {
            "title": "✨ Vision & Value",
            "fields": [
                ("👁️ Our Vision", "Create a healing universe where loss transforms into creation, and every being finds their place among the stars."),
                ("💎 Our Values", "The Bearth universe is guided by a core set of values, rooted in the story of the Bear Tribe:"),
                ("🌱 Sustainability in action", "Sustainability isn't just a slogan—it's a commitment woven into every decision. From eco-friendly materials to responsible production, our actions speak louder than words."),
                ("❤️ Healing First", "Bearth began with a story of loss and rebirth. We believe art and creation can heal hearts, allowing precious memories to live on in new forms."),
                ("🐻 Coexistence over competition", "Like the Bear Tribe's laid-back philosophy, we believe the best future isn't about fighting for space, but finding a planet where everyone can rest comfortably."),
                ("🏗️ Thoughtfully Crafted", "Inspired by architectural thinking, every detail of Bearth is designed with careful consideration. We pursue meaning, not speed."),
            ]
        },
        "community": {
            "title": "🤝 Community",
            "fields": [
                ("🌍 Community", "We are travelers of the universe, navigating between loss and creation, solitude and belonging. We influence web3 culture through warmth, not noise."),
                ("🚀 Creator Empowerment", "We empower creators from within, building infrastructure that helps artists, storytellers, musicians, and dreamers of all kinds rise and thrive."),
                ("⚖️ Value Alignment", "Our community supports healing, coexistence, and intentional creation. We lead and support movements that share our vision, building a kinder, more thoughtful web3."),
                ("🌱 Growing Together", "We're recruiting global ambassadors and establishing governance structures that let the community shape Bearth's future. But we won't rush—we trust the process."),
                ("🏛️ Decentralized Governance (DAO)", "As our community matures, we're moving toward a DAO structure, enabling holders to shape Bearth's future through collective decision-making."),
            ]
        },
        "expansion": {
            "title": "📈 Expansion",
            "fields": [
                ("⏳ Organic Growth", "Growth isn't about rushing—it's about finding the right rhythm. Just as the Fibonacci sequence guides our minting phases, Bearth expands organically, one thoughtful step at a time."),
                ("🖼️ NFT Collection (In Progress)", "The first entry into the Bearth universe is through our genesis NFT collection. These 9,999 digital collectibles serve as your identity and key within our world. The collection will be released in seven phases, following the Fibonacci sequence: 303, 303, 606, 909, 1515, 2424, 3939."),
                ("🤝 Partnerships (In Progress)", "We're exploring collaborations with artists, brands, and projects that share our values, helping us reach new audiences while staying true to our mission."),
                ("🌟 Ambassador Program (Exploring)", "Ambassadors are co-creators and community builders who help Bearth find home worldwide. We're seeking:\n\n• **Community Builders** - Organize local meet-ups and gatherings\n• **Story Tellers** - Create content and share personal journeys\n• **Brand Advocates** - Represent Bearth authentically on social media"),
            ]
        },
        "digital": {
            "title": "💻 Digital",
            "fields": [
                ("🌐 The Digital Realm", "The digital realm is the native home of the Bearth IP, where our community gathers and the world comes to life."),
                ("🏙️ The City (In Progress)", "A web-based metaverse, similar to Azuki's Hilumia platform, that will become our community's digital home."),
                ("🐻 3D Characters (Exploring)", "We'll create 3D versions of every bear following OTHERSIDE specifications. Your bear is a traveler, free to explore anywhere on the journey, just like you."),
                ("🎮 Digital Experiences (Exploring)", "We're exploring interactive experiences, mini-games, and storytelling formats that make the digital universe feel alive."),
            ]
        },
        "physical": {
            "title": "🧸 Physical",
            "fields": [
                ("📦 The Physical World", "The Bearth IP extends into the physical world, bringing the universe to life in your hands. These products are tangible extensions of our story, not just merchandise."),
                ("🎨 Toys & Collectibles (Exploring)", "We're creating high-quality Bear Tribe toys and collectibles that bring joy and comfort. These aren't just merchandise—they're companions that make the universe tangible."),
                ("♻️ Sustainable Production (Exploring)", "Every product uses eco-friendly materials and ethical manufacturing. Our values aren't just digital."),
                ("👕 Apparel (Exploring)", "We're exploring clothing that brings Bearth into everyday life."),
                ("🖼️ Others (Exploring)", "We're exploring art prints, home goods, and other merchandise that bring Bearth into daily life."),
            ]
        },
        "hybrid": {
            "title": "🔗 Hybrid",
            "fields": [
                ("⚡ Phygital Fusion", "At the heart of the Bearth IP is the fusion of physical and digital experiences. We experiment with new media and interactive formats that blur the boundaries, creating a truly immersive universe."),
                ("📖 Interactive Storytelling (Exploring)", "Imagine RPG games where the community shapes the storyline, or animated shorts where your Bear plays a role."),
                ("🤳 Phygital Technology (Exploring)", "We're creating products that seamlessly blend physical and digital, collectibles that exist in both worlds and unlock experiences in each."),
                ("💼 IP Licensing & Monetization (Exploring)", "Enabling holders to license their NFTs to brands, transforming digital ownership into real commercial value and revenue."),
            ]
        },
    },
    "zh": {
        "header": "**🐻 Bearth 資訊導覽中心**\n請點擊下方按鈕探索我們的宇宙：",
        "vision_value": {
            "title": "✨ 願景與價值",
            "fields": [
                ("👁️ 我們的願景", "創造一個療癒的宇宙，讓失去轉化為創造，讓每個生命都能在星空中找到歸屬。"),
                ("💎 我們的價值觀", "Bearth 宇宙由一套核心價值觀引導，根植於熊族的故事："),
                ("🌱 永續行動", "永續不只是口號——它是融入每個決策的承諾。從環保材料到負責任的生產，我們的行動勝於言語。"),
                ("❤️ 療癒優先", "Bearth 始於一個關於失去與重生的故事。我們相信藝術和創作能療癒心靈，讓珍貴的回憶以新的形式延續。"),
                ("🐻 共存勝於競爭", "如同熊族悠閒的哲學，我們相信最好的未來不是爭奪空間，而是找到一個每個人都能舒適休息的星球。"),
                ("🏗️ 用心打造", "受建築思維啟發，Bearth 的每個細節都經過深思熟慮。我們追求意義，而非速度。"),
            ]
        },
        "community": {
            "title": "🤝 社群",
            "fields": [
                ("🌍 社群", "我們是宇宙的旅人，在失去與創造、孤獨與歸屬之間航行。我們用溫暖而非喧囂來影響 web3 文化。"),
                ("🚀 創作者賦能", "我們從內部賦能創作者，建立基礎設施幫助藝術家、故事講述者、音樂家和各類夢想家崛起並蓬勃發展。"),
                ("⚖️ 價值一致", "我們的社群支持療癒、共存和有意識的創作。我們領導並支持與我們願景相同的運動，建立一個更友善、更有思想的 web3。"),
                ("🌱 共同成長", "我們正在招募全球大使，並建立治理結構，讓社群塑造 Bearth 的未來。但我們不會急躁——我們相信過程。"),
                ("🏛️ 去中心化治理 (DAO)", "隨著社群成熟，我們正朝向 DAO 結構發展，讓持有者透過集體決策來塑造 Bearth 的未來。"),
            ]
        },
        "expansion": {
            "title": "📈 擴展",
            "fields": [
                ("⏳ 有機成長", "成長不是急躁——而是找到正確的節奏。正如費波那契數列引導我們的鑄造階段，Bearth 有機地擴展，一次一個深思熟慮的步驟。"),
                ("🖼️ NFT 收藏系列（進行中）", "進入 Bearth 宇宙的第一步是透過我們的創世 NFT 收藏。這 9,999 個數位收藏品是你在我們世界中的身份和鑰匙。收藏將分七個階段發布，遵循費波那契數列：303, 303, 606, 909, 1515, 2424, 3939。"),
                ("🤝 合作夥伴（進行中）", "我們正在探索與分享我們價值觀的藝術家、品牌和專案的合作，幫助我們觸及新受眾，同時保持對使命的忠誠。"),
                ("🌟 大使計劃（探索中）", "大使是共同創作者和社群建設者，幫助 Bearth 在全球找到家園。我們正在尋找：\n\n• **社群建設者** - 組織本地聚會和活動\n• **故事講述者** - 創作內容並分享個人旅程\n• **品牌倡導者** - 在社交媒體上真實地代表 Bearth"),
            ]
        },
        "digital": {
            "title": "💻 數位",
            "fields": [
                ("🌐 數位領域", "數位領域是 Bearth IP 的原生家園，社群在此聚集，世界在此活起來。"),
                ("🏙️ 城市（進行中）", "一個基於網頁的元宇宙，類似 Azuki 的 Hilumia 平台，將成為我們社群的數位家園。"),
                ("🐻 3D 角色（探索中）", "我們將依照 OTHERSIDE 規格創建每隻熊的 3D 版本。你的熊是旅行者，可以自由探索旅途中的任何地方，就像你一樣。"),
                ("🎮 數位體驗（探索中）", "我們正在探索互動體驗、小遊戲和故事格式，讓數位宇宙充滿生命力。"),
            ]
        },
        "physical": {
            "title": "🧸 實體",
            "fields": [
                ("📦 實體世界", "Bearth IP 延伸到實體世界，將宇宙帶到你手中。這些產品是我們故事的有形延伸，而不只是商品。"),
                ("🎨 玩具與收藏品（探索中）", "我們正在創造高品質的熊族玩具和收藏品，帶來歡樂與慰藉。這些不只是商品——它們是讓宇宙變得有形的夥伴。"),
                ("♻️ 永續生產（探索中）", "每個產品都使用環保材料和道德製造。我們的價值觀不只存在於數位世界。"),
                ("👕 服飾（探索中）", "我們正在探索將 Bearth 帶入日常生活的服飾。"),
                ("🖼️ 其他（探索中）", "我們正在探索藝術印刷品、家居用品和其他將 Bearth 帶入日常生活的商品。"),
            ]
        },
        "hybrid": {
            "title": "🔗 混合",
            "fields": [
                ("⚡ 虛實融合", "Bearth IP 的核心是實體與數位體驗的融合。我們嘗試新媒體和互動格式，模糊界限，創造真正沉浸式的宇宙。"),
                ("📖 互動故事（探索中）", "想像一下 RPG 遊戲，社群塑造故事線，或者你的熊在動畫短片中扮演角色。"),
                ("🤳 虛實技術（探索中）", "我們正在創造無縫融合實體與數位的產品，存在於兩個世界的收藏品，在每個世界解鎖體驗。"),
                ("💼 IP 授權與變現（探索中）", "讓持有者能夠將他們的 NFT 授權給品牌，將數位所有權轉化為真正的商業價值和收入。"),
            ]
        },
    }
}

# 伺服器規則內容
RULES_CONTENT = {
    "en": {
        "title": "📜 SERVER RULES",
        "description": "Welcome to the community! To maintain a safe and fun environment, please adhere to the following rules.",
        "rules": [
            ("1️⃣ Be Respectful", "Treat everyone with courtesy. No hate speech, harassment, insults, or toxic behavior will be tolerated."),
            ("2️⃣ No NSFW or Illegal Content", "Keep it clean. No explicit (NSFW), violent, illegal content, or pirated material."),
            ("3️⃣ No Spam or Self-Promotion", "Do not flood the chat. Unauthorized advertising, invite links, and DM spam are strictly prohibited."),
            ("4️⃣ Keep Channels On-Topic", "Please use the appropriate channels for your discussions. Check channel descriptions before posting."),
            ("5️⃣ Protect Privacy & Safety", "No doxxing. Never share your private keys, passwords, or personal info. Staff will NEVER ask for your password."),
            ("6️⃣ Follow Discord ToS", "You must abide by Discord's Terms of Service and Community Guidelines."),
            ("7️⃣ Respect Moderation", "Moderators have the final say. If you have issues, please open a ticket or DM a mod politely."),
        ]
    },
    "zh": {
        "title": "📜 伺服器規則",
        "description": "歡迎來到我們的社群！為了維護安全且有趣的環境，請務必遵守以下規範。",
        "rules": [
            ("1️⃣ 保持尊重與友善", "請禮貌待人。嚴禁仇恨言論、騷擾、侮辱或任何惡意攻擊行為。"),
            ("2️⃣ 禁止不當與非法內容", "請保持版面乾淨。嚴禁色情、暴力、非法活動或盜版內容。"),
            ("3️⃣ 禁止洗版與未經許可的廣告", "請勿重複發送訊息刷頻。嚴禁未經許可的廣告宣傳、邀請連結或私訊騷擾。"),
            ("4️⃣ 遵守頻道分類", "請在正確的頻道討論相關話題。發言前請先閱讀頻道說明。"),
            ("5️⃣ 保護隱私與安全", "禁止肉搜他人。請勿公開您的私鑰、密碼或個人資料。管理員絕不會向您索取密碼。"),
            ("6️⃣ 遵守 Discord 官方條款", "所有成員必須遵守 Discord 的服務條款與社群準則。"),
            ("7️⃣ 尊重管理員權限", "管理員擁有最終決定權。若有疑問，請透過工單 (Ticket) 或私訊冷靜溝通。"),
        ]
    }
}


def get_rules_embed(lang: str = "en") -> discord.Embed:
    """根據語言返回伺服器規則 Embed"""
    content = RULES_CONTENT[lang]
    embed = discord.Embed(
        title=content["title"],
        description=content["description"],
        color=0xED4245  # 紅色，表示重要規則
    )
    for name, value in content["rules"]:
        embed.add_field(name=name, value=value, inline=False)
    return embed


def get_embed_content(embed_type: str, lang: str = "en") -> discord.Embed:
    """根據類型和語言返回對應的 Embed"""
    content = CONTENT[lang][embed_type]
    embed = discord.Embed(title=content["title"], color=0x9b59b6)
    
    for name, value in content["fields"]:
        embed.add_field(name=name, value=value, inline=False)
    
    return embed


# 私人訊息按鈕視圖（編輯同一則訊息）
class PrivateNavigationView(discord.ui.View):
    def __init__(self, lang: str = "en"):
        super().__init__(timeout=None)
        self.lang = lang
        self._build_buttons()
    
    def _build_buttons(self):
        """根據語言建立按鈕（全部藍色）"""
        self.clear_items()
        labels = BUTTON_LABELS[self.lang]
        
        # 第一排按鈕（全部藍色 primary）
        btn_vision = discord.ui.Button(
            label=labels["vision_value"], 
            style=discord.ButtonStyle.primary, 
            emoji="\u2728",  # ✨
            row=0
        )
        btn_vision.callback = self.vision_value_callback
        self.add_item(btn_vision)
        
        btn_community = discord.ui.Button(
            label=labels["community"], 
            style=discord.ButtonStyle.primary, 
            emoji="\U0001F91D",  # 🤝
            row=0
        )
        btn_community.callback = self.community_callback
        self.add_item(btn_community)
        
        btn_expansion = discord.ui.Button(
            label=labels["expansion"], 
            style=discord.ButtonStyle.primary, 
            emoji="\U0001F4C8",  # 📈
            row=0
        )
        btn_expansion.callback = self.expansion_callback
        self.add_item(btn_expansion)
        
        # 第二排按鈕（全部藍色 primary）
        btn_digital = discord.ui.Button(
            label=labels["digital"], 
            style=discord.ButtonStyle.primary, 
            emoji="\U0001F4BB",  # 💻
            row=1
        )
        btn_digital.callback = self.digital_callback
        self.add_item(btn_digital)
        
        btn_physical = discord.ui.Button(
            label=labels["physical"], 
            style=discord.ButtonStyle.primary, 
            emoji="\U0001F9F8",  # 🧸
            row=1
        )
        btn_physical.callback = self.physical_callback
        self.add_item(btn_physical)
        
        btn_hybrid = discord.ui.Button(
            label=labels["hybrid"], 
            style=discord.ButtonStyle.primary, 
            emoji="\U0001F517",  # 🔗
            row=1
        )
        btn_hybrid.callback = self.hybrid_callback
        self.add_item(btn_hybrid)
        
        # 第三排：語言切換按鈕（藍色）
        btn_lang = discord.ui.Button(
            label=labels["lang_switch"], 
            style=discord.ButtonStyle.primary, 
            emoji=labels["lang_emoji"],
            row=2
        )
        btn_lang.callback = self.lang_callback
        self.add_item(btn_lang)
    
    async def vision_value_callback(self, interaction: discord.Interaction):
        embed = get_embed_content("vision_value", self.lang)
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def community_callback(self, interaction: discord.Interaction):
        embed = get_embed_content("community", self.lang)
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def expansion_callback(self, interaction: discord.Interaction):
        embed = get_embed_content("expansion", self.lang)
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def digital_callback(self, interaction: discord.Interaction):
        embed = get_embed_content("digital", self.lang)
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def physical_callback(self, interaction: discord.Interaction):
        embed = get_embed_content("physical", self.lang)
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def hybrid_callback(self, interaction: discord.Interaction):
        embed = get_embed_content("hybrid", self.lang)
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def lang_callback(self, interaction: discord.Interaction):
        # 切換語言並顯示首頁
        self.lang = "zh" if self.lang == "en" else "en"
        self._build_buttons()
        header = CONTENT[self.lang]["header"]
        await interaction.response.edit_message(content=header, embed=None, view=self)


# 公共訊息按鈕視圖（閱讀按鈕 + 語言切換）
class PublicNavigationView(discord.ui.View):
    def __init__(self, lang: str = "en"):
        super().__init__(timeout=None)
        self.lang = lang
        self._build_buttons()
    
    def _build_buttons(self):
        """建立公共按鈕"""
        self.clear_items()
        labels = BUTTON_LABELS[self.lang]
        
        # 閱讀按鈕（藍色）
        btn_read = discord.ui.Button(
            label="Read" if self.lang == "en" else "\u95b1\u8b80",
            style=discord.ButtonStyle.primary, 
            emoji="\U0001F4D6",  # 📖
            custom_id=f"public_read_{self.lang}"
        )
        btn_read.callback = self.read_callback
        self.add_item(btn_read)
        
        # 語言切換按鈕（藍色）
        btn_lang = discord.ui.Button(
            label=labels["lang_switch"], 
            style=discord.ButtonStyle.primary, 
            emoji=labels["lang_emoji"],
            custom_id=f"public_lang_{self.lang}"
        )
        btn_lang.callback = self.lang_callback
        self.add_item(btn_lang)
    
    async def read_callback(self, interaction: discord.Interaction):
        """點擊閱讀按鈕，發送私人訊息"""
        embed = get_embed_content("vision_value", self.lang)
        await interaction.response.send_message(
            embed=embed, 
            view=PrivateNavigationView(self.lang),
            ephemeral=True
        )
    
    async def lang_callback(self, interaction: discord.Interaction):
        # 切換語言
        self.lang = "zh" if self.lang == "en" else "en"
        self._build_buttons()
        await interaction.response.edit_message(
            embed=get_public_embed(self.lang), 
            view=self
        )


# 伺服器規則視圖（含語言切換）
class RulesView(discord.ui.View):
    def __init__(self, lang: str = "en"):
        super().__init__(timeout=None)
        self.lang = lang
        self._build_buttons()
    
    def _build_buttons(self):
        """建立語言切換按鈕"""
        self.clear_items()
        labels = BUTTON_LABELS[self.lang]
        
        # 語言切換按鈕
        btn_lang = discord.ui.Button(
            label=labels["lang_switch"], 
            style=discord.ButtonStyle.primary, 
            emoji=labels["lang_emoji"],
            custom_id=f"rules_lang_{self.lang}"
        )
        btn_lang.callback = self.lang_callback
        self.add_item(btn_lang)
    
    async def lang_callback(self, interaction: discord.Interaction):
        # 切換語言
        self.lang = "zh" if self.lang == "en" else "en"
        self._build_buttons()
        await interaction.response.edit_message(
            embed=get_rules_embed(self.lang), 
            view=self
        )


# 2. 註冊斜線指令
@tree.command(name="mindmap", description="開啟 Bearth 資訊導覽")
async def mindmap(interaction: discord.Interaction):
    await interaction.response.send_message(
        embed=get_public_embed("en"),
        view=PublicNavigationView("en")
    )


@tree.command(name="rules", description="顯示伺服器規則 / Show server rules")
async def rules(interaction: discord.Interaction):
    await interaction.response.send_message(
        embed=get_rules_embed("en"),
        view=RulesView("en")
    )


# 3. 機器人啟動時執行
# Guild ID for immediate command sync (測試用伺服器)
TEST_GUILD = discord.Object(id=1394953618779672607)

@client.event
async def on_ready():
    print(f"目前登入身份 --> {client.user}")
    # 同步到指定伺服器（即時生效）
    await tree.sync(guild=TEST_GUILD)
    print("指令已同步到測試伺服器！")
    # 也同步全域指令（需等待最多1小時）
    await tree.sync()
    print("全域指令已同步！")


# 4. 啟動機器人
if __name__ == "__main__":
    # 從環境變數讀取 Token（安全做法）
    TOKEN = os.environ.get("DISCORD_TOKEN")
    
    if not TOKEN:
        print("錯誤：請設定 DISCORD_TOKEN 環境變數")
        print("在 Render 上，請到 Environment 設定中加入 DISCORD_TOKEN")
        exit(1)
    
    # 啟動 keep_alive HTTP 服務（用於 Render 免費方案）
    from keep_alive import keep_alive
    keep_alive()
    print("Keep-alive 服務已啟動在 port 8080")
    
    client.run(TOKEN)
