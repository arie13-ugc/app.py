import streamlit as st

# Configuration & Custom High-Contrast Styling (Age 45+ & Beginner Friendly)
st.set_page_config(
    page_title="Pembuat Cerita Seram 30 Detik",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-title {
        font-size: 32px !important;
        font-weight: bold;
        color: #E50914;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px !important;
        color: #DDDDDD;
        text-align: center;
        margin-bottom: 25px;
    }
    .step-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid #E50914;
        margin-bottom: 20px;
    }
    .step-header {
        font-size: 20px !important;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 12px;
    }
    .script-card {
        background-color: #252525;
        border: 1px solid #383838;
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 15px;
    }
    .time-badge {
        background-color: #E50914;
        color: white;
        padding: 5px 12px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 15px;
    }
    .stButton>button {
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #E50914 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 14px 28px !important;
        width: 100%;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<div class="main-title">🎬 PEMBUAT CERITA SERAM 30 DETIK</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Aplikasi Pembuat Naskah Video & Preview Gambar Thriller (Sangat Mudah Digunakan)</div>', unsafe_allow_html=True)

# Sidebar Guidance
with st.sidebar:
    st.header("ℹ️ Petunjuk Mudah")
    st.info("""
    **4 Langkah Sederhana:**
    1. **Ketik/Pilih Cerita** di Langkah 1.
    2. **Pilih Gaya Gambar** di Langkah 2.
    3. **Pilih Suasana Cerita** di Langkah 3.
    4. Klik tombol merah **BUAT CERITA SEKARANG**.
    """)
    st.markdown("---")
    st.subheader("💡 Aturan Retensi Naskah")
    st.caption("• **0-3s Hook**: Langsung menarik perhatian penonton.")
    st.caption("• **Story Flow**: Alur cerita lurus tanpa gangguan.")
    st.caption("• **Re-Hook**: Kejutan puncak di detik ke-20.")

# Form Input - Langkah 1
st.markdown('<div class="step-box">', unsafe_allow_html=True)
st.markdown('<div class="step-header">📝 LANGKAH 1: Apa Cerita Yang Ingin Dibuat?</div>', unsafe_allow_html=True)

contoh_ide = [
    "Ibu Siska melihat bayangan di cermin bergerak sendiri 2 detik terlambat",
    "Pak Budi sedang sendirian di kantor lalu mendengar suara langkah kaki dari lorong kosong",
    "Maya menemukan pesan suara di HP-nya yang merekam percakapan dirinya besok malam"
]

pilihan_contoh = st.selectbox(
    "💡 Klik di sini jika ingin menggunakan contoh cerita siap pakai:",
    ["-- Ketik cerita sendiri di bawah --"] + contoh_ide
)

if pilihan_contoh != "-- Ketik cerita sendiri di bawah --":
    user_story = st.text_area("Kalimat Cerita Anda:", value=pilihan_contoh, height=80)
else:
    user_story = st.text_area("Kalimat Cerita Anda (Tuliskan secara bebas):", value="Karakter A sedang sendirian di kamar dan menyadari bayangannya di cermin bergerak terlambat.", height=80)

st.markdown('</div>', unsafe_allow_html=True)

# Form Input - Langkah 2 & 3
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    st.markdown('<div class="step-header">🎨 LANGKAH 2: Pilih Gaya Gambar</div>', unsafe_allow_html=True)
    visual_style = st.radio(
        "Pilih salah satu jenis gambar:",
        [
            "📸 Foto Nyata / Bioskop (Hyperrealistic 4K)",
            "🎨 Boneka Tanah Liat (Clay Animation)",
            "📱 Kamera HP / Nyata (Realistic Found Footage)",
            "🌀 Efek Kedalaman 3D (Parallax 3D)"
        ]
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    st.markdown('<div class="step-header">🎭 LANGKAH 3: Pilih Suasana Cerita</div>', unsafe_allow_html=True)
    narrative_style = st.radio(
        "Pilih alur cerita yang Anda sukai:",
        [
            "👻 Horor Klasik (Orthodox - Pembangunan Rasa Cemas Bertahap)",
            "🧩 Teka-Teki Waktu (Nolan Style - Mind-Bending & Time Loop)",
            "⚡ Pembalasan Mendadak (Tarantino Style - Dialog Tajam & Karmic Retribution)"
        ]
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Action Button
btn_generate = st.button("🚀 BUAT CERITA SEKARANG", use_container_width=True)

def generate_script_data(story_text, v_style, n_style):
    v_tag = "claymation stop-motion" if "Clay" in v_style else ("hyperrealistic 4K" if "4K" in v_style else "realistic found footage")
    
    if "Orthodox" in n_style:
        style_title = "Horor Klasik (Orthodox)"
        scene_1 = {
            "time": "0–5 Detik (Hook Cepat)",
            "visual": f"Karakter berdiri diam di tempat redup. {story_text[:50]}...",
            "audio": "SFX: Detak jam dinding lambat.\nNarasi: 'Ada hal yang salah malam ini.'",
            "prompt": f"Orthodox horror style, {v_tag}, close up shot of character in dim room, tense atmosphere"
        }
        scene_2 = {
            "time": "5–20 Detik (Story Flow Lurus)",
            "visual": "Karakter melangkah pelan. Terjadi keanehan fisik yang bertahap di sekitarnya.",
            "audio": "SFX: Dengung frekuensi rendah.\nNarasi: 'Kamu melangkah... tapi bayanganmu memilih tinggal.'",
            "prompt": f"Suspenseful horror shot, {v_tag}, character moving away while shadow stays still"
        }
        scene_3 = {
            "time": "20–25 Detik (Re-Hook / Kejutan)",
            "visual": "Ancaman tak terlihat perlahan menunjuk ke arah belakang karakter.",
            "audio": "Bisikan Halus: 'Dia di belakangmu...'",
            "prompt": f"High tension thriller, {v_tag}, shadowy figure pointing from behind"
        }
        scene_4 = {
            "time": "25–30 Detik (Klimaks / Blackout)",
            "visual": "Pintu terbuka sendiri secara mendadak. Layar blackout.",
            "audio": "SFX: Jeritan terputus & pintu membanting keras!",
            "prompt": f"Dark thriller climax, {v_tag}, opening door into pitch darkness, dramatic lighting"
        }
    elif "Nolan" in n_style:
        style_title = "Teka-Teki Waktu (Nolan Style)"
        scene_1 = {
            "time": "0–5 Detik (Flash-Forward Hook)",
            "visual": "Karakter memegang petunjuk yang mencantumkan tanggal hari ini.",
            "audio": "SFX: Detakan jam tempo cepat.\nNarasi: 'Ini terjadi bukan pertama kalinya.'",
            "prompt": f"Christopher Nolan style, {v_tag}, IMAX 4K shot, panicked character holding clue"
        }
        scene_2 = {
            "time": "5–20 Detik (Story Flow / Time Shift)",
            "visual": "Melompat ke 10 detik lalu: Karakter melakukan percakapan dan melihat dirinya di layar.",
            "audio": "SFX: Dengung masa lalu.\nDialog: 'Suara apa yang ada di seberang sana?'",
            "prompt": f"Nolan sci-fi thriller aesthetics, {v_tag}, split view revealing duplicate character"
        }
        scene_3 = {
            "time": "20–25 Detik (Re-Hook / Twist Loop)",
            "visual": "Karakter menyadari orang di layar adalah dirinya dari garis waktu lain.",
            "audio": "Narasi: 'Kamu bukan korban. Kamu adalah masa lalu yang akan menggantikannya.'",
            "prompt": f"Mind-bending parallax depth, {v_tag}, two identical characters staring across dimension"
        }
        scene_4 = {
            "time": "25–30 Detik (Klimaks Dimensi)",
            "visual": "Kamera berputar 360 derajat saat masa kini dan masa depan bertabrakan.",
            "audio": "SFX: Gema jam dinding berbalik arah!",
            "prompt": f"Cinematic sci-fi climax, {v_tag}, room shattering into glass time shards"
        }
    else:
        style_title = "Pembalasan Mendadak (Tarantino Style)"
        scene_1 = {
            "time": "0–5 Detik (Hook & Dialog Tajam)",
            "visual": "Karakter bersikap sombong di hadapan lawan bicaranya.",
            "audio": "Dialog: 'Kamu pikir kamu bisa mengancamku dari situ?'",
            "prompt": f"Tarantino aesthetic, {v_tag}, vintage warm color grading, arrogant character close up"
        }
        scene_2 = {
            "time": "5–20 Detik (Story Flow Lurus)",
            "visual": "Lawan bicara tersenyum dingin. Tiba-tiba karakter merasakan guncangan fisik.",
            "audio": "SFX: Detak jantung kencang.\nDialog: 'Hitunganmu salah. Cek sakumu.'",
            "prompt": f"Extreme close up shot of eyes, {v_tag}, high contrast film grain, intense confrontation"
        }
        scene_3 = {
            "time": "20–25 Detik (Re-Hook / Retribution)",
            "visual": "Karakter menyadari kesalahan fatalnya. Efek retakan menjalar.",
            "audio": "Narasi: 'Kesombongan selalu membawa harga yang harus dibayar.'",
            "prompt": f"Explosive retribution shot, {v_tag}, red neon lighting, dramatic confrontation"
        }
        scene_4 = {
            "time": "25–30 Detik (Klimaks Pembalasan)",
            "visual": "Benda hancur berhamburan dalam slow-motion.",
            "audio": "SFX: Kaca pecah keras!\nTeks Layar: 'PEMBALASAN TANPA AMPUN.'",
            "prompt": f"Action thriller climax, {v_tag}, shattered glass flying in slow motion, high contrast"
        }
        
    return style_title, [scene_1, scene_2, scene_3, scene_4]

if btn_generate or 'script_generated' in st.session_state:
    st.session_state['script_generated'] = True
    style_title, scenes = generate_script_data(user_story, visual_style, narrative_style)
    
    st.markdown("---")
    st.subheader(f"🎬 HASIL NASKAH THRILLER 30 DETIK ({style_title.upper()})")
    st.caption("Naskah dirancang otomatis mengikuti kaidah retensi penonton tinggi (Speed-to-Value Hook & Clear Flow).")
    
    for idx, sc in enumerate(scenes, 1):
        st.markdown(f"""
        <div class="script-card">
            <span class="time-badge">SCENE {idx} | {sc['time']}</span>
            <p style="margin-top:12px; font-size:17px; color:#FFFFFF;"><b>👁️ Visual Scene:</b> {sc['visual']}</p>
            <p style="font-size:17px; color:#58A6FF;"><b>🎙️ Suara / Dialog / SFX:</b><br>{sc['audio']}</p>
            <p style="font-size:14px; color:#AAAAAA;"><b>🖼️ Prompt AI Gambar:</b> <code>{sc['prompt']}</code></p>
        </div>
        """, unsafe_allow_html=True)
            
    st.markdown("### 🔄 Pilihan Selanjutnya:")
    c_btn1, c_btn2, c_btn3 = st.columns(3)
    with c_btn1:
        if st.button("🔄 Buat Versi Alternatif"):
            st.rerun()
    with c_btn2:
        st.button("🔊 Putar Contoh Suara")
    with c_btn3:
        st.button("💾 Simpan Naskah")
