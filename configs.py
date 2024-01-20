
import os

class Config(object):
    API_ID = (os.environ.get("API_ID", 14699743)
    API_HASH = os.environ.get("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792" )
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5115356918:AAFH3T-1f2x4ZdikRQnNoOXXgonLUlwryAQ")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001764670025")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001625277697")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 4))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "5eb945e0fc5266091de2")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "gLV2QdvKaRhqlrJ")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://nohari3255:lK4QeDDOZKefymH0@cluster0.rka3l8x.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5059280908))

    START_TEXT = """
𝐇𝐢 𝐃𝐞𝐚𝐫 𝐔𝐬𝐞𝐫 , 𝐈 𝐚𝐦 𝐕𝐢𝐝𝐞𝐨 𝐌𝐞𝐫𝐠𝐞 𝐁𝐨𝐭!
𝐈 𝐜𝐚𝐧 𝐌𝐞𝐫𝐠𝐞 𝐌𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐢𝐧 𝐎𝐧𝐞 𝐕𝐢𝐝𝐞𝐨. 𝐕𝐢𝐝𝐞𝐨 𝐅𝐨𝐫𝐦𝐚𝐭𝐬 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞 𝐬𝐚𝐦𝐞.

𝐌𝐚𝐝𝐞 𝐛𝐲 @Savior_128
"""
    CAPTION = "ᵛⁱᵈᵉᵒ ᵐᵉʳᵍᵉᵈ ᵇʸ @{}\n\n𝙼𝚊𝚍𝚎 𝚋𝚢 @𝚂𝚊𝚟𝚒𝚘𝚛_𝟷𝟸𝟾"
    PROGRESS = """
𝐏𝐞𝐫𝐜𝐞𝐧𝐭𝐚𝐠𝐞 : {𝟎}%
𝐃𝐨𝐧𝐞: {𝟏}
𝐓𝐨𝐭𝐚𝐥: {𝟐}
𝐒𝐩𝐞𝐞𝐝: {𝟑}/𝐬
𝐄𝐓𝐀: {𝟒}
"""
