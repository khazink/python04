def main() -> None:
    try:
        print("Accesing Storage Vault: ancient_fragment.txt")
        with open("ancient_fragment.txt") as fragment:
            print("Connection established...")
            print()
            print("RECOVERED DATA:")
            print(fragment.read())
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except Exception as e:
        print(f"there's an error {e}")

if __name__ == "__main__":
    print("=== CYBER ARCHIEVES - DATA RECOVERY SYSTEM ===")
    main()