def main():
    print("\nStarting system scan...\n")
    for i in range(5):
        print(f"Progress: [{'█'*(i+1)}{' '*(4-i)}] {20*(i+1)}%")
        for _ in range(1000000): pass
    
    print("\nAnalyzing network traffic...")
    for _ in range(3):
        for _ in range(1000000): pass
        print(f"Packet {_+1} intercepted")
    
    print("\n" + "="*40)
    print("||" + "WARNING: SYSTEM BREACH".center(36) + "||")
    print("="*40)
    print("\nYOU HAVE BEEN HACKED!\n")
    print("\n" + "="*40)

if __name__ == "__main__":
    main()