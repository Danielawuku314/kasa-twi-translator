import streamlit as st
import streamlit.components.v1 as components

# Set page configuration to wide mode to fit the translation interface
st.set_page_config(
    page_title="KASA — Twi ⇄ English Translator",
    page_icon="🌍",
    layout="wide"
)

# Hide standard Streamlit header/footer for a clean full-screen look
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Embedded HTML Content
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KASA — Twi ⇄ English Translator</title>
<meta name="description" content="A free, live Twi–English translator with a hand-checked phrasebook of everyday Akan expressions.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --void:#15100c;
    --surface:#1e1710;
    --surface-2:#261c13;
    --hairline:#3a2c1d;
    --gold:#cc9a3d;
    --gold-soft:#e8c877;
    --rust:#b3492f;
    --green:#3d6b52;
    --bone:#f2e8d5;
    --bone-dim:#b9a98c;
    --bone-faint:#8a7c63;
    --shadow: 0 20px 60px -20px rgba(0,0,0,.6);
    --radius: 14px;
    --serif: "Fraunces", "Georgia", serif;
    --sans: "Manrope", "Noto Sans", "Segoe UI", sans-serif;
    --twi-sans: "Manrope", "Noto Sans", "Segoe UI", sans-serif;
    --mono: "IBM Plex Mono", ui-monospace, monospace;
  }

  *{ box-sizing:border-box; }
  html{ scroll-behavior:smooth; }
  body{
    margin:0;
    background:
      radial-gradient(ellipse 900px 500px at 15% -10%, rgba(204,154,61,.10), transparent 60%),
      radial-gradient(ellipse 700px 500px at 100% 0%, rgba(179,73,47,.08), transparent 55%),
      var(--void);
    color:var(--bone);
    font-family:var(--sans);
    -webkit-font-smoothing:antialiased;
    line-height:1.5;
  }

  ::selection{ background:var(--gold); color:var(--void); }

  a{ color:inherit; }

  .wrap{ max-width:1080px; margin:0 auto; padding:0 24px; }

  /* ---------- Nav ---------- */
  nav.top{
    display:flex; align-items:center; justify-content:space-between;
    padding:26px 24px;
    max-width:1080px; margin:0 auto;
  }
  .brand{ display:flex; align-items:center; gap:12px; }
  .brand svg{ width:30px; height:30px; flex:none; }
  .brand-text{ font-family:var(--serif); font-weight:600; font-size:20px; letter-spacing:.03em; color:var(--bone); }
  .brand-sub{ font-family:var(--mono); font-size:10.5px; letter-spacing:.14em; color:var(--bone-faint); text-transform:uppercase; margin-top:1px; }
  nav .status{
    font-family:var(--mono); font-size:11px; color:var(--bone-faint);
    display:flex; align-items:center; gap:8px;
  }
  .dot{ width:6px; height:6px; border-radius:50%; background:var(--green); box-shadow:0 0 0 3px rgba(61,107,82,.25); }

  /* ---------- Hero ---------- */
  header.hero{ position:relative; overflow:hidden; padding-top:8px; }
  .sankofa-watermark{
    position:absolute; right:-60px; top:-40px; width:420px; height:420px;
    opacity:.06; pointer-events:none; z-index:0;
  }
  .hero-inner{ position:relative; z-index:1; padding:36px 0 30px; }
  .eyebrow{
    display:inline-flex; align-items:center; gap:8px;
    font-family:var(--mono); font-size:11px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--gold-soft); background:rgba(204,154,61,.1); border:1px solid rgba(204,154,61,.25);
    padding:6px 12px; border-radius:100px; margin-bottom:22px;
  }
  h1.headline{
    font-family:var(--serif); font-weight:600; font-size:clamp(38px, 6vw, 64px);
    line-height:1.04; margin:0 0 18px; letter-spacing:-.01em; max-width:780px;
  }
  h1.headline em{ font-style:italic; color:var(--gold-soft); font-weight:500; }
  p.sub{
    font-size:17px; color:var(--bone-dim); max-width:560px; margin:0 0 8px; font-weight:400;
  }

  .kente-rule{
    height:5px; width:100%; margin:34px 0 0;
    background: repeating-linear-gradient(90deg,
      var(--gold) 0 34px, var(--rust) 34px 46px, var(--green) 46px 58px, var(--surface) 58px 64px);
    border-radius:3px; opacity:.85;
  }

  /* ---------- Translator ---------- */
  section.translator{ padding:44px 0 8px; }
  .panes{
    display:grid; grid-template-columns:1fr 56px 1fr; gap:0; align-items:stretch;
  }
  @media (max-width:760px){
    .panes{ grid-template-columns:1fr; gap:14px; }
    .swap-col{ display:flex; justify-content:center; margin:-2px 0; }
  }

  .pane{
    background:var(--surface);
    border:1px solid var(--hairline);
    border-radius:var(--radius);
    display:flex; flex-direction:column;
    min-height:230px;
    box-shadow:var(--shadow);
  }
  .pane-head{
    display:flex; align-items:center; justify-content:space-between;
    padding:14px 18px; border-bottom:1px solid var(--hairline);
  }
  .lang-tag{
    font-family:var(--mono); font-size:11.5px; letter-spacing:.12em; text-transform:uppercase;
    color:var(--bone-dim); display:flex; align-items:center; gap:8px;
  }
  .lang-tag b{ color:var(--gold-soft); font-weight:600; }
  .pane textarea{
    flex:1; resize:none; border:none; outline:none; background:transparent;
    color:var(--bone); font-family:var(--twi-sans); font-size:19px; line-height:1.55;
    padding:18px; min-height:150px;
  }
  .pane textarea::placeholder{ color:var(--bone-faint); }
  .result-box{
    flex:1; padding:18px; font-size:19px; line-height:1.55; font-family:var(--twi-sans);
    color:var(--bone); white-space:pre-wrap; overflow-wrap:anywhere;
  }
  .result-box.empty{ color:var(--bone-faint); font-style:italic; font-family:var(--sans); font-size:15px; }
  .badge{
    font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase;
    padding:4px 9px; border-radius:100px; border:1px solid;
  }
  .badge.verified{ color:#a9d6bb; border-color:rgba(61,107,82,.5); background:rgba(61,107,82,.15); }
  .badge.machine{ color:var(--gold-soft); border-color:rgba(204,154,61,.4); background:rgba(204,154,61,.1); }
  .badge.corpus{ color:#e8a98c; border-color:rgba(179,73,47,.45); background:rgba(179,73,47,.14); }

  .pane-foot{
    display:flex; align-items:center; justify-content:space-between;
    padding:10px 14px; border-top:1px solid var(--hairline);
  }
  .charcount{ font-family:var(--mono); font-size:11px; color:var(--bone-faint); padding-left:4px; }

  button{ font-family:var(--sans); cursor:pointer; }
  .btn{
    border:none; border-radius:9px; padding:9px 16px; font-size:13.5px; font-weight:700;
    letter-spacing:.01em; transition:transform .12s ease, background .15s ease, opacity .15s ease;
  }
  .btn:active{ transform:scale(.97); }
  .btn-primary{ background:var(--gold); color:#1c1408; }
  .btn-primary:hover{ background:var(--gold-soft); }
  .btn-primary:disabled{ opacity:.55; cursor:default; transform:none; }
  .btn-ghost{
    background:transparent; color:var(--bone-dim); border:1px solid var(--hairline);
    padding:7px 12px; font-size:12.5px; font-weight:600;
  }
  .btn-ghost:hover{ color:var(--bone); border-color:var(--bone-faint); }
  .btn-ghost.copied{ color:#a9d6bb; border-color:rgba(61,107,82,.5); }

  .swap-col{ display:flex; align-items:center; justify-content:center; }
  .swap-btn{
    width:44px; height:44px; border-radius:50%;
    background:var(--surface-2); border:1px solid var(--hairline);
    display:flex; align-items:center; justify-content:center;
    color:var(--gold-soft); transition:transform .4s cubic-bezier(.2,.8,.2,1), border-color .15s ease;
  }
  .swap-btn:hover{ border-color:var(--gold); }
  .swap-btn svg{ width:20px; height:20px; }
  .swap-btn.spin svg{ transform:rotate(180deg); }
  .swap-btn svg{ transition:transform .4s cubic-bezier(.2,.8,.2,1); }

  .translate-row{ display:flex; align-items:center; gap:14px; margin-top:18px; flex-wrap:wrap; }
  .hint{ font-size:12.5px; color:var(--bone-faint); }
  .hint kbd{
    font-family:var(--mono); background:var(--surface-2); border:1px solid var(--hairline);
    padding:1px 6px; border-radius:5px; font-size:11px;
  }

  .status-line{
    font-size:13px; color:var(--bone-faint); margin-top:14px; min-height:18px;
    display:flex; align-items:center; gap:8px;
  }
  .status-line.error{ color:#dba48f; }
  .spinner{
    width:13px; height:13px; border-radius:50%; border:2px solid var(--hairline);
    border-top-color:var(--gold); animation:spin .7s linear infinite;
  }
  @keyframes spin{ to{ transform:rotate(360deg); } }

  .suggest-wrap{ margin-top:22px; }
  .suggest-label{
    font-family:var(--mono); font-size:11px; letter-spacing:.12em; text-transform:uppercase;
    color:var(--bone-faint); margin-bottom:10px;
  }
  .suggest-list{ display:flex; flex-wrap:wrap; gap:8px; }
  .suggest-chip{
    background:var(--surface-2); border:1px solid var(--hairline); border-radius:100px;
    padding:8px 14px; font-size:13.5px; color:var(--bone-dim); display:flex; gap:8px; align-items:center;
  }
  .suggest-chip:hover{ border-color:var(--gold); color:var(--bone); }
  .suggest-chip b{ color:var(--bone); font-weight:600; }
  .suggest-chip .arrow{ color:var(--bone-faint); }

  /* ---------- History ---------- */
  section.history{ padding:10px 0 6px; }
  .history-row{
    display:flex; gap:10px; overflow-x:auto; padding-bottom:6px; scrollbar-width:thin;
  }
  .history-chip{
    flex:none; background:var(--surface); border:1px solid var(--hairline); border-radius:10px;
    padding:10px 14px; min-width:160px; max-width:240px;
  }
  .history-chip .h-src{ font-size:12.5px; color:var(--bone-dim); margin-bottom:3px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .history-chip .h-tgt{ font-size:13.5px; color:var(--gold-soft); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .history-chip:hover{ border-color:var(--gold); }

  /* ---------- Phrasebook ---------- */
  section.phrasebook{ padding:70px 0 40px; }
  .section-head{ display:flex; align-items:flex-end; justify-content:space-between; gap:20px; margin-bottom:26px; flex-wrap:wrap; }
  h2.section-title{
    font-family:var(--serif); font-weight:600; font-size:30px; margin:0 0 6px; letter-spacing:-.01em;
  }
  p.section-desc{ color:var(--bone-dim); margin:0; font-size:14.5px; max-width:460px; }

  .tabs{ display:flex; gap:8px; flex-wrap:wrap; margin-bottom:26px; }
  .tab{
    background:transparent; border:1px solid var(--hairline); color:var(--bone-dim);
    padding:8px 16px; border-radius:100px; font-size:13px; font-weight:600;
  }
  .tab.active{ background:var(--gold); border-color:var(--gold); color:#1c1408; }
  .tab:not(.active):hover{ color:var(--bone); border-color:var(--bone-faint); }

  .phrase-grid{
    display:grid; grid-template-columns:repeat(auto-fill, minmax(240px,1fr)); gap:12px;
  }
  .phrase-card{
    background:var(--surface); border:1px solid var(--hairline); border-radius:12px;
    padding:16px 18px; text-align:left; transition:transform .15s ease, border-color .15s ease;
  }
  .phrase-card:hover{ transform:translateY(-2px); border-color:var(--gold); }
  .phrase-en{ font-size:13.5px; color:var(--bone-dim); margin-bottom:6px; }
  .phrase-tw{ font-family:var(--twi-sans); font-size:18px; color:var(--bone); font-weight:600; }
  .phrase-note{ font-size:11.5px; color:var(--bone-faint); margin-top:6px; font-style:italic; }

  /* ---------- About / footer ---------- */
  section.about{ padding:50px 0 10px; }
  .about-grid{ display:grid; grid-template-columns:1.1fr .9fr; gap:40px; }
  @media (max-width:760px){ .about-grid{ grid-template-columns:1fr; } }
  .about-card{
    background:var(--surface); border:1px solid var(--hairline); border-radius:var(--radius); padding:26px;
  }
  .about-card h3{ font-family:var(--serif); font-size:19px; font-weight:600; margin:0 0 10px; }
  .about-card p{ color:var(--bone-dim); font-size:14px; margin:0 0 10px; }
  .about-card p:last-child{ margin-bottom:0; }
  .about-card ul{ margin:0; padding-left:18px; color:var(--bone-dim); font-size:14px; }
  .about-card li{ margin-bottom:6px; }

  footer{
    border-top:1px solid var(--hairline); margin-top:60px; padding:26px 0 40px;
    display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;
  }
  footer .fine{ font-size:12.5px; color:var(--bone-faint); }
  footer .fine a{ color:var(--bone-dim); text-decoration:underline; text-underline-offset:3px; }

  @media (prefers-reduced-motion: reduce){
    *{ animation-duration:0.001ms !important; transition-duration:0.001ms !important; }
    html{ scroll-behavior:auto; }
  }

  :focus-visible{ outline:2px solid var(--gold); outline-offset:2px; }
</style>
</head>
<body>

<nav class="top">
  <div class="brand">
    <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
      <path d="M24 6c8 0 13 5.5 13 12 0 5-3 8-7 9.5 2 .5 3.5 2 3.5 4.5 0 3-2.5 5-6.5 5-1 0-2-.1-3-.4V42c0 0-1.5.4-3.5.4S13 42 13 42V22c-3.5-1.2-6-4.3-6-8.3C7 8 13.5 6 24 6Z" stroke="#CC9A3D" stroke-width="2"/>
      <circle cx="30" cy="16" r="1.6" fill="#CC9A3D"/>
    </svg>
    <div>
      <div class="brand-text">KASA</div>
      <div class="brand-sub">Twi · English</div>
    </div>
  </div>
  <div class="status"><span class="dot"></span> live translation engine</div>
</nav>

<header class="hero">
  <svg class="sankofa-watermark" viewBox="0 0 48 48" fill="none" aria-hidden="true">
    <path d="M24 6c8 0 13 5.5 13 12 0 5-3 8-7 9.5 2 .5 3.5 2 3.5 4.5 0 3-2.5 5-6.5 5-1 0-2-.1-3-.4V42c0 0-1.5.4-3.5.4S13 42 13 42V22c-3.5-1.2-6-4.3-6-8.3C7 8 13.5 6 24 6Z" stroke="#CC9A3D" stroke-width="1.4"/>
  </svg>
  <div class="wrap">
    <div class="hero-inner">
      <span class="eyebrow">Sankofa &nbsp;·&nbsp; go back and fetch it</span>
      <h1 class="headline">Kasa means <em>speak</em>.<br>Say it in Twi.</h1>
      <p class="sub">A live Twi–English translator, backed by a hand-checked phrasebook of everyday Akan expressions — for when the machine gets it wrong.</p>
    </div>
  </div>
  <div class="kente-rule"></div>
</header>

<main class="wrap">

  <section class="translator" aria-label="Translator">
    <div class="panes">
      <div class="pane">
        <div class="pane-head">
          <span class="lang-tag" id="srcTag"><b>EN</b> English</span>
        </div>
        <textarea id="srcText" placeholder="Type a word or phrase — try “thank you” or “where is the market?”" maxlength="500"></textarea>
        <div class="pane-foot">
          <span class="charcount"><span id="charCount">0</span>/500</span>
          <button class="btn-ghost" id="clearBtn" type="button">Clear</button>
        </div>
      </div>

      <div class="swap-col">
        <button class="swap-btn" id="swapBtn" type="button" aria-label="Swap languages" title="Swap languages">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h11l-3-3M17 17H6l3 3"/></svg>
        </button>
      </div>

      <div class="pane">
        <div class="pane-head">
          <span class="lang-tag" id="tgtTag"><b>TWI</b> Akan Twi</span>
          <span id="resultBadge"></span>
        </div>
        <div class="result-box empty" id="resultBox">Your translation will appear here.</div>
        <div class="pane-foot">
          <span class="charcount" id="engineNote">Phrasebook + GhanaNLP corpus + MyMemory</span>
          <button class="btn-ghost" id="copyBtn" type="button">Copy</button>
        </div>
      </div>
    </div>

    <div class="translate-row">
      <button class="btn btn-primary" id="translateBtn" type="button">Translate</button>
      <span class="hint">or press <kbd>Enter</kbd> — <kbd>Shift</kbd>+<kbd>Enter</kbd> for a new line</span>
    </div>

    <div class="status-line" id="statusLine"></div>

    <div class="suggest-wrap" id="suggestWrap" style="display:none;">
      <div class="suggest-label">You might also mean</div>
      <div class="suggest-list" id="suggestList"></div>
    </div>
  </section>

  <section class="history" id="historySection" style="display:none;">
    <div class="suggest-label" style="margin-bottom:10px;">Recent</div>
    <div class="history-row" id="historyRow"></div>
  </section>

  <section class="phrasebook" aria-label="Phrasebook">
    <div class="section-head">
      <div>
        <h2 class="section-title">Everyday phrasebook</h2>
        <p class="section-desc">Hand-checked expressions you can trust — tap any card to load it into the translator.</p>
      </div>
    </div>
    <div class="tabs" id="tabs"></div>
    <div class="phrase-grid" id="phraseGrid"></div>
  </section>

  <section class="about">
    <div class="about-grid">
      <div class="about-card">
        <h3>How translation works here</h3>
        <p>Three tiers, checked in order. First, a small hand-curated phrasebook — marked <strong>verified phrase</strong>, safe to rely on.</p>
        <p>Second, a 291-sentence corpus of real, human-translated English–Twi sentence pairs from GhanaNLP — marked <strong>GhanaNLP corpus</strong>. An exact match is a genuine professional translation; a close match shows you the matched sentence directly, so you can judge the fit yourself.</p>
        <p>Anything outside both is sent to MyMemory, a free community-edited translation API, and marked <strong>machine translation</strong>. Twi is low-resource for MT, so double-check anything important — a wedding toast, a medical note, a contract — with a fluent speaker.</p>
      </div>
      <div class="about-card">
        <h3>Data &amp; attribution</h3>
        <ul>
          <li>Sentence corpus: <a href="https://huggingface.co/datasets/Ghana-NLP/ENGLISH_TWI_PARALLEL_TEXT" target="_blank" rel="noopener">Ghana-NLP/ENGLISH_TWI_PARALLEL_TEXT</a>, a sample of 291 of ~6,090 professionally-translated sentence pairs</li>
          <li>GhanaNLP's data card mixes CC BY 4.0 and Non-Commercial/Share-Alike terms — treated here as CC BY-NC-SA; confirm with GhanaNLP before commercial use</li>
          <li>No build step — one HTML file, deploy anywhere static</li>
          <li>Extend the corpus by adding <code>{en, tw}</code> pairs to the <code>CORPUS</code> array</li>
        </ul>
      </div>
    </div>
  </section>

  <footer>
    <div class="fine">Kasa — a Twi–English translator. Sentence data © GhanaNLP, used under attribution. Machine output may be imperfect; corrections welcome.</div>
    <div class="fine">Sankofa: <em>se wo were fi na wosankofa a yenkyi</em> — it's not wrong to go back for what you forgot.</div>
  </footer>
</main>

<script>
(function(){
  "use strict";

  var PHRASEBOOK = {
    "Greetings": [
      { en: "Hello", tw: "Ɛte sɛn?", note: "Literally “how is it?” — the everyday greeting." },
      { en: "Good morning", tw: "Maakye" },
      { en: "Good afternoon", tw: "Maaha" },
      { en: "Good evening", tw: "Maadwo" },
      { en: "Welcome", tw: "Akwaaba" },
      { en: "How are you?", tw: "Wo ho te sɛn?" },
      { en: "I'm fine", tw: "Me ho yɛ" },
      { en: "What is your name?", tw: "Wo din de sɛn?" },
      { en: "My name is...", tw: "Me din de..." },
      { en: "Nice to meet you", tw: "Ɛyɛ me anigye sɛ mahyia wo" },
      { en: "Goodbye", tw: "Nante yie", note: "Literally “walk well.”" },
      { en: "See you again", tw: "Yɛbɛhyia bio" },
      { en: "Thank you", tw: "Medaase" },
      { en: "Thank you very much", tw: "Medaase paa" },
      { en: "Please", tw: "Mepaakyɛw" },
      { en: "Yes", tw: "Aane" },
      { en: "No", tw: "Daabi" },
      { en: "Sorry", tw: "Kafra" }
    ],
    "Common phrases": [
      { en: "I don't understand", tw: "Mente aseɛ" },
      { en: "Do you speak English?", tw: "Wo ka Borɔfo kasa?" },
      { en: "I don't speak Twi well", tw: "Menka Twi yiye" },
      { en: "Please speak slowly", tw: "Mepaakyɛw, kasa brɛoo" },
      { en: "Where is the market?", tw: "Ɛhe na dwam no wɔ?" },
      { en: "How much is this?", tw: "Sɛn na eyi yɛ?" },
      { en: "That's too expensive", tw: "Ɛyɛ den dodo" },
      { en: "Help me", tw: "Boa me" },
      { en: "I need water", tw: "Mehia nsu" },
      { en: "I'm hungry", tw: "Ɛkɔm de me" },
      { en: "I'm thirsty", tw: "Sukɔm de me" },
      { en: "Where is the bathroom?", tw: "Ɛhe na tiafi no wɔ?" },
      { en: "I love you", tw: "Me dɔ wo" },
      { en: "Let's go", tw: "Momma yɛnkɔ" },
      { en: "Wait for me", tw: "Twɛn me" },
      { en: "I'm coming", tw: "Mereba" }
    ],
    "Numbers": [
      { en: "One", tw: "Baako" }, { en: "Two", tw: "Mmienu" }, { en: "Three", tw: "Mmiɛnsa" },
      { en: "Four", tw: "Ɛnan" }, { en: "Five", tw: "Enum" }, { en: "Six", tw: "Nsia" },
      { en: "Seven", tw: "Nson" }, { en: "Eight", tw: "Nwɔtwe" }, { en: "Nine", tw: "Nkron" },
      { en: "Ten", tw: "Du" }, { en: "Twenty", tw: "Aduonu" }, { en: "One hundred", tw: "Ɔha" }
    ],
    "Days & time": [
      { en: "Sunday", tw: "Kwasiada" }, { en: "Monday", tw: "Dwowda" }, { en: "Tuesday", tw: "Benada" },
      { en: "Wednesday", tw: "Wukuda" }, { en: "Thursday", tw: "Yawda" }, { en: "Friday", tw: "Fida" },
      { en: "Saturday", tw: "Memeneda" }, { en: "Today", tw: "Ɛnnɛ" }, { en: "Tomorrow", tw: "Ɔkyena" },
      { en: "Yesterday", tw: "Nnɛra" }, { en: "Now", tw: "Seesei" }, { en: "Later", tw: "Akyire yi" }
    ],
    "Family": [
      { en: "Father", tw: "Papa" }, { en: "Mother", tw: "Maame" }, { en: "Child", tw: "Ɔba" },
      { en: "Brother/sister (sibling)", tw: "Nua" }, { en: "Husband", tw: "Okunu" }, { en: "Wife", tw: "Ɔyere" },
      { en: "Grandmother", tw: "Nana", note: "Also used for grandfather and traditional chiefs." },
      { en: "Friend", tw: "Adamfo" }, { en: "Family", tw: "Abusua" }
    ],
    "Food & drink": [
      { en: "Water", tw: "Nsu" }, { en: "Food", tw: "Aduane" }, { en: "Rice", tw: "Ɛmo" },
      { en: "Fish", tw: "Apataa", note: "General term; fresh fish is “apataa mono.”" },
      { en: "Meat", tw: "Nam" }, { en: "Pepper (spicy)", tw: "Mako" },
      { en: "It's delicious", tw: "Ɛyɛ dɛ" }, { en: "I'm full", tw: "Amee me" }
    ]
  };

  var CORPUS = [{"en":"His supporters were very rowdy during the campaign.","tw":"N'akyigyinafo yɛɛ basabasa kɛse wɔ ɔsatu no mu."},{"en":"The children were students in the mission schools who split their time between general education, religious studies, and unpaid labor.","tw":"Na mmofra no yɛ sukuufo a wɔwɔ asɛmpatrɛw sukuu ahorow mu a wɔkyekyɛ wɔn bere mu wɔ nhomasua a ɛkɔ akyiri, nyamesom adesua, ne adwuma a wontua hwee ntam."},{"en":"Industrial parks greatly benefit nearby villages and districts.","tw":"Mfiridwuma mmɔnten so mfaso kɛse wɔ nkuraa ne amantam a ɛbɛn hɔ no so."},{"en":"The Second Development Plan of 1959–1964 followed the Soviet model, and shifted away from expanding state services toward raising productivity in the key sectors.","tw":"Nkɔsoɔ Nhyehyɛeɛ a ɛtɔ so mmienu a ɛbaa 1959–1964 no dii Soviet nhwɛsoɔ no akyi, na ɛdanee ne ho firii ɔman nnwuma a wɔbɛtrɛ mu no so kɔɔ adwumayɛ a ɛkɔ soro wɔ nnwuma titire no mu."},{"en":"Bridge construction is expected to be complete in four years.","tw":"Wɔhwɛ kwan sɛ wobewie abɔntenban no wɔ mfe anan mu."},{"en":"In that way, valuable species of trees are cut down.","tw":"Saa kwan no so no, wotwa nnua ahorow a ɛsom bo."},{"en":"The vice of drug abuse is killing the youths.","tw":"Nnubɔne a wɔde di dwuma ɔkwammɔne so no rekunkum mmerante ne mmabaa no."},{"en":"There were more COVID-19 cases from Eastern Ghana at the end of September.","tw":"Nnipa a wɔnyaa COVID-19 no bubɔɔ ho wɔ Ghana Atɔeɛ fam wɔ Ɛbɔ bosome no awieeɛ."},{"en":"How best can laws made by local authorities be implemented?","tw":"Ɔkwan bɛn so na wobetumi de mmara a mpɔtam hɔ atumfoɔ ahyɛ no adi dwuma yiye?"},{"en":"Whiles Gbewaa was still alive, his daughter Yennenga, travelled north and founded the Mossi Kingdoms, who constitute the majority of present day Burkina Faso.","tw":"Berɛ a na Gbewaa da so ara te ase no, ne babaa Yennenga, tuu kwan kɔɔ atifi na ɔkɔtee Mossi ahemman no, a wɔn mu dodoɔ no ara yɛ ɛnnɛ Burkina Fasofoɔ no."},{"en":"Furthermore, the ineffectiveness of the council, indicated by its failure to execute council resolutions, further hampers progress","tw":"Bio nso, nea ɛkyerɛ sɛ bagua no nyɛ adwuma yiye, nea ɛkyerɛ ne sɛ wɔrennyae baguam gyinaesi, na eyi kɔ so siw nkɔso kwan."},{"en":"The police are investigating the mismanagement of tea project money and disappearance of project files.","tw":"Polisifoɔ no reyɛ tea dwumadie sika a wɔanhwɛ so yie no nhwehwɛmu ne dwumadie no nkrataa a ɛyeraeɛ no."},{"en":"The public needs awareness on how to maintain a healthy body.","tw":"Ɛsɛ sɛ ɔmanfo hu sɛnea wobetumi akura nipadua a ɛte apɔw mu."},{"en":"It life rerieving to forgive those that wronged us.","tw":"Ɛyɛ nkwa nkanyan sɛ yɛde bɛkyɛ wɔn a wɔyɛɛ yɛn bɔne."},{"en":"His rude comments offended everyone in the room and caused tension and discomfort.","tw":"Nsɛm a ɔkae a ɛnyɛ aniberesɛm no hyɛɛ obiara a ɔwɔ dan no mu abufuw na ɛde nhyɛso ne ahotɔ bae."},{"en":"Some districts receive little funds from the government.","tw":"Amansin bi nnya sika kakraa bi fi aban hɔ."},{"en":"The council has informed people to contribute money towards the construction of a stadium.","tw":"Agyinatukuo no abɔ nkurɔfo amanneɛ sɛ wɔmfa sika mma mfa nsi agumadibea."},{"en":"Students who successfully finish their degree, shouldn't sit home but look for jobs.","tw":"Asuafoɔ a wɔwie wɔn abodin krataa no yie, ɛnsɛ sɛ wɔtena fie na mmom wɔhwehwɛ nnwuma."},{"en":"The main challenge is lack of fishing nets.","tw":"Ɔhaw no titire pa ara ne asau a wɔde kye mpataa a enni hɔ no."},{"en":"The performance of the district depends on the performance of the finance department.","tw":"Ɔmansin no adwumayɛ gyina sikasɛm dwumadibea no adwumayɛ so."},{"en":"Ghana imports most of its products, and most funding in Ghana comes from foreigners.","tw":"Ghana kra wɔn neama dodow no ara, na Ghana ya ne sika dodow no firi amanfoforo hɔ."},{"en":"I still struggle to understand why Ghanaians generally do not care about the state of affairs of the country. It is very sad and alarming.","tw":"Meda so ara repere sɛ mɛte nea enti a mpɛn pii no Ghanafo mfa ɔman no tebea ho asɛm no ase. Ɛyɛ awerɛhow na ɛyɛ hu pa ara."},{"en":"Police deployment in the night has helped to reduce on the crime rates in the sub-regions.","tw":"Polisifoɔ a wɔde wɔn kɔ hɔ anadwo no aboa ma nsɛmmɔnedi dodow a ɛwɔ mpɔtam nketewa no mu no so atew"},{"en":"They explored the ancient ruins and marveled at the level of expertise these civilizations of old had.","tw":"Wɔhwehwɛɛ tete amamfo no mu na wɔn ho dwirii wɔn wɔ nimdeɛ a na saa tete anibuei ahodoɔ yi wɔ no ho."},{"en":"The accident happened on Thursday morning a few kilometers from Underbridge bridge on the Motorway.","tw":"Akwanhyia no sii Dwoda anɔpa wɔ kilomita kakraa bi fi Underbridge bridge a ɛwɔ Motorway no so."},{"en":"People have poor health because they lack drugs for treatment.","tw":"Nkorɔfoɔ apɔmuden nyɛ ɛfirI sɛ wɔnni nnuro a wɔde bɛsa wɔn ho yadeɛ."},{"en":"Students joining higher level can acquire students loans from banks and funding organizations.","tw":"Asuafoɔ a wɔde wɔn ho hyɛ sukuupɔn mu no bɛtumi anya asuafoɔ bosea afiri sikakorabea ne ahyehyɛdeɛ a wɔde sika ma."},{"en":"Artists are earning less from music which makes them quit the fierd.","tw":"Adwumfo renya sika kakraa bi afi nnwom mu a ɛma wogyae fierd no."},{"en":"Churches need to vacate the land when their lease expires.","tw":"Ɛsɛ sɛ asɔre ahorow fi asase no so bere a wɔn dan a wɔde ahyɛ wɔn nsa no twam no."},{"en":"She was coming from the bank when the thief robbed her.","tw":"Na ofiri sikakorabea reba bere a owifoɔ no bɔɔ no korɔno no"},{"en":"The role of police is to protect and serve the people within the country.","tw":"Polisifo dwumadie ne sɛ wɔbɛbɔ nnipa a wɔwɔ ɔman no mu ho ban na wɔasom wɔn."},{"en":"People are resorting to saving money on mobile money other than banks.","tw":"Nkorɔfoɔ de wɔn sika resie wɔn foono sika so kyɛn sikakorabea."},{"en":"To solve sanitation problems ,they'll implement Albertine physical development plans and establish hygienic structures.","tw":"Sɛ yɛbɛma ahonidie haw anoyie no, wɔde Albertine honam mu nkɔsoɔ nhyehyɛeɛ ahodoɔ bɛdi dwuma na wɔde ahoteɛ nhyehyɛeɛ ahodoɔ asi hɔ."},{"en":"There are many things in the community that hinder girls from continuing with education.","tw":"Nneɛma pii wɔ mpɔtam hɔ a ɛmma mmaayewa ntumi ntoa wɔn nwomasua so."},{"en":"The headteacher was arrested for asking students' money to bribe invigilators.","tw":"Wɔkyeree sukuupanin no so ɔbisaa sika firii asuafoɔ no hɔ sɛ ɔde reyɛ ademudeɛ ama wɔn a wɔhwɛ nsɔhwɛ so no."},{"en":"The region reports a high number of deaths.","tw":"Ɔmantam no bɔ amanneɛ sɛ nnipa dodow a wowuwui no dɔɔso."},{"en":"Breast Feeding is a necessity for any baby as it increases it's immunity against diseases","tw":"Nufu a wɔde ma no yɛ ade a ɛho hia ma akokoaa biara efisɛ ɛma ne tumi a ɛko tia nyarewa no yɛ kɛse"},{"en":"People need to vote for the right people.","tw":"Ɛsɛ sɛ nkorɔfoɔ to aba ma nnipa papa."},{"en":"Member of parliaments make laws for the country.","tw":"Mmarahyɛbadwafoɔ hyehyɛ mmara ma ɔman no."},{"en":"All local leaders should be involved at all levels.","tw":"Ɛsɛ sɛ mpɔtam hɔ akannifo nyinaa de wɔn ho hyɛ mu wɔ gyinabea ahorow nyinaa mu."},{"en":"It is important to keep land for sherter and also to plant trees.","tw":"Ɛho hia sɛ wɔkora asase so ma onwono na wodua nnua nso."},{"en":"Parents are concerned about their interests and not the future of their children.","tw":"Awofoɔ dwene deɛ wɔn ani gye ho na ɛnyɛ wɔn mma daakye."},{"en":"All nationals above eighteen years have a right to vote for their leaders.","tw":"Amamma wɔn mfeɛ boro dunwɔtwe (18) wɔ mmara ho kwan sɛ wɔbɛto aba ama wɔn mpanimfoɔ."},{"en":"The chairperson was a good person kindly follow his footsteps.","tw":"Na oguamtrani no yɛ onipa pa fi ayamye mu di n'anammɔn akyi."},{"en":"The rich should come out to help the vulnerable people in society.","tw":"Ɛsɛ sɛ asikafoɔ no ba abɔntene bɛhwɛ nnipa wɔnni bi wɔn kuro no mu."},{"en":"Parents should support their children while in school.","tw":"Ɛsɛ awofoɔ boa wɔn mma berɛ a wɔwɔ sukuu mu."},{"en":"District committees are not consulted in the allocating of government funds","tw":"Wɔnbisabisa ɔmantam boayikuw ahorow wɔ aban sika a wɔkyekyɛ mu"},{"en":"The main objective is to appraise and validate the performance of the Education Sector in the ministry.","tw":"Atirimpɔ titire no ara ne sɛ ɛbɛkyerɛ nnwuma a Nwomasua Asoeɛ no redi wɔ asoeɛ no mu ho anisɔ na ama yɛahunu ne mpɔmpɔnsoɔ."},{"en":"Our man will win this election with a landslide","tw":"Yɛn nipa no bɛnya aba pii adi nkonim mapa wɔ saa abatoɔ yi mu."},{"en":"The defendant pleaded not guilty of defilement charges.","tw":"Nea wɔde asɛm no kɔdan no no gye toom sɛ onni fɔ wɔ sobo a wɔde bɔɔ no sɛ ɔde efĩ ho no ho."},{"en":"Savings groups need to have a manageable number of members to prevent fraud.","tw":"ɛsɛ sɛ sikakorabea akuw nya emufo dodow a wotumi di ho dwuma na wɔasiw nsisi ano."},{"en":"It's the traffic officers that provide concrete reports about road accidents.","tw":"Ɛyɛ kar akwan so adwumayɛfo na wɔde akwanhyia ahodoɔ ho amanneɛbɔ a ɛyɛ nokware ma."},{"en":"Ghana Muslim Supreme Council governs all Muslims in Ghana and is located in Accra","tw":"Ghana Nkramofo Asɛnnibea Kunini no na ɛhwɛ Nkramofo a wɔwɔ Ghana nyinaa so, na ɛwɔ Accra"},{"en":"The officers who committed the crime went into hiding.","tw":"Polisifo a wɔyɛɛ amumɔyɛde no kɔhintaw."},{"en":"The winner of the election has been declared.","tw":"Wɔakyerɛ sɛ nea odi nkonim wɔ abatow no mu."},{"en":"The future has to be brighter than today.","tw":"Ɛsɛ sɛ daakye yɛ papa kyɛn ɛnnɛ"},{"en":"Every homestead must have a latrine for hygiene purposes.","tw":"Ɛsɛ sɛ ofie biara nya tiafi a wɔde siesie wɔn ho."},{"en":"Pregnant women prefer traditional birth attendants to hospitals.","tw":"mmea a wɔyem pɛ awo ho adwumayɛfo a wɔtaa de di dwuma sen ayaresabea ahorow."},{"en":"Due to limited capacity, the school bus cannot accommodate most of the students, leading to transportation challenges.","tw":"Esiane sɛ sukuu bɔs no ntumi mfa sukuufo dodow no ara nkɔ, na ɛde akwantu ho nsɛnnennen ba."},{"en":"Male and female leaders are welcomed for gender balance purposes.","tw":"Wɔgye mmarima ne mmaa akannifoɔ nyinaa sɛnea ɛbɛkari pɛ wɔ mmarima ne mmaa ntam."},{"en":"The opposition leader has pledged to help in planting more trees.","tw":"Ɔsɔretia kannifo no ahyɛ bɔ sɛ ɔbɛboa ma wɔadua nnua pii."},{"en":"On what date shall the general elections take place?","tw":"Da bɛn na wɔnbɛyɛ amansan abatow no?"},{"en":"Proper disposal and treatment of all materials that may have come into contact with the feces of other people with cholera (e.g., clothing, bedding, etc.) are essential.","tw":"nneɛma a ebia ɛbaa nnipa afoforo a wɔwɔ kɔlera nsu mu (sɛ nhwɛso no, ntade, mpa, ne nea ɛkeka ho) nyinaa a wɔbɛtow agu yiye na wɔasa no yare."},{"en":"In 1951, the CPP created the Accelerated Development Plan for Education. This plan set up a six-year primary course, to be attended as close to universally as possible, with a range of possibilities to follow.","tw":"Wɔ afe 1951 mu no, CPP yɛɛ mpontuo nhyehyɛe maa nwomasua. Saa nhyehyɛe yi de mfe asia mfitiase adesua sii hɔ, a wɔbɛkɔ bi a ɛbɛn amansan nyinaa sɛnea ɛbɛyɛ yiye biara, a nneɛma ahorow a wobetumi adi akyi."},{"en":"I bought the pain killers from the pharmacy outside the hospital.","tw":"Metɔɔ nnuru a wɔde kum ɛyaw no fii nnurutɔnbea a ɛwɔ ayaresabea no akyi no."},{"en":"The warm embrace of a parent is always enough to lift one's spirits.","tw":"Ɔwofo atuu a ɛyɛ hyew dɔɔso bere nyinaa na ama ne honhom akɔ soro."},{"en":"All nationals are free to vote for any candidate they wish.","tw":"Amamma nyinaa wɔ akwanya sɛ wɔbɛto aba ama ɔkansifoɔ biara wɔpɛ."},{"en":"The president of Ghana will attend the Day celebrations that will take place at Independence Square","tw":"Ghana ɔmanpanyin bɛkɔ Da afahyɛ a ɛbɛkɔ so wɔ Independence Square no ase"},{"en":"The district health department should inform people that human immune virus is real.","tw":"Ɛsɛ sɛ ɔmantam akwahosan dwumadibea no ka kyerɛ nkurɔfo sɛ nnipa nipadua mu nkwammoaa a ɛko tia nyarewa no yɛ nokware."},{"en":"With the north under British control, the three territories of the Gold Coast—the Colony (the coastal regions), Ashanti, and the Northern Territories—became, for all practical purposes, a single political unit, or crown colony, known as the Gold Coast.","tw":"Berɛ a na Atifi no hyɛ Engresifoɔ ase no, Gold Coast nsasesini mmiɛnsa no - wɔn a wɔdi wɔn so no (amantam a ɛwɔ mpoano no), Asantefoɔ, ne Atifi Nsasesini no - bɛyɛɛ, amanyɔkuo baako, anaa beaeɛ titire a wɔdi so, a na wɔnim no sɛ Gold Coast."},{"en":"The armyworm has been a big problem in the last ten years.","tw":"Asraafo nwansena ayɛ ɔhaw kɛse wɔ mfe du a atwam no mu."},{"en":"The village leader offered land for the construction of the school, contributing to educational infrastructure development.","tw":"Akuraase kannifoɔ no de asase mae ma wɔde sii sukuu dan no a ɛreboa nwomasua adansie nkɔsoɔ."},{"en":"Investigations must be carried out without any interruptions.","tw":"Ɛsɛ sɛ wɔyɛ nhwehwɛmu a wɔmfa biribiara ntwitwa mu."},{"en":"At the end of the project, we had to account for all the expenses.","tw":"Wɔ adwuma no awiei no, na ɛsɛ sɛ yebu ɛka a yɛbɔe no nyinaa ho akontaa."},{"en":"Police stressed the need to discourage the use of military attire by people.","tw":"Polisifoɔ sii hia a ehia sɛ wobu asraafoɔ ntade a nkurɔfoɔ de di dwuma no abam so dua."},{"en":"Use of contraceptives helps families to lay prospective strategies for their children.","tw":"Nnuro a wɔde si nyinsɛn ano boa ma mmusua tumi toto wɔn mma yie."},{"en":"During the lockdown people couldn't go to work, yet they had to feed families.","tw":"Wɔ lockdown bere no mu no na nkurɔfo ntumi nkɔ adwuma, nanso na ɛsɛ sɛ wɔma mmusua aduan."},{"en":"Constructing a school is one way of keeping one's legacy.","tw":"Sukuu a wobesi yɛ ɔkwan biako a obi fa so kura n'agyapade mu."},{"en":"Farmers rent land to carry out agricultural activities.","tw":"Akuafo tu asase de yɛ wɔn mfuw."},{"en":"The reason for the big number of migrants in Ghana is not yet known.","tw":"Wonnya nhuu nea enti a atubrafo dodow a ɛwɔ Ghana no dɔɔso."},{"en":"During hunting the prey was tracked with the help of dogs","tw":"Bere a wɔrebɔ abɔmmɔ no, na wɔde akraman mmoa di mmoa a wɔkyere wɔn no akyi"},{"en":"The country is stable under the current government","tw":"Ɔman no gyina hɔ pintinn wɔ mprempren aban no ase"},{"en":"In rural areas, girls are at a high risk of being forced into marriage.","tw":"Wɔ nkuraase no, mmeawa wɔ asiane kɛse mu sɛ wɔbɛhyɛ wɔn ma wɔaware."},{"en":"Our school lacks funds to construct a new latrine.","tw":"Yɛn sukuu nni sika a wɔde bɛsi tiafi foforɔ."},{"en":"The dangers of this disease will be assessed and remedies will be provided.","tw":"Wɔbɛhwɛ asiane a ɛwɔ saa yare yi mu na wɔde ano aduru ama."},{"en":"Investigations are being done to find out the thief.","tw":"Wɔreyɛ nhwehwɛmu de ahunu awifoɔ no."},{"en":"People were warned against poaching in game reserves.","tw":"Wɔbɔɔ nkorɔfoɔ kɔkɔ sɛ ɛnsɛ sɛ wɔkyere mmoa wɔ mmeaeɛ a wɔakora mmoa so."},{"en":"People have resisted offering their land to cater for road expansion.","tw":"Nkorɔfoɔ atia sɛ wɔde wɔn nsase bɛma sɛ wɔmfa mmue ɛkwan no mu."},{"en":"My mother loves hugging us every time she comes back from work.","tw":"Me maame ani gye ho sɛ ɔbɛyɛ yɛn atuu bere biara a obefi adwuma aba no."},{"en":"In order to have a better life, one needs to have children they can afford.","tw":"Sɛ obi benya asetra pa a, ɛsɛ sɛ ɔwo mma a obetumi ahwɛ."},{"en":"The local chairperson gives the seeds to the people well known to him.","tw":"Otitenani a ɔwɔ kuro no mu no de aba no ma nnipa a ɔnnim wɔn yie no."},{"en":"It is important to report any linkage to authorities in charge.","tw":"Ɛho hia sɛ wɔbɔ adeɛ biara apue ho amanneɛ kyerɛ atumfoɔ a wɔhwɛ so."},{"en":"Various task forces have been given donations to help in fighting this coronavirus .","tw":"Wɔma akuo a wɔde dwumadie ahyɛ wɔn nsa no akyɛdeɛ bebree a ɛbɛboa ama wɔako atia coronavirus."},{"en":"The coronavirus has led to the closer of many organizations.","tw":"Coronavirus ama ahyehyɛdeɛ bebree abɛn."},{"en":"The fertility of our soil favors the growth of many crops annually.","tw":"Ɛsiane sɛdeɛ yɛ nsase no wɔ ahoɔden nti, ɛtumi boa ma yɛdua nnɔbaeɛ ahodoɔ bebree"},{"en":"Muslim clerics requested the government to build a mosque.","tw":"Nkramofo asɔfo srɛɛ aban no sɛ wonsi mkramo asɔredan."},{"en":"The project was started with the aim of giving back to the community.","tw":"Wɔhyɛɛ adwuma no ase a na wɔn botae ne sɛ wɔbɛsan de nneɛma ama ɔmanfo."},{"en":"The hospital contractor was given forty days to complete the construction project.","tw":"Wɔmaa onipa a wɔde ayaresabea no sie no hyɛɛ ne nsa no adaduanan sɛ ɔmfa nsi ɛdan no nwie"},{"en":"Border districts should always prepare attacks from neighbors.","tw":"Ɛsɛ sɛ ɔhye so amansin siesie ntua a efi afipamfo hɔ bere nyinaa."},{"en":"The community was shocked to hear of his death.","tw":"Mpɔtam hɔfo ho dwiriw wɔn bere a wɔtee ne wu no."},{"en":"Some borders are seen as weaknesses in stopping the coronavirus spread.","tw":"Wohu ahye binom sɛ mmerɛwyɛ wɔ coronavirus trɛw a wosiw ano no mu."},{"en":"A cocoa business can be inherited by a child from his parent.","tw":"Kookoo dwadie bɛtumi ayɛ agyapadeɛ bi a abɔfra bi awofoɔ de bɛgya no."},{"en":"People form cooperatives to do something better they couldn't do individually.","tw":"Nkorɔfoɔ ka wɔn ho bɔm yɛ nnoɔma pa wɔn nko ara ntumi nyɛ."},{"en":"Many veterans have now joined other professionals after retiring from the army.","tw":"Mprempren asraafoɔ a wɔadi ako pii akɔka adwumayɛfo afoforɔ ho bere a wɔakɔ pɛnhyen wɔ asraafo adwuma mu akyi."},{"en":"People must have the skills and knowledge to engage in business activities.","tw":"Ɛwɔ sɛ nkorɔfoɔ nya akadeɛ ne nimdeɛ de yɛ nnwuma."},{"en":"The major goal of Wanderai irrigation scheme is to improve agriculture and commercial farming .","tw":"Anisoadehunu a ɛsi Wanderai Irrigation scheme ani so ne sɛ ɛbɛboa ama kuadwuma ne mfuwyɛ akɔ so."},{"en":"Media is one of the channers for creating awareness to the public.","tw":"Nsɛm ho amanneɛbɔ yɛ kwan a wɔde ma ɔmanfo hu nea asi no mu baako."},{"en":"There are few male parents who talk to their daughter about menstruation periods.","tw":"Yɛwɔ awofoɔ mmarima ketewa a wɔne wɔn ba baa kasa fa mfikyirikɔ berɛ."},{"en":"The festival is celebrated on the first Saturday in May.","tw":"Wɔhyɛ saa fa no Memeneda a ɛdi kan wɔ bosome Kɔtɔnima mu."},{"en":"Signs of affected cattle should be reported to the district.","tw":"Ɛsɛ sɛ wɔbɔ ɔmantam no amanneɛ sɛ anantwie a wɔanya yare no ho sɛnkyerɛnne."},{"en":"How can the teaching and learning process be perfected?","tw":"Ɔkwan bɛn so na wobetumi ama nkyerɛkyerɛ ne adesua nhyehyɛe no ayɛ pɛ?"},{"en":"The government has encouraged technological advancement for the people.","tw":"Aban no ahyɛ sɛ ɛsɛ sɛ wɔma ɔmanfoɔ no nya mfididwuma a ɛtu mpɔn"},{"en":"Without a police station in an area, there is a possibility of crime increasing.","tw":"Polisi atenaeɛ biara nni mpɔtam hɔ nti, ɛnyɛ den koraa Sɛ nsɛmmɔnedie bɛkɔ so."},{"en":"In order to follow the curriculum principal individual-study material for learners have been synchronized.","tw":"Sɛnea ɛbɛyɛ a wobedi adesua nhyehyɛe no akyi no, wɔde ankorankoro adesua nneɛma atitiriw a wɔde ma asuafo no ayɛ biako."},{"en":"Settling land disputes is not an easy thing to do.","tw":"asase ho ntawntawdi a wobesiesie no nyɛ ade a ɛyɛ mmerɛw sɛ wɔbɛyɛ"},{"en":"The civil servants that abuse funds are to appear in court on Monday this year.","tw":"Ɛsɛ sɛ aban adwumayɛfo a wɔde sika di dwuma ɔkwammɔne so no kɔ asɛnnibea Memeneda afe yi."},{"en":"People protested over bad roads in their region.","tw":"Nkorɔfoɔ yɛɛ ɔsɔretia wɔ akwan bɔne a ɛwɔ wɔn mantam mu no ho."},{"en":"Health units offer health services to people in the community.","tw":"Akwahosan akuw de akwahosan ho nnwuma ma nnipa a wɔwɔ mpɔtam hɔ."},{"en":"The district council will receive a paper presentation for social services.","tw":"Mansini badwa no nsa bɛka nkrataa bi ɛsiane nnipa ho adwuma a wɔreyɛ nti."},{"en":"The community needs access to clean and safe water.","tw":"Mpɔtam hɔfo hia nsu a ɛho tew na ahobammɔ wom."},{"en":"Muslims use the fasting period to reawaken their spirit of righteousness.","tw":"Nkramofo de mmuadadi bere no san kanyan wɔn trenee honhom."},{"en":"Many people lost their lives in the war.","tw":"Nnipa pii hweree wɔn nkwa wɔ ɔko no mu."},{"en":"Sewerage management is still a challenge in town areas.","tw":"nsu fĩ a wɔde di dwuma no da so ara yɛ asɛnnennen wɔ nkurow akɛse mu."},{"en":"How much money was allocated for the construction of the bridge?","tw":"Sika ahe na wɔde sii abɔntenban no?"},{"en":"Condoms help prevent the spread of sexually transmitted diseases.","tw":"Kɔndɔm boa ma wosiw nyarewa a wonya fi nna mu ntrɛwmu ano."},{"en":"The local governments have failed to collect enough revenue.","tw":"Aban ananmusifoɔ a wɔhwɛ nkuro nkumaa amamuo so no ammɔ wɔn ho mmɔden wɔ sika gyegyeeɛ mu."},{"en":"The flying squad is effective in its operations.","tw":"Akuo a wɔtu fa wiem no bɔ wɔn ho mmɔden wɔ wɔn dwumadie mu pa ara."},{"en":"A number of girls have been sexually abused in our village.","tw":"Wɔato mmeawa dodow bi mmonnaa wɔ yɛn akuraa ase"},{"en":"There is an increase in diseases yet drugs in health centres are not enough.","tw":"Yɛwɔ nyarewa a akɔ soro nanso nnuro a ɛwɔ apɔmuden beaeɛ no sua."},{"en":"Fraud will affect the outcome of an election.","tw":"Apoobɔ betumi anya nsunsuanso wɔ abatow mu"},{"en":"His success in entrepreneurship has motivated young men, making him their role model, and he actively encourages people to embrace entrepreneurship, highlighting the advantages of being one's own boss.","tw":"Ne nkonimdi wɔ adwumayɛ mu no akanyan mmerante, na ama wayɛ wɔn nhwɛsofo, na ɔde nsi hyɛ nkurɔfo nkuran sɛ wonnye adwumayɛ ntom, na ɔtwe adwene si mfaso a ɛwɔ so sɛ obi yɛ n'ankasa panyin."},{"en":"After a long day at school, I always relax on the couch and then watch my favorite TV show.","tw":"Bere a makɔ sukuu da tenten akyi no, bere nyinaa migye m'ahome wɔ mpa so na afei mehwɛ TV so dwumadi a m'ani gye ho paa."},{"en":"After saving some money, he started selling sandals.","tw":"Bere a ɔkoraa sika bi so akyi no, ofii ase tɔn mpaboa."},{"en":"People lack skills to participate in business activities.","tw":"Nkorɔfoɔ nni nimdeɛ a wɔde bɛyɛ nnwuma ahodoɔ."},{"en":"The Northern region of Ghana is home to many refugees.","tw":"Ghana Atifi fam mantam no yɛ beae a aguanfo pii te."},{"en":"Schools are usually allocated funds during the beginning of the financial year.","tw":"wɔtaa kyekyɛ sika wɔ sukuu ahodoɔ mu wɔ sikasɛm afe no mfiase."},{"en":"Despite apologizing for not attending the meeting, he sought approval from the committee to use the funds for improving service delivery.","tw":"Ɛmfa ho sɛ ɔpaa kyɛw sɛ wankɔ nhyiam no, ɔhwehwɛɛ kwan fii boayikuw no hɔ sɛ wɔmfa sika no nni dwuma mfa mma ɔsom adwuma no atu mpɔn."},{"en":"The Ministry of Education and Sports will work hand in hand with agencies to train teachers about professional training and development opportunities","tw":"Asoɛeɛ a ɛhwɛ nwomasua ne Agodie so nsɛm no ne nwumakuo ahodoɔ bɛnya nkitahodie ahodoɔ apɛ nteteeɛ papa de ama akyerɛkyerɛfoɔ afa wɔn ankasa nteteeɛ ne wɔn mpuntuo ho."},{"en":"It will lift the economic growth of the country.","tw":"Ɛbɛma ɔman no mpuntuo akɔ soro."},{"en":"Always wear your mask when you go into a public space","tw":"Bere nyinaa hyɛ wo akatawia bere a worekɔ ɔmanfo beae no"},{"en":"I do not like to be part of the mass vaccination.","tw":"M'ani nnye ho sɛ mɛka nnuru a wɔde bɔ nkurɔfo ho ban kɛse no ho."},{"en":"People need a place to rerax, enjoy and get fresh air.","tw":"Nkorɔfoɔ hia beaeɛ a wɔde bɛgye wɔn ahome, agye wɔn ani na wɔanya mframa pa."},{"en":"The body was of a middle-aged female adult.","tw":"Naamu no yɛ ɔbea panyin bi a wadi mfe mfinimfini de."},{"en":"Low pay scales and wages has led to corruption among police officers.","tw":"Akatua nsenia ne akatua a ɛba fam no ama adifudepɛ aba polisifoɔ mu."},{"en":"In order to giving room to more learning breakoff periods shouldn't be lengthy.","tw":"Sɛnea ɛbɛyɛ a wɔbɛma kwan ama adesua pii no, ɛnsɛ sɛ ahomegye bere yɛ tenten."},{"en":"It looks at breeds of animals, their resistance to diseases and the environment.","tw":"Ɛhwɛ mmoa ahorow, sɛnea wɔko tia nyarewa ne nneɛma a atwa wɔn ho ahyia."},{"en":"Another farmer added that seeds are being used to make breakfast recipes .","tw":"Okuafo foforo de kaa ho sɛ wɔde aba reyɛ anɔpaduan ho nyansahyɛ ahorow"},{"en":"How is a petition written, asking about the process and structure of drafting a petition.","tw":"Ɔkwan bɛn so na wɔkyerɛw adesrɛ krataa, bisa ɔkwan ne nhyehyɛe a wɔfa so kyerɛw adesrɛ krataa."},{"en":"No business person ever wants to make losses.","tw":"Oguadifo biara mpɛ sɛ ɔhwere ade da."},{"en":"The community is derighted to have such an opportunity.","tw":"Mpɔtam hɔfo ani agye sɛ wɔanya hokwan a ɛte saa."},{"en":"Before it becomes law the president has to sign on it.","tw":"Ansa na ɛbɛyɛ mmara no ɛsɛ sɛ ɔmampanyin no de ne nsa hyɛ ase."},{"en":"The public should join the effort in controlling diseases.","tw":"Ɛsɛ sɛ ɔmanfo de wɔn ho hyɛ mmɔdenbɔ no mu de siw nyarewa ano."},{"en":"The case files are missing from the court.","tw":"Asɛm no ho nkrataa no nni asɛnnibea hɔ."},{"en":"People were complaining about water shortage in that area.","tw":"Na nkorɔfoɔ renwiinwii wɔ nsuo a asa wɔ mpɔtam hɔ."},{"en":"People do not use protection when engaging in sex.","tw":"Nkorɔfoɔ mmɔ wɔn ho ban sɛ wɔreyɛ ɔbarima ne ɔbaa nna a."},{"en":"It's always good to do want you want.","tw":"Ɛyɛ papa berɛ nyinaa sɛ wobɛyɛ nea w'ani gye ho."},{"en":"The church has helped people understand the values of Christians faith.","tw":"Asɔre no aboa nkurɔfo ma wɔate Kristofo gyidi gyinapɛn ahorow ase."},{"en":"By facilitating trade and connectivity, the bridge will contribute to the economic development of the area and enhance trade with neighboring countries.","tw":"Ɛdenam aguadi ne nkitahodi a ɛbɛma ayɛ mmerɛw so no, abɔntenban no bɛboa ma mpɔtam hɔ sikasɛm anya nkɔso na ama aguadi a wɔne aman a ɛbemmɛn no di no anya nkɔso."},{"en":"The order of opening of a police post has to come from the police headquarters.","tw":"Ɛsɛ sɛ ahyɛde a wɔde bebue polisifo adwumayɛbea no fi polisifo adwumayɛbea ti hɔ."},{"en":"After 1896 protection was extended to northern areas whose trade with the coast had been controlled by Ashanti.","tw":"Ɛwɔ afe apem ahanwɔtwe ne aduokron nsia (1896) akyire no wɔtrɛɛ ahobammɔ mu kɔɔ atifi fam mmeae a na Asante na odi wɔn aguadi ne mpoano no so"},{"en":"There are still land conflicts among people in the rural areas.","tw":"Nsase ho apereperedie binom da so ara wɔ nnipa a wɔwɔ nkuro nketewa mu no ntam."},{"en":"The election between the two candidates was very tight.","tw":"Abatoɔ a ɛkɔɔ so wɔ saa nnipa mmienu no ntam no mu yɛɛ den pa ara"},{"en":"The tax will also be charged on the sale of goods like alcohol.","tw":"Wɔbɛgye toɔ no nso wɔ nneɛma te sɛ nsa a wɔtɔn ho."},{"en":"A football match has ereven players from both sides.","tw":"Bɔɔlbɔ akansie wɔ bɔɔlɔbɔfoɔ du-baako wɔ afa ne afa."},{"en":"Criminals who want to take advantage of the lockdown will be punished.","tw":"Wɔbɛtwe nsɛmmɔnedifoɔ a wɔpɛ sɛ wɔde lockdown no di dwuma no aso"},{"en":"Let us applaud his contribution to the country","tw":"Momma yɛmmɔ yɛn nsam mma mmɔden a wabɔ ama ɔman no"},{"en":"Registration to join the group is at fifty thousandcedis only.","tw":"dinkyerɛw a wɔde bɛka kuw no ho no yɛ mpem aduonumcedis nkutoo."},{"en":"School heads are advised against excessive consumption of alcohol.","tw":"wotu sukuu mpanyimfo fo sɛ ɛnsɛ sɛ wɔnom nsa dodo."},{"en":"There was a new COVID-19 death almost everyday in mid September.","tw":"Yɛwɔ COVID-19 wuo foforɔ daa wɔ Ɛbɔ mfinimfini mu."},{"en":"He sued his opponent in court over cheating the elections.","tw":"Ɔde nea ɔne no reko no kɔɔ asɛnnibea wɔ asɛnnibea sɛ ɔdaadaa abatow no."},{"en":"The most loved sport in this country is football.","tw":"Agodie a obiara pɛ pa ara wɔ ɔman yi mu ne bɔɔlobɔ."},{"en":"These roads create a vital role in promoting development in rural communities.","tw":"Saa akwan yino di akotene pa ara wɔ nkuro nketewa no mpuntuo mu."},{"en":"Not all new seeds on market are resistant to pests and diseases.","tw":"Ɛnyɛ aba foforo a ɛwɔ gua so nyinaa na ɛko tia mmoawa ne nyarewa."},{"en":"People should follow the law and respect it.","tw":"Ɛsɛ sɛ nkorɔfoɔ di mmara no akyi na wɔbu no."},{"en":"You have the power to change the undesirable things around you, emphasizing personal agency and empowerment.","tw":"Wowɔ tumi so sɛ wobɛsesa nneɛma a w'ani nnye ho a atwa wo ho ahyia no, resi ankorɛankorɛ adwumakuo ne nkuranhyɛ so."},{"en":"It is difficult for people to access health services at night.","tw":"Ɛyɛ den ma nkurɔfo sɛ wobenya apomuden ho nhyehyɛe anadwo."},{"en":"High levels of poverty lead to an increased school dropout rate.","tw":"Ohia a ɛkɔ soro ma nnipa dodow a wogyae sukuukɔ no kɔ soro."},{"en":"The hospital management needs to have a motivated workforce.","tw":"Ɛsɛ sɛ mapnimfoɔ a wɔda ayaresabea no ano no nya adwumayɛfoɔ a wɔwɔ ɔpɛ pa."},{"en":"If children attend school then there will be no child labour.","tw":"Sɛ mmofra kɔ sukuu a ɛnde mmofra adwumayɛ biara nni hɔ."},{"en":"Its a community's responsibility to raise a child.","tw":"Ɛyɛ nnipa a wɔwɔ mpɔtam no nyinaa asɛyɛde sɛ wɔbɛtete abofra."},{"en":"People have lost their property in the area.","tw":"Nkorɔfoɔ ahwere wɔn agyapadeɛ wɔ beaeɛ hɔ."},{"en":"The community leaders, who unfairly distributed health funds, will redistribute them in the next financial year based on the requests from health units for more drugs and better service delivery.","tw":"Mpɔtam hɔ akannifo a wɔkyekyɛɛ akwahosan ho sika wɔ ɔkwan a ɛnteɛ so no bɛsan akyekyɛ wɔ sikasɛm afe a edi hɔ no mu a egyina adesrɛ a efi akwahosan asoɛe ahorow hɔ sɛ wɔmfa nnuru pii ne ɔsom adwuma pa a wɔde bɛma no so."},{"en":"Cocoa planting will generate income to the locals.","tw":"Koko dua a wobedua no bɛma ɛhɔfo anya sika."},{"en":"I won't make it for the end of year party.","tw":"Merentumi nkɔ afe awiei apontow ase."},{"en":"In this context, officials, parents, and headteachers should all share the blame for the overall decline in academic achievements","tw":"Wɔ saa tebea yi mu no, ɛsɛ sɛ mpanyimfo, awofo, ne akyerɛkyerɛfo mpanyimfo nyinaa kyɛ asodi a ɛfa adesua mu nkɔso a ɛso atew nyinaa ho."},{"en":"Ebola is a viral disease that can easily spread.","tw":"Ebola yɛ ɔyare bi a ekunkum nnipa a ebetumi atrɛw ntɛmntɛm."},{"en":"Leaders need to recognize and respect fellow leaders.","tw":"Ɛsɛ sɛ akannifoɔ hu wɔn mfɛfo akannifoɔ na wobu wɔn."},{"en":"There is a lot that goes on in the government that we do not know about.","tw":"Nneɛma pii wɔ hɔ a ɛkɔ so wɔ aban no mu a yɛnnim ho hwee."},{"en":"Various projects have come up to educate young people about reproductive health challenges.","tw":"Wɔde nnwuma bebree agugu akwan mu a ɛreboa akyerɛkyerɛ mmabunu afa awoɔ mu haw ahodoɔ ho."},{"en":"The council needs data about the possible new sources of revenue.","tw":"Agyinatukuo no hia data a ɛfa sika foforɔ a ɛbɛtumi aba no ho."},{"en":"Religious leaders urged government to open churches during the lockdown.","tw":"nyamesom akannifo hyɛɛ aban sɛ onbue asɔredan ahorow wɔ bere a wɔatoto mu no."},{"en":"The district will include youth development projects in the next year's budget.","tw":"Sikasɛm ho ntotoeɛ a wɔbɛyɛ no afe a yɛbɛsi mu no, mansini no de dwumadie ahodoɔ a ɛbɛboa mmabunu nso bɛka ho"},{"en":"In Ghana, forty-one percent of people live in poverty.","tw":"Wɔ Ghana no, nnipa ɔha mu aduanan biako di hia."},{"en":"It is his job to monitor and supervise the ongoing project.","tw":"Ɛyɛ n'adwuma sɛ ɔbɛhwɛ adwuma a ɛrekɔ so no so na wahwɛ so."},{"en":"The match ended in a draw. Fans are cheering their respective teams.","tw":"Wɔde akansie no baa awieɛ wɔ 'drɔɔ' mu. Akyitaafoɔ no rebɔ wɔn akuo biara ose."},{"en":"The journalists reported about the car accident, informing the public about the incident.","tw":"Nsɛntwerɛfoɔ no bɔɔ amaneɛ faa kaa akwanhyia no ho, wɔreka deɛ ɛsiiɛ no ho asɛm akyerɛ ɔmanfoɔ no."},{"en":"People were injured in the fight over land.","tw":"Wɔpiraa nkorɔfoɔ wɔ asase no ho ko no mu."},{"en":"Industries employ heavy machines that consume a lot of electricity.","tw":"Nnwumakuw de mfiri a emu yɛ duru a ɛde anyinam ahoɔden pii di dwuma."},{"en":"Most of the land has been left bare.","tw":"Wɔagyaw asase no fã kɛse no ara a ato hɔ kwa."},{"en":"These days you need to bribe someone so as to get a government job.","tw":"Nna yinom mu deɛ, gye sɛ woma obi ademudeɛ ansa na wo nsa aka aban adwuma."},{"en":"The Ghana museum has exhibits of traditional culture.","tw":"Ghana tete nneɛma akorae no wɔ amammerɛ amammerɛ ho ɔyɛkyerɛ."},{"en":"Ninety-five people graduated from the Kofi Annan International Peacekeeping Training Center","tw":"Nnipa aduɔkron anum na wɔwiee Kofi Annan Amanaman Ntam Asomdwoeɛ Nteteeɛ Beaeɛ"},{"en":"Ramadhan is considered to be the holiest period on the Islam calendar.","tw":"wobu ramadhan sɛ ɛyɛ bere kronkron sen biara wɔ Islam kalenda so."},{"en":"The bridge will reduce the number of accidents.","tw":"Bridge no bɛma akwanhyia dodow so atew."},{"en":"The additional classrooms shall accommodate the increasing number of children in school.","tw":"Adesuadan a wɔde bɛka ho no bɛma mmofra dodow a wɔrekɔ sukuu no akɔ mu."},{"en":"He was arrested and taken to prison until the debt was paid.","tw":"Wɔkyeree no de no kɔɔ afiase kosii sɛ wotuaa ɛka no."},{"en":"The project generally aims at creating a market for farm products and gives farmers a number of benefits in the Nandom districts","tw":"Dwumadie no botaeɛ ne sɛ ɛbɛma wɔanya dwa ama kuayɛ nnoɔma na ɛma akuafoɔ nya mfasoɔ dodoɔ bi wɔ Nandom mansini mu."},{"en":"A big number of refugees enter the country every year.","tw":"Nnipa a wɔfiri aman foforɔ so dwane bɛhinta wɔ Ghana ɛnam ahotɔ wo pɛ nti no wɔba ɔman no mu afe biara no yɛ bebree."},{"en":"The highest number of deaths in a single day was recorded yesterday.","tw":"Ɛda nnipa dodoɔ ahwere wɔn nkwa pa ara ne nnipa dodoɔ a wɔwuu nnora no."},{"en":"He spent half of the budget on his personal interests.","tw":"Ɔde sikasɛm nhyehyɛe no fã yɛɛ n'ankasa nneɛma a n'ani gye ho."},{"en":"He was arrested because of abuse of office.","tw":"Wɔkyeree no esiane dibea a ɔde dii dwuma ɔkwammɔne so nti."},{"en":"The period of Nkrumah's active political involvement has been described as the \"golden age of high pan-African ambitions\"; the continent had experienced rising nationalist movements and decolonization by most European colonial powers.","tw":"Wɔaka berɛ a Nkrumah de ne ho hyɛɛ amanyɔsɛm mu denneennen no ho asɛm sɛ \"pan-Afrika anisoadehunu kɛseɛ sika kɔkɔɔ berɛ\"; na asasepɔn no anya ɔmampɛ akuo a ɛrekɔ soro ne Europefoɔ nkoasom aman dodoɔ no ara a wɔayi afiri nkoasom mu."},{"en":"Investigations are instrumental in coming up with a final judgement.","tw":"Nhwehwɛmu boa kɛseɛ ma wɔde atemmuo a etwa toɔ ba."},{"en":"Through culture we get an insight on where we come from.","tw":"Yɛnam amammerɛ so nya nhunu fa baabi a yɛfiri."},{"en":"The vaccine is safe and not harmful and United Nations experts can confirm that too.","tw":"Vaccine no yɛ nea asiane biara nni ho na ɛnyɛ nea epira na Amanaman Nkabom no abenfo betumi asi ɛno nso so dua."},{"en":"The voting process was free and fair to the concerned parties.","tw":"Na abatoɔ nhyehyɛeɛ no deɛ ɛmu da hɔ ma amanyɔkuo a wɔreto no."},{"en":"The district enacted laws that provide how stray animals should be treated.","tw":"Ɔmantam no hyehyɛɛ mmara ahorow a ɛkyerɛ sɛnea ɛsɛ sɛ wɔne mmoa a wɔayera di."},{"en":"The district lacks funds to implement programs and solve challenges faced by people.","tw":"Mansini no sika a wɔbɛtumi de ayɛ nnwuma asosɔ ɔhaw ahodoɔ a ne manfoɔ rehyia no ano."},{"en":"He was arrested in the middle of the night during the curfew time.","tw":"Wɔkyeree no anadwo fa wɔ bere a wɔahyɛ sɛ wɔmfa nkɔ fie no mu."},{"en":"The structures are bound to collapse in case of heavy rains.","tw":"Akyinnye biara nni ho sɛ adan no bebubu sɛ osu kɛse tɔ a."},{"en":"The teacher said it was awkward to share toilets with students.","tw":"Ɔkyerɛkyerɛfo no kae sɛ na ɛyɛ fɛre sɛ wɔne sukuufo bɛkyɛ tiafi."},{"en":"It's important to understand project benefits before implementation.","tw":"Ɛho hia sɛ yɛte mfasoɔ a ɛwɔ adwuma bi so ase ansa na yɛafiri aseɛ de adi dwuma."},{"en":"Ask the secretary, she must have all the minutes for the meeting.","tw":"Bisa twerɛtwerɛfoɔ no, ɛsɛ sɛ onya nhyiam no simma nyinaa"},{"en":"The community should continuously fight against gender based violence.","tw":"Ɛsɛ sɛ mpɔtam hɔfo kɔ so ko tia basabasayɛ a egyina ɔbarima ne ɔbea nna so."},{"en":"The money should be used to solve our challenges, addressing our current difficulties.","tw":"sika no ɛsɛ sɛ yɛde boa siesie yɛn haw, ɛnhwɛ yɛn mprɛmprɛn haw."},{"en":"The workers are not satisfied with the working conditions, leading to discontentment.","tw":"Adwumayɛfoɔ no ani annye adwuma nhyehyɛeɛ no ho na amma ansɔ wɔn ani."},{"en":"The youths took the cut timber as evidence of the illegal act.","tw":"Mmabun no faa nnua a wɔatwitwa no sɛ adeyɛ a mmara mma ho kwan no ho adanse."},{"en":"Flu is considered as one of the communicable killer diseases,","tw":"Wosusu sɛ Flu yɛ ɛsanyare ɛfa nframa mu ku nipa"},{"en":"Volunteers have come up to provide basic needs to the refugees.","tw":"Atuhoamafoɔ binom aka wɔn ho abom sɛ wɔde nneɛma atitire binom a atubrafoɔ no bɛhia no bɛma wɔn."},{"en":"Student leaders should show a good example in all that they do.","tw":"Ɛsɛ sɛ asuafoɔ akannifoɔ kyerɛ nhwɛsoɔ pa wɔ deɛ wɔyɛ nyinaa mu."},{"en":"The minister advised Christians to have faith in God.","tw":"Ɔsoafoɔ no tuu akristofoɔ fo sɛ wɔnya gyidie wɔ Nyankopɔn mu."},{"en":"Most coronavirus cases in Ghana are among truck drivers.","tw":"Nnipa dodow no ara a wɔanya korona nsanyare wɔ Ghana no ka lɔrekafo ho."},{"en":"Graduates are likely to get jobs they never trained for.","tw":"Wɔn a wɔawie sukuu no betumi anya adwuma a wɔansua ho."},{"en":"The team failed to accept the match results.","tw":"Ɛkuo no annye deɛ ɛbaa akansie no mu no anto mu."},{"en":"Having engaged in economic activities, women are now financially independent.","tw":"Esiane sɛ mmea de wɔn ho ahyɛ sikasɛm mu nti, seesei wɔn ho nni wɔn ho so wɔ sikasɛm mu."},{"en":"A discontented parent said failure to pay three thousandcedis got her daughter sent home.","tw":"Awofoɔ bi a ne bo nnwo ne ho kaa sɛ tua a wantumi antua Ghana sika sidi mpem mmiɛnsa na ɛde ne ba baa baa efie."},{"en":"Invited members will receive a daily allowance and thus the done deal","tw":"Nnipa a wɔato nsa afrɛ wɔn no bɛnya da biara da sika na wɔnam saayɛ so ayɛ apam a wɔayɛ."},{"en":"The president advised people to divert from cash crops to food crops.","tw":"Ɔmanpanin no tuu nkorɔfoɔ fo sɛ wɔnsesa mfiri sika nnuaba so nkɔ nnuane nnuaba."},{"en":"Most cyclists have little knowledge of road safety laws.","tw":"Wɔn a wɔde sakre tu kwan no mu dodow no ara nni nimdeɛ pii wɔ akwan so ahobammɔ ho mmara ho."},{"en":"A list of Ghanaian music artists has joined politics.","tw":"Ghana adwontofoɔ bebere de wɔn ho afra amanyɔsɛm mu."},{"en":"The municipal council will relocate the municipality offices.","tw":"Mansini no kansele no de mansini no ɔfese ahodoɔ no kɔ baabi foforɔ."},{"en":"The thieves took the gun from the policeman after killing him.","tw":"Akorɔmfo no gyee tuo no fii polisini no nsam bere a wokum no wiei no."},{"en":"People in the rural areas prefer to get water from streams because the boreholes are far away from them.","tw":"Nkorɔfoɔ a wɔwɔ nkuraase no pɛ sɛ wɔsa nsuo wɔ nsutene mu ɛfiri sɛ wɔn nsuo a wɔatu ama wɔn no mu wa firi wɔn nkyɛn."},{"en":"The Junior Africa Golf Challenge hosted in South Africa was won by Keisha Witshire.","tw":"Keisha Witshire na ɔdii nkunim wɔ Junior Afrika Golf akansie a wɔsii no wɔ South Africa no mu."},{"en":"Failure to fulfil people's request could initiate bad doings.","tw":"Sɛ obi anyɛ nea nkurɔfo bisae no a, ebetumi ama wayɛ bɔne."},{"en":"There are no garbage trucks to collect the garbage from the business centers.","tw":"Kaa a ɛsesa nwura biara nni hɔ a wɔde bɛsesa nwura afiri mmeaeɛ ahodoɔ a wɔdi dwa no."},{"en":"Due to shortage of funds, they have failed to implement anything.","tw":"Esiane sika a wonnya nti, wɔantumi amfa biribiara anni dwuma."},{"en":"The training center equips youth with vocational skills.","tw":"Nteteebea no ma mmabun nya adwumayɛ ho nimdeɛ."},{"en":"Maintaining social distance is one way of preventing the transmission of the coronavirus and protecting public health.","tw":"Nnipa ntam kwan a wɔbɛkɔ so akura mu no yɛ ɔkwan baako a wɔfa so siw coronavirus yareɛ no ano na wɔbɔ ɔmanfoɔ akwahosan no ho ban."},{"en":"People who go to the disco enjoy dancing.","tw":"Nnipa a wɔkɔ disko no ani gye asa ho."},{"en":"Keeping girls in school helps prevent early pregnancies.","tw":"Mmabaa a wɔde wɔn kɔ sukuu no boa ma wosi nyinsɛn ntɛm ano."},{"en":"School children are commonly kidnapped on their way back home from school.","tw":"Wɔtaa kyere sukuu mmɔfra sie bere a wofiri sukuu resan akɔ fie no."},{"en":"By the mid-18th century, Ashanti was a highly organized state.","tw":"Eduu afeha a ɛto so 18 mfinimfini no, na Ashanti yɛ ɔman a wɔahyehyɛ no yiye."},{"en":"Different campaigns are being run to create health awareness.","tw":"Wɔreyɛ ɔsatu ahorow de ama wɔanya akwahosan ho nimdeɛ."},{"en":"All witnesses, in this case, have to testify before the court.","tw":"Adansefo nyinaa, wɔ asɛm yi mu no, ɛsɛ sɛ wodi adanse wɔ asɛnnibea no anim."},{"en":"Health workers have been named heroes for subjecting individuals to handwashing and screening.","tw":"Wɔabɔ akwahosan ho adwumayɛfo din sɛ abran esiane sɛ wɔhohoro ankorankoro nsa na wɔhwehwɛ wɔn mu nti."},{"en":"The decisions made by the leaders is for the benefit of the people.","tw":"Gyinaesi ahorow a akannifo no si no yɛ nea ɛbɛboa ɔmanfo."},{"en":"In everything you do, your health comes first","tw":"Wɔ biribiara a woyɛ mu no, w'apomuden di kan."},{"en":"Latrines are advocated for in the effort to improve hygiene.","tw":"Wɔkamfo tiafi a wɔde ma wɔ mmɔden a wɔbɔ sɛ wɔbɛma ahoteɛ atu mpɔn no mu."},{"en":"This year's festive season may not be as exciting as usual since public gatherings have been banned","tw":"Ebia afe yi afahyɛ berɛ no renyɛ anigyeɛ sɛdeɛ wɔtaa yɛ no ɛfiri sɛ wɔabra badwam nhyiam ahodoɔ."},{"en":"Several health workers have lost their lives due to the deadly pandemic.","tw":"akwahosan ho adwumayɛfo pii ahwere wɔn nkwa esiane ɔyaredɔm a edi awu no nti."},{"en":"Service centres will ease accessibility for the local government officials.","tw":"ɔsom mmeae bɛma mpɔtam hɔ aban mpanyimfo no anya kwan akɔ hɔ."},{"en":"For children to become great men and women, they have to be raised the right way.","tw":"Sɛ mmofra betumi abɛyɛ mmarima pa ne mmea pa a wɔbɔ moɔden a, ɛsɛ sɛ wɔtete wɔn wɔ ɔkwan pa"},{"en":"Mothers need to be fed well throughout their pregnancy to be healthy.","tw":"Ɛsɛ sɛ wɔma ɛnanom aduan pa wɔ wɔn nyinsɛn aber mu na ama wɔanya apɔwmuden."},{"en":"Businesses requested for tax holidays from the revenue authority.","tw":"Nnwumakuo bisaa towtua akwamma fii sikakorabea hɔ."},{"en":"Appeals are decided by paners of three judges.","tw":"Atemmufo baasa na wosi asɛm a wɔde kɔdan asɛnnibea no ho gyinae."},{"en":"People need access to better health services in the area.","tw":"Nkorɔfoɔ hia apɔmuden nhyehyɛeɛ pa wɔ saa mpɔtam hɔ."},{"en":"The road heading to the district headquarters was swept away by the floods.","tw":"Nsuyiri no faa ɔkwan a ɛkɔ ɔmantam adwumayɛbea ti no so."},{"en":"Only two members of parliament attended the meeting.","tw":"Mmarahyɛ bagua no mufo baanu pɛ na wɔbaa nhyiam no ase."},{"en":"The organization has provided equipment to start the process.","tw":"Ahyehyɛde no de nnwinnade a wɔde befi adwuma no ase ama."},{"en":"The total number of cases of coronavirus have reduced steadily in the past three days","tw":"Nnipa dodow a wɔanya coronavirus nyinaa so atew nkakrankakra wɔ nnansa a atwam no mu"},{"en":"The ministry will not tolerate any form of strikes from the teachers.","tw":"Asoeɛ no nsosɔ atuateɛ basabasa biara a ɛbɛfiri akyerɛkyerɛfoɔ hɔ aba so"},{"en":"Once given a transfer, the teacher has no other option but to comply.","tw":"Sɛ wɔma ɔkyerɛkyerɛfo no kwan sɛ ɔbɛkɔ baabi foforo pɛ a, onni ɔkwan foforo biara a ɔbɛfa so gye di a obedi so."},{"en":"People lost their property in the process of constructing the health unit.","tw":"Nkorɔfoɔ hweree wɔn agyapadeɛ berɛ a na wɔresi apɔmuden beaeɛ dan no."},{"en":"People have turned their hope in the District to create relief for them.","tw":"Nkorɔfoɔ adane wɔn anidasoɔ akɔsi Mansini so sɛ wɔbɛma wɔn ahomegyeɛ."},{"en":"He was arrested for carrying two passengers on his motorcycle.","tw":"Wɔkyeree no sɛ ɔde akwantufoɔ mmienu traa ne moto so."},{"en":"The weed destroyed the tree they use for shade.","tw":"Nwura no sɛee dua a wɔde yɛ sunsuma no."},{"en":"One rebel tried to sell a gun at the border.","tw":"Otuatewfo bi bɔɔ mmɔden sɛ ɔbɛtɔn tuo wɔ ɔhye no so."},{"en":"He was attacked by thieves in the night.","tw":"Akorɔmfoɔ to hyɛɛ no so anadwo."},{"en":"How do we stop students from copying in an online exam?","tw":"Yɛbɛyɛ dɛn asiw asuafo kwan sɛ wɔnyɛ mfonini wɔ intanɛt so sɔhwɛ bi mu?"},{"en":"Excommunication is the biggest punishment a church can give to a guilty Christian.","tw":"Sɛ wohu sɛ Kristoni bi nni fɔ a, wobetumi ayi no afi asafo no mu."},{"en":"The priority should be to finish your degree program.","tw":"Ɛsɛ sɛ nea ɛho hia titiriw ne sɛ wubewie wo abodin krataa nhyehyɛe no."},{"en":"Policies should be put in place to control the number of children being born.","tw":"Ɛsɛ sɛ wɔde nhyehyɛe ahodoɔ sisi hɔ de hwɛ mmofra dodoɔ a wɔwo wɔn so."},{"en":"The district has devised new plans and strategies for the people.","tw":"Ɔmansin no ayɛ nhyehyɛe ne akwan foforo ama ɔmanfo."},{"en":"In case of lack of adequate funds, one is free to borrow.","tw":"Sɛ obi nni sika a ɛfata a, ɔde ne ho sɛ ɔbɛbɔ bosea."},{"en":"People should learn better farming techniques to improve agricultural productivity.","tw":"Ɛsɛ sɛ nkorɔfoɔ sua kuayɛ ho akwan a ɛyɛ na ama kuayɛ mu nnɔbae atu mpɔn."},{"en":"People must be informed and updated about the dangers of non-communicable diseases.","tw":"Ɛsɛ sɛ wɔbɔ nkorɔfoɔ amanneɛ na wɔma wɔn nsɛm foforɔ fa asiane a ɛwɔ nyarewa a ɛnyɛ yare mmoawa mu no ho."},{"en":"Money should not be the only reason for leaders to work hard.","tw":"Ɛnsɛ sɛ sika nkutoo na ɛma akannifo yɛ adwumaden."},{"en":"Sick people should be taken to the hospital.","tw":"Ɛsɛ sɛ wɔde ayarefo kɔ ayaresabea."},{"en":"Lawrence is a trustworthy friend; he always keeps his promises and maintains confidentiality.","tw":"Lawrence yɛ adamfoɔ a wotumi de ho to no so; odi ne bɔhyɛ ahodoɔ so berɛ nyinaa na ɔkora kokoam nsɛm so."},{"en":"Mobilizing people is not a very easy task.","tw":"Nnipa a wɔbɛboaboa wɔn ano no nyɛ adwuma a ɛyɛ mmerɛw koraa."}];

  var direction = "en-tw";
  var history = [];
  try {
    var saved = localStorage.getItem("kasa-history");
    if (saved) history = JSON.parse(saved);
  } catch (e) {}

  var srcText   = document.getElementById("srcText");
  var srcTag    = document.getElementById("srcTag");
  var tgtTag    = document.getElementById("tgtTag");
  var resultBox = document.getElementById("resultBox");
  var resultBadge = document.getElementById("resultBadge");
  var translateBtn = document.getElementById("translateBtn");
  var swapBtn   = document.getElementById("swapBtn");
  var clearBtn  = document.getElementById("clearBtn");
  var copyBtn   = document.getElementById("copyBtn");
  var charCount = document.getElementById("charCount");
  var statusLine = document.getElementById("statusLine");
  var suggestWrap = document.getElementById("suggestWrap");
  var suggestList = document.getElementById("suggestList");
  var historySection = document.getElementById("historyRow") ? document.getElementById("historySection") : null;
  var historyRow = document.getElementById("historyRow");
  var tabsEl = document.getElementById("tabs");
  var gridEl = document.getElementById("phraseGrid");

  var lastResult = { text: "", verified: false };

  function norm(s){
    return (s || "").toLowerCase().trim().replace(/[.,!?;:"'’“”]/g, "").replace(/\s+/g, " ");
  }

  function flatEntries(){
    var out = [];
    Object.keys(PHRASEBOOK).forEach(function(cat){
      PHRASEBOOK[cat].forEach(function(e){ out.push(e); });
    });
    return out;
  }
  var ALL_ENTRIES = flatEntries();

  function exactPhraseMatch(text, dir){
    var n = norm(text);
    if (!n) return null;
    for (var i=0;i<ALL_ENTRIES.length;i++){
      var e = ALL_ENTRIES[i];
      var key = dir === "en-tw" ? e.en : e.tw;
      if (norm(key) === n) return e;
    }
    return null;
  }

  function fuzzyMatches(text, dir, limit){
    var n = norm(text);
    if (!n || n.length < 2) return [];
    var words = n.split(" ").filter(Boolean);
    var scored = ALL_ENTRIES.map(function(e){
      var key = norm(dir === "en-tw" ? e.en : e.tw);
      var score = 0;
      if (key.indexOf(n) !== -1 || n.indexOf(key) !== -1) score += 3;
      words.forEach(function(w){ if (w.length > 2 && key.indexOf(w) !== -1) score += 1; });
      return { e: e, score: score };
    }).filter(function(s){ return s.score > 0; });
    scored.sort(function(a,b){ return b.score - a.score; });
    return scored.slice(0, limit || 4).map(function(s){ return s.e; });
  }

  function corpusExactMatch(text, dir){
    var n = norm(text);
    if (!n) return null;
    for (var i = 0; i < CORPUS.length; i++){
      var c = CORPUS[i];
      var key = dir === "en-tw" ? c.en : c.tw;
      if (norm(key) === n) return c;
    }
    return null;
  }

  function corpusNearestMatch(text, dir){
    var n = norm(text);
    var words = n.split(" ").filter(function(w){ return w.length > 2; });
    if (!words.length) return null;
    var best = null, bestScore = 0;
    for (var i = 0; i < CORPUS.length; i++){
      var c = CORPUS[i];
      var key = norm(dir === "en-tw" ? c.en : c.tw);
      var keyWords = key.split(" ");
      var overlap = 0;
      words.forEach(function(w){ if (keyWords.indexOf(w) !== -1) overlap++; });
      var score = overlap / words.length;
      if (overlap >= 2 && score > bestScore){
        bestScore = score;
        best = c;
      }
    }
    return bestScore >= 0.6 ? best : null;
  }

  function updateTags(){
    if (direction === "en-tw"){
      srcTag.innerHTML = "<b>EN</b> English";
      tgtTag.innerHTML = "<b>TWI</b> Akan Twi";
      srcText.placeholder = "Type a word or phrase — try “thank you” or “where is the market?”";
    } else {
      srcTag.innerHTML = "<b>TWI</b> Akan Twi";
      tgtTag.innerHTML = "<b>EN</b> English";
      srcText.placeholder = "Kyerɛw asɛmfua bi — sɔ hwɛ “medaase”";
    }
  }

  function setStatus(msg, isError, showSpinner){
    statusLine.className = "status-line" + (isError ? " error" : "");
    statusLine.innerHTML = (showSpinner ? '<span class="spinner"></span>' : '') + (msg ? '<span>'+msg+'</span>' : '');
  }

  var BADGES = {
    verified: '<span class="badge verified">Verified phrase</span>',
    corpus:   '<span class="badge corpus">GhanaNLP corpus</span>',
    machine:  '<span class="badge machine">Machine translation</span>'
  };

  function renderResult(text, kind){
    lastResult = { text: text, kind: kind };
    if (!text){
      resultBox.className = "result-box empty";
      resultBox.textContent = "Your translation will appear here.";
      resultBadge.innerHTML = "";
      return;
    }
    resultBox.className = "result-box";
    resultBox.textContent = text;
    resultBadge.innerHTML = BADGES[kind] || "";
  }

  function renderSuggestions(text, dir){
    var matches = fuzzyMatches(text, dir, 4).filter(function(e){
      var key = dir === "en-tw" ? e.en : e.tw;
      return norm(key) !== norm(text);
    });
    if (!matches.length){ suggestWrap.style.display = "none"; return; }
    suggestWrap.style.display = "block";
    suggestList.innerHTML = "";
    matches.forEach(function(e){
      var chip = document.createElement("button");
      chip.type = "button";
      chip.className = "suggest-chip";
      var left = dir === "en-tw" ? e.en : e.tw;
      var right = dir === "en-tw" ? e.tw : e.en;
      chip.innerHTML = "<b>" + escapeHtml(left) + "</b><span class='arrow'>→</span>" + escapeHtml(right);
      chip.addEventListener("click", function(){
        srcText.value = left;
        updateCharCount();
        doTranslate();
      });
      suggestList.appendChild(chip);
    });
  }

  function escapeHtml(s){
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  function updateCharCount(){
    charCount.textContent = srcText.value.length;
  }

  function pushHistory(srcVal, tgtVal, dir){
    history.unshift({ src: srcVal, tgt: tgtVal, dir: dir });
    history = history.slice(0, 10);
    try { localStorage.setItem("kasa-history", JSON.stringify(history)); } catch(e){}
    renderHistory();
  }

  function renderHistory(){
    if (!history.length){ historySection.style.display = "none"; return; }
    historySection.style.display = "block";
    historyRow.innerHTML = "";
    history.forEach(function(h){
      var chip = document.createElement("button");
      chip.type = "button";
      chip.className = "history-chip";
      chip.innerHTML = '<div class="h-src">' + escapeHtml(h.src) + '</div><div class="h-tgt">' + escapeHtml(h.tgt) + '</div>';
      chip.addEventListener("click", function(){
        direction = h.dir;
        updateTags();
        srcText.value = h.src;
        updateCharCount();
        doTranslate();
      });
      historyRow.appendChild(chip);
    });
  }

  function callMyMemory(text, dir){
    var pair = dir === "en-tw" ? "en|tw" : "tw|en";
    var url = "https://api.mymemory.translated.net/get?q=" + encodeURIComponent(text) + "&langpair=" + pair;
    var controller = new AbortController();
    var timeout = setTimeout(function(){ controller.abort(); }, 9000);
    return fetch(url, { signal: controller.signal })
      .then(function(res){
        clearTimeout(timeout);
        if (!res.ok) throw new Error("Service returned " + res.status);
        return res.json();
      })
      .then(function(data){
        if (data && data.responseData && data.responseData.translatedText){
          return data.responseData.translatedText;
        }
        throw new Error("No translation returned");
      });
  }

  function doTranslate(){
    var text = srcText.value.trim();
    suggestWrap.style.display = "none";
    if (!text){
      setStatus("Type something to translate, or tap a phrase below.", false, false);
      renderResult("", null);
      return;
    }

    var exact = exactPhraseMatch(text, direction);
    if (exact){
      var out = direction === "en-tw" ? exact.tw : exact.en;
      renderResult(out, "verified");
      setStatus(exact.note ? "Note: " + exact.note : "Matched against the hand-checked phrasebook.", false, false);
      pushHistory(text, out, direction);
      return;
    }

    var corpusExact = corpusExactMatch(text, direction);
    if (corpusExact){
      var cOut = direction === "en-tw" ? corpusExact.tw : corpusExact.en;
      renderResult(cOut, "corpus");
      setStatus("Exact match in the GhanaNLP sentence corpus (human-translated).", false, false);
      pushHistory(text, cOut, direction);
      return;
    }
    var corpusNear = corpusNearestMatch(text, direction);
    if (corpusNear){
      var cNearOut = direction === "en-tw" ? corpusNear.tw : corpusNear.en;
      var cNearSrc = direction === "en-tw" ? corpusNear.en : corpusNear.tw;
      renderResult(cNearOut, "corpus");
      setStatus("Closest sentence in the GhanaNLP corpus: “" + cNearSrc + "” — not an exact match for your text, so check it fits.", false, false);
      pushHistory(text, cNearOut, direction);
      return;
    }

    translateBtn.disabled = true;
    setStatus("Translating…", false, true);

    callMyMemory(text, direction).then(function(translated){
      renderResult(translated, "machine");
      setStatus("Machine translation via MyMemory — Twi is low-resource, so treat this as a starting point.", false, false);
      renderSuggestions(text, direction);
      pushHistory(text, translated, direction);
    }).catch(function(err){
      var fuzzy = fuzzyMatches(text, direction, 1)[0];
      if (fuzzy){
        var val = direction === "en-tw" ? fuzzy.tw : fuzzy.en;
        renderResult(val, "verified");
        setStatus("Couldn't reach the translation service — showing the closest phrasebook match instead.", true, false);
      } else {
        renderResult("", null);
        setStatus("Couldn't reach the translation service and no phrasebook or corpus match was found. Check your connection and try again.", true, false);
      }
    }).finally(function(){
      translateBtn.disabled = false;
    });
  }

  var categories = Object.keys(PHRASEBOOK);
  var activeCat = categories[0];

  function renderTabs(){
    tabsEl.innerHTML = "";
    categories.forEach(function(cat){
      var b = document.createElement("button");
      b.type = "button";
      b.className = "tab" + (cat === activeCat ? " active" : "");
      b.textContent = cat;
      b.addEventListener("click", function(){
        activeCat = cat;
        renderTabs();
        renderGrid();
      });
      tabsEl.appendChild(b);
    });
  }

  function renderGrid(){
    gridEl.innerHTML = "";
    PHRASEBOOK[activeCat].forEach(function(e){
      var card = document.createElement("button");
      card.type = "button";
      card.className = "phrase-card";
      card.innerHTML =
        '<div class="phrase-en">' + escapeHtml(e.en) + '</div>' +
        '<div class="phrase-tw">' + escapeHtml(e.tw) + '</div>' +
        (e.note ? '<div class="phrase-note">' + escapeHtml(e.note) + '</div>' : '');
      card.addEventListener("click", function(){
        direction = "en-tw";
        updateTags();
        srcText.value = e.en;
        updateCharCount();
        renderResult(e.tw, "verified");
        setStatus(e.note ? "Note: " + e.note : "Loaded from the phrasebook.", false, false);
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
      gridEl.appendChild(card);
    });
  }

  translateBtn.addEventListener("click", doTranslate);

  srcText.addEventListener("input", updateCharCount);
  srcText.addEventListener("keydown", function(ev){
    if (ev.key === "Enter" && !ev.shiftKey){
      ev.preventDefault();
      doTranslate();
    }
  });

  clearBtn.addEventListener("click", function(){
    srcText.value = "";
    updateCharCount();
    renderResult("", null);
    setStatus("", false, false);
    suggestWrap.style.display = "none";
    srcText.focus();
  });

  swapBtn.addEventListener("click", function(){
    direction = direction === "en-tw" ? "tw-en" : "en-tw";
    updateTags();
    swapBtn.classList.toggle("spin");
    var newSrc = lastResult.text || "";
    srcText.value = newSrc;
    updateCharCount();
    renderResult("", null);
    setStatus("", false, false);
    suggestWrap.style.display = "none";
    if (newSrc) doTranslate();
  });

  copyBtn.addEventListener("click", function(){
    if (!lastResult.text) return;
    var done = function(){
      copyBtn.textContent = "Copied";
      copyBtn.classList.add("copied");
      setTimeout(function(){ copyBtn.textContent = "Copy"; copyBtn.classList.remove("copied"); }, 1500);
    };
    if (navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(lastResult.text).then(done).catch(function(){});
    } else {
      var ta = document.createElement("textarea");
      ta.value = lastResult.text;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy"); done(); } catch(e){}
      document.body.removeChild(ta);
    }
  });

  updateTags();
  updateCharCount();
  renderTabs();
  renderGrid();
  renderHistory();
})();
</script>
</body>
</html>
"""

# Render HTML component inside Streamlit
components.html(html_code, height=1400, scrolling=True)