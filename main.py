def main():
    from stats import get_word_count
    from stats import get_character_count
    from stats import report
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        report(sys.argv[1])
main()

