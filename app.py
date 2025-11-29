import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def summarize_text(text: str, sentence_count: int = 3) -> str:
    """
    Summarize the given text into a smaller number of sentences
    using the LexRank algorithm (extractive summarization).
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary_sentences = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary_sentences)


def main():
    st.set_page_config(page_title="AI Text Summarizer", layout="centered")

    st.title("🧠 AI Text Summarizer")
    st.write("Paste any long paragraph and get a short summary.")

    # Text input
    text = st.text_area(
        "Enter your text here:",
        height=250,
        placeholder="Paste a long article, paragraph, notes, etc..."
    )

    # Sentence count slider
    sentence_count = st.slider(
        "How many sentences do you want in the summary?",
        min_value=1,
        max_value=7,
        value=3,
    )

    if st.button("Summarize ✨"):
        if not text.strip():
            st.warning("Please enter some text first.")
        else:
            with st.spinner("Summarizing..."):
                try:
                    summary = summarize_text(text, sentence_count=sentence_count)
                    st.subheader("📌 Summary")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
