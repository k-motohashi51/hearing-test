import pitch_check as pc

def main():
    freq_base = 660

    pci = pc.PitchCheck(freq_base)
    pci.run()

if __name__ == '__main__':
    main()