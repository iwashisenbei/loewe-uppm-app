import streamlit as st

# ページの設定
st.set_page_config(page_title="LOEWE UPPM 逆引きツール", layout="centered")

# --- データ定義 ---
perfumes = [
    {
        "name_jp": "ドーレ",
        "name_es": "Doré",
        "type": "スパイシー・ウッディ・アンバー",
        "story": "映画館『シネ・ドレ』のアーカイブ上映から着想。パチョリ、シナモン、ミルラが響き合う魅力的な香り。",
        "ingredients": ["シナモン", "ミルラ", "バニラ", "ナツメグ", "ロエベ アコード", "パチョリ"]
    },
    {
        "name_jp": "シベレス",
        "name_es": "La Bella Cibeles",
        "type": "フローラル・フルーティ",
        "story": "大地と豊穣のシンボル。シベレス広場の噴水のように情熱的で官能的なアイリスやローズの香り。",
        "ingredients": ["ベルガモット", "レモン", "ジャスミン", "アイリス", "ローズ", "オレンジブロッサム", "バイオレット", "キャロット", "バニラ", "パチョリ", "ムスク"]
    },
    {
        "name_jp": "デボー",
        "name_es": "Debod",
        "type": "フローラル・ウッディ・アンバー",
        "story": "神秘的なデボー神殿。夕日の赤を表現したウードやサフラン、ローズの希少な香り。",
        "ingredients": ["ローズ", "ゼラニウム", "ジャスミン", "ラブダナム", "シプリオール", "ウード", "パチョリ", "ベチバー", "アンバー", "マンダリン", "ココナッツリーフ", "サフラン"]
    },
    {
        "name_jp": "マイリット",
        "name_es": "Mayrit",
        "type": "フローラル・ウッディ",
        "story": "アラブ時代のマドリード。オレンジブロッサムやアンバーが漂う謎めいた歴史の記憶。",
        "ingredients": ["オレンジブロッサム", "パッションフルーツ", "グレープフルーツ", "カルダモン", "ローズ", "ジャスミン", "アンバー", "サンダルウッド", "バニラ"]
    },
    {
        "name_jp": "オペラ",
        "name_es": "Ópera",
        "type": "フローラル・パウダリー・ウッディ",
        "story": "宮廷文化のエレガンス。スズランやサンダルウッド、バニラが優雅に漂う夢見心地なひととき。",
        "ingredients": ["ベルガモット", "スズラン", "フリージア", "ローズ", "ジャスミン", "バニラ", "ベンゾイン", "ベチバー", "サンダルウッド", "ムスク"]
    },
    {
        "name_jp": "ロサレダ",
        "name_es": "Rosaleda",
        "type": "フローラル・スパイシー",
        "story": "レティーロ公園のバラ園。ローズオットーが主役の華やかな庭園のシンフォニー。",
        "ingredients": ["ベルガモット", "ビターオレンジ", "アップル", "ピーチ", "バイオレット", "サンバックジャスミン", "ローズオットー", "ダマスクローズ", "ネロリ", "シダー", "アンバー", "ムスク"]
    },
    {
        "name_jp": "サン・ミゲル",
        "name_es": "San Miguel",
        "type": "フローラル・ウッディ",
        "story": "活気あるサン・ミゲル市場。ローズ、パチョリ、アンバーが混ざり合うエネルギッシュな香り。",
        "ingredients": ["ベルガモット", "バイオレット", "ゼラニウム", "ローズエキス", "ダバナ", "パチョリ", "ベチバー", "アンバー", "トルーバルサム"]
    },
    {
        "name_jp": "プラド",
        "name_es": "Prado",
        "type": "アロマティック・ウッディ・アンバー",
        "story": "プラド美術館へのオマージュ。カモミールやセージが織りなす楽園のような調和。",
        "ingredients": ["カモミール", "クラリセージ", "カシス", "ライチ", "ロエベ アコード"]
    },
    {
        "name_jp": "カサ・デ・カンポ",
        "name_es": "Casa de Campo",
        "type": "ウッディ・フローラル・ムスキー",
        "story": "市民の憩いの場。アルテミシアやサンダルウッドが自然の中での休息を想起させます。",
        "ingredients": ["グリーンマンダリン", "ブラッドオレンジ", "アルテミシア", "サンダルウッド", "ムスク", "ロエベ アコード"]
    }
]

# --- 類義語辞書の定義 ---
# 「ユーザーが入力しそうな言葉」: 「データ上の正式名称」
SYNONYMS = {
    "バラ": "ローズ", "薔薇": "ローズ", "rose": "ローズ",
    "ヨモギ": "アルテミシア", "よもぎ": "アルテミシア",
    "蜜柑": "マンダリン", "みかん": "マンダリン",
    "白檀": "サンダルウッド",
    "乳香": "フランキンセンス",
    "麝香": "ムスク",
    "菫": "バイオレット", "すみれ": "バイオレット",
    "菖蒲": "アイリス",
    "パチュリ": "パチョリ"
}

# 検索用の関数
def normalize_search_term(term):
    term = term.strip().lower()
    # 辞書にあれば変換、なければそのまま返す
    return SYNONYMS.get(term, term)

# --- UI構築 ---
st.title("LOEWE UPPM 逆引き検索")
st.markdown("マドリードを巡る香りの旅。お好みの香料から探せます。")

# サイドバー：検索機能
st.sidebar.header("香料で検索")
search_query = st.sidebar.text_input("例：バラ、バニラ、サンダルウッド", help="類義語（バラ＝ローズなど）にも対応しています")

# 全香料リスト（選択式も残す）
all_ingredients = sorted(list(set([ing for p in perfumes for ing in p["ingredients"]])))
selected_ings = st.sidebar.multiselect("リストから選択", options=all_ingredients)

# --- 検索ロジック ---
# テキスト入力と選択肢の両方を統合
query_terms = []
if search_query:
    query_terms.append(normalize_search_term(search_query))
if selected_ings:
    query_terms.extend(selected_ings)

# 表示
if query_terms:
    st.subheader(f"検索条件: {', '.join(query_terms)}")
    found_any = False
    
    for p in perfumes:
        # 香水に含まれる全香料を1つの文字列にして、部分一致を確認
        p_ingredients_str = "".join(p["ingredients"]).lower()
        
        # 検索語のいずれかが含まれているかチェック
        match = False
        for term in query_terms:
            if term in p_ingredients_str:
                match = True
                break
        
        if match:
            found_any = True
            with st.expander(f"✨ {p['name_jp']} ({p['name_es']})"):
                st.write(f"**【香調】** {p['type']}")
                st.write(f"**【物語】** {p['story']}")
                st.write(f"**【主要香料】** {', '.join(p['ingredients'])}")
                
    if not found_any:
        st.info("該当する香水は見つかりませんでした。")
else:
    st.subheader("コレクション一覧")
    for p in perfumes:
        with st.expander(f"{p['name_jp']} ({p['name_es']})"):
            st.write(f"**香調:** {p['type']}")
            st.write(f"**ストーリー:** {p['story']}")
            st.caption(f"香料: {', '.join(p['ingredients'])}")

st.sidebar.markdown("---")
st.sidebar.info("類義語を自動で判別します。")
