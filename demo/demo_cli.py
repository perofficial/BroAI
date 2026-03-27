def main():
    from humanizer import humanize

    while True:
        text = input("\nEnter text (or 'exit'): ")

        if text == "exit":
            break

        output = humanize(text, tone="genz", noise_level=0.2)

        print("→", output)


if __name__ == "__main__":
    main()