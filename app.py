import streamlit as st

# ページの設定
st.set_page_config(page_title="LOEWE UPPM データベース", layout="centered")

# --- 1. シリーズ解説 ---
st.title("LOEWE Un Paseo Por Madrid")
st.write("マドリードへの散歩 コレクション")

st.markdown("""
ロエベの歴史的本拠地であるマドリードの文化や風景をテーマにしたユニセックスフレグランスシリーズです。
各香りは、特定の場所や歴史的な背景に基づいた調香がなされています。
""")
st.write("---")

# --- 2. データ定義 ---
perfumes = [
    {
        "name_jp": "ドーレ",
        "name_es": "Doré",
        "type": "スパイシー・ウッディ・アンバー",
        "story": "モダニズム映画館「シネ・ドレ」の上映アーカイブから着想を得た香り。パチョリ、シナモン、ミルラが調和します。",
        "ingredients": ["シナモン", "ミルラ", "バニラ", "ナツメグ", "ロエベ アコード", "パチョリ"]
    },
    {
        "name_jp": "シベレス",
        "name_es": "La Bella Cibeles",
        "type": "フローラル・フルーティ",
        "story": "大地と豊穣のシンボルであるシベレス広場の噴水をイメージ。アイリスやローズ、バニラが重なる官能的な構成です。",
        "ingredients": ["ベルガモット", "レモン", "ジャスミン", "アイリス", "ローズ", "オレンジブロッサム", "バイオレット", "キャロット", "バニラ", "パチョリ", "ムスク"]
    },
    {
        "name_jp": "デボー",
        "name_es": "Debod",
        "type": "フローラル・ウッディ・アンバー",
        "story": "マドリードにある古代エジプトのデボー神殿。夕日で赤く染まる空と水面の情景を表現しています。",
        "ingredients": ["ローズ", "ゼラニウム", "ジャスミン", "ラブダナム", "シプリオール", "ウード", "パチョリ", "ベチバー", "アンバー", "マンダリン", "ココナッツリーフ", "サフラン"]
    },
    {
        "name_jp": "マイリット",
        "name_es": "Mayrit",
        "type": "フローラル・ウッディ",
        "story": "9世紀のアラブ統治時代のマドリードを指す名称。オレンジブロッサムやアンバーが漂う謎めいた歴史を想起させます。",
        "ingredients": ["オレンジブロッサム", "パッションフルーツ", "グレープフルーツ", "カルダモン", "ローズ", "ジャスミン", "アンバー", "サンダルウッド", "バニラ"]
    },
    {
        "name_jp": "オペラ",
        "name_es": "Ópera",
        "type": "フローラル・パウダリー・ウッディ",
        "story": "フェリペ2世の宮廷文化。劇場や音楽の調べに包まれる、スズランやバニラの気品ある調香です。",
        "ingredients": ["ベルガモット", "スズラン", "フリージア", "ローズ", "ジャスミン", "バニラ", "ベンゾイン", "ベチバー", "サンダルウッド", "ムスク"]
    },
    {
        "name_jp": "ロサレダ",
        "name_es": "Rosaleda",
        "type": "フローラル・スパイシー",
        "story": "レティーロ公園内のバラ園。水連の池や彫像に囲まれた、ローズオットーが主役の華やかな庭園をイメージしています。",
        "ingredients": ["ベルガモット", "ビターオレンジ", "アップル", "ピーチ", "バイオレット", "サンバックジャスミン", "ローズオットー", "ダマスクローズ", "ネロリ", "シダー", "アンバー", "ムスク"]
    },
    {
        "name_jp": "サン・ミゲル",
        "name_es": "San Miguel",
        "type": "フローラル・ウッディ",
        "story": "歴史的なサン・ミゲル市場。活気あふれる市場の色彩と香りが混ざり合う、エネルギッシュな構成です。",
        "ingredients": ["ベルガモット", "バイオレット", "ゼラニウム", "ローズエキス", "ダバナ", "パチョリ", "ベチバー", "アンバー", "トルーバルサム"]
    },
    {
        "name_jp": "プラド",
        "name_es": "Prado",
        "type": "アロマティック・ウッディ・アンバー",
        "story": "プラド美術館と「草原」へのオマージュ。風景画のように調和のとれた、カモミールやセージによる休息の香り。",
        "ingredients": ["カモミール", "クラリセージ", "カシス", "ライチ", "ロエベ アコード"]
    },
    {
        "name_jp": "カサ・デ・カンポ",
        "name_es": "Casa de Campo",
        "type": "ウッディ・フローラル・ムスキー",
        "story": "かつての王室狩猟地であり、現在は市民のオアシスとなっている公園。自然の中での安らぎを想起させる香り。",
        "ingredients": ["グリーンマンダリン", "ブラッドオレンジ", "アルテミシア", "サンダルウッド", "ムスク", "ロエベ アコード"]
    }
]

# --- 3. 類義語処理 ---
SYNONYMS = {
    "バラ": "ローズ", "薔薇": "ローズ", "rose": "ローズ",
    "ヨモギ": "アルテミシア", "よもぎ": "アルテミシア",
    "蜜柑": "マンダリン", "みかん": "マンダリン",
    "白檀": "サンダルウッド", "麝香": "ムスク",
    "菫": "バイオレット", "すみれ": "バイオレット",
    "パチュリ": "パチョリ"
}

def normalize_search_term(term):
    term = term.strip().lower()
    return SYNONYMS.get(term, term)

# --- 4. 検索機能 ---
st.write("### 香料検索")
search_query = st.text_input(
    "検索したい香料を入力してください", 
    placeholder="例：バラ、バニラ、サンダルウッドなど"
)

# --- 5. 表示ロジック ---
query_term = normalize_search_term(search_query) if search_query else ""

if query_term:
    st.write(f"「{search_query}」の検索結果")
    found_any = False
    for p in perfumes:
        all_ings_str = "".join(p["ingredients"]).lower()
        if query_term in all_ings_str:
            found_any = True
            with st.expander(f"{p['name_jp']} ({p['name_es']})"):
                st.write(f"**香調**：{p['type']}")
                st.write(f"**背景**：{p['story']}")
                st.write(f"**主要香料**：{', '.join(p['ingredients'])}")
    if not found_any:
        st.write("該当する香水は見つかりませんでした。")
else:
    st.write("### コレクション一覧")
    for p in perfumes:
        with st.expander(f"{p['name_jp']} ({p['name_es']})"):
            st.write(f"**香調**：{p['type']}")
            st.write(f"**背景**：{p['story']}")
            st.write(f"**主要香料**：{', '.join(p['ingredients'])}")

st.write("---")
st.caption("LOEWE Un Paseo Por Madrid Collection Database")
