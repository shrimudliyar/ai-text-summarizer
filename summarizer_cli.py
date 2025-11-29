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

    # Join sentences back into a single string
    return " ".join(str(sentence) for sentence in summary_sentences)


def main():
    print("\n=== AI TEXT SUMMARIZER (LexRank) ===")
    print("Paste your text below. When you're done, press Enter on an empty line:\n")

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "":
            break

        lines.append(line)

    text = " ".join(lines).strip()

    if not text:
        print("\nNo text entered. Exiting.")
        return

    print("\nSummarizing... Please wait...\n")

    # You can change sentence_count (2, 3, 5, etc.)
    summary = summarize_text(text, sentence_count=3)

    print("========== SUMMARY ==========\n")
    print(summary)
    print("\n=============================\n")


if __name__ == "__main__":
    main()
