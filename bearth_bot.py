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

# 定義 Embed 內容的輔助函數
def get_embed_content(embed_type: str) -> discord.Embed:
    """根據類型返回對應的 Embed"""
    embed = discord.Embed(color=0x9b59b6)
    
    if embed_type == "vision_value":
        embed.title = "✨ Vision & Value"
        embed.add_field(name="👁️ Our Vision", value="Create a healing universe where loss transforms into creation, and every being finds their place among the stars.", inline=False)
        embed.add_field(name="💎 Our Values", value="The Bearth universe is guided by a core set of values, rooted in the story of the Bear Tribe:", inline=False)
        embed.add_field(name="🌱 Sustainability in action", value="Sustainability isn't just a slogan—it's a commitment woven into every decision. From eco-friendly materials to responsible production, our actions speak louder than words.", inline=False)
        embed.add_field(name="❤️ Healing First", value="Bearth began with a story of loss and rebirth. We believe art and creation can heal hearts, allowing precious memories to live on in new forms.", inline=False)
        embed.add_field(name="🐻 Coexistence over competition", value="Like the Bear Tribe's laid-back philosophy, we believe the best future isn't about fighting for space, but finding a planet where everyone can rest comfortably.", inline=False)
        embed.add_field(name="🏗️ Thoughtfully Crafted", value="Inspired by architectural thinking, every detail of Bearth is designed with careful consideration. We pursue meaning, not speed.", inline=False)
    
    elif embed_type == "community":
        embed.title = "🤝 Community"
        embed.add_field(name="🌍 Community", value="We are travelers of the universe, navigating between loss and creation, solitude and belonging. We influence web3 culture through warmth, not noise.", inline=False)
        embed.add_field(name="🚀 Creator Empowerment", value="We empower creators from within, building infrastructure that helps artists, storytellers, musicians, and dreamers of all kinds rise and thrive.", inline=False)
        embed.add_field(name="⚖️ Value Alignment", value="Our community supports healing, coexistence, and intentional creation. We lead and support movements that share our vision, building a kinder, more thoughtful web3.", inline=False)
        embed.add_field(name="🌱 Growing Together", value="We're recruiting global ambassadors and establishing governance structures that let the community shape Bearth's future. But we won't rush—we trust the process.", inline=False)
        embed.add_field(name="🏛️ Decentralized Governance (DAO)", value="As our community matures, we're moving toward a DAO structure, enabling holders to shape Bearth's future through collective decision-making.", inline=False)
    
    elif embed_type == "expansion":
        embed.title = "📈 Expansion"
        embed.add_field(name="⏳ Organic Growth", value="Growth isn't about rushing—it's about finding the right rhythm. Just as the Fibonacci sequence guides our minting phases, Bearth expands organically, one thoughtful step at a time.", inline=False)
        embed.add_field(name="🖼️ NFT Collection (In Progress)", value="The first entry into the Bearth universe is through our genesis NFT collection. These 9,999 digital collectibles serve as your identity and key within our world. The collection will be released in seven phases, following the Fibonacci sequence: 303, 303, 606, 909, 1515, 2424, 3939.", inline=False)
        embed.add_field(name="🤝 Partnerships (In Progress)", value="We're exploring collaborations with artists, brands, and projects that share our values, helping us reach new audiences while staying true to our mission.", inline=False)
        embed.add_field(name="🌟 Ambassador Program (Exploring)", value="Ambassadors are co-creators and community builders who help Bearth find home worldwide. We're seeking:\n\n• **Community Builders** - Organize local meet-ups and gatherings\n• **Story Tellers** - Create content and share personal journeys\n• **Brand Advocates** - Represent Bearth authentically on social media", inline=False)
    
    elif embed_type == "digital":
        embed.title = "💻 Digital"
        embed.add_field(name="🌐 The Digital Realm", value="The digital realm is the native home of the Bearth IP, where our community gathers and the world comes to life.", inline=False)
        embed.add_field(name="🏙️ The City (In Progress)", value="A web-based metaverse, similar to Azuki's Hilumia platform, that will become our community's digital home.", inline=False)
        embed.add_field(name="🐻 3D Characters (Exploring)", value="We'll create 3D versions of every bear following OTHERSIDE specifications. Your bear is a traveler, free to explore anywhere on the journey, just like you.", inline=False)
        embed.add_field(name="🎮 Digital Experiences (Exploring)", value="We're exploring interactive experiences, mini-games, and storytelling formats that make the digital universe feel alive.", inline=False)
    
    elif embed_type == "physical":
        embed.title = "🧸 Physical"
        embed.add_field(name="📦 The Physical World", value="The Bearth IP extends into the physical world, bringing the universe to life in your hands. These products are tangible extensions of our story, not just merchandise.", inline=False)
        embed.add_field(name="🎨 Toys & Collectibles (Exploring)", value="We're creating high-quality Bear Tribe toys and collectibles that bring joy and comfort. These aren't just merchandise—they're companions that make the universe tangible.", inline=False)
        embed.add_field(name="♻️ Sustainable Production (Exploring)", value="Every product uses eco-friendly materials and ethical manufacturing. Our values aren't just digital.", inline=False)
        embed.add_field(name="👕 Apparel (Exploring)", value="We're exploring clothing that brings Bearth into everyday life.", inline=False)
        embed.add_field(name="🖼️ Others (Exploring)", value="We're exploring art prints, home goods, and other merchandise that bring Bearth into daily life.", inline=False)
    
    elif embed_type == "hybrid":
        embed.title = "🔗 Hybrid"
        embed.add_field(name="⚡ Phygital Fusion", value="At the heart of the Bearth IP is the fusion of physical and digital experiences. We experiment with new media and interactive formats that blur the boundaries, creating a truly immersive universe.", inline=False)
        embed.add_field(name="📖 Interactive Storytelling (Exploring)", value="Imagine RPG games where the community shapes the storyline, or animated shorts where your Bear plays a role.", inline=False)
        embed.add_field(name="🤳 Phygital Technology (Exploring)", value="We're creating products that seamlessly blend physical and digital, collectibles that exist in both worlds and unlock experiences in each.", inline=False)
        embed.add_field(name="💼 IP Licensing & Monetization (Exploring)", value="Enabling holders to license their NFTs to brands, transforming digital ownership into real commercial value and revenue.", inline=False)
    
    return embed


# 定義按鈕視圖
class NavigationView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    # 第一排按鈕
    @discord.ui.button(label="Vision & Value", style=discord.ButtonStyle.primary, emoji="✨", custom_id="btn_vision_value", row=0)
    async def vision_value_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = get_embed_content("vision_value")
        await interaction.response.edit_message(content=None, embed=embed, view=self)

    @discord.ui.button(label="Community", style=discord.ButtonStyle.success, emoji="🤝", custom_id="btn_community", row=0)
    async def community_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = get_embed_content("community")
        await interaction.response.edit_message(content=None, embed=embed, view=self)

    @discord.ui.button(label="Expansion", style=discord.ButtonStyle.secondary, emoji="📈", custom_id="btn_expansion", row=0)
    async def expansion_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = get_embed_content("expansion")
        await interaction.response.edit_message(content=None, embed=embed, view=self)

    # 第二排按鈕
    @discord.ui.button(label="Digital", style=discord.ButtonStyle.success, emoji="💻", custom_id="btn_digital", row=1)
    async def digital_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = get_embed_content("digital")
        await interaction.response.edit_message(content=None, embed=embed, view=self)

    @discord.ui.button(label="Physical", style=discord.ButtonStyle.secondary, emoji="🧸", custom_id="btn_physical", row=1)
    async def physical_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = get_embed_content("physical")
        await interaction.response.edit_message(content=None, embed=embed, view=self)

    @discord.ui.button(label="Hybrid", style=discord.ButtonStyle.danger, emoji="🔗", custom_id="btn_hybrid", row=1)
    async def hybrid_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = get_embed_content("hybrid")
        await interaction.response.edit_message(content=None, embed=embed, view=self)


# 2. 註冊斜線指令
@tree.command(name="mindmap", description="開啟 Bearth 資訊導覽")
async def mindmap(interaction: discord.Interaction):
    await interaction.response.send_message(
        content="**🐻 Bearth 資訊導覽中心**\n請點擊下方按鈕探索我們的宇宙：",
        view=NavigationView()
    )


# 3. 機器人啟動時執行
@client.event
async def on_ready():
    print(f"目前登入身份 --> {client.user}")
    await tree.sync()
    print("指令已同步！")


# 4. 啟動機器人
if __name__ == "__main__":
    # 從環境變數讀取 Token（安全做法）
    TOKEN = os.environ.get("DISCORD_TOKEN")
    
    if not TOKEN:
        print("錯誤：請設定 DISCORD_TOKEN 環境變數")
        print("在 Render 上，請到 Environment 設定中加入 DISCORD_TOKEN")
        exit(1)
    
    client.run(TOKEN)
