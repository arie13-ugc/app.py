import streamlit as st

# Configuration & Custom High-Contrast Styling (Super Simple & Beginner Friendly)
st.set_page_config(
    page_title="Dashboard Generator Naskah & Prompt Video",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-title {
        font-size: 30px !important;
        font-weight: bold;
        color: #E50914;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 16px !important;
        color: #CCCCCC;
        text-align: center;
        margin-bottom: 25px;
    }
    .step-box {
        background-color: #181818;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #333333;
        border-left: 6px solid #E50914;
        margin-bottom: 20px;
    }
    .step-header {
        font-size: 19px !important;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 12px;
    }
    .script-card {
        background-color: #222222;
        border: 1px solid #3d3d3d;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 18px;
    }
    .time-badge {
        background-color: #E50914;
        color: white;
        padding: 6px 14px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 15px;
        display: inline-block;
        margin-bottom: 10px;
    }
    .aspect-badge {
        background-color: #2E7D32;
        color: white;
        padding: 6px 14px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 14px;
        display: inline-block;
        margin-bottom: 10px;
        margin-left: 8px;
    }
    .stButton>button {
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #E50914 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 16px 30px !important;
        width: 100%;
        cursor: pointer;
        border: none !important;
    }
    .stButton>button:hover {
        background-color: #FF0F1A !important;
    }
    .prompt-code {
        background-color: #111111;
        border-left: 3px solid #2196F3;
        padding: 10px 14px;
        font-family: monospace;
        color: #00E676;
        border-radius: 4px;
        word-break: break-word;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown('<div class="main-title">🎬 PANEL GENERATOR CERITA & PROMPT VIDEO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Pembuat Naskah 30 Detik & Prompt Google Flow / Veo (Style Hollywood & Rasio Fleksibel)</div>', unsafe_allow_html=True)

# SECTION 1: Deskripsi / Ide Cerita
st.markdown('<div class="step-box">', unsafe_allow_html=True)
st.markdown('<div class="step-header">📝 1. Deskripsi / Ide Cerita Maunya Apa</div>', unsafe_allow_html=True)

contoh_ide = [
    "Karakter sedang sendirian di kamar dan menyadari bayangannya di cermin bergerak 2 detik terlambat.",
    "Seorang wanita berjalan di tempat sepi dan merasa diikuti, lalu menyadari yang mengikutinya adalah dirinya sendiri.",
    "Pelanggan sombong memaki petugas toko, lalu tiba-tiba mengalami keanehan fisik dan karmic retribution."
]

pilihan_contoh = st.selectbox(
    "💡 Pilih contoh cerita instan (atau ketik sendiri di bawah):",
    ["-- Ketik Cerita Sendiri --"] + contoh_ide
)

if pilihan_contoh != "-- Ketik Cerita Sendiri --":
    user_story = st.text_area("Deskripsi Cerita:", value=pilihan_contoh, height=80)
else:
    user_story = st.text_area("Deskripsi Cerita (Tuliskan secara bebas):", value="Karakter sedang sendirian di kamar dan menyadari bayangannya di cermin bergerak terlambat.", height=80)

st.markdown('</div>', unsafe_allow_html=True)

# SECTION 2: Style Movie & Aspect Ratio
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    st.markdown('<div class="step-header">🎭 2. Style Movie</div>', unsafe_allow_html=True)
    movie_style = st.radio(
        "Pilih Alur & Gaya Sinematik:",
        [
            "👻 Orthodoks (Horor Klasik - Pembangunan Cemas & Dread)",
            "🧩 Nolan (Mind-Bending - Teka-Teki Waktu & Time Loop)",
            "⚡ Tarantino (Pembalasan Karma - Dialog Tajam & Karmic Retribution)"
        ]
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    st.markdown('<div class="step-header">📐 3. Rasio Video (Aspect Ratio)</div>', unsafe_allow_html=True)
    aspect_ratio = st.radio(
        "Pilih Format Layar Video:",
        [
            "📱 9:16 (Vertikal - HP / TikTok / Instagram Reels / YouTube Shorts)",
            "🖥️ 16:9 (Horizontal - Layar Lebar / YouTube / Film Bioskop)"
        ]
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Generate Button
btn_generate = st.button("🚀 BUAT NASKAH & PROMPT GOOGLE FLOW", use_container_width=True)

def generate_prompts_and_script(story_text, style, ratio):
    ratio_tag = "9:16 vertical aspect ratio" if "9:16" in ratio else "16:9 widescreen cinematic aspect ratio"
    
    if "Orthodoks" in style:
        style_label = "Orthodoks (Horor Klasik)"
        scene_1 = {
            "title": "SCENE 1: Hook Cepat (0–3 Detik)",
            "vis": f"Close-up ketakutan di depan cermin/ruangan redup. {story_text[:50]}...",
            "audio": "SFX: Detak jam lambat & dengung bass.\nVoiceover: 'Ada hal yang salah malam ini.'",
            "camera": "Hollywood Camera: Dolly Zoom / Vertigo Push-In",
            "prompt": f"Cinematic slow push-in dolly zoom shot. Extreme close-up on a terrified character's eyes in a dimly lit room, staring at a mirror. Atmospheric dark room, moody volumetric rim lighting, {ratio_tag}, 24fps film grain, high-contrast shadows, 4K Hollywood horror aesthetic."
        }
        scene_2 = {
            "title": "SCENE 2: Story Flow (5–20 Detik)",
            "vis": "Karakter melangkah mundur secara pelan. Keanehan fisik/bayangan tetap diam.",
            "audio": "SFX: Frekuensi suara rendah (dread).\nVoiceover: 'Kamu melangkah... tapi bayanganmu memilih tinggal.'",
            "camera": "Hollywood Camera: Steadicam Tracking Shot",
            "prompt": f"Smooth Steadicam tracking shot, over-the-shoulder perspective following a character walking away down a dark hallway while their reflection stays frozen. Cold blue ambient lighting, deep chiaroscuro contrast, {ratio_tag}, 4K photorealistic horror."
        }
        scene_3 = {
            "title": "SCENE 3: Re-Hook / Twist (20–25 Detik)",
            "vis": "Kamera miring 45 derajat. Sosok gelap muncul di belakang karakter.",
            "audio": "SFX: Bisikan tajam.\nVoiceover: 'Dia berdiri tepat di belakangmu...'",
            "camera": "Hollywood Camera: Dutch Angle + 360-Degree Orbit",
            "prompt": f"Dramatic Dutch-angle shot rotating in a slow 360-degree orbit around the protagonist. A tall shadowy dark figure slowly emerges from behind. Crimson red neon backlight, heavy atmospheric fog, {ratio_tag}, IMAX 8K depth."
        }
        scene_4 = {
            "title": "SCENE 4: Klimaks & Blackout (25–30 Detik)",
            "vis": "Pintu membanting keras ke kegelapan total. Cahaya merah menyambar.",
            "audio": "SFX: Pintu membanting keras & layar blackout!",
            "camera": "Hollywood Camera: Fast Snap Zoom + Crane Tilt Down",
            "prompt": f"Fast snap zoom shot tilting down dynamically. Heavy wooden door violently slams open into pitch darkness with dramatic red strobe light spilling through. Motion blur, high-contrast climax, {ratio_tag}, 24fps."
        }
    elif "Nolan" in style:
        style_label = "Nolan (Mind-Bending)"
        scene_1 = {
            "title": "SCENE 1: Flash-Forward Hook (0–3 Detik)",
            "vis": "Karakter terkejut memegang petunjuk jam/foto berulang.",
            "audio": "SFX: Detakan jam tempo cepat.\nVoiceover: 'Ini terjadi bukan pertama kalinya.'",
            "camera": "Hollywood Camera: Rapid Push-In Focus Shift",
            "prompt": f"Christopher Nolan style rapid push-in focus shift shot. Panicked character holding a mysterious time clue. Cold muted color grading, IMAX 4K aesthetic, volumetric rays, {ratio_tag}, high tension sci-fi thriller."
        }
        scene_2 = {
            "title": "SCENE 2: Story Flow / Time Shift (5–20 Detik)",
            "vis": "Layar terbelah / rekaman memperlihatkan duplikat karakter di waktu berdeda.",
            "audio": "SFX: Dengung pembalik waktu.\nVoiceover: 'Suara yang kamu dengar adalah dirimu dari kemarin.'",
            "camera": "Hollywood Camera: Parallax Tracking Shot",
            "prompt": f"Parallax tracking camera shot. Split view or reflection revealing duplicate character operating in a parallel time loop. IMAX 70mm film aesthetic, cold blue tone, {ratio_tag}, photorealistic sci-fi."
        }
        scene_3 = {
            "title": "SCENE 3: Re-Hook / Twist Loop (20–25 Detik)",
            "vis": "Karakter sadar dirinya adalah pelaku di garis waktu lain.",
            "audio": "Voiceover: 'Kamu bukan korban. Kamu yang menjebaknya.'",
            "camera": "Hollywood Camera: 360-Degree Revolving Orbit",
            "prompt": f"Mind-bending 360-degree revolving orbit camera around two identical characters confronting each other across a shattering reality plane. High contrast lighting, {ratio_tag}, dramatic depth of field."
        }
        scene_4 = {
            "title": "SCENE 4: Klimaks Dimensi (25–30 Detik)",
            "vis": "Kaca shattered berhamburan dalam time-reversal slow motion.",
            "audio": "SFX: Gema jam dinding berbalik arah keras!",
            "prompt": f"Cinematic sci-fi climax with slow-motion time-reversal particle effect. Glass shards floating as reality collapses into darkness. High resolution, {ratio_tag}, IMAX 8K."
        }
    else:
        style_label = "Tarantino (Karmic Retribution)"
        scene_1 = {
            "title": "SCENE 1: Hook & Dialog Sombong (0–3 Detik)",
            "vis": "Karakter bersikap sombong meremehkan lawan bicara.",
            "audio": "Dialog: 'Kamu pikir kamu bisa mengancamku?'",
            "prompt": f"Quentin Tarantino style low-angle extreme close-up shot. Arrogant character speaking, warm vintage technicolor grading, sharp shadows, {ratio_tag}, 35mm film grain aesthetic."
        }
        scene_2 = {
            "title": "SCENE 2: Story Flow & Confrontation (5–20 Detik)",
            "vis": "Lawan bicara tersenyum dingin. Karakter merasakan keanehan/pembalasan fisik.",
            "audio": "SFX: Detak jantung kencang.\nDialog: 'Hitunganmu salah. Cek sakumu.'",
            "prompt": f"Tight whip-pan camera movement between two characters in a high-stakes standoff. Intense eye contact, high contrast dramatic lighting, {ratio_tag}, photorealistic cinematic tension."
        }
        scene_3 = {
            "title": "SCENE 3: Re-Hook / Retribution (20–25 Detik)",
            "vis": "Karakter menyadari perangkap fatalnya. Lampu merah menyala.",
            "audio": "Voiceover: 'Kesombongan selalu meminta bayaran tunai.'",
            "camera": "Hollywood Camera: High-Angle Crash Zoom",
            "prompt": f"Dramatic crash zoom shot from high angle. Arrogant character realizing their fatal mistake in a trapped room, sudden red key lighting, {ratio_tag}, 4K action thriller."
        }
        scene_4 = {
            "title": "SCENE 4: Klimaks Pembalasan (25–30 Detik)",
            "vis": "Benda hancur berhamburan dalam slow-motion.",
            "audio": "SFX: Kaca pecah keras!\nTeks Layar: 'PEMBALASAN TANPA AMPUN.'",
            "prompt": f"Action thriller climax, shattered glass and debris flying in ultra slow-motion, high contrast cinematic lighting, dramatic motion blur, {ratio_tag}, 4K."
        }
        
    return style_label, ratio, [scene_1, scene_2, scene_3, scene_4]

if btn_generate or 'generated' in st.session_state:
    st.session_state['generated'] = True
    style_label, ratio_used, scenes = generate_prompts_and_script(user_story, movie_style, aspect_ratio)
    
    st.markdown("---")
    st.subheader(f"🎬 HASIL NASKAH & PROMPT GOOGLE FLOW")
    st.caption(f"Style: **{style_label}** | Format Layar: **{ratio_used.split(' ')[0]} {ratio_used.split(' ')[1]}**")
    
    for idx, sc in enumerate(scenes, 1):
        st.markdown(f"""
        <div class="script-card">
            <span class="time-badge">{sc['title']}</span>
            <span class="aspect-badge">Rasio {aspect_ratio.split(' ')[0]}</span>
            <p style="margin-top:12px; font-size:16px; color:#FFFFFF;"><b>👁️ Visual Scene:</b> {sc['vis']}</p>
            <p style="font-size:16px; color:#58A6FF;"><b>🎙️ Suara / Voiceover / SFX:</b><br>{sc['audio'].replace('\n', '<br>')}</p>
            <p style="font-size:14px; color:#FFD54F;"><b>🎥 Teknik Kamera Hollywood:</b> {sc.get('camera', 'Hollywood Camera Shot')}</p>
            <p style="font-size:14px; color:#AAAAAA; margin-bottom:4px;"><b>📋 Prompt Google Flow / Veo (Ready to Copy):</b></p>
            <div class="prompt-code">{sc['prompt']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.success("✅ Prompt di atas sudah diformat khusus untuk Google Flow / Veo! Cukup copy-paste kode hijau di atas ke Google Flow.")
